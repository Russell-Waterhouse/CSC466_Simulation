import sys

# setting path
sys.path.append('../CSC466_Simulation')
from util import *


# *****Deprecated*****
# Configure the org switches so they simulate bad networks
def configure_org_switches_with_settings(mininet, switch_info=get_settings()["RouterInfo"]["OrgSwitches"]):
    for (switch_name, interface) in switch_info.items():
        print("Configuring org switch =>", switch_name, interface)
        node = mininet[switch_name]
        setup_delay_interface(node, interface)


# Configure the org switches so they simulate bad networks
def configure_org_switches(mininet, simulation_size=get_settings()["RouterInfo"]["SimulationSize"]):
    org_count = simulation_size["OrgCount"]
    host_count = simulation_size["HostCount"]
    for org_id in range(org_count):
        for host_id in range(host_count):
            switch_name = get_switch_name(org_id)
            interface = get_switch_ISP_infname(org_id)[0]
            print("Configuring org switch =>", switch_name, interface)
            setup_delay_interface(mininet[switch_name], interface)


# *****Deprecated*****
# Configure the ISP node so all of its interfaces have QoS Traffic control
def configure_isp_with_settings(isp_node, isp_interfaces=get_settings()["RouterInfo"]["ISPInterfaces"]):
    for interface in isp_interfaces:
        print("Configuring ISP interface=>", interface)
        setup_prioritization_interface(isp_node, interface)


# Configure the ISP node so all of its interfaces have QoS Traffic control
def configure_isp(mininet, simulation_size=get_settings()["RouterInfo"]["SimulationSize"]):
    isp_name = get_isp_name()
    isp_node = mininet[isp_name]
    org_count = simulation_size["OrgCount"]
    for org_id in range(org_count):
        interface = get_switch_ISP_infname(org_id)[1]
        print("Configuring ISP interface=>", interface)
        setup_prioritization_interface(isp_node, interface)


# Set up a interface with 3 class network shaping (For ISP node)
def setup_prioritization_interface(node, interface, settings=get_settings()["TrafficControl"]["QoSSettings"]):
    # Setup root qdisc
    command = f"tc qdisc add dev {interface} root handle 1:0 htb default {settings['DefaultID']}"
    print(command)
    node.cmd(command)

    # Setup speed limiter qdisc, default to fast channel
    command = (f"tc class add dev {interface} parent 1:0 classid 1:1 "
               f"htb rate {settings['TotalBandwidth']} ceil {settings['TotalBandwidth']}")
    print(command)
    node.cmd(command)

    # Setup class speed
    for channel_type in [settings['SlowChannel'], settings['MidChannel'], settings['FastChannel']]:
        command = (f"tc class add dev {interface} parent 1:1 classid 1:{channel_type['ID']} "
                   f"htb rate {channel_type['Rate']} ceil {channel_type['Ceil']}")
        print(command)
        node.cmd(command)

    # Setup filters
    for channel_type in [settings['SlowChannel'], settings['MidChannel'], settings['FastChannel']]:
        command = (f"tc filter add dev {interface} parent 1:0 protocol ip prio {channel_type['Prio']} "
                   f"u32 match ip sport {channel_type['Match']} 0xffff flowid 1:{channel_type['ID']}")
        print(command)
        node.cmd(command)

        command = (f"tc filter add dev {interface} parent 1:0 protocol ip prio {channel_type['Prio']} "
                   f"u32 match ip dport {channel_type['Match']} 0xffff flowid 1:{channel_type['ID']}")
        print(command)
        node.cmd(command)


# Set up
def setup_delay_interface(node, interface, settings=get_settings()["TrafficControl"]["OrgSettings"]):
    command = f"tc qdisc add dev {interface} root handle 1:0"
    print(command)
    node.cmd(command)

    command = (f"tc qdisc add dev {interface} parent 1:0 handle 2:0 "
               f"netem delay {settings['OrgDelay']} loss {settings['OrgLost']}")
    print(command)
    node.cmd(command)

    command = (f"tc qdisc add dev {interface} parent 2:0 handle 3:0 "
               f"tbf rate {settings['OrgRate']} ceil {settings['OrgRate']} burst {settings['OrgBurst']} limit {settings['OrgBurstLimit']}")
    print(command)
    node.cmd(command)


# Remove root tc
def clear_tc(node, interface):
    node.cmd(f"tc qdisc del dev {interface} root")
