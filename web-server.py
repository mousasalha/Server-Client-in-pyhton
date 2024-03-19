import http.server
import socketserver
import os

PORT = 9966

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html' or self.path == '/main_en.html' or self.path == '/en':
            self.send_html_response('index_en.html')
        elif self.path == '/ar':
            self.send_html_response('index_ar.html')
        elif self.path == '/cr':
            self.send_redirect('https://cornell.edu', 307)
        elif self.path == '/so':
            self.send_redirect('https://stackoverflow.com', 307)
        elif self.path == '/rt':
            self.send_redirect('https://ritaj.birzeit.edu', 307)
        else:
            file_extension = self.path.split('.')[-1].lower()
            if file_extension == 'html':
                self.send_html_response(self.path[1:])
            elif file_extension == 'css':
                self.send_css_response(self.path[1:])
            elif file_extension == 'png':
                self.send_image_response(self.path[1:], 'image/png')
            elif file_extension == 'jpg':
                self.send_image_response(self.path[1:], 'image/jpeg')
            else:
                self.send_not_found_response()

    def send_html_response(self, filename):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_css_response(self, filename):
        self.send_response(200)
        self.send_header('Content-type', 'text/css')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_image_response(self, filename, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_redirect(self, url, status_code):
        self.send_response(status_code)
        self.send_header('Location', url)
        self.end_headers()

    def send_not_found_response(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'HTTP/1.1 404 Not Found\n\nError 404\nThe file is not found \n')

if __name__ == '__main__':
    handler = MyRequestHandler
    httpd = socketserver.TCPServer(('', PORT), handler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
