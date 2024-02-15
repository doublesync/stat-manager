def realRange(start: int, end: int) -> range:
    return range(start, (end+1))

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
        realRange(1, 4): 72,
        realRange(5, 30): 73,
        realRange(31, 70): 74,
        realRange(71, 95): 75,
        realRange(96, 100): 76,
    },
    "SG": {
        realRange(1, 4): 74,
        realRange(5, 30): 75,
        realRange(31, 71): 76,
        realRange(72, 96): 77,
        realRange(97, 100): 78,
    },
    "SF": {
        realRange(1, 3): 76,
        realRange(4, 28): 77,
        realRange(29, 70): 78,
        realRange(71, 95): 79,
        realRange(96, 100): 80,
    },
    "PF": {
        realRange(1, 3): 78,
        realRange(4, 28): 79,
        realRange(29, 70): 80,
        realRange(71, 95): 81,
        realRange(96, 100): 82,
    },
    "C": {
        realRange(1, 4): 80,
        realRange(5, 28): 81,
        realRange(29, 70): 82,
        realRange(71, 95): 83,
        realRange(96, 100): 84,
    },
}

# Height and wingspan odds used for giant players
heightOdds: dict[str, dict[str, dict[int, float]]] = {
    "Skilled": defaultHeightOdds,
    "Athletic": defaultHeightOdds,
    "Giant": {
        "PG": {
            realRange(1, 5): 75,
            realRange(6, 26): 76,
            realRange(26, 74): 77,
            realRange(75, 96): 78,
            realRange(97, 100): 79,
        },
        "SG": {
            realRange(1, 4): 76,
            realRange(5, 27): 77,
            realRange(28, 77): 78,
            realRange(78, 95): 79,
            realRange(96, 100): 80,
        },
        "SF": {
            realRange(1, 3): 78,
            realRange(4, 25): 79,
            realRange(26, 70): 80,
            realRange(71, 93): 81,
            realRange(94, 100): 82,
        },
        "PF": {
            realRange(1, 7): 80,
            realRange(8, 28): 81,
            realRange(29, 70): 82,
            realRange(71, 96): 83,
            realRange(97, 100): 84,
        },
        "C": {
            realRange(1, 5): 83,
            realRange(6, 35): 84,
            realRange(36, 91): 85,
            realRange(92, 95): 86,
            realRange(96, 96): 87,
            realRange(97, 97): 88,
            realRange(98, 98): 89,
            realRange(99, 99): 90,
            realRange(100, 100): 91,
        },
    },
}

wingspanOdds: dict[str, range] = {
    "Skilled": range(45, 55),
    "Athletic": range(50, 65),
    "Giant": range(70, 80),
}
