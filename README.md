
```markdown
# 🛠 Toolbox Project

![CI Status](https://github.com/IamMerove/Toolbox/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

Une boîte à outils Python industrialisée avec une pipeline CI complète, des tests automatisés et une conteneurisation Docker.

---

## 🏗 Structure du Projet
```plaintext
.
├── .github/                # Configuration CI, Contributing et Code of Conduct
├── app/                    # Code source et modules métier
├── docs/                   # Documentation du projet
├── tests/                  # Tests unitaires et d'intégration
├── .coverage               # Rapport de couverture de tests
├── Dockerfile              # Configuration du conteneur
├── pyproject.toml          # Gestion des dépendances (uv)
├── uv.lock                 # Lockfile des dépendances
└── README.md

```

---

## 🚀 Installation & Usage

### Avec `uv` (Recommandé)

Ce projet utilise `uv` pour une gestion moderne des environnements Python.

1. **Synchronisation** de l'environnement :
```bash
uv sync

```


2. **Exécution** de l'application :
```bash
uv run app/main.py

```



### Avec Docker

Pour une exécution isolée :

```bash
docker build -t toolbox-final .
docker run toolbox-final

```

---

## 🧪 Qualité & Automatisation (CI)

Le "Juge de Paix" GitHub Actions exécute automatiquement les étapes suivantes à chaque push sur `main` ou `dev` :

1. **Linting** : Validation du style de code avec `ruff`.
2. **Tests** : Exécution des tests unitaires avec `pytest`.
3. **Sécurité** : Audit des secrets avec `trufflehog`.

---

## 🤝 Communauté

* **Contributions** : Voir le guide [CONTRIBUTING.md](https://www.google.com/search?q=.github/CONTRIBUTING.md).
* **Code de conduite** : Voir [CODE_OF_CONDUCT.md](https://www.google.com/search?q=.github/CODE_OF_CONDUCT.md).
* **Contributeurs** : Sébastien GARCONNET.

---

## 📜 Licence

Ce projet est sous licence **MIT**.



