import socket
import sys
import threading

def send_cmds(sock: socket.socket):
    """
    read lines from stdin and send valid commands back to the server
    :param sock:
    :return:
    """
    try:
        while True:
            cmd = input("> ").strip()
            if cmd in ("data"):
                sock.sendall((cmd + "\n").encode('utf-8'))
            else:
                print("use: `start_stream` or `stop_stream`")
    except (EOFError, KeyboardInterrupt):
        # cleaner exit on ctrl-d or ctrl-c in input thread
        pass

def rcv_data(sock: socket.socket):
    """
    continously receive lines  and print either floats or status messages.
    :param sock:
    :return:
    """
    buffer = ""
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("server closed the connection")
                break

            buffer += data.decode('utf-8', errors='replace')
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue

                # try parsing as float; otherwise treat as text
                try:
                    v = float(line)
                    print(f"-> {v}")
                except ValueError:
                    print(f"<- {line}")
    except (ConnectionResetError, BrokenPipeError):
        print("connection lost")
    except KeyboardInterrupt:
        print("\nconnection interrupted by user")


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8080

    try:
        sock = socket.create_connection((host, port), timeout=10)
    except Exception as e:
        print(f"could not connect to {host}:{port} {e}")
        return

    print(f"connected to {host}:{port}")
    sock.settimeout(None)

    # start input/sender thread
    sender = threading.Thread(target=send_cmds, args=(sock,), daemon=True)
    sender.start()

    # main thread handles receiving
    rcv_data(sock)

    sock.close()

if __name__ == "__main__":
    main()
