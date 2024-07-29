import socket
import argparse
import time

from loguru import logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--file", default='images/img.png')
    args = parser.parse_args()
    filename = args.file
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    MULTICAST_TTL = 2

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
    with open(filename, 'rb') as file:
        tmp = file.read()
        logger.debug(f'{len(tmp)=}')
        sock.sendto(f'start_data:{len(tmp)}'.encode('utf-8'), (MCAST_GRP, MCAST_PORT))
        for index in range(0, len(tmp), 1024):
            sock.sendto(tmp[index: index + 1024], (MCAST_GRP, MCAST_PORT))
            time.sleep(0.001)
        logger.info(f'{filename} received')
    sock.close()


if __name__ == '__main__':
    main()
