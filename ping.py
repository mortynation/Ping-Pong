import http.client
import time
import socket
import argparse


def send_ping_request(host: str, port_no: int) -> None:
    conn = http.client.HTTPConnection(host, port_no)
    conn.request("GET", "/ping")
    response = conn.getresponse()
    data = response.read().decode()
    print(data)
    conn.close()


if __name__ == "__main__":
    # server_host = socket.gethostname()
    # server_port = 80

    parser = argparse.ArgumentParser(description="Ping Server")
    parser.add_argument('--hostname', type=str,
                        default=socket.gethostname(), help='Hostname')
    parser.add_argument(
        '--port', type=int, default=80, help='Port Number')
    args = parser.parse_args()
    hostname = args.hostname
    port = args.port

    while True:
        try:
            send_ping_request(hostname, port)
            time.sleep(1)
        except KeyboardInterrupt:
            print("Ping client stopped.")
            break
        except Exception as e:
            print("Pong: Failed")
            time.sleep(1)
