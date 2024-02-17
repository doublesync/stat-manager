import random
import basketball.leagueSettings.pHeight as pHeight

from random import choices


def calculateBMI(weight: int, height: int) -> float:
    return round((weight / (height**2)) * 703, 2)


def formatHeight(height: int) -> str:
    return f"{height // 12}'{height % 12}"
