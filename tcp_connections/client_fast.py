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
    for packet_id in range(settings["PacketCount"]):
        try:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect((host, port))
            c.send(payload)
        except ConnectionRefusedError:
            print("Connection refused, terminating thread")
            return 0
        time.sleep(settings["PacketFrequency"])


def connection_loop(servers):
    connections = []
    while True:
        server_ip = servers[0]
        # Start connections
        port = port_selector.generate_port_high()
        print(f"Connection to {server_ip} at {port}")
        connection = threading.Thread(target=establish_connection, args=(server_ip, port))
        connection.start()
        connections.append(connection)
        # Wait for connections to finish
        for connection in connections:
            connection.join()


def main():
    if len(sys.argv) < 1:
        print("Please specify the host and port number in the following format"
              "\n$ python client_slow.py <servers> ")
        exit(0)

    servers = sys.argv[1:]
    connection_loop(servers)


if __name__ == '__main__':
    main()
