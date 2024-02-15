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
    print(f"No height found: {roll} for {archetype} {position}")
