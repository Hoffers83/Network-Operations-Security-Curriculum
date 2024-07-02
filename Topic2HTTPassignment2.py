from http.server import HTTPServer, BaseHTTPRequestHandler

print ("open a web browser and navigate to http://localhost:8000")

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with a 200 OK status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write the HTML content
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple HTTP Server</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTTP server in Python.</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8000)
