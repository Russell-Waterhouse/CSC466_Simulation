import socket
import sys

if len(sys.argv) < 2:
    print("Please specify the host and port number in the following format"
          "\n$ python client.py <server> <port>")
    exit(0)

port = int(sys.argv[2])
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
        # name = c.recv(1024).decode()dd
        print('connected with', addr)
        c.send(bytes.fromhex("FF"))  # 0xFF in ascii
        c.close()
finally:
    s.close()
