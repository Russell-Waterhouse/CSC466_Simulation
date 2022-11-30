import socket
import sys
import threading
import random

# setting path
sys.path.append('../CSC466_Simulation')

import time
import util

settings = util.get_settings()["NetworkSimulation"]
port = settings["ConnectionPort"]


def establish_connection(host):
    for packet_id in range(settings["PacketCount"]):
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((host, port))
        c.send(bytes.fromhex("00") * settings["PacketByteSize"])  # 0xFF in bytes
        time.sleep(settings["PacketFrequency"])


def connection_loop(server_ip):
    while True:
        establish_connection(server_ip)


def main():
    if len(sys.argv) < 2:
        print("Please specify the host and port number in the following format"
              "\n$ python client.py <server> ")
        exit(0)

    server_ip = sys.argv[1]
    connection_loop(server_ip)


if __name__ == '__main__':
    main()