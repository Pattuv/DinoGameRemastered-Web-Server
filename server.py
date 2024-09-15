import http.server
import socketserver

PORT = 8080  # Or any other available port
DIRECTORY = "godot_game"  # Directory where your Godot game files are located

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Add required headers for Cross-Origin Isolation and SharedArrayBuffer (if needed for the game)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

    def do_GET(self):
        # Serve index.html as the default file for the root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()



# Run the server
handler = MyHttpRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

try:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
finally:
    print("Shutting down server...")
    httpd.shutdown()

