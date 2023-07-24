from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket
import argparse
import logging
from typing import Any


logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = f"pong {socket.gethostname()} {self.server.server_address[0]}"
            self.wfile.write(response.encode())
            logging.info(
                f"GET request received: {self.path}, Response: {response}")

        else:
            self.send_response(404)
            self.end_headers()
            logging.warning(f"Invalid request: {self.path}")

    def log_message(self, format: str, *args: Any) -> None:
        pass


def run_server_http(port_no: int) -> None:
    server_address = (socket.gethostname(), port_no)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print("Server started at port", port_no)
    logging.info(f"Server started at port {port_no}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pong Server")
    parser.add_argument('--protocol', type=str,
                        default="http", help='Protocol(http)')
    parser.add_argument('--port', type=int, default=80, help='Port Number')
    args = parser.parse_args()

    protocol = args.protocol.lower()
    port = args.port

    if protocol == "http":
        run_server_http(port)
    else:
        print("Invalid Protocol")
