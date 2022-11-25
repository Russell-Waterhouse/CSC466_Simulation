from mininet.topo import Topo
from mininet.node import Node

# The number of organizations and the number of hosts
ORG_COUNT = 1
HOST_COUNT = 3

# General ip setup for org K => 10.K.PREFIX.ID
HOST_PREFIX = 0
SWITCH_PREFIX = 1
ROUTER_PREFIX = 2


# Taken from mininet examples
class LinuxRouter(Node):
    # A Node with IP forwarding enabled.

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable forwarding on the router
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        """Create the custom network topology"""

        # Step 1, create ISP router
        isp_ip = "10.0.0.0/24"
        isp_router = self.addHost('r999', cls=LinuxRouter, ip=isp_ip)

        # Step 2, setup orgs
        for org_id in range(ORG_COUNT):
            # Create the router e.g. for org K => rK, 10.K.1.0
            router_ip = f'10.{org_id}.{ROUTER_PREFIX}.0/24'
            router_obj = self.addHost(f'r{org_id}', cls=LinuxRouter, ip=router_ip)

            # Connect the router to the ISP
            self.addLink(isp_router, router_obj,
                         intfName1=f'r999-eth{org_id}', intfName2=f'r{org_id}-eth2',
                         params1={'ip': router_ip}, params2={'ip': isp_ip})

            # Create the switch e.g. for org K => sK, 10.K.2.0
            switch_ip = f'10.{org_id}.{SWITCH_PREFIX}.0/24'
            switch_obj = self.addSwitch(f"s{org_id}")

            # Connect the router and the switch in a two-way connection
            self.addLink(router_obj, switch_obj,
                         intfName2=f'r{org_id}-eth1',
                         params2={'ip': router_ip})

            # Set up the host
            for host_id in range(HOST_COUNT):
                # Create the host e.g. for org K host H => hK_H, 10.K.3.10H
                host_ip = f'10.{org_id}.{HOST_PREFIX}.10{host_id}/24'
                host_obj = self.addHost(f'h{org_id}_{host_id}',
                                        ip=host_ip,
                                        defaultRoute=f'via {router_ip}')

                # Connect the host to it's switch
                self.addLink(host_obj, switch_obj,
                             intfName2=f'h{host_id}-eth1',
                             params2={'ip': host_ip})


topos = {'QoSTopology': (lambda: QoSTopology())}
