# Utilise une image Python officielle
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app/

# Installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposer le port Django
EXPOSE 8000

# Lancer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
