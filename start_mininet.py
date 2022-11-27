from QoSTopology import QoSTopology

from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI


def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology())
    mininet.start()
    CLI(mininet)
    mininet.stop()


if __name__ == '__main__':
    main()
