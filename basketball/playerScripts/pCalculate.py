import random
import basketball.leagueSettings.pSettings as pSettings

from random import choices

def calculateBMI(weight: int, height: int) -> float:
    return round((weight / (height ** 2)) * 703, 2)

def formatHeight(height: int) -> str:
    return f"{height // 12}'{height % 12}"

def heightRoll(position: str) -> list[int, str, float]:
    heightOdds: dict[int, float] = pSettings.heightOdds[position]
    chosenHeight: int = choices(list(heightOdds.keys()), list(heightOdds.values()))[0]
    return [
        chosenHeight, 
        formatHeight(chosenHeight), 
        calculateBMI(random.randint(200, 300), chosenHeight)
    ]