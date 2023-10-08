# network education repo
## Scapy 
Scapy - python based module \
simple example [scapy_test.py](scspy_py/scapy_test.py)
```bash
rustam@rustam-ZenBook:~/IP_edu/scapy_py$ sudo python3 scapy_test.py 
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
[{'IP': '192.168.50.1', 'MAC': 'd4:5d:64:c5:a6:00'}]
Begin emission:
Finished sending 1024 packets.
.************************************************************************************************************************************************************************..Begin emission:
Finished sending 856 packets.
*****************************************************************************************************************************************************************************...................................................................................................................................
Received 475 packets, got 341 answers, remaining 683 packets
[53, 80]
```
## PcapPlusPlus
Cpp util for packet stat
### Install
[go to link](https://pcapplusplus.github.io/docs/install/linux)
### Simple listening port by IP
[pcap_cpp](pcap_cpp/main.cpp) set ip for interface
```cpp
std::string interfaceIPAddr = "192.168.50.146";
```
run with sudo permission
```bash
rustam@rustam-ZenBook:~/IP_edu/pcap_cpp$ sudo ./cmake-build-debug/pcap_cpp  
Interface info:
   Interface name:        wlp1s0
   Interface description: 
   MAC address:           5c:80:b6:f7:a4:63
   Default gateway:       192.168.50.1
   Interface MTU:         1500
   DNS server:            192.168.50.1

Starting async capture...
Results:
Ethernet packet count: 19
IPv4 packet count:     17
IPv6 packet count:     0
TCP packet count:      16
UDP packet count:      0
DNS packet count:      0
HTTP packet count:     0
SSL packet count:      2

Starting capture with packet vector...
Results:
Ethernet packet count: 174
IPv4 packet count:     174
IPv6 packet count:     0
TCP packet count:      10
UDP packet count:      162
DNS packet count:      8
HTTP packet count:     0
SSL packet count:      0

Starting capture in blocking mode...
Results:
Ethernet packet count: 19
IPv4 packet count:     16
IPv6 packet count:     1
TCP packet count:      15
UDP packet count:      2
DNS packet count:      2
HTTP packet count:     0
SSL packet count:      2

Sending 174 packets one by one...
174 packets sent

Sending 174 packets...
174 packets sent

Starting packet capture with a filter in place...
Results:
Ethernet packet count: 0
IPv4 packet count:     0
IPv6 packet count:     0
TCP packet count:      0
UDP packet count:      0
DNS packet count:      0
HTTP packet count:     0
SSL packet count:      0

```
