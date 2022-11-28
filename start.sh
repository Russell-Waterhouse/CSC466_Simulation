#!/bin/bash

StartMN(){
	sudo python3 init_mininet_full.py
	read -p "Press ENTER to finish"
	clear
	echo -e "** Mininet stopped **"
	echo -e "** Consider cleaning cache **\n"
}

StartSimpleMN(){
  sudo python3 init_mininet.py
	read -p "Press ENTER to finish"
	clear
	echo -e "** Mininet stopped **"
	echo -e "** Consider cleaning cache **\n"
}

CleanMN(){
	sudo mn -c
	clear
	echo -e "** Cleaned up Mininet **\n"
}

Main(){
	clear
	if [ "$EUID" -ne 0 ]; then
		echo "Error: Please run as root"
		exit
	fi

	ModeSelection="-1"
	while true ; do
		echo "==== Select mode ===="
		echo "1) 	Start Mininet"
		echo "2) 	Clear Mininet"
		echo "3) 	Simulate Mininet Topology"
		echo "4) 	Configure settings"
		echo "0) 	Quit application"
		read -p "Mode selection: " ModeSelection
		echo

		case "$ModeSelection" in
			"1")
				StartMN
				;;
			"2")
				CleanMN
				;;
			"3")
				StartSimpleMN
				;;
      "4")
				nano settings.json
				clear
				;;
			"0")
				echo "==== End of program ===="
				exit ;;
			*)
				echo "Unknown command, abort" ;;
		esac
	done
}

Main
