# Player position limits used for skilled and athletic players
defaultPlayerLimits: dict[str, dict[str, int]] = {
    "PG": {
        "heightLimits": [72, 76],
        "weightLimits": [160, 200],
    },
    "SG": {
        "heightLimits": [74, 78],
        "weightLimits": [180, 220],
    },
    "SF": {
        "heightLimits": [76, 80],
        "weightLimits": [200, 240],
    },
    "PF": {
        "heightLimits": [78, 82],
        "weightLimits": [220, 260],
    },
    "C": {
        "heightLimits": [80, 84],
        "weightLimits": [240, 300],
    },
}

# Player limits (height and weight)
playerLimits: dict[str, dict[str, int]] = {
    "Skilled": defaultPlayerLimits,
    "Athletic": defaultPlayerLimits,
    "Giants": {
        "PG": {
            "heightLimits": [75, 79],
            "weightLimits": [160, 200],
        },
        "SG": {
            "heightLimits": [76, 80],
            "weightLimits": [180, 220],
        },
        "SF": {
            "heightLimits": [78, 82],
            "weightLimits": [200, 240],
        },
        "PF": {
            "heightLimits": [80, 84],
            "weightLimits": [220, 260],
        },
        "C": {
            "heightLimits": [83, 91],
            "weightLimits": [240, 300],
        },
    },
}
