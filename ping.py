import http.client
import time
import socket
import argparse

# time: 8.42 pm
# time: 8.57 pm
# time: 9.04 pm
# time: 9.10 pm


def send_ping_request(host_ip: str, port_no: int) -> None:
    conn = http.client.HTTPConnection(host_ip, port_no)
    conn.request("GET", "/ping")
    response = conn.getresponse()
    data = response.read().decode()
    print(data)
    conn.close()


if __name__ == "__main__":
    localhost_name = socket.gethostname()

    parser = argparse.ArgumentParser(description="Ping Server")
    parser.add_argument('--hostname', type=str, help='Hostname')
    parser.add_argument(
        '--ip', type=str, help='IP')
    parser.add_argument(
        '--port', type=int, default=80, help='Port Number')
    args = parser.parse_args()
    hostname = args.hostname
    port = args.port
    ip = args.ip

    while True:
        try:
            if not hostname and ip:
                send_ping_request(ip, port)
            elif not ip and hostname:
                send_ping_request(hostname, port)
            elif not ip and not hostname:
                send_ping_request(localhost_name, port)
            time.sleep(1)
        except KeyboardInterrupt:
            print("Ping client stopped.")
            break
        except Exception as e:
            print("Pong: Failed")
            time.sleep(1)
