from mininet.topo import Topo
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI


# Taken from mininet examples
class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        defaultIP = '192.168.1.1/24'  # IP address for r0-eth1
        router = self.addNode('r0', cls=LinuxRouter, ip=defaultIP)

        s1, s2, s3 = [self.addSwitch(s) for s in ('s1', 's2', 's3')]

        self.addLink(s1, router, intfName2='r0-eth1',
                     params2={'ip': defaultIP})  # for clarity
        self.addLink(s2, router, intfName2='r0-eth2',
                     params2={'ip': '172.16.0.1/12'})
        self.addLink(s3, router, intfName2='r0-eth3',
                     params2={'ip': '10.0.0.1/8'})

        h1 = self.addHost('h1', ip='192.168.1.100/24',
                          defaultRoute='via 192.168.1.1')
        h2 = self.addHost('h2', ip='172.16.0.100/12',
                          defaultRoute='via 172.16.0.1')
        h3 = self.addHost('h3', ip='10.0.0.100/8',
                          defaultRoute='via 10.0.0.1')

        for h, s in [(h1, s1), (h2, s2), (h3, s3)]:
            self.addLink(h, s)

        """Create the custom network topology"""

        # org_switches = []
        # org_routers = []
        # for i in range(0, 5):
        #     h0 = self.addHost('h0_' + str(i))
        #     h1 = self.addHost('h1_' + str(i))
        #     h2 = self.addHost('h2_' + str(i))
        #     h3 = self.addHost('h3_' + str(i))
        #     h4 = self.addHost('h4_' + str(i))
        #     r1 = self.addHost('r' + str(i))
        #     self.setup_router(r1)
        #     org_switch = self.addSwitch('s' + str(i))
        #     self.addLink(h0, org_switch)
        #     self.addLink(h1, org_switch)
        #     self.addLink(h2, org_switch)
        #     self.addLink(h3, org_switch)
        #     self.addLink(h4, org_switch)
        #     self.addLink(r1, org_switch)
        #     org_switches.append(org_switch)
        #     org_routers.append(r1)
        # isp_router = self.addHost('r999')
        # self.setup_router(isp_router)
        # for router in org_routers:
        #     self.addLink(isp_router, router)


def run():
    "Test linux router"
    topo = QoSTopology()
    net = Mininet( topo=topo )  # controller is used by s1-s3
    net.start()
    info( '*** Routing Table on Router:\n' )
    print(net[ 'r0' ].cmd( 'route' ))
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()

# topos = {'QoSTopology': (lambda: QoSTopology())}
