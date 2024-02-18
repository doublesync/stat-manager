# Attribute dependent badges will live inside of this file.
attributeDependentBadges: dict[str, dict[str, int]] = {
    # Bully
    "Bully": {
        1: {
            "Strength": 75,
        },
        2: {
            "Strength": 83,
        },
        3: {
            "Strength": 90,
        },
        4: {
            "Strength": 95,
        },
    },
    # Brick Wall
    "Bully": {
        1: {
            "Strength": 60,
        },
        2: {
            "Strength": 75,
        },
        3: {
            "Strength": 85,
        },
        4: {
            "Strength": 90,
        },
    },
    # Clamps
    "Clamps": {
        1: {
            "Perimeter Defense": 75,
            "Strength": 45,
        },
        2: {
            "Perimeter Defense": 85,
            "Strength": 50,
        },
        3: {
            "Perimeter Defense": 93,
            "Strength": 55,
        },
        4: {
            "Perimeter Defense": 99,
            "Strength": 60,
        },
    },
    # Posterizer
    "Posterizer": {
        1: {
            "Driving Dunk": 75,
            "Vertical": 70,
        },
        2: {
            "Driving Dunk": 86,
            "Vertical": 75,
        },
        3: {
            "Driving Dunk": 93,
            "Vertical": 80,
        },
        4: {
            "Driving Dunk": 99,
            "Vertical": 83,
        },
    },
    # Anchor
    "Anchor": {
        1: {
            "Strength": 77,
        },
        2: {
            "Strength": 85,
        },
        3: {
            "Strength": 92,
        },
        4: {
            "Strength": 99,
        },
    },
}

badgeCategories: dict[str, list[str]] = {
    "Shooting": [
        "Agent 3",
        "Blinders",
        "Catch & Shoot",
        "Claymore",
        "Comeback Kid",
        "Corner Specialist",
        "Deadeye",
        "Free Points",
        "Green Machine",
        "Guard Up",
        "Limitless Range",
        "Middy Magician",
        "Open Looks",
        "Post Fade Phenom",
        "Slippery Off-Ball",
        "Space Creator",
        "Spot Finder",
    ],
    "Playmaking": [
        "Ankle Breaker",
        "Bail Out",
        "Blow-By",
        "Break Starter",
        "Dimer",
        "Handles for Days",
        "Hyperdrive",
        "Killer Combos",
        "Needle Threader",
        "Physical Handles",
        "Post Playmaker",
        "Relay Passer",
        "Special Delivery",
        "Speed Booster",
        "Touch Passer",
        "Triple Spike",
        "Unpluckable",
    ],
    "Finishing": [
        "Acrobat",
        "Aerial Wizard",
        "Backdown Punisher",
        "Big Driver",
        "Bulldozer",
        "Bunny",
        "Dream Shake",
        "Dropstepper",
        "Fast Twitch",
        "Fearless Finisher",
        "Float Game",
        "Giant Slayer",
        "Hook Specialist",
        "Masher",
        "Post Spin Technician",
        "Posterizer",
        "Precision Dunker",
        "Pro Touch",
        "Rise Up",
        "Scooper",
        "Slithery",
        "Spin Cycle",
        "Two Step",
        "Whistle",
    ],
    "Defensive": [
        "94 Feet",
        "Anchor",
        "Ankle Braces",
        "Boxout Beast",
        "Brick Wall",
        "Challenger",
        "Chase Down Artist",
        "Clamps",
        "Fast Feet",
        "Glove",
        "Interceptor",
        "Immovable Enforcer",
        "Off-Ball Pest",
        "Pick Dodger",
        "Pogo Stick",
        "Post Lockdown",
        "Rebound Chaser",
        "Right Stick Ripper",
        "Work Horse",
    ],
}

badgePrices: dict[str, int] = {}


def checkEligibility(player: any, badge: str, badgeTier: str) -> bool:
    for attribute, value in attributeDependentBadges[badge][badgeTier].items():
        if player.attributes[attribute] < value:
            return False
    return True
