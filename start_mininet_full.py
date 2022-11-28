from QoSTopology import QoSTopology
from TrafficControl import *

from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.util import dumpNodeConnections


def set_tc(isp_node, org_data):
    # ISP tc
    interfaces = []
    for interface in interfaces:
        setup_prioritization_interface(isp_node, interface)

    org_data = []
    for (node, interface) in org_data:
        setup_delay_interface(node, interface)


def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology())
    mininet.start()

    print("==== Configure traffic control ====")
    configure_org_switches(mininet)
    configure_isp(mininet)

    print("==== Dumping host connections ====")
    CLI(mininet, script="mininet_init.sh")

    CLI(mininet)
    mininet.stop()


if __name__ == '__main__':
    main()
