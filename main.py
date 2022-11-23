from QoSTopology import QoSTopology

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI

def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology(), controller=None)
    mininet.start()
    mininet[ 'h0_0' ].cmd( 'ping h2_2' )
    CLI(mininet)
    mininet.stop()

if __name__ == '__main__':
    main()
