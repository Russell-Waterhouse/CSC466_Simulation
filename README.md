# CSC466 Simulation
A repo all about the simulation we will be running on mininet

# About the Configuration

Inspired by the [mininet custom topologies](https://mininet.org/walkthrough/#custom-topologies) section, I have created main.py. 
This sets up the network topology similar to this photo: ![image](https://user-images.githubusercontent.com/39814909/202114359-b1702e19-836d-4b83-9eda-b69eb2584009.png)

# How it runs
Use main.sh to run Mininet
  1) Setup mininet with QoS topology and traffic control. If there is every a failure in this step, use mode 2 to clear the cache before restarting mininet
  2) Clear mininet cache
  3) Only setup QoS topology without traffic control
