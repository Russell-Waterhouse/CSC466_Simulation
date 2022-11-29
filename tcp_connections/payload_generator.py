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
    return payload


def select_mode() -> int:
    mode = random.randrange(0, total_weight)
    range_00 = range(0, weights["00"])
    range_11 = range(weights["00"], weights["00"] + weights["11"])
    range_01 = range(weights["00"] + weights["11"], weights["00"] + weights["11"] + weights["01"])
    if mode in range_00:
        return 0
    if mode in range_11:
        return 1
    if mode in range_01:
        return 2
