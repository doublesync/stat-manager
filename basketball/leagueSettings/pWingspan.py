import random
from basketball.leagueSettings.pHeight import realRange

# Wingspan odds for players
wingspanOdds: dict[range, str] = {
    realRange(1, 5): 40,
    realRange(6, 10): 45,
    realRange(11, 31): 50,
    realRange(32, 50): 55,
    realRange(51, 60): 60,
    realRange(61, 70): 65,
    realRange(71, 78): 70,
    realRange(79, 84): 75,
    realRange(85, 91): 80,
    realRange(92, 95): 85,
    realRange(96, 98): 90,
    realRange(99, 99): 95,
    realRange(100, 100): 100,
}


# Roll for the players wingspan
def wingspanRoll() -> int:
    roll = random.randint(1, 100)
    for key in wingspanOdds:
        if roll in key:
            wingspan = wingspanOdds[key]
            randomIncrement = random.randint(-3, 3)
            if (wingspan + randomIncrement) > 100:
                return wingspan - randomIncrement
            else:
                return wingspan + randomIncrement
