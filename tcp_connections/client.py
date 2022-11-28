import socket
import sys
import time

if len(sys.argv) < 3:
    print("Please specify the host and port number in the following format"
          "\n$ python client.py <server> <port>")
    exit(0)

port = int(sys.argv[2])
host = sys.argv[1]

while True:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))
    c.send(bytes.fromhex("FF"))  # 0xFF in bytes
    print("sent bytes")
    time.sleep(5)
