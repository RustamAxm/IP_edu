#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<netinet/ip.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include <iostream>


class RawSocket {
public:
    RawSocket() {
        sock = socket (PF_INET, SOCK_RAW, IPPROTO_TCP);
        if(sock == -1)
        {
            //socket creation failed, may be because of non-root privileges
            perror("Failed to create socket");
            exit(1);
        }
        buffer = new unsigned char [65536]();
    }

    virtual ~ RawSocket() {
        delete buffer;
    }

    struct iphdr & getPacket () {
        int packet_size;
        packet_size = recvfrom(sock , buffer , 65536 , 0 , NULL, NULL);
        if (packet_size == -1) {
            printf("Failed to get packets\n");
        }

        struct iphdr * ip_packet = reinterpret_cast<iphdr *>(buffer);
        return *ip_packet;
    }

    struct sockaddr_in getSourceSocket(struct iphdr & ip_packet) {
        struct sockaddr_in source_socket_address;
        memset(&source_socket_address, 0, sizeof(source_socket_address));
        source_socket_address.sin_addr.s_addr = ip_packet.saddr;
        return source_socket_address;
    }

    struct sockaddr_in getDestSocket(struct iphdr & ip_packet) {
        struct sockaddr_in dest_socket_address;
        memset(&dest_socket_address, 0, sizeof(dest_socket_address));
        dest_socket_address.sin_addr.s_addr = ip_packet.daddr;
        return dest_socket_address;
    }

    void printStr () {
        struct iphdr & ip_packet = getPacket();
        auto source_socket_address = getSourceSocket(ip_packet);
        auto dest_socket_address = getDestSocket(ip_packet);

//        std::cout << "Incoming Packet: \n" << std::endl;
        printf("Incoming Packet: \n");
        printf("Packet Size (bytes): %d\n",ntohs(ip_packet.tot_len));
        printf("Source Address: %s\n", reinterpret_cast<char *>(inet_ntoa(source_socket_address.sin_addr)));
        printf("Destination Address: %s\n", reinterpret_cast<char *>(inet_ntoa(dest_socket_address.sin_addr)));
        printf("Identification: %d\n\n", ntohs(ip_packet.id));
    }

private:
    int sock;
    unsigned char *buffer;
};

int main() {
    // Structs that contain source IP addresse
    RawSocket raw = RawSocket();
    for (auto i = 0; i < 10; i++) {
        raw.printStr();
    }
    return 0;
}
