import http.server
import socketserver

HOST = "192.168.1.103"
PORT = 80
DIRECTORY = "books"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving books at {HOST}:{PORT}")
    httpd.serve_forever()