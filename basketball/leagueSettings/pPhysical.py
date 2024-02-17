# Where physical attributes are calculated for players
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pWeight as pWeight

startingPhysicals: dict[int, dict[str, int]] = {
    72: {
        "Default": {
            "Vertical": 84,
            "Speed": 90,
        },
        "Athletic": {
            "Vertical": 94,
            "Speed": 95,
        },
    },
    73: {
        "Default": {
            "Vertical": 83,
            "Speed": 87,
        },
        "Athletic": {
            "Vertical": 93,
            "Speed": 92,
        },
    },
    74: {
        "Default": {
            "Vertical": 82,
            "Speed": 84,
        },
        "Athletic": {
            "Vertical": 92,
            "Speed": 89,
        },
    },
    75: {
        "Default": {
            "Vertical": 81,
            "Speed": 81,
        },
        "Athletic": {
            "Vertical": 91,
            "Speed": 86,
        },
    },
    76: {
        "Default": {
            "Vertical": 80,
            "Speed": 78,
        },
        "Athletic": {
            "Vertical": 90,
            "Speed": 83,
        },
    },
    77: {
        "Default": {
            "Vertical": 79,
            "Speed": 75,
        },
        "Athletic": {
            "Vertical": 89,
            "Speed": 80,
        },
    },
    78: {
        "Default": {
            "Vertical": 78,
            "Speed": 72,
        },
        "Athletic": {
            "Vertical": 88,
            "Speed": 77,
        },
    },
    79: {
        "Default": {
            "Vertical": 77,
            "Speed": 69,
        },
        "Athletic": {
            "Vertical": 87,
            "Speed": 74,
        },
    },
    80: {
        "Default": {
            "Vertical": 76,
            "Speed": 66,
        },
        "Athletic": {
            "Vertical": 86,
            "Speed": 71,
        },
    },
    81: {
        "Default": {
            "Vertical": 75,
            "Speed": 63,
        },
        "Athletic": {
            "Vertical": 85,
            "Speed": 68,
        },
    },
    82: {
        "Default": {
            "Vertical": 74,
            "Speed": 60,
        },
        "Athletic": {
            "Vertical": 84,
            "Speed": 65,
        },
    },
    83: {
        "Default": {
            "Vertical": 73,
            "Speed": 57,
        },
        "Athletic": {
            "Vertical": 83,
            "Speed": 62,
        },
    },
    84: {
        "Default": {
            "Vertical": 72,
            "Speed": 50,
        },
        "Athletic": {
            "Vertical": 82,
            "Speed": 55,
        },
    },
    85: {
        "Default": {
            "Vertical": 70,
            "Speed": 47,
        },
        "Athletic": {
            "Vertical": 80,
            "Speed": 52,
        },
    },
    86: {
        "Default": {
            "Vertical": 68,
            "Speed": 44,
        },
        "Athletic": {
            "Vertical": 78,
            "Speed": 49,
        },
    },
    87: {
        "Default": {
            "Vertical": 76,
            "Speed": 41,
        },
        "Athletic": {
            "Vertical": 86,
            "Speed": 46,
        },
    },
    88: {
        "Default": {
            "Vertical": 74,
            "Speed": 38,
        },
        "Athletic": {
            "Vertical": 84,
            "Speed": 43,
        },
    },
    89: {
        "Default": {
            "Vertical": 72,
            "Speed": 35,
        },
        "Athletic": {
            "Vertical": 82,
            "Speed": 40,
        },
    },
    90: {
        "Default": {
            "Vertical": 68,
            "Speed": 32,
        },
        "Athletic": {
            "Vertical": 78,
            "Speed": 37,
        },
    },
    91: {
        "Default": {
            "Vertical": 66,
            "Speed": 29,
        },
        "Athletic": {
            "Vertical": 76,
            "Speed": 34,
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
