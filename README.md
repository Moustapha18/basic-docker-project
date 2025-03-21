from http.server import HTTPServer, BaseHTTPRequestHandler

# Définition du gestionnaire de requêtes HTTP
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # En-tête de réponse
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Contenu de la réponse
        message = "<html><body><h1>Hello, Docker!</h1></body></html>"
        self.wfile.write(message.encode("utf-8"))

# Configuration du serveur
if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()

# Projet DevOps - Serveur HTTP avec Docker

##  Prérequis
- Docker installé
- Python 3 installé (pour test en local)

##  Exécution sans Docker
```bash
python app/server.py
# trigger after fixing scope
