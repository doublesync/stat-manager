from basketabll.leagueSettings.pHeight import realRange

# Starting attributes depending on the players build will live here.
physicalAttributes: list = [
    "Speed",
    "Acceleration",
    "Vertical",
    "Strength",
    "Speed with Ball",
]

startingAttributes: dict[str, dict[str, int]] = {
    "PG": {
        "Driving Layup": 75,
        "Post Fade": 40,
        "Post Hook": 40,
        "Post Moves": 40,
        "Draw Foul": 50,
        "Close Shot": 60,
        "Midrange Shot": 75,
        "3pt Shot": 70,
        "Free Throw": 75,
        "Ball Control": 75,
        "Passing IQ": 75,
        "Pass Accuracy": 75,
        "Offensive Rebound": 40,
        "Standing Dunk": 40,
        "Driving Dunk": 60,
        "Shot IQ": 60,
        "Passing Vision": 75,
        "Hands": 70,
        "Defensive Rebound": 40,
        "Interior Defense": 40,
        "Perimeter Defense": 75,
        "Block": 40,
        "Steal": 60,
        "Lateral Quickness": 70,
        "Speed with Ball": 75,
        "Hustle": 75,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense IQ": 60,
        "Offensive Consistency": 60,
        "Intangibles": 70,
        "Speed": 83,
        "Acceleration": 80,
        "Vertical": 70,
        "Strength": 60,
    },
    "SG": {
        "Driving Layup": 70,
        "Post Fade": 40,
        "Post Hook": 40,
        "Post Moves": 40,
        "Draw Foul": 50,
        "Close Shot": 65,
        "Midrange Shot": 75,
        "3pt Shot": 75,
        "Free Throw": 75,
        "Ball Control": 65,
        "Passing IQ": 60,
        "Pass Accuracy": 60,
        "Offensive Rebound": 40,
        "Standing Dunk": 40,
        "Driving Dunk": 70,
        "Shot IQ": 60,
        "Passing Vision": 65,
        "Hands": 70,
        "Defensive Rebound": 50,
        "Interior Defense": 50,
        "Perimeter Defense": 70,
        "Block": 40,
        "Steal": 60,
        "Lateral Quickness": 65,
        "Speed with Ball": 70,
        "Hustle": 70,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense IQ": 60,
        "Offensive Consistency": 60,
        "Intangibles": 70,
        "Speed": 79,
        "Acceleration": 75,
        "Vertical": 65,
        "Strength": 65,
    },
    "SF": {
        "Driving Layup": 70,
        "Post Fade": 50,
        "Post Hook": 40,
        "Post Moves": 50,
        "Draw Foul": 50,
        "Close Shot": 70,
        "Midrange Shot": 70,
        "3pt Shot": 70,
        "Free Throw": 70,
        "Ball Control": 65,
        "Passing IQ": 60,
        "Pass Accuracy": 60,
        "Offensive Rebound": 40,
        "Standing Dunk": 50,
        "Driving Dunk": 70,
        "Shot IQ": 60,
        "Passing Vision": 60,
        "Hands": 65,
        "Defensive Rebound": 60,
        "Interior Defense": 55,
        "Perimeter Defense": 65,
        "Block": 50,
        "Steal": 60,
        "Lateral Quickness": 60,
        "Speed with Ball": 65,
        "Hustle": 70,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense IQ": 60,
        "Offensive Consistency": 60,
        "Intangibles": 70,
        "Speed": 75,
        "Acceleration": 70,
        "Vertical": 60,
        "Strength": 70,
    },
    "PF": {
        "Driving Layup": 65,
        "Post Fade": 65,
        "Post Hook": 65,
        "Post Moves": 65,
        "Draw Foul": 50,
        "Close Shot": 75,
        "Midrange Shot": 65,
        "3pt Shot": 65,
        "Free Throw": 65,
        "Ball Control": 60,
        "Passing IQ": 55,
        "Pass Accuracy": 55,
        "Offensive Rebound": 60,
        "Standing Dunk": 70,
        "Driving Dunk": 65,
        "Shot IQ": 60,
        "Passing Vision": 55,
        "Hands": 60,
        "Defensive Rebound": 70,
        "Interior Defense": 65,
        "Perimeter Defense": 55,
        "Block": 65,
        "Steal": 60,
        "Lateral Quickness": 55,
        "Speed with Ball": 60,
        "Hustle": 65,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense IQ": 65,
        "Offensive Consistency": 60,
        "Intangibles": 70,
        "Speed": 68,
        "Acceleration": 65,
        "Vertical": 60,
        "Strength": 75,
    },
    "C": {
        "Driving Layup": 60,
        "Post Fade": 70,
        "Post Hook": 70,
        "Post Moves": 70,
        "Draw Foul": 50,
        "Close Shot": 75,
        "Midrange Shot": 60,
        "3pt Shot": 60,
        "Free Throw": 60,
        "Ball Control": 55,
        "Passing IQ": 50,
        "Pass Accuracy": 50,
        "Offensive Rebound": 65,
        "Standing Dunk": 75,
        "Driving Dunk": 65,
        "Shot IQ": 60,
        "Passing Vision": 50,
        "Hands": 60,
        "Defensive Rebound": 75,
        "Interior Defense": 70,
        "Perimeter Defense": 50,
        "Block": 70,
        "Steal": 60,
        "Lateral Quickness": 50,
        "Speed with Ball": 55,
        "Hustle": 60,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense IQ": 65,
        "Offensive Consistency": 60,
        "Intangibles": 70,
        "Speed": 60,
        "Acceleration": 60,
        "Vertical": 60,
        "Strength": 80,
    },
}

