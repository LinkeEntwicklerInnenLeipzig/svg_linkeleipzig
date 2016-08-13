from os import path
from http.server import HTTPServer, BaseHTTPRequestHandler

svgname = 'karte.svg'
basepath = path.dirname(path.realpath(__file__))


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def provide_svg():
    filename = path.join(basepath, svgname)
    with open(filename) as f:
        return f.read()

def get_html():
    tpl = """<html>
<head><title>SVGTest</title>
<style>.outer {{ margin-top: 50px; }}</style>
</head>
<body>
<div class="outer">
{}
</div>
</body>
</html>"""
    return tpl.format(provide_svg())

class SVGTestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(get_html().encode())

run(handler_class=SVGTestHandler)
