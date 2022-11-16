# CSC466 Simulation
A repo all about the simulation we will be running on mininet

# About the Configuration

Inspired by the [mininet custom topologies](https://mininet.org/walkthrough/#custom-topologies) section, I have created main.py. 
This sets up the network topology similar to this photo: ![image](https://user-images.githubusercontent.com/39814909/202114359-b1702e19-836d-4b83-9eda-b69eb2584009.png)

# How it runs
To run a ping test of this network topology, simply run the following command. 
```
$ sudo mn --custom ./main.py --topo mytopo --test pingall
```

To run with logged output, run the command as follows: 
```
$ sudo mn --custom ./main.py --topo mytopo --test pingall > test1.log 2>test2.log
```
The output will be in test2.log
