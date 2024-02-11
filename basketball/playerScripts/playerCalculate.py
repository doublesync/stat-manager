import random
import basketball.leagueSettings.playerSettings as playerSettings

from random import choices
from typing import Dict


def calculateBMI(weight: int, height: int) -> float:
    return round((weight / (height ** 2)) * 703, 2)

def formatHeight(height: int) -> str:
    return f"{height // 12}'{height % 12}"

def heightRoll(position: str) -> [int, str, float]:
    heightWeights: Dict[int, float] = playerSettings.heightWeights[position]
    chosenHeight: int = choices(list(heightWeights.keys()), list(heightWeights.values()))[0]
    return [
        chosenHeight, 
        formatHeight(chosenHeight), 
        calculateBMI(random.randint(200, 300), chosenHeight)
    ]