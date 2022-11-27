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
    node.cmd(f"tc qdisc add dev {interface} root handle 1:0 htb default 30")

    # Setup speed limiter qdisc
    node.cmd(f'''tc class add dev {interface} parent 1:0 classid 1:1 \
    htb rate {settings['TotalBandwidth']} ceil {settings['TotalBandwidth']}''')

    # Setup class speed
    for (rate, ceil, htb_id) in [
        (settings['SlowRate'], settings['SlowCeil'], settings['SlowID']),
        (settings['MidRate'], settings['MidCeil'], settings['MidID']),
        (settings['FastRate'], settings['FastCeil'], settings['FastID'])
    ]:
        node.cmd(f'''tc class add dev {interface} parent 1:1 classid {htb_id} \
        htb rate {rate} ceil {ceil}''')

    # Setup filters TODO: make match statement
    # for (port, flow_id) in [
    #     (settings['SlowPort'], settings['SlowID']),
    #     (settings['MidPort'], settings['MidID']),
    #     (settings['FastPort'], settings['FastID'])
    # ]:
    #     node.cmd(
    #         f'''tc filter add dev {interface} parent 1:0 protocol ip prio 10
    #         u32 match port {port} flowid {flow_id}
    #         '''
    #     )


# Set up
def setup_delay_interface(node, interface, settings=get_settings()["TrafficControl"]["OrgSettings"]):
    node.cmd(
        f'''tc qdisc add dev {interface} root handle 1:0 \
        netem delay {settings['OrgDelay']} loss {settings['OrgLost']}'''
    )
    node.cmd(
        f'''tc qdisc add dev {interface} parent 1:0 handle 2:0 \
        tbf rate {settings['OrgRate']} burst {settings['OrgBurst']} limit {settings['OrgBurstLimit']}'''
    )


# Remove root tc
def clear_tc(node, interface):
    node.cmd(f"tc qdisc del dev {interface} root")
