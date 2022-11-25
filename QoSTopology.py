from mininet.topo import Topo


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        """Create the custom network topology"""

        org_switches = []
        for i in range(0, 5):
            h0 = self.addHost('h0_' + str(i))
            h1 = self.addHost('h1_' + str(i))
            h2 = self.addHost('h2_' + str(i))
            h3 = self.addHost('h3_' + str(i))
            h4 = self.addHost('h4_' + str(i))
            org_switch = self.addSwitch('s' + str(i))
            self.addLink(h0, org_switch)
            self.addLink(h1, org_switch)
            self.addLink(h2, org_switch)
            self.addLink(h3, org_switch)
            self.addLink(h4, org_switch)
            org_switches.append(org_switch)
        isp_switch = self.addSwitch('s999')
        for switch in org_switches:
            self.addLink(isp_switch, switch)


topos = {'QoSTopology': (lambda: QoSTopology())}
