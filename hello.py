
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/image.jpg":
            image_path = Path("app/image.jpg")
            if image_path.exists():
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                self.wfile.write(image_path.read_bytes())
            else:
                self.send_error(404, "Image not found")
            return

        html = """
        <!DOCTYPE html>
        <html>
        <head><title>Docker Hello World</title></head>
        <body style="text-align:center; font-family:Arial;">
            <h1>Hello World!</h1>
            <h2>My First Containerized Application</h2>
            <img src="/image.jpg" alt="Application picture"
                 style="max-width:500px; width:80%;">
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("Application running on port 8000")
server.serve_forever()
