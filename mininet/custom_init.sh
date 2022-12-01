h1_1 iperf3 -s -p 8000 &
h2_1 iperf3 -c 10.0.1.1 -t 5 -p 8000

h1_1 iperf3 -s -p 7000 &
h2_1 iperf3 -c 10.0.1.1 -t 5 -p 7000

h1_1 iperf3 -s -p 6000 &
h2_1 iperf3 -c 10.0.1.1 -t 5 -p 6000

