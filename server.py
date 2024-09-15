import webbrowser
import http.server
import socketserver

PORT = 8080  # Or any other available port

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS and cross-origin headers for game compatibility
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

    def guess_type(self, path):
        # Serve WebAssembly and Godot PCK files with correct MIME types
        mime_type = super().guess_type(path)
        if path.endswith(".wasm"):
            return "application/wasm"
        elif path.endswith(".pck"):
            return "application/octet-stream"
        return mime_type

# Open the default web browser to the server's address (local access)
webbrowser.open(f'http://localhost:{PORT}/game/')

# Run the server (external access)
handler = MyHttpRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", PORT), handler)

try:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
finally:
    print("Shutting down server...")
    httpd.shutdown()
