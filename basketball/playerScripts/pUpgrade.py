import basketball.leagueSettings.pBadges as pBadges


def validateUpgrades(data: dict):
    # Make dictionary for return data
    upgradeCart: dict[str, list[str]] = {
        "successful": [],
        "failed": [],
    }
    # Get the upgrade data
    upgradeAttributes: dict[str, list[int, int]] = data["attributes"]
    upgradeBadges: dict[str, list[int, int]] = data["badges"]
    # Check limits. If any are exceeded, return False
    for attributeName, upgradeList in upgradeAttributes.items():
        newLevel: int = upgradeList[1]
        if newLevel > 99:
            upgradeCart["failed"].append([attributeName, "Attribute limit exceeded"])
            continue
        # Check if the user is eligible for the attribute
        pass
        # Check if the user has enough cash to purchase the upgrades
        pass
        # If player passes all checks, add to successful upgrades
        upgradeCart["successful"].append(attributeName)

    for badgeName, upgradeList in upgradeBadges.items():
        newLevel: int = upgradeList[1]
        if newLevel > 4:
            upgradeCart["failed"].append([badgeName, "Badge limit exceeded"])
            continue
        # Check if the user is eligible for the badge
        # fmt: off
        canUpgrade: bool = pBadges.checkEligibility(badgeName, newLevel)
        if not canUpgrade:
            upgradeCart["failed"].append([badgeName, "User is not eligible for this badge"])
            continue
        # fmt: on
        # Check if the user has enough cash to purchase the upgrades
        pass
        # If player passes all checks, add to successful upgrades
        upgradeCart["successful"].append(badgeName)
    # Return successful and failed upgrades
    return upgradeCart


def purchaseUpgrades(data: dict):
    # Validate the upgrades
    upgradeCart: dict[str, list[str]] = validateUpgrades(data)
    # Upgrade from the successful list
    pass
    # Send the failed list back to the user
    pass
