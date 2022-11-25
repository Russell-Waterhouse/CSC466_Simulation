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
        """Create the custom network topology"""

        # Step 1, create ISP router
        isp_router = self.addHost('r999', cls=LinuxRouter, ip='10.0.0.0/24')

        # Step 2, create subnet switches
        s0, s1, s2, s3, s4 = [self.addSwitch(s) for s in ('s0', 's1', 's2', 's3', 's4')]
        org_switches = [s0,s1,s2,s3,s4]


        # Step 3, setup org routers
        r0 = self.addHost('r0', cls=LinuxRouter, ip='10.0.0.1/24')
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.1.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.0.2.1/24')
        r3 = self.addHost('r3', cls=LinuxRouter, ip='10.0.3.1/24')
        r4 = self.addHost('r4', cls=LinuxRouter, ip='10.0.4.1/24')

        # Step 4, setup host-switch links within subnets
        self.addLink(s0, r0, intfName2='r0-eth1', params2={'ip': '10.0.0.1'})
        self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.0.1.1'})
        self.addLink(s2, r2, intfName2='r2-eth1', params2={'ip': '10.0.2.1'})
        self.addLink(s3, r3, intfName2='r3-eth1', params2={'ip': '10.0.3.1'})
        self.addLink(s4, r4, intfName2='r4-eth1', params2={'ip': '10.0.4.1'})

        # Step 5, connect routers together
        self.addLink(isp_router,
                     r0,
                     intfName1='r999-eth1',
                     intfName2='r0-eth3',
                     params1={'ip': '10.100.0.1/24'},
                     params2={'ip': '10.100.0.2/24'})
        self.addLink(isp_router,
                     r1,
                     intfName1='r999-eth2',
                     intfName2='r1-eth3',
                     params1={'ip': '10.100.0.1/24'},
                     params2={'ip': '10.100.0.2/24'})
        self.addLink(isp_router,
                     r2,
                     intfName1='r999-eth3',
                     intfName2='r2-eth3',
                     params1={'ip': '10.100.0.1/24'},
                     params2={'ip': '10.100.0.2/24'})
        self.addLink(isp_router,
                     r3,
                     intfName1='r999-eth4',
                     intfName2='r3-eth3',
                     params1={'ip': '10.100.0.1/24'},
                     params2={'ip': '10.100.0.2/24'})
        self.addLink(isp_router,
                     r4,
                     intfName1='r999-eth5',
                     intfName2='r4-eth3',
                     params1={'ip': '10.100.0.1/24'},
                     params2={'ip': '10.100.0.2/24'})

        for i in range(0, 5):
            # Add hosts and host-switch links
            org_switch = org_switches[i]
            org_num = str(i)
            print("Creating the hosts")
            h0 = self.addHost(name='h0_' + str(i),
                              ip='10.0.' + org_num + '.200/24',
                              defaultRoute='via 10.0.' + org_num + '.1')
            h1 = self.addHost('h1_' + str(i),
                              ip='10.0.' + org_num + '.200/24',
                              defaultRoute='via 10.0.' + org_num + '.1')
            h2 = self.addHost('h2_' + str(i),
                              ip='10.0.' + org_num + '.200/24',
                              defaultRoute='via 10.0.' + org_num + '.1')
            h3 = self.addHost('h3_' + str(i),
                              ip='10.0.' + org_num + '.200/24',
                              defaultRoute='via 10.0.' + org_num + '.1')
            h4 = self.addHost('h4_' + str(i),
                              ip='10.0.' + org_num + '.200/24',
                              defaultRoute='via 10.0.' + org_num + '.1')
            r1 = self.addHost('r' + str(i),
                              ip='10.0.' + org_num + '.200/24',
                              defaultRoute='via 10.0.' + org_num + '.1')
            self.addLink(h0, org_switch)
            self.addLink(h1, org_switch)
            self.addLink(h2, org_switch)
            self.addLink(h3, org_switch)
            self.addLink(h4, org_switch)
            self.addLink(r1, org_switch)


def run():
    "Test linux router"
    topo = QoSTopology()
    net = Mininet( topo=topo )  # controller is used by switches
    net.start()
    info( '*** Routing Table on Router:\n' )
    print(net[ 'r0' ].cmd( 'route' ))
    CLI( net )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    run()



topos = {'QoSTopology': (lambda: QoSTopology())}

