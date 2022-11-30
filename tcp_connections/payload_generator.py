import random
import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util
settings = util.get_settings()["NetworkSimulation"]
weights = settings["PayloadWeights"]
total_weight = weights["00"] + weights["11"] + weights["01"]


def generate_payload(mode:int) -> str:
    if mode == 0:
        payload = "00"  # 0b00000000
    elif mode == 1:
        payload = "FF"  # 0b11111111
    elif mode == 2:
        payload = "55"  # 0b01010101
    else:
        raise ValueError(f"Mode in client.py must be 0, 1, or 2, but instead was {mode}")
    return payload * settings["PacketByteSize"]


def select_mode() -> int:
    weight_buffer = total_weight
    for (mode, weight) in weights.items():
        weight_buffer -= weight
        if weight < 0:
            return mode
    return 0
