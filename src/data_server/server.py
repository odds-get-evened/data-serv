import random
import socket
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor

import select

DS_HOST: str = "127.0.0.1"
DS_PORT: int = 8080

class DataServer:
    BUF_LEN = 1024

    def __init__(self, host: str = '127.0.0.1', port: int = 8080):
        self.host_spec: tuple = (host, port)
        # self.connections: list[ClientHandler] = []

        self.executor = ThreadPoolExecutor(max_workers=2)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.serv:
            self.serv.bind(self.host_spec)
            self.serv.listen(5)
            print(f"listening on {self.host_spec[0]}:{self.host_spec[1]}")

            while True:
                # accept client connections
                cli_sock, addr = self.serv.accept()
                print(f"connection from {addr[0]}:{addr[1]}")

                threading.Thread(target=self.handle_cli, args=(cli_sock, addr)).start()

    def handle_cli(self, sock: socket.socket, addr: tuple):
        streaming = False
        sock.setblocking(False)

        try:
            while True:
                # check for incoming commands
                ready, _, _ = select.select([sock], [], [], 1)
                if ready:
                    data = sock.recv(self.BUF_LEN)
                    if not data:
                        # client closed
                        break

                    cmd = data.decode('utf-8').strip()
                    print(f"cmd: {cmd}")
                    if cmd == "data":
                        streaming = True
                        sock.sendall(b"streaming started\n")
                    else:
                        msg = f"unknown command: {cmd}\n"
                        sock.sendall(msg.encode('utf-8'))

                if streaming:
                    val = random.random()
                    sock.sendall(f"{val}\n".encode('utf-8'))
                    time.sleep(1)

        except (BrokenPipeError, ConnectionResetError):
            print(f"client disconnected abrubtly: {addr[0]}:{addr[1]}")
        finally:
            print(f"connection closed: {addr[0]}:{addr[1]}")
            sock.close()
        '''
        try:
            while True:
                val = random.random()
                sock.send(f"{val}\n".encode('utf-8'))
                time.sleep(1)
        except (BrokenPipeError, ConnectionResetError):
            print(f"client disconnected {addr[0]}:{addr[1]}")
        finally:
            print(f"connection to {addr[0]}:{addr[1]} closed")
            sock.close()
        '''


def main():
    serv = DataServer()

if __name__ == "__main__":
    main()