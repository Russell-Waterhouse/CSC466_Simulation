import socket
import sys
import time
import threading

# setting path
sys.path.append('../CSC466_Simulation')

import util

settings = util.get_settings()["NetworkSimulation"]


def listen(host, port, id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Socket Created")
        print(s)
        s.bind((host, port))
        s.listen()
        print('waiting for connections')
        time0 = -1
        while True:
            c, addr = s.accept()
            c.send(bytes.fromhex("00") * settings["PacketByteSize"])  # 0xFF in ascii
            if (time0 == -1):
                time0 = time.time()
            print("Receive packet at time:", time.time() - time0, "at id", id)
            c.close()
    finally:
        s.close()


def main():
    port = util.get_settings()["NetworkSimulation"]["ConnectionPort"]

    if len(sys.argv) < 1:
        print("Please specify the host and port number in the following format"
              "\n$ python client.py <server>")
        exit(0)

    host = sys.argv[1]

    connection1 = threading.Thread(target=listen, args=(host, 8000, "FAST"))
    connection2 = threading.Thread(target=listen, args=(host, 7000, "SLOW"))
    connection1.start()
    connection2.start()


if __name__ == '__main__':
    main()
