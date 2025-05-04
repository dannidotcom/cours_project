# Makefile pour automatiser les commandes Docker + Django

# Variables
COMPOSE=docker compose
APP=web

# 📦 Lancer le projet
up:
	$(COMPOSE) up --build

# 🛑 Stopper le projet
down:
	$(COMPOSE) down

# 🗃 Appliquer les migrations
migrate:
	$(COMPOSE) exec $(APP) python manage.py migrate

# 💥 Supprimer toutes les migrations (optionnel/dev)
clean_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete

# 👤 Créer un superutilisateur
superuser:
	$(COMPOSE) exec $(APP) python manage.py createsuperuser

# 🧪 Lancer les tests
test:
	$(COMPOSE) exec $(APP) python manage.py test

# 🧼 Lint avec flake8 (si installé)
lint:
	$(COMPOSE) exec $(APP) flake8 .

# 📂 Ouvrir un shell dans le container
shell:
	$(COMPOSE) exec $(APP) sh

# 🐍 Accéder à la console Django
manage:
	$(COMPOSE) exec $(APP) python manage.py shell
