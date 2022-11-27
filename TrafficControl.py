import json


def U32(interface, parent): return f"tc filter add dev {interface} protocol ip parent {parent} prio 1 u32"


def filter_command(port):
    return f"u32 match ip sport {port}"


def get_settings(file_name="settings.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data


def setup_interface(node, interface):
    settings = get_settings()["TrafficControl"]

    # Setup root qdisc
    node.cmd(f"tc qdisc add dev {interface} root handle 1:0 htb default 30")

    # Setup speed limiter qdisc
    node.cmd(
        f'''tc qdisc add dev {interface} parent 1:0 classid 1:1 htb 
        rate {settings['TotalBandwidth']} ceil {settings['TotalBandwidth']}'''
    )

    # Setup class speed
    node.cmd(
        f'''tc qdisc add dev {interface} parent 1:1 classid 1:10 htb 
        rate {settings['SlowRate']} ceil {settings['SlowCeil']}'''
    )
    node.cmd(
        f'''tc qdisc add dev {interface} parent 1:1 classid 1:10 htb 
        rate {settings['MidRate']} ceil {settings['MidCeil']}'''
    )
    node.cmd(
        f'''tc qdisc add dev {interface} parent 1:1 classid 1:10 htb 
        rate {settings['FastRate']} ceil {settings['FastCeil']}'''
    )

    # Setup filters
    node.cmd(
        f'''tc filter add dev {interface} protocol ip parent 1:0 prio 1 u32'''
    )