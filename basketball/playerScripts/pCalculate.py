import random
import basketball.leagueSettings.pSettings as pSettings

from random import choices


def calculateBMI(weight: int, height: int) -> float:
    return round((weight / (height**2)) * 703, 2)


def formatHeight(height: int) -> str:
    return f"{height // 12}'{height % 12}"


def heightRoll(archetype: str, position: str) -> list[int, str, float]:
    heightOdds: dict[int, float] = pSettings.heightOdds[archetype][position]
    roll: int = random.randint(1, 100)
    for _range, height in heightOdds.items():
        if roll in _range:
            return [height, formatHeight(height), None]

# for a in archetypes:
    # for i in range(1000):
    #     for p in positions:
    #         inches, feet, bmi = heightRoll(a, p)
    #         if p not in tally[a]:
    #             tally[a][p] = {}
    #         if not feet in tally[a][p]:
    #             tally[a][p][feet] = 1
    #         else:
    #             tally[a][p][feet] += 1
    # print(a)
    # print(json.dumps(tally[a], indent=2))
