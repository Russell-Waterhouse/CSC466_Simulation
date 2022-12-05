# This client only connect to 1 server at 1 port, until it's killed or connection is unavailable
import socket
import sys
import threading
import random

# setting path
sys.path.append('../CSC466_Simulation')

import time
import util
import port_selector

settings = util.get_settings()["NetworkSimulation"]
payload = bytes.fromhex("00") * settings["PacketByteSize"]


def establish_connection(host, port):
    while True:
        try:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect((host, port))
            c.send(payload)
        except ConnectionRefusedError:
            print("Connection refused, terminating thread")
            return 0
        time.sleep(settings["PacketFrequency"])


def main():
    if len(sys.argv) < 1:
        print("Please specify the host and port number in the following format"
              "\n$ python client.py <servers> ")
        exit(0)

    servers = sys.argv[1]
    port = sys.argv[2]
    establish_connection(servers, int(port))


if __name__ == '__main__':
    main()
