# Player position limits used for skilled and athletic players
defaultPlayerLimits: dict[str, dict[str, int]] = {
    "PG": {
        "heightLimits": [70, 77],
        "weightLimits": [160, 200],
    },
    "SG": {
        "heightLimits": [72, 79],
        "weightLimits": [180, 220],
    },
    "SF": {
        "heightLimits": [78, 81],
        "weightLimits": [200, 240],
    },
    "PF": {
        "heightLimits": [79, 82],
        "weightLimits": [220, 260],
    },
    "C": {
        "heightLimits": [81, 88],
        "weightLimits": [240, 300],
    }
}
# Default height odds used for skilled and athletic players
defaultHeightOdds: dict[str, dict[int, float]] = {
    "PG": {70: 0, 71: 0, 72: 0, 73: 0, 74: 0, 75: 0, 76: 0, 77: 0},
    "SG": {72: 0, 73: 0, 74: 0, 75: 0, 76: 0, 77: 0, 78: 0, 79: 0},
    "SF": {78: 0, 79: 0, 80: 0, 81: 0},
    "PF": {79: 0, 80: 0, 81: 0, 82: 0},
    "C": {81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0, 88: 0}
}

# Player limits (height and weight) 
playerLimits: dict[str, dict[str, int]] = {
    "Skilled": defaultPlayerLimits,
    "Athletic": defaultPlayerLimits,
    "Giants": {
        "PG": {
            "heightLimits": [73, 80],
            "weightLimits": [160, 200],
        },
        "SG": {
            "heightLimits": [75, 82],
            "weightLimits": [180, 220],
        },
        "SF": {
            "heightLimits": [81, 84],
            "weightLimits": [200, 240],
        },
        "PF": {
            "heightLimits": [82, 85],
            "weightLimits": [220, 260],
        },
        "C": {
            "heightLimits": [84, 88],
            "weightLimits": [240, 300],
        }
    }
}

heightOdds: dict[str, dict[str, dict[int, float]]] = {
    "Skilled": defaultHeightOdds,
    "Athletic": defaultHeightOdds,
    "Giant": {
        "PG": {73: 0, 74: 0, 75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0},
        "SG": {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0},
        "SF": {81: 0, 82: 0, 83: 0, 84: 0},
        "PF": {82: 0, 83: 0, 84: 0, 85: 0},
        "C": {84: 0, 85: 0, 86: 0, 87: 0, 88: 0}
    },
}