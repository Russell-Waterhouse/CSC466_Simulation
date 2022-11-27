import json


# Read setting from json
def get_settings(file_name="settings.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data


# Generate the org switch name by org id
def gen_switch_name(org_id): return f"s{org_id}"


# Generate the host name by org id and host id
def gen_host_name(org_id, host_id): return f"h{org_id}_{host_id}"


# Generate the host ip by org id and host id
def gen_host_ip(org_id, host_id): return f"10.0.{org_id}.{host_id + 1}/48"
