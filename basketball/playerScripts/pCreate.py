# Where creation of players is handled
import basketball.leagueSettings.pPhysical as pPhysical  # setStartingPhysicals()
import basketball.leagueSettings.pHeight as pHeight  # heightRoll()
import basketball.leagueSettings.pWeight as pWeight  # getWeightFromModel()
import basketball.leagueSettings.pWingspan as pWingspan  # wingspanRoll()
import basketball.leagueSettings.pAnomaly as pAnomaly  # anomalyRoll()

import basketball.models as models  # BasketballPlayer


# Validate the player creation data
def validatePlayerData(discordUser: any, data: dict) -> bool:
    # Check for how many players the user has
    players: any = models.BasketballPlayer.objects.filter(discordUser=discordUser)
    playerCount: int = len(players)
    if playerCount >= 1000:
        return [False, "You have too many players."]


# Player creation function
def createPlayer(discordUser: any, data: dict) -> any:
    # Validate the player creation data
    validated = validatePlayerData(discordUser, data)
    if validated and not validated[0]:
        return validated
    # Get creation data
    firstName: str = data["firstName"]
    lastName: str = data["lastName"]
    position: str = data["position"]
    secondaryPosition: str = data["secondaryPosition"]
    archetype: str = data["archetype"]
    weightModel: str = data["weightModel"]
    weight: int = pWeight.getWeightFromModel(position, weightModel)
    # Create the player object
    player: any = models.BasketballPlayer(
        firstName=firstName,
        lastName=lastName,
        position=position,
        secondaryPosition=secondaryPosition,
        archetype=archetype,
        height=pHeight.heightRoll(archetype, position),
        wingspan=pWingspan.wingspanRoll(),
        weight=weight,
        weightModel=weightModel,
        discordUser=discordUser,
    )
    # Set the starting physicals and attributes
    player: any = pPhysical.setStartingPhysicals(player)
    # Run player rolls
    player: any = pAnomaly.anomalyRoll(player)
    # Save the player
    player.save()
    return [player, "Player created successfully."]
