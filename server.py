import http.server
import socketserver

PORT = 8080

class HealthCheckHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health' or self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        else:
            self.send_error(404, "Not Found")

with socketserver.TCPServer(("", PORT), HealthCheckHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
