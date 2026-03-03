# Utilisation d'une image légère pour réduire la taille du conteneur

FROM python:3.10-slim

# Installation de uv pour gérer les dependances
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

#Définition du réppertoire de travial dans le conteneur
WORKDIR /app

# --- ÉTAPE CRUCIALE ---
# On copie d'abord UNIQUEMENT les fichiers de dépendances
COPY pyproject.toml uv.lock ./

# Copie des fichiers 
RUN uv sync --frozen --no-dev

#Copie du reste du code source (le dossier app)
COPY app/ ./app/

#On s'arrure que le chemin vers l'environnement virtuel est prioritaire
ENV PATH="/app/.venv/bin:$PATH"

#Commande de lancement de l'application
CMD ["python", "app/main.py"]
