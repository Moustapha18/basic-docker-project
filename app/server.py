from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Contenu HTML amélioré avec du style
        message = """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Apprentissage Git & Docker</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; text-align: center; background-color: #f4f4f4; }
                h1 { color: #2c3e50; }
                p { font-size: 18px; color: #333; max-width: 600px; margin: auto; }
                .container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bienvenue dans le Monde de Git & Docker 🚀</h1>
                <p>Git est un système de gestion de version distribué qui permet de suivre les modifications de fichiers et de collaborer efficacement.</p>
                <p>Docker est une plateforme qui permet de créer, déployer et exécuter des applications dans des conteneurs légers et portables.</p>
                <p>Avec ces outils, tu peux améliorer ton workflow DevOps et automatiser tes déploiements.</p>
                <p>Bon apprentissage ! 🎉</p>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
