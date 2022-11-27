from mininet.topo import Topo
from util import *


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        """Create the custom network topology"""
        settings = get_settings()["RouterInfo"]["SimulationSize"]

        isp_switch = self.addSwitch('s999')
        for org_id in range(settings["OrgCount"]):
            org_switch = self.addSwitch(gen_switch_name(org_id))
            self.addLink(org_switch, isp_switch)
            for host_id in range(settings["HostCount"]):
                host_ip = gen_host_ip(org_id, host_id)
                host = self.addHost(gen_host_name(org_id, host_id), ip=host_ip)
                self.addLink(org_switch, host)


topos = {'QoSTopology': (lambda: QoSTopology())}
