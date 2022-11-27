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
            self.addLink(org_switch, isp_switch)
            for host_id in range(HOST_COUNT):
                host_ip = f"10.0.{org_id}.{host_id+1}/48"
                host = self.addHost(f'h{org_id}_{host_id}', ip=host_ip)
                self.addLink(org_switch, host)


topos = {'QoSTopology': (lambda: QoSTopology())}
