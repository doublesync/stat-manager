import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pBadges as pBadges
import basketball.leagueSettings.pDefault as pDefault

from basketball.models import UpgradeReceipt


def compileUpgradeData(player: any, data: dict[str, int]) -> dict:
    # Format the data to be used in the upgrade form
    upgradeData: dict[str, any] = {
        "cost": 0,
        "attributes": {},
        "badges": {},
    }
    # fmt: off
    for key, newValue in data.items():
        if key.startswith("attributes_"):
            attributeName: str = key.replace("attributes_", "")
            attributeLevel: int = player.attributes[attributeName]
            # Check if the attribute has been increased
            if int(newValue) > attributeLevel:
                attributeCost: int = pAttributes.checkAttributePrice(
                    archetype=player.archetype,
                    attribute=attributeName,
                    startLevel=attributeLevel,
                    endLevel=int(newValue),
                )
                upgradeData["attributes"][attributeName] = [attributeLevel, int(newValue), attributeCost]
                upgradeData["cost"] += attributeCost
        elif key.startswith("badges_"):
            badgeName: str = key.replace("badges_", "")
            badgeLevel: int = player.badges[badgeName]
            # Check if the badge has been increased
            # Add one to badgeLevel because HTML dropdowns start at 1
            if int(newValue) >= (badgeLevel + 1):
                badgeCost: int = pBadges.checkBadgePrice(
                    startLevel=badgeLevel, 
                    endLevel=int(newValue)
                )
                upgradeData["badges"][badgeName] = [badgeLevel, int(newValue), badgeCost]
                upgradeData["cost"] += badgeCost

    return upgradeData
    # fmt: on


def validateUpgrades(data: dict, player: any):
    # Make dictionary for return data
    upgradeCart: dict[str, list[str]] = {
        "cost": 0,
        "successful": {
            "attributes": [],
            "badges": [],
        },
        "failed": [],
    }
    # Get the upgrade data
    upgradeAttributes: any = data["attributes"]
    upgradeBadges: any = data["badges"]
    # Check limits. If any are exceeded, return False
    # Attribute upgrades
    for attributeName, upgradeList in upgradeAttributes.items():
        oldLevel: int = upgradeList[0]
        newLevel: int = upgradeList[1]
        if newLevel > 99:
            upgradeCart["failed"].append([attributeName, "Attribute limit exceeded"])
            continue
        # Add cash to the cost
        individualCost = pAttributes.checkAttributePrice(
            archetype=player.archetype,
            attribute=attributeName,
            startLevel=oldLevel,
            endLevel=newLevel,
        )
        # Check if the player has enough cash to purchase the upgrade
        # fmt: off
        if player.cash < (upgradeCart["cost"] + individualCost):
            upgradeCart["failed"].append(["Cash", "Not enough cash to purchase upgrades"])
            return upgradeCart
        # fmt: on
        # Add to the successful upgrades list
        upgradeCart["cost"] += individualCost
        upgradeCart["successful"]["attributes"].append(
            [attributeName, oldLevel, newLevel, individualCost]
        )
    # Badge upgrades
    for badgeName, upgradeList in upgradeBadges.items():
        oldLevel: int = upgradeList[0]
        newLevel: int = upgradeList[1]
        if newLevel > 4:
            upgradeCart["failed"].append([badgeName, "Badge limit exceeded"])
            continue
        # Check if the user is eligible for the badge
        eligibleBadge: bool = pBadges.checkEligibility(player, badgeName, newLevel)
        canUpgrade: bool = eligibleBadge[0]
        errorReason: str = eligibleBadge[1]
        if not canUpgrade:
            upgradeCart["failed"].append([badgeName, errorReason.upper()])
            continue
        # Add cash to the cost
        individualCost = pBadges.checkBadgePrice(startLevel=oldLevel, endLevel=newLevel)
        # Check if the player has enough cash to purchase the upgrade
        # fmt: off
        if player.cash < (upgradeCart["cost"] + individualCost):
            upgradeCart["failed"].append(["Cash", "Not enough cash to purchase upgrades"])
            return upgradeCart
        # fmt: on
        # Add to the successful upgrades list
        upgradeCart["cost"] += individualCost
        upgradeCart["successful"]["badges"].append(
            [badgeName, oldLevel, newLevel, individualCost]
        )

    # Return successful and failed upgrades
    return upgradeCart


def purchaseUpgrades(data: dict, player: any):
    # Validate the upgrades
    upgradeCart: dict[str, list[str]] = validateUpgrades(data, player)
    # Upgrade from the successful list
    for attributeInfo in upgradeCart["successful"]["attributes"]:
        player.attributes[attributeInfo[0]] = data["attributes"][attributeInfo[0]][1]
    for badgeInfo in upgradeCart["successful"]["badges"]:
        player.badges[badgeInfo[0]] = data["badges"][badgeInfo[0]][1]
    # Subtract the cost from the player's cash
    if upgradeCart["cost"] > 0:
        player.cash -= upgradeCart["cost"]
        player.save()
    # Save the receipt
    receipt = UpgradeReceipt(
        discordUser=player.discordUser,
        player=player,
        successful=upgradeCart["successful"],
        failed=upgradeCart["failed"],
    )
    receipt.save()
    # Send the whole upgradeCart back
    return upgradeCart
