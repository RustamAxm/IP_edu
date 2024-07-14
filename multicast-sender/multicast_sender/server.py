import socket
import struct
from datetime import datetime
from loguru import logger

def main():
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    IS_ALL_GROUPS = False

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if IS_ALL_GROUPS:
        sock.bind(('', MCAST_PORT))
    else:
        sock.bind((MCAST_GRP, MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    buffer = b''
    while True:
        tmp = sock.recv(1024)
        buffer += tmp
        logger.debug(f'{len(tmp)=}, {len(buffer)=}')
        if len(tmp) < 1024:
            name_to_save = f'data_{datetime.now().strftime("%d%m%y_%H_%M_%S")}.bin'
            with open(name_to_save, 'wb') as file:
                file.write(buffer)
                logger.info(f'{name_to_save} saved!')


if __name__ == '__main__':
    main()
