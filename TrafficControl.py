import json


# Read setting from json
def get_settings(file_name="settings.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data


# Configure the org switches so they simulate bad networks
def configure_org_switches(mininet, switch_info=get_settings()["RouterInfo"]["OrgSwitches"]):
    for (switch_name, interface) in switch_info.items():
        print("Configuring org switch =>", switch_name, interface)
        node = mininet[switch_name]
        setup_delay_interface(node, interface)


# Configure the ISP node so all of its interfaces have QoS Traffic control
def configure_isp(isp_node, isp_interfaces=get_settings()["RouterInfo"]["ISPInterfaces"]):
    for interface in isp_interfaces:
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
