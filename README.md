# 📚 Plateforme de gestion de cours en ligne (Django + DRF)

Une API RESTful pour gérer les cours, les enseignants, les étudiants, les catégories, les notes, etc., développée avec Django, Django REST Framework et PostgreSQL.

---

## 🚀 Fonctionnalités principales

- Gestion des utilisateurs (enseignants et étudiants)
- Création de cours avec catégorie
- Attribution de notes via une relation ManyToMany (table Grade)
- API REST complète (CRUD) avec DRF
- Utilise PostgreSQL comme base de données

---

## 🧱 Technologies utilisées

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- JWT 

---

## ⚙️ Installation locale

### 1. Cloner le projet

```bash
git clone https://github.com/dannidotcom/cours_project.git
cd cours_project

## 🚀 Exemple d'utilisation avec `make`

Une fois Docker installé et configuré, tu peux utiliser le `Makefile` pour exécuter toutes les actions nécessaires à ton environnement de développement.

---

### 1. Démarrer l’environnement de développement

```bash
make up
```
### 3. Créer les migrations

```bash
make makemigrations
```
### 4. Appliquer les migrations

```bash
make migrate
```
### 5. Créer un superutilisateur

```bash
make superuser
```
### 6. Arrêter les conteneurs

```bash
make down
```
### 7. Ouvrir un shell dans le conteneur

```bash
make shell
```
### 8. Lancer la console Python Django

```bash
make manage
```
### 9. Supprimer tous les fichiers de migration

```bash
make clean_migrations
```
