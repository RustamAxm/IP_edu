import socket
import struct
from datetime import datetime
from loguru import logger
from io import BytesIO

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
    sock.settimeout(1)
    buffer = BytesIO()
    buffer_size = 0
    while True:
        try:
            tmp = sock.recv(1024)
        except Exception as ex:
            logger.error(f'timeout error {ex} {ex.args}')
            continue
        try:
            header = tmp.decode('utf-8').split(':')
        except Exception as ex:
            logger.error(f'timeout error {ex} {ex.args}')
            continue

        if 'start_data' in header:
            count = int(header[1])
            while buffer_size != count:
                data = sock.recv(1024)
                buffer.write(data)
                buffer_size = buffer.getbuffer().nbytes
                logger.info(f'received {buffer_size=}')

            name_to_save = f'data_{datetime.now().strftime("%d%m%y_%H_%M_%S")}.bin'
            with open(name_to_save, 'wb') as file:
                file.write(buffer.getvalue())
                logger.info(f'{name_to_save} saved!')
                buffer = BytesIO()


if __name__ == '__main__':
    main()
