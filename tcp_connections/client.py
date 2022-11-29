import socket
import sys
import threading
import random

# setting path
sys.path.append('../CSC466_Simulation')

import time
import util
import payload_generator

settings = util.get_settings()["NetworkSimulation"]
port = settings["ConnectionPort"]


def establish_connection(mode, host):

    payload = payload_generator.generate_payload(mode)
    for packet_id in range(settings["PacketCount"]):
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((host, port))
        c.send(bytes.fromhex(payload) * settings["PacketByteSize"])
        time.sleep(settings["PacketFrequency"])


def connection_loop(mode, servers):
    connections = []
    while True:
        random_servers = random.sample(servers, settings["ParallelConnection"])
        # Start connections
        for server_ip in random_servers:
            connection = threading.Thread(target=establish_connection, args=(mode, server_ip,))
            connection.start()
            connections.append(connection)
        # Wait for connections to finish
        for connection in connections:
            connection.join()


def main():
    if len(sys.argv) < 2:
        print("Please specify the host and port number in the following format"
              "\n$ python client.py <mode, one of {0, 1, 2}> <servers> ")
        exit(0)

    mode = sys.argv[1]
    servers = sys.argv[2:]
    connection_loop(int(mode), servers)


if __name__ == '__main__':
    main()
