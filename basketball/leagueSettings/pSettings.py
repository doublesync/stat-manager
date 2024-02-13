# Player positions and their height and weight limits
playerPositions: dict[str, dict[str, int]] = {
    "PG": {
        "heightLimits": [68, 75],
        "weightLimits": [160, 200],
    },
    "SG": {
        "heightLimits": [70, 77],
        "weightLimits": [180, 220],
    },
    "SF": {
        "heightLimits": [73, 80],
        "weightLimits": [200, 240],
    },
    "PF": {
        "heightLimits": [75, 82],
        "weightLimits": [220, 260],
    },
    "C": {
        "heightLimits": [78, 88],
        "weightLimits": [240, 300],
    }
}

heightOdds: dict[str, dict[str, dict[int, float]]] = {
    "Skilled": {
        "PG": {68: 0, 69: 0, 70: 0, 71: 0, 72: 0, 73: 0, 74: 0, 75: 0},
        "SG": {70: 0, 71: 0, 72: 0, 73: 0, 74: 0, 75: 0, 76: 0, 77: 0},
        "SF": {73: 0, 74: 0, 75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0},
        "PF": {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0},
        "C": {78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0, 88: 0}
    },
    "Athletic": {
        
    },
    "Giant": {

    },
    "Tiny": {

    }
}

# Weights (probability) for heights -- follow playerPositions heightLimits
heightOdds: dict[str, dict[int, float]] = {
    "PG": {68: 0, 69: 0, 70: 0, 71: 0, 72: 0, 73: 0, 74: 0, 75: 0},
    "SG": {70: 0, 71: 0, 72: 0, 73: 0, 74: 0, 75: 0, 76: 0, 77: 0},
    "SF": {73: 0, 74: 0, 75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0},
    "PF": {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0},
    "C": {78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0, 88: 0}
}