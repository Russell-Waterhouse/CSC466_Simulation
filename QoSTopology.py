from mininet.topo import Topo

ORG_COUNT = 3
HOST_COUNT = 5


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        """Create the custom network topology"""

        isp_switch = self.addSwitch('s999')
        for org_id in range(ORG_COUNT):
            org_switch = self.addSwitch(f's{org_id}')
            self.addLink(isp_switch, org_switch)
            for host_id in range(HOST_COUNT):
                host = self.addHost(f'h{org_id}_{host_id}')
                self.addLink(host, org_switch)


topos = {'QoSTopology': (lambda: QoSTopology())}
