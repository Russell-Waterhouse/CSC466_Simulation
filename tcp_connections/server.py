import socket
import sys
import threading

# setting path
sys.path.append('../CSC466_Simulation')

import util
import port_selector

settings = util.get_settings()["NetworkSimulation"]
payload = bytes.fromhex("ff") * settings["PacketByteSize"]


def start_listening(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Socket Created")
        print(s)
        s.bind((host, port))
        s.listen()
        print('waiting for connections')
        while True:
            c, addr = s.accept()
            if addr[0] != settings["allowList"]:
                c.close()
            else:
                print('connected with', addr)
                c.send(payload)
                c.close()
    finally:
        s.close()


def main():
    if len(sys.argv) <= 1:
        print("Please specify the host number in the following format"
              "\n$ python client_slow.py <server> ")
        exit(0)

    host = sys.argv[1]
    for port in port_selector.ports:
        thread = threading.Thread(target=start_listening, args=(host, int(port)))
        thread.start()


if __name__ == '__main__':
    main()
