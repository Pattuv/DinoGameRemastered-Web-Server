from flask import Flask, send_from_directory

import os

app = Flask(__name__, static_folder="../game")

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory(app.static_folder, filename)

# Vercel needs this handler
def handler(event, context):
    return app(event, context)
