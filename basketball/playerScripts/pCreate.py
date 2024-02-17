# Where creation of players is handled
import basketball.leagueSettings.pPhysical as pPhysical  # setStartingPhysicals()
import basketball.leagueSettings.pHeight as pHeight  # heightRoll()
import basketball.leagueSettings.pWeight as pWeight  # getWeightFromModel()
import basketball.leagueSettings.pWingspan as pWingspan  # wingspanRoll()
import basketball.leagueSettings.pAnomaly as pAnomaly  # anomalyRoll()

import basketball.models as models  # BasketballPlayer


# Validate the player creation data
def validatePlayerData(data: dict) -> bool:
    # Check for how many players the user has
    playerCount = models.BasketballPlayer.objects.filter(
        discordUser=data["discord_user"]
    ).count()
    if playerCount >= 1:
        return False


# Player creation function
def createPlayer(discordUser: any, data: dict) -> any:
    # Validate the player creation data
    if not validatePlayerData(data):
        return None
    # Get creation data
    firstName = data["first_name"]
    lastName = data["last_name"]
    position = data["position"]
    secondaryPosition = data["secondary_position"]
    archetype = data["archetype"]
    weightModel = data["weight_model"]
    weight = pWeight.getWeightFromModel(position, weightModel)
    # Create the player object
    player = models.BasketballPlayer(
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
    player = pPhysical.setStartingPhysicals(player)
    # Run player rolls
    player = pAnomaly.anomalyRoll(player)
    # Save the player
    player.save()
    return player
