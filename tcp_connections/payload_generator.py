import random
import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util

settings = util.get_settings()["NetworkSimulation"]
weights = settings["PayloadWeights"]
total_weight = weights["00"] + weights["11"] + weights["01"]


def generate_payload() -> int:
    weight_buffer = random.randrange(total_weight)
    for (payload, weight) in weights.items():
        weight_buffer -= weight
        if weight_buffer < 0:
            return payload * settings["PacketByteSize"]
    return "00" * settings["PacketByteSize"]
