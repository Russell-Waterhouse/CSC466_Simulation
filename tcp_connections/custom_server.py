import socket
import sys

# setting path
sys.path.append('../CSC466_Simulation')

import util
settings = util.get_settings()["NetworkSimulation"]

def main():
    port = util.get_settings()["NetworkSimulation"]["ConnectionPort"]

    if len(sys.argv) < 1:
        print("Please specify the host and port number in the following format"
              "\n$ python client.py <server>")
        exit(0)

    host = sys.argv[1]

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
            c.send(bytes.fromhex("00") * settings["PacketByteSize"])  # 0xFF in ascii
            c.close()
    finally:
        s.close()


if __name__ == '__main__':
    main()