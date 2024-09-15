import http.server
import socketserver

PORT = 8080  # Or any other available port
DIRECTORY = "game"  # Directory with your exported Godot game

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add required headers for Cross-Origin Isolation and SharedArrayBuffer
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

    def translate_path(self, path):
        # Serve files from the godot_game directory
        path = super().translate_path(path)
        return path.replace("/godot_game", DIRECTORY, 1)

# Run the server
handler = MyHttpRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", PORT), handler)  # Bind to all network interfaces

try:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
finally:
    print("Shutting down server...")
    httpd.shutdown()
