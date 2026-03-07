#!/usr/bin/env python3
"""
Simple web server to serve the NewsWeaver application
Run: python server.py
Then open http://localhost:8080 in your browser
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8080
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run_server():
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 NewsWeaver Server Started!")
        print(f"📍 Open http://localhost:{PORT} in your browser")
        print(f"📁 Serving from: {DIRECTORY}")
        print(f"\n Press Ctrl+C to stop the server\n")
        
        # Open browser automatically
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✓ Server stopped")

if __name__ == "__main__":
    run_server()
