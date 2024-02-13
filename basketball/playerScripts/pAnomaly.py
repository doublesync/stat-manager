import random

# These are anomaly methods that are called when an anomaly is received
def heightAnomaly(player: any) -> any:
    player.vitals["height"] += 3
    return player
def wingspanAnomaly(player: any) -> any:
    player.vitals["wingspan"] += 20
    return player
def verticalAnomaly(player: any) -> any:
    player.physicals["vertical"] = 99
    return player

# Changes the chance of an anomaly occurring
# Each anomaly points to a function that applies the anomaly
anomalyChance: float = 0.01
anomalies: dict[str, callable] = {
    "height": heightAnomaly,
    "vertical": verticalAnomaly,
    "wingspan": wingspanAnomaly,
}

# Rolls for an anomaly
# 1% chance of an anomaly
# If an anomaly is received, choose one at random and apply it
def anomalyRoll(player: any) -> dict | bool:
    receivedAnomaly = random.random() < anomalyChance
    if receivedAnomaly:
        anomalyChosen = random.choice(list(anomalies.keys()))
        anomalyPlayer = anomalies[anomalyChosen](player)
        return anomalyPlayer
    else:
        return False