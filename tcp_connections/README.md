# CSC466 Custom Packet Creation

## What is this?
This is a proof of concept of a script to send customized TCP packets 
in a simulated networking environment.  
It will send a custom packet every 5 seconds. 

## How to use it
On the server:
```
$ server.py <port number to receive connections on>
```

On the Client: 
```
$ client.py <host ip running server.py> <port number on server> 
```