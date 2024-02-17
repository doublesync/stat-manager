from django.test import TestCase


# Create your tests here.
def test():
    import json
    from basketball.leagueSettings.pPhysical import setStartingPhysicals
    from basketball.models import BasketballPlayer

    player = BasketballPlayer.objects.get(pk=1)
    print(json.dumps(player.attributes, indent=2))
    updatedPlayer = setStartingPhysicals(player)
    print(json.dumps(updatedPlayer.attributes, indent=2))
    print("Test ran successfully")
