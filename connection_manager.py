import util


def setup_network_traffic(mininet):
    settings = util.get_settings()["RouterInfo"]["SimulationSize"]
    for org_id in range(settings["OrgCount"]):
        for host_id in range(settings["HostCount"]):
            host_name = util.get_host_name(org_id, host_id)
            host_ip = util.get_host_ip(org_id, host_id, False)
            node = mininet[host_name]
            print(f"Setting up {host_name} {host_ip}")
            node.cmd(f"python3 ./tcp_connections/server.py {host_ip} 8080 &")
