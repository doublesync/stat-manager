import random


# A function used to return an accurate range by incrementing the end of the range
def realRange(start: int, end: int) -> range:
    return range(start, (end + 1))


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
            realRange(1, 20): 76,
            realRange(21, 65): 77,
            realRange(66, 90): 78,
            realRange(91, 100): 79,
        },
        "SG": {
            realRange(1, 20): 77,
            realRange(21, 65): 79,
            realRange(66, 90): 80,
            realRange(91, 100): 81,
        },
        "SF": {
            realRange(1, 20): 80,
            realRange(21, 65): 81,
            realRange(66, 90): 82,
            realRange(91, 100): 83,
        },
        "PF": {
            realRange(1, 20): 82,
            realRange(21, 65): 83,
            realRange(66, 90): 84,
            realRange(91, 100): 85,
        },
        "C": {
            realRange(1, 25): 84,
            realRange(26, 65): 85,
            realRange(66, 90): 86,
            realRange(91, 96): 87,
            realRange(97, 97): 88,
            realRange(98, 98): 89,
            realRange(99, 99): 90,
            realRange(100, 100): 91,
        },
    },
}


# Roll for the players height
def heightRoll(archetype: str, position: str) -> int:
    roll = random.randint(1, 100)
    for key, value in heightOdds[archetype][position].items():
        if roll in key:
            return value
