# Description: This file contains the player settings for the basketball league. This includes the player positions and their height and weight limits.
# Dependencies: None
# Contributor(s): Doublesync


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

# Weights (probability) for heights -- follow playerPositions heightLimits
heightWeights: dict[str, dict[int, float]] = {
    "PG": {68: 0.05, 69: 0.10, 70: 0.15, 71: 0.20, 72: 0.20, 73: 0.15, 74: 0.10, 75: 0.05},
    "SG": {70: 0.05, 71: 0.10, 72: 0.15, 73: 0.20, 74: 0.20, 75: 0.15, 76: 0.10, 77: 0.05},
    "SF": {73: 0.05, 74: 0.10, 75: 0.15, 76: 0.20, 77: 0.20, 78: 0.15, 79: 0.10, 80: 0.05},
    "PF": {75: 0.05, 76: 0.10, 77: 0.15, 78: 0.20, 79: 0.20, 80: 0.15, 81: 0.10, 82: 0.05},
    "C": {78: 0.05, 79: 0.10, 80: 0.15, 81: 0.20, 82: 0.20, 83: 0.15, 84: 0.10, 85: 0.05, 86: 0.05, 87: 0.05, 88: 0.05}
}