attributeCategories: dict[str, list[str]] = {
    "Shooting": [
        "Post Fade",
        "Post Hook",
        "Post Moves",
        "Midrange Shot",
        "3pt Shot",
        "Free Throw",
        "Offensive Consistency",
    ],
    "Playmaking": [
        "Ball Control",
        "Passing IQ",
        "Pass Accuracy",
        "Shot IQ",
        "Passing Vision",
        "Hands",
    ],
    "Finishing": [
        "Draw Foul",
        "Driving Layup",
        "Close Shot",
        "Standing Dunk",
        "Driving Dunk",
    ],
    "Defensive": [
        "Offensive Rebound",
        "Defensive Rebound",
        "Interior Defense",
        "Perimeter Defense",
        "Block",
        "Steal",
        "Hustle",
        "Pass Perception",
        "Defensive Consistency",
        "Help Defense IQ",
    ],
    "Physical": [
        "Speed",
        "Acceleration",
        "Vertical",
        "Strength",
        "Lateral Quickness",
        "Speed with Ball",
    ],
}

# Starting attributes are set in pPhysical.py [!]

attributePrices: dict[str, dict[range, int]] = {
    "proficient": {
        realRange(0, 74): 1,
        realRange(75, 79): 2,
        realRange(80, 84): 4,
        realRange(85, 89): 5,
        realRange(90, 94): 8,
        realRange(95, 99): 10,
    },
    "normal": {
        realRange(0, 64): 1,
        realRange(65, 74): 2,
        realRange(75, 79): 4,
        realRange(80, 84): 5,
        realRange(85, 89): 7,
        realRange(90, 94): 10,
        realRange(95, 99): 11,
    }
}

attributeProficiencies: dict[str, list[str]] = {
  "Giant": [],
  "Skilled": [],
  "Athletic": [],
}

def checkProficiency(archetype: str, attribute: str) -> str:
  proficiency: list = attributeProficiencies[archetype]
  if attribute in proficiency:
    return "Proficient"
  else:
    return "Normal"

def checkAttributePrice(archetype: str, attribute: str, startLevel: int, endLevel: int) -> int:
  cost: int = 0
  proficiency: str = checkProficiency(archetype, attribute)
  for i in range(startLevel + 1, endLevel + 1):
    for priceRange in attributePrices[proficiency]:
      if i in priceRange:
        print(f"{i} will cost user {attributePrices[proficiency][priceRange]}")
        cost += attributePrices[proficiency][priceRange]
        continue
  return cost
