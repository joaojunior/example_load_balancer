from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from sys import argv


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        host_name = os.environ['HOSTNAME']
        self.wfile.write(bytes(f'server:{host_name}', "utf-8"))


def run(port, server_class=HTTPServer, handler_class=Server):
    server_address = ("0.0.0.0", port)
    httpd = server_class(server_address, handler_class)
    print('Server started')
    httpd.serve_forever()


if __name__ == "__main__":
    run(port=int(argv[1]))
