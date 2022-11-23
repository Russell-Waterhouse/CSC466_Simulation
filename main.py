from mininet.topo import Topo
from QoSTopology import QoSTopology

def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology(), controller=None)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    main()
