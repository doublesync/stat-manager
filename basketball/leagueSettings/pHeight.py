# A function used to return an accurate range by incrementing the end of the range
def realRange(start: int, end: int) -> range:
    return range(start, (end+1))

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
