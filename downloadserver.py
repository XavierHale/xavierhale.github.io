import http.server

import socketserver


PORT = 8000
header = "yo you got games"
handler = http.server.SimpleHTTPRequestHandler

def do_GET(self):
    self.send_header('games', )

with socketserver.TCPServer(("10.180.234.119", PORT), handler, header) as httpd:
    print("Server started at " + str(PORT))
    httpd.serve_forever()
