# Where physical attributes are calculated for players
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pWeight as pWeight

startingPhysicals: dict[int, dict[str, int]] = {
    72: {
        "Default": {
            "Vertical": 84,
            "Speed": 92,
        },
        "Athletic": {
            "Vertical": 94,
            "Speed": 97,
        },
    },
    73: {
        "Default": {
            "Vertical": 83,
            "Speed": 89,
        },
        "Athletic": {
            "Vertical": 93,
            "Speed": 94,
        },
    },
    74: {
        "Default": {
            "Vertical": 82,
            "Speed": 86,
        },
        "Athletic": {
            "Vertical": 92,
            "Speed": 91,
        },
    },
    75: {
        "Default": {
            "Vertical": 81,
            "Speed": 83,
        },
        "Athletic": {
            "Vertical": 91,
            "Speed": 88,
        },
    },
    76: {
        "Default": {
            "Vertical": 80,
            "Speed": 80,
        },
        "Athletic": {
            "Vertical": 90,
            "Speed": 85,
        },
    },
    77: {
        "Default": {
            "Vertical": 79,
            "Speed": 77,
        },
        "Athletic": {
            "Vertical": 89,
            "Speed": 82,
        },
    },
    78: {
        "Default": {
            "Vertical": 78,
            "Speed": 74,
        },
        "Athletic": {
            "Vertical": 88,
            "Speed": 79,
        },
    },
    79: {
        "Default": {
            "Vertical": 77,
            "Speed": 71,
        },
        "Athletic": {
            "Vertical": 87,
            "Speed": 76,
        },
    },
    80: {
        "Default": {
            "Vertical": 76,
            "Speed": 68,
        },
        "Athletic": {
            "Vertical": 86,
            "Speed": 73,
        },
    },
    81: {
        "Default": {
            "Vertical": 75,
            "Speed": 65,
        },
        "Athletic": {
            "Vertical": 85,
            "Speed": 70,
        },
    },
    82: {
        "Default": {
            "Vertical": 74,
            "Speed": 62,
        },
        "Athletic": {
            "Vertical": 84,
            "Speed": 67,
        },
    },
    83: {
        "Default": {
            "Vertical": 73,
            "Speed": 59,
        },
        "Athletic": {
            "Vertical": 83,
            "Speed": 64,
        },
    },
    84: {
        "Default": {
            "Vertical": 72,
            "Speed": 54,
        },
        "Athletic": {
            "Vertical": 82,
            "Speed": 59,
        },
    },
    85: {
        "Default": {
            "Vertical": 70,
            "Speed": 51,
        },
        "Athletic": {
            "Vertical": 80,
            "Speed": 56,
        },
    },
    86: {
        "Default": {
            "Vertical": 68,
            "Speed": 48,
        },
        "Athletic": {
            "Vertical": 78,
            "Speed": 53,
        },
    },
    87: {
        "Default": {
            "Vertical": 76,
            "Speed": 45,
        },
        "Athletic": {
            "Vertical": 86,
            "Speed": 50,
        },
    },
    88: {
        "Default": {
            "Vertical": 74,
            "Speed": 42,
        },
        "Athletic": {
            "Vertical": 84,
            "Speed": 47,
        },
    },
    89: {
        "Default": {
            "Vertical": 72,
            "Speed": 39,
        },
        "Athletic": {
            "Vertical": 82,
            "Speed": 44,
        },
    },
    90: {
        "Default": {
            "Vertical": 68,
            "Speed": 36,
        },
        "Athletic": {
            "Vertical": 78,
            "Speed": 41,
        },
    },
    91: {
        "Default": {
            "Vertical": 66,
            "Speed": 33,
        },
        "Athletic": {
            "Vertical": 76,
            "Speed": 38,
        },
    },
}


def setStartingPhysicals(player: any) -> any:
    modelToUse = "Athletic" if player.archetype == "Athletic" else "Default"
    # Find the starting attributes
    player.attributes: dict = pAttributes.startingAttributes[player.position]
    # Set the starting physicals before weight model boosts
    # fmt: off
    player.attributes["Strength"] = pWeight.weightModels[player.position][player.weightModel]["Strength"]
    player.attributes["Speed"] = startingPhysicals[player.height][modelToUse]["Speed"]
    player.attributes["Speed with Ball"] = startingPhysicals[player.height][modelToUse]["Speed"]
    player.attributes["Acceleration"] = startingPhysicals[player.height][modelToUse]["Speed"]
    player.attributes["Vertical"] = startingPhysicals[player.height][modelToUse]["Vertical"]
    # fmt: on
    # Check if the player qualifies for athletic boosts
    weightModelBoosts: dict = pWeight.weightBoosts[player.weightModel][modelToUse]
    # Apply the weight model boosts
    for attribute, boost in weightModelBoosts.items():
        if player.attributes[attribute] + boost > 99:
            player.attributes[attribute] = 99
        else:
            player.attributes[attribute] += boost
    return player
