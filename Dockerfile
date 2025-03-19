# Utilisation d'une image Python légère
FROM python:3.13.2

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier server.py dans le conteneur
COPY app/server.py /app/server.py

# Exposer le port 8000
EXPOSE 8000

# Commande pour exécuter le serveur
CMD ["python", "/app/server.py"]
