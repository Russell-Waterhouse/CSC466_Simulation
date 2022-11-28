import json


# Read setting from json
def get_settings(file_name="settings.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data


def get_isp_name(): return "s999"


# Generate the org switch name by org id
def get_switch_name(org_id): return f"s{org_id + 1}"


# Generate the host name by org id and host id
def get_host_name(org_id, host_id): return f"h{org_id + 1}_{host_id + 1}"


# Generate the host ip by org id and host id
def get_host_ip(org_id, host_id, with_prefix=True):
    ip = f"10.0.{org_id + 1}.{host_id + 1}"
    if with_prefix:
        ip += "/48"
    print(ip)
    return ip


# Generate the org switch to isp interface name by org id
# Returns (switch to isp, isp to switch)
def get_switch_ISP_infname(org_id):
    return f"{get_switch_name(org_id)}-eth{get_isp_name()}", f"eth{get_isp_name()}-{get_switch_name(org_id)}"


# Generate the org host to switch interface name by org id
# Returns (host to switch, switch to host)
def get_host_switch_infname(org_id,
                            host_id): return f"{get_host_name(org_id, host_id)}-{get_switch_name(org_id)}", f"{get_switch_name(org_id)}-{get_host_name(org_id, host_id)}"
