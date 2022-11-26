# CSC466 Simulation
A repo all about the simulation we will be running on mininet

# About the Configuration

Inspired by the [mininet custom topologies](https://mininet.org/walkthrough/#custom-topologies) section, I have created main.py. 
This sets up the network topology similar to this photo: 
![image](https://user-images.githubusercontent.com/39814909/204109878-a6d22fa5-a9d5-494a-8810-af2b127b1687.png)

# How it runs
Use main.sh to run Mininet
  1) Setup mininet with QoS topology and traffic control. If there is every a failure in this step, use mode 2 to clear the cache before restarting mininet
  2) Clear mininet cache
  3) Only setup QoS topology without traffic control
