import json


# Read setting from json
def get_settings(file_name="settings.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data


def gen_isp_name(): return "s999"


# Generate the org switch name by org id
def gen_switch_name(org_id): return f"s{org_id + 1}"


# Generate the host name by org id and host id
def gen_host_name(org_id, host_id): return f"h{org_id + 1}_{host_id + 1}"


# Generate the host ip by org id and host id
def gen_host_ip(org_id, host_id): return f"10.0.{org_id + 1}.{host_id + 1}/48"


# Generate the org switch to isp interface name by org id
# Returns (switch to isp, isp to switch)
def gen_switch_ISP_infname(org_id): return f"{gen_switch_name(org_id)}-{gen_isp_name()}", f"{gen_isp_name()}-{gen_switch_name(org_id)}"


# Generate the org host to switch interface name by org id
# Returns (host to switch, switch to host)
def gen_host_switch_infname(org_id,
                            host_id): return f"{gen_host_name(org_id, host_id)}-{gen_switch_name(org_id)}", f"{gen_switch_name(org_id)}-{gen_host_name(org_id, host_id)}"
