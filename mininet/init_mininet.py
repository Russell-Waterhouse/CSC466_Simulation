import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util
from QoSTopology import QoSTopology
from TrafficControl import *
from tcp_connections.connection_manager import setup_network_traffic

from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI


def configure_tc(mininet):
    print("==== Configure traffic control ====")
    configure_org_switches(mininet)
    configure_isp(mininet)


def start_traffic(mininet):
    print("==== Setup network traffics ====")
    setup_network_traffic(mininet)


def run_init_shell(mininet):
    print("==== running custom script ====")
    CLI(mininet, script="./mininet/custom_init.sh")


def main():
    setLogLevel("info")

    settings = util.get_settings()["StartupSettings"]

    mininet = Mininet(topo=QoSTopology())
    mininet.start()

    print("==== Dumping host connections ====")
    CLI(mininet, script="./mininet/mininet_init.sh")

    if settings["TrafficControl"]:
        configure_tc(mininet)

    if settings["TrafficSimulation"]:
        start_traffic(mininet)

    if settings["RunCustomScriptOnStart"]:
        run_init_shell(mininet)

    CLI(mininet)
    mininet.stop()


if __name__ == '__main__':
    main()
