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

# Default height and wingspan odds used for skilled and athletic players
defaultHeightOdds: dict[str, dict[range, int]] = {
    "PG": {
        range(1, 4): 72,
        range(5, 30): 73,
        range(31, 70): 74,
        range(71, 95): 75,
        range(96, 100): 76,
    },
    "SG": {
        range(1, 4): 74,
        range(5, 30): 75,
        range(31, 71): 76,
        range(72, 96): 77,
        range(97, 100): 78,
    },
    "SF": {
        range(1, 3): 76,
        range(4, 28): 77,
        range(29, 70): 78,
        range(71, 95): 79,
        range(96, 100): 80,
    },
    "PF": {
        range(1, 3): 78,
        range(4, 28): 79,
        range(29, 70): 80,
        range(71, 95): 81,
        range(96, 100): 82,
    },
    "C": {
        range(1, 4): 80,
        range(5, 28): 81,
        range(29, 70): 82,
        range(71, 95): 83,
        range(96, 100): 84,
    },
}

# Height and wingspan odds used for giant players
heightOdds: dict[str, dict[str, dict[int, float]]] = {
    "Skilled": defaultHeightOdds,
    "Athletic": defaultHeightOdds,
    "Giant": {
        "PG": {
            range(1, 5): 75,
            range(6, 26): 76,
            range(26, 74): 77,
            range(75, 96): 78,
            range(97, 100): 79,
        },
        "SG": {
            range(1, 4): 76,
            range(5, 27): 77,
            range(28, 77): 78,
            range(78, 95): 79,
            range(96, 100): 80,
        },
        "SF": {
            range(1, 3): 78,
            range(4, 25): 79,
            range(26, 70): 80,
            range(71, 93): 81,
            range(94, 100): 82,
        },
        "PF": {
            range(1, 7): 80,
            range(8, 28): 81,
            range(29, 70): 82,
            range(71, 96): 83,
            range(97, 100): 84,
        },
        "C": {
            range(1, 5): 83,
            range(6, 35): 84,
            range(36, 91): 85,
            range(92, 95): 86,
            range(96, 96): 87,
            range(97, 97): 88,
            range(98, 98): 89,
            range(99, 99): 90,
            range(100, 100): 91,
        },
    },
}

wingspanOdds: dict[str, range] = {
    "Skilled": range(45, 55),
    "Athletic": range(50, 65),
    "Giant": range(70, 80),
}
