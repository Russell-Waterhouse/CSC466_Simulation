import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util


def get_other_ips(self_org_id, org_count, host_count):
    result = []
    for org_id in range(org_count):
        if org_id == self_org_id:
            continue
        for host_id in range(host_count):
            result.append(util.get_host_ip(org_id, host_id, False))
    return result


def setup_servers(mininet):
    settings = util.get_settings()["RouterInfo"]["SimulationSize"]
    for org_id in range(settings["OrgCount"]):
        for host_id in range(settings["HostCount"]):
            host_name = util.get_host_name(org_id, host_id)
            host_ip = util.get_host_ip(org_id, host_id, False)
            node = mininet[host_name]
            print(f"Setting up server for {host_name} {host_ip}")
            node.cmd(f"python3 ./tcp_connections/server.py {host_ip} &")


def setup_clients(mininet):
    settings = util.get_settings()["RouterInfo"]["SimulationSize"]
    for org_id in range(settings["OrgCount"]):
        other_ips = get_other_ips(org_id, settings["OrgCount"], settings["HostCount"])
        for host_id in range(settings["HostCount"]):
            for ip in other_ips:
                host_name = util.get_host_name(org_id, host_id)
                node = mininet[host_name]
                print(f"Setting up client for {host_name} {ip}")
                node.cmd(f"python3 ./tcp_connections/client.py {ip} &")


def setup_network_traffic(mininet):
    setup_servers(mininet)
    setup_clients(mininet)
