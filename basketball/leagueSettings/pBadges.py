# Attribute dependent badges will live inside of this file.
attributeDependentBadges: dict[str, dict[str, int]] = {
    # Bully
    "Bully": {
        "Bronze": {
            "Strength": 75,
        },
        "Silver": {
            "Strength": 83,
        },
        "Gold": {
            "Strength": 90,
        },
        "Hall of Fame": {
            "Strength": 95,
        },
    },
    # Brick Wall
    "Bully": {
        "Bronze": {
            "Strength": 60,
        },
        "Silver": {
            "Strength": 75,
        },
        "Gold": {
            "Strength": 85,
        },
        "Hall of Fame": {
            "Strength": 90,
        },
    },
    # Clamps
    "Clamps": {
        "Bronze": {
            "Perimeter Defense": 75,
            "Strength": 45,
        },
        "Silver": {
            "Perimeter Defense": 85,
            "Strength": 50,
        },
        "Gold": {
            "Perimeter Defense": 93,
            "Strength": 55,
        },
        "Hall of Fame": {
            "Perimeter Defense": 99,
            "Strength": 60,
        },
    },
    # Posterizer
    "Posterizer": {
        "Bronze": {
            "Driving Dunk": 75,
            "Vertical": 70,
        },
        "Silver": {
            "Driving Dunk": 86,
            "Vertical": 75,
        },
        "Gold": {
            "Driving Dunk": 93,
            "Vertical": 80,
        },
        "Hall of Fame": {
            "Driving Dunk": 99,
            "Vertical": 83,
        },
    },
    # Anchor
    "Anchor": {
        "Bronze": {
            "Strength": 77,
        },
        "Silver": {
            "Strength": 85,
        },
        "Gold": {
            "Strength": 92,
        },
        "Hall of Fame": {
            "Strength": 99,
        },
    },
}


def checkEligibility(player: any, badge: str, badgeTier: str) -> bool:
    for attribute, value in attributeDependentBadges[badge][badgeTier].items():
        if player.attributes[attribute] < value:
            return False
    return True
