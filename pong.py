#! /usr/bin/python3
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
            response = f"pong from {socket.gethostname()} {self.server.server_address[0]}"
            self.wfile.write(response.encode())
            logging.info(
                f"GET request received: {self.path}, Response: {response}")

        else:
            return super().do_GET()

    def log_message(self, format: str, *args: Any) -> None:
        pass


def run_server_http(port_no: int) -> None:

    host_name = socket.gethostname()
    html_code = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Host Information</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: top;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Host Information</h1>
            <p><b>Hostname:</b> {host_name}</p>
            <p><b>IP:</b> {socket.gethostbyname(host_name)}</p>
        </div>
    </body>
    </html>
    '''
    with open('index.html', 'w') as file:
        file.write(html_code)
    server_address = (host_name, port_no)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print("Server started at port", port_no)
    logging.info(f"Server started at port {port_no}")
    print(
        f'Open this link - http://{socket.gethostbyname(host_name)}:{port_no}')
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
