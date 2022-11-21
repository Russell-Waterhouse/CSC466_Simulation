#!/bin/bash

Interfaces=s999-eth1,s999-eth2,s999-eth3,s999-eth4,s999-eth5

#Max bandwidth per organization
OrgRateLimit=150mbit
#Total amount of bandwidth available
TotalBandWidth=500mbit

StartTC(){
	echo "== Starting TC =="

	for Interface in ${Interfaces//,/ };do
		tc qdisc add dev $Interface root teql0
	done
	ip link set dev teql0 up
	
	#Create root qdisc
	tc qdisc add dev $Interface root handle 1:0 htb default 30

	#Create max bandwidth
	tc class add dev $Interface parent 1:0 classid 1:1 htb rate $TotalBandWidth
	
	echo "== Finished Setup TC =="
}

StopTC(){
	echo "== Stopping TC =="
	
	for Interface in ${Interfaces//,/ };do
		tc qdisc del dev $Interface root
	done
	
	echo "== TC Stopped =="
}

Main(){
	if [ "$EUID" -ne 0 ]
	  then echo "Error: Please run as root"
	  exit
	fi


	echo "== Select mode =="
	echo "1) Start traffic control"
	echo "2) Stop traffic control"
	read -p "Mode selection: " ModeSelection
	echo

	case "$ModeSelection" in
		"1")
			StartTC
			;;
		"2")
			StopTC
			;;
		*)
			echo "Unknown command, aboard"
			;;
	esac

	echo "== End of program =="
}

Main
