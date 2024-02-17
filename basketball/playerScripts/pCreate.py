# Where creation of players is handled
import basketball.leagueSettings.pPhysical as pPhysical  # setStartingPhysicals()
import basketball.leagueSettings.pHeight as pHeight  # heightRoll()
import basketball.leagueSettings.pWeight as pWeight  # getWeightFromModel()
import basketball.leagueSettings.pWingspan as pWingspan  # wingspanRoll()
import basketball.leagueSettings.pAnomaly as pAnomaly  # anomalyRoll()

import basketball.models as models  # BasketballPlayer


# Player creation function
def createPlayer(data: dict) -> any:
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
    )
    # Set the starting physicals and attributes
    player = pPhysical.setStartingPhysicals(player)
    # Run player rolls
    player = pAnomaly.anomalyRoll(player)
    # Save the player
    player.save()
    return player
