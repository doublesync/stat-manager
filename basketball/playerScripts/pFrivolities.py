import basketball.playerScripts.pCalculate as pCalculate
from basketball.models import BasketballPlayer, BasketballTeam
from basketball.models import UpgradeReceipt, CashReceipt


def calculateTotalSpent(player) -> list[int]:
    totalSpent: str = 0
    totalEarned: str = player.cash
    upgradeReceipts: any = UpgradeReceipt.objects.filter(player=player)
    cashReceipts: any = CashReceipt.objects.filter(player=player)
    # First calculate the total spent
    for receipt in upgradeReceipts:
        for attribute in receipt.successful["attributes"]:
            totalSpent += attribute[3]
        for badge in receipt.successful["badges"]:
            totalSpent += badge[3]
    # Now calculate the total earned
    for receipt in cashReceipts:
        totalEarned += receipt.amount if not receipt.taken else -(receipt.amount)
    return [totalSpent, totalEarned]  # [0] = totalSpent, [1] = totalEarned


def spentFrivolity() -> dict[str, int]:
    players: any = BasketballPlayer.objects.all()
    spentCount: dict = {}
    for player in players:
        spentCount[f"{player.firstName} {player.lastName}"] = calculateTotalSpent(
            player
        )[0]
    # Now sort the 'spentCount' dictionary & limit it to the top ten
    spentCount = dict(
        sorted(spentCount.items(), key=lambda item: item[1], reverse=True)
    )
    spentCount = dict(list(spentCount.items())[:10])
    return spentCount


def earnedFrivolity() -> dict[str, int]:
    players: any = BasketballPlayer.objects.all()
    earnedCount: dict = {}
    for player in players:
        earnedCount[f"{player.firstName} {player.lastName}"] = calculateTotalSpent(
            player
        )[1]
    # Now sort the 'earnedCount' dictionary & limit it to the top ten
    earnedCount = dict(
        sorted(earnedCount.items(), key=lambda item: item[1], reverse=True)
    )
    earnedCount = dict(list(earnedCount.items())[:10])
    return earnedCount


def positionFrivolity() -> dict[str, int]:
    positions: any = BasketballPlayer.objects.values_list(
        "position", flat=True
    ).distinct()
    positionCount: dict = {}
    for position in positions:
        positionCount[position] = BasketballPlayer.objects.filter(
            position=position
        ).count()
    return positionCount


def archetypeFrivolity() -> dict[str, int]:
    archetypes: any = BasketballPlayer.objects.values_list(
        "archetype", flat=True
    ).distinct()
    archetypeCount: dict = {}
    for archetype in archetypes:
        archetypeCount[archetype] = BasketballPlayer.objects.filter(
            archetype=archetype
        ).count()
    return archetypeCount


def heightFrivolity() -> dict[int, int]:
    heights = BasketballPlayer.objects.values_list("height", flat=True).distinct()
    heightCount = {}
    for height in heights:
        formattedHeight: int = pCalculate.formatHeight(height)
        heightCount[formattedHeight] = BasketballPlayer.objects.filter(
            height=height
        ).count()
    return heightCount


def weightModelFrivolity() -> dict[int, int]:
    weightModels: any = BasketballPlayer.objects.values_list(
        "weightModel", flat=True
    ).distinct()
    weightModelCount: dict = {}
    for weightModel in weightModels:
        weightModelCount[weightModel] = BasketballPlayer.objects.filter(
            weightModel=weightModel
        ).count()
    return weightModelCount


def bmiFrivolity() -> dict[str, int]:
    # We need to list the top ten BMI's (by player)
    players: any = BasketballPlayer.objects.all()
    bmiCount: dict = {}
    for player in players:
        bmiCount[f"{player.firstName} {player.lastName}"] = player.bmi
    # Now sort the 'bmiCount' dictionary & limit it to the top ten
    bmiCount = dict(sorted(bmiCount.items(), key=lambda item: item[1], reverse=True))
    # Get the first ten
    bmiCount = dict(list(bmiCount.items())[:10])
    return bmiCount
