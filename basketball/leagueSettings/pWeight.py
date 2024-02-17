# Weight settings & information will live inside of this file.
weightModels: dict[str, dict[str, int]] = {
    "PG": {
        "Lightest": {"Weight": 155, "Strength": 35},
        "Lighter": {"Weight": 165, "Strength": 40},
        "Light": {"Weight": 175, "Strength": 45},
        "Default": {"Weight": 185, "Strength": 55},
        "Heavy": {"Weight": 195, "Strength": 60},
        "Heavier": {"Weight": 205, "Strength": 65},
        "Heaviest": {"Weight": 215, "Strength": 70},
    },
    "SG": {
        "Lightest": {"Weight": 165, "Strength": 45},
        "Lighter": {"Weight": 175, "Strength": 50},
        "Light": {"Weight": 185, "Strength": 55},
        "Default": {"Weight": 195, "Strength": 60},
        "Heavy": {"Weight": 205, "Strength": 65},
        "Heavier": {"Weight": 215, "Strength": 70},
        "Heaviest": {"Weight": 225, "Strength": 75},
    },
    "SF": {
        "Lightest": {"Weight": 175, "Strength": 50},
        "Lighter": {"Weight": 185, "Strength": 55},
        "Light": {"Weight": 195, "Strength": 60},
        "Default": {"Weight": 205, "Strength": 65},
        "Heavy": {"Weight": 215, "Strength": 70},
        "Heavier": {"Weight": 225, "Strength": 75},
        "Heaviest": {"Weight": 235, "Strength": 80},
    },
    "PF": {
        "Lightest": {"Weight": 195, "Strength": 55},
        "Lighter": {"Weight": 206, "Strength": 60},
        "Light": {"Weight": 215, "Strength": 65},
        "Default": {"Weight": 225, "Strength": 70},
        "Heavy": {"Weight": 235, "Strength": 75},
        "Heavier": {"Weight": 245, "Strength": 80},
        "Heaviest": {"Weight": 255, "Strength": 85},
    },
    "C": {
        "Lightest": {"Weight": 205, "Strength": 60},
        "Lighter": {"Weight": 215, "Strength": 65},
        "Light": {"Weight": 225, "Strength": 70},
        "Default": {"Weight": 235, "Strength": 75},
        "Heavy": {"Weight": 245, "Strength": 80},
        "Heavier": {"Weight": 255, "Strength": 85},
        "Heaviest": {"Weight": 265, "Strength": 90},
    },
}

weightBoosts: dict[str, dict[str, int]] = {
    "Lightest": {
        "Default": {
            "Acceleration": 10,
        },
        "Athletic": {
            "Acceleration": 15,
        },
    },
    "Lighter": {
        "Default": {
            "Acceleration": 8,
        },
        "Athletic": {
            "Acceleration": 13,
        },
    },
    "Light": {
        "Default": {
            "Acceleration": 5,
        },
        "Athletic": {
            "Acceleration": 10,
        },
    },
    "Default": {
        "Default": {
            "Acceleration": 0,
        },
        "Athletic": {
            "Acceleration": 5,
        },
    },
    "Heavy": {
        "Default": {
            "Acceleration": -10,
        },
        "Athletic": {
            "Acceleration": -5,
        },
    },
    "Heavier": {
        "Default": {
            "Acceleration": -15,
        },
        "Athletic": {
            "Acceleration": -10,
        },
    },
    "Heaviest": {
        "Default": {
            "Acceleration": -20,
        },
        "Athletic": {
            "Acceleration": -15,
        },
    },
}


# Set weight from weight model
def getWeightFromModel(position: str, weightModel) -> int:
    return weightModels[position][weightModel]["Weight"]
