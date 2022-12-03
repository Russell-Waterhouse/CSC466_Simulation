import random
import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util

settings = util.get_settings()["NetworkSimulation"]
weights = settings["ChannelWeights"]
weights = [weights["Slow"], weights["Mid"], weights["Fast"]]
total_weight = sum(weights)

port_settings = util.get_settings()["TrafficControl"]["QoSSettings"]
ports = [port_settings["SlowChannel"], port_settings["MidChannel"], port_settings["FastChannel"]]
ports = [s["Match"] for s in ports]


def generate_port_nominal() -> int:
    weight_buffer = random.randrange(total_weight)
    for (port, weight) in zip(ports, weights):
        weight_buffer -= weight
        if weight_buffer < 0:
            return int(port)
    return ports[0]


def generate_port_high() -> int:
    return int(port_settings["FastChannel"]["Match"])
