import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    url = f"http://localhost:{PORT}/index.html"
    print("=" * 60)
    print("  CITIZEN ASSIST AI — SERVIDOR WEB LOCAL")
    print("=" * 60)
    print(f"  Abrindo o assistente no seu navegador: {url}")
    print("  Pressione Ctrl+C para encerrar o servidor.")
    print("=" * 60)
    
    webbrowser.open(url)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado.")

if __name__ == "__main__":
    main()
