from QoSTopology import QoSTopology

from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.util import dumpNodeConnections

def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology())
    mininet.start()
    print("Dumping host connections")
    dumpNodeConnections(mininet.hosts)
    dumpNodeConnections(mininet.switches)
    CLI(mininet)
    mininet.stop()

if __name__ == '__main__':
    main()
