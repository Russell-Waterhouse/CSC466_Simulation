h1_1 iperf3 -s -p 1000 &
h1_1 iperf3 -s -p 2000 &
h1_1 iperf3 -s -p 3000 &

h2_1 iperf3 -c 10.0.1.1 -t 3 -p 1000
h2_1 iperf3 -c 10.0.1.1 -t 3 -p 2000
h2_1 iperf3 -c 10.0.1.1 -t 3 -p 3000

