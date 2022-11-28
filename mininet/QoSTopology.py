import sys
# setting path
sys.path.append('../CSC466_Simulation')

from mininet.topo import Topo
from util import *


class QoSTopology(Topo):
    """Topology of network test"""

    def build(self):
        """Create the custom network topology"""
        settings = get_settings()["RouterInfo"]["SimulationSize"]

        isp_switch = self.addSwitch(get_isp_name())
        for org_id in range(settings["OrgCount"]):
            org_switch = self.addSwitch(get_switch_name(org_id))
            interface_names = get_switch_ISP_infname(org_id)
            print(interface_names)
            self.addLink(org_switch, isp_switch,
                         intfName1=interface_names[0], intfName2=interface_names[1])
            for host_id in range(settings["HostCount"]):
                host_ip = get_host_ip(org_id, host_id)
                host = self.addHost(get_host_name(org_id, host_id), ip=host_ip)
                interface_names = get_host_switch_infname(org_id, host_id)
                self.addLink(host, org_switch,
                             intfName1=interface_names[0], intfName2=interface_names[1])


topos = {'QoSTopology': (lambda: QoSTopology())}
