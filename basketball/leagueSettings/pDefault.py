# Django model choices
positionChoices: list[str] = ["PG", "SG", "SF", "PF", "C"]
archetypeChoices: list[str] = ["Skilled", "Athletic", "Giant"]


# Default callables for models
def defaultAttributes() -> dict[str, int]:
    return {}


def defaultBadges() -> dict[str, int]:
    return {}


def defaultTendencies() -> dict[str, int]:
    return {}
