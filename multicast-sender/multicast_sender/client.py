import socket
import argparse
import time

import numpy as np
from loguru import logger
from multicast_sender.header import header


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
        size_ = len(tmp)
        logger.debug(f'{len(tmp)=}')
        time.sleep(0.01)
        stru = np.zeros(1, dtype=header)
        stru['size'] = size_

        for index in range(0, len(tmp), 1024):
            payload = tmp[index: index + 1024]
            stru['chunk_size'] = len(payload)

            data_to_send = stru.tobytes() + payload
            sock.sendto(data_to_send, (MCAST_GRP, MCAST_PORT))
            time.sleep(0.001)
        logger.info(f'{filename} received')
    sock.close()


if __name__ == '__main__':
    main()
