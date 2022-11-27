from mininet.topo import Topo
from util import *


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        """Create the custom network topology"""
        settings = get_settings()["RouterInfo"]["SimulationSize"]

        isp_switch = self.addSwitch(gen_isp_name())
        for org_id in range(1, settings["OrgCount"] + 1):
            org_switch = self.addSwitch(gen_switch_name(org_id))
            interface_names = gen_switch_ISP_infname(org_id)
            self.addLink(org_switch, isp_switch,
                         intfName1=interface_names[0], intfName2=interface_names[1])
            for host_id in range(1, settings["HostCount"] + 1):
                host_ip = gen_host_ip(org_id, host_id)
                host = self.addHost(gen_host_name(org_id, host_id), ip=host_ip)
                interface_names = gen_host_switch_infname(org_id, host_id)
                self.addLink(org_switch, host,
                             intfName1=interface_names[0], intfName2=interface_names[1])


topos = {'QoSTopology': (lambda: QoSTopology())}
