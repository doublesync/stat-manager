# Where physical attributes are calculated for players
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pWeight as pWeight

startingPhysicals: dict[int, dict[str, int]] = {
    72: {
        "Default": {
            "Vertical": 84,
            "Speed": 94,
        },
        "Athletic": {
            "Vertical": 94,
            "Speed": 99,
        },
    },
    73: {
        "Default": {
            "Vertical": 83,
            "Speed": 93,
        },
        "Athletic": {
            "Vertical": 93,
            "Speed": 98,
        },
    },
    74: {
        "Default": {
            "Vertical": 82,
            "Speed": 91,
        },
        "Athletic": {
            "Vertical": 92,
            "Speed": 96,
        },
    },
    75: {
        "Default": {
            "Vertical": 81,
            "Speed": 89,
        },
        "Athletic": {
            "Vertical": 91,
            "Speed": 94,
        },
    },
    76: {
        "Default": {
            "Vertical": 80,
            "Speed": 87,
        },
        "Athletic": {
            "Vertical": 90,
            "Speed": 92,
        },
    },
    77: {
        "Default": {
            "Vertical": 79,
            "Speed": 85,
        },
        "Athletic": {
            "Vertical": 89,
            "Speed": 90,
        },
    },
    78: {
        "Default": {
            "Vertical": 78,
            "Speed": 83,
        },
        "Athletic": {
            "Vertical": 88,
            "Speed": 88,
        },
    },
    79: {
        "Default": {
            "Vertical": 77,
            "Speed": 81,
        },
        "Athletic": {
            "Vertical": 87,
            "Speed": 86,
        },
    },
    80: {
        "Default": {
            "Vertical": 76,
            "Speed": 79,
        },
        "Athletic": {
            "Vertical": 86,
            "Speed": 84,
        },
    },
    81: {
        "Default": {
            "Vertical": 75,
            "Speed": 75,
        },
        "Athletic": {
            "Vertical": 85,
            "Speed": 80,
        },
    },
    82: {
        "Default": {
            "Vertical": 74,
            "Speed": 70,
        },
        "Athletic": {
            "Vertical": 84,
            "Speed": 75,
        },
    },
    83: {
        "Default": {
            "Vertical": 73,
            "Speed": 68,
        },
        "Athletic": {
            "Vertical": 83,
            "Speed": 73,
        },
    },
    84: {
        "Default": {
            "Vertical": 72,
            "Speed": 65,
        },
        "Athletic": {
            "Vertical": 82,
            "Speed": 70,
        },
    },
    85: {
        "Default": {
            "Vertical": 70,
            "Speed": 60,
        },
        "Athletic": {
            "Vertical": 80,
            "Speed": 65,
        },
    },
    86: {
        "Default": {
            "Vertical": 68,
            "Speed": 57,
        },
        "Athletic": {
            "Vertical": 78,
            "Speed": 62,
        },
    },
    87: {
        "Default": {
            "Vertical": 76,
            "Speed": 54,
        },
        "Athletic": {
            "Vertical": 86,
            "Speed": 59,
        },
    },
    88: {
        "Default": {
            "Vertical": 74,
            "Speed": 50,
        },
        "Athletic": {
            "Vertical": 84,
            "Speed": 55,
        },
    },
    89: {
        "Default": {
            "Vertical": 72,
            "Speed": 45,
        },
        "Athletic": {
            "Vertical": 82,
            "Speed": 50,
        },
    },
    90: {
        "Default": {
            "Vertical": 68,
            "Speed": 42,
        },
        "Athletic": {
            "Vertical": 78,
            "Speed": 47,
        },
    },
    91: {
        "Default": {
            "Vertical": 66,
            "Speed": 40,
        },
        "Athletic": {
            "Vertical": 76,
            "Speed": 45,
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
    player.attributes["Lateral Quickness"] = (player.attributes["Speed"] + player.attributes["Perimeter Defense"]) // 2 
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
