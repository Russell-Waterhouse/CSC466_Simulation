from QoSTopology import QoSTopology
from TrafficControl import *
from tcp_connections.connection_manager import setup_network_traffic

from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI


def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology())
    mininet.start()

    print("==== Configure traffic control ====")
    configure_org_switches(mininet)
    configure_isp(mininet)

    print("==== Setup network traffics ====")
    setup_network_traffic(mininet)

    print("==== Dumping host connections ====")
    CLI(mininet, script="mininet_init.sh")

    CLI(mininet)
    mininet.stop()


if __name__ == '__main__':
    main()
