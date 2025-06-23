from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            html_content = """
            <html><body>
            <h1>Meow! Voici un GIF de chat nul 🐱</h1>
            <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" alt="Chat gif">
            </body></html>
            """
            self.wfile.write(html_content.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serveur HTTP en écoute sur le port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
