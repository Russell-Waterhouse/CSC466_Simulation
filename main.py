from QoSTopology import QoSTopology

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI

def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology(), controller=None)
    mininet.start()
    CLI(mininet)
    mininet.stop()

if __name__ == '__main__':
    main()
