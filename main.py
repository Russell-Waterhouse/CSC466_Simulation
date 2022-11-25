from QoSTopology import QoSTopology

from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.util import dumpNodeConnections


def set_isp_tc(mininet):
    isp_ip = "s999"

    total_bandwidth = 100
    slow_bandwidth = 30
    mid_bandwidth = 50
    fast_bandwidth = 80

    interfaces = []
    for interface in interfaces:
        mininet[isp_ip].cmd(f"tc qdisc add dev {interface} root handle 1:0 htb default 30")
        mininet[isp_ip].cmd(
            f"tc qdisc add dev {interface} parent 1:0 classid 1:1 htb rate {total_bandwidth}mbit ceil {total_bandwidth}mbit")

        mininet[isp_ip].cmd(
            f"tc qdisc add dev {interface} parent 1:1 classid 2:10 htb rate {slow_bandwidth}mbit ceil {mid_bandwidth}mbit")
        mininet[isp_ip].cmd(
            f"tc qdisc add dev {interface} parent 1:1 classid 2:20 htb rate {mid_bandwidth}mbit ceil {fast_bandwidth}mbit")
        mininet[isp_ip].cmd(
            f"tc qdisc add dev {interface} parent 1:1 classid 2:30 htb rate {fast_bandwidth}mbit ceil {total_bandwidth}mbit")


def setup_org_tc(mininet):
    org_ips = ["s0", "s1", "s2", "s3", "s4", "s5"]
    for org_ip in org_ips:
        interface = "todo"
        mininet[org_ip].cmd(f"tc qdisc add dev {interface} root netem delay 100ms 10ms loss 10%")


def main():
    setLogLevel("info")
    mininet = Mininet(topo=QoSTopology())
    mininet.start()

    print("==== Dumping host connections ====")
    dumpNodeConnections(mininet.hosts)
    dumpNodeConnections(mininet.switches)

    print("==== Configure traffic control ====")
    #setup_org_tc(mininet)
    #set_isp_tc(mininet)

    CLI(mininet)
    mininet.stop()


if __name__ == '__main__':
    main()
