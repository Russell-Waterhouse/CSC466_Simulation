from QoSTopology import QoSTopology
from TrafficControl import *

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

    print("==== Dumping host connections ====")
    CLI(mininet, script="mininet_init.sh")

    CLI(mininet)
    mininet.stop()


if __name__ == '__main__':
    main()