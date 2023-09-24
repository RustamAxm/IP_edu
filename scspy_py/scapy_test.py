import socket
from scapy.all import srp, sr, raw, sniff, hexdump
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether, ARP
from scapy.packet import Raw


def arp_scan(ip):

    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return result


def tcp_scan(ip, ports):
    try:
        syn = IP(dst=ip) / TCP(dport=ports, flags="S")
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(ip))

    ans, unans = sr(syn, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        if received[TCP].flags == "SA":
            result.append(received[TCP].sport)

    return result


def sniffer():
    packets = sniff(count=10)
    packets.nsummary()


def raw_show():
    while True:
        packets = sniff(count=1)
        for x_ in packets:
            print(x_.show())

            print(x_.layers())
            print(x_.fields)
            if IP in x_.layers():
                print(x_[IP].fields)

            if TCP in x_.layers():
                print(x_[TCP].fields)
                print(x_[TCP])
            elif UDP in x_.layers():
                print(x_[UDP].fields)

            if Raw in x_.layers():
                print(x_[Raw].fields)
                exit(0)

print(arp_scan('192.168.50.1'))
print(tcp_scan(ip='192.168.50.1', ports=(1, 1024)))
raw_show()
