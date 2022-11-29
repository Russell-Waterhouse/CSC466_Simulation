import socket
import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util
import payload_generator
settings = util.get_settings()["NetworkSimulation"]


def main():
    port = util.get_settings()["NetworkSimulation"]["ConnectionPort"]

    if len(sys.argv) < 2:
        print("Please specify the host and port number in the following format"
              "\n$ python server.py <mode, one of {0, 1, 2}> <server IP address>")
        exit(0)

    mode = int(sys.argv[1])

    host = sys.argv[2]
    payload = payload_generator.generate_payload(mode)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Socket Created")
        print(s)
        s.bind((host, port))
        s.listen()
        print('waiting for connections')
        while True:
            c, addr = s.accept()
            print('connected with', addr)
            c.send(bytes.fromhex(payload) * settings["PacketByteSize"])
            c.close()
    finally:
        s.close()


if __name__ == '__main__':
    main()
