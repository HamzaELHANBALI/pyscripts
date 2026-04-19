# PyScripts CNAM

Depot fil rouge pour le cours **Git, GitHub & CI/CD**.

L'objectif est de construire progressivement une petite collection de scripts Python :

- session 1 : Git local, commits, historique, branches ;
- session 2 : collaboration, Pull Requests, reviews et conflits ;
- session 3 : integration continue avec GitHub Actions ;
- session 4 : generation et publication d'une page GitHub Pages.

## Structure

```text
src/pyscripts/          Code Python
tests/                  Tests unitaires pytest
scripts/generate_index.py  Generation d'une page HTML
.github/workflows/     Workflows GitHub Actions
```

## Commandes utiles

Installer les outils de developpement :

```bash
python -m pip install -r requirements-dev.txt
```

Lancer les tests :

```bash
PYTHONPATH=src pytest
```

Verifier le style :

```bash
flake8 src tests scripts
pylint src/pyscripts
```

Generer la page HTML :

```bash
python scripts/generate_index.py
```

## Idees de contributions

- ajouter une fonction dans `calculator.py` ;
- ajouter un outil de texte dans `text_tools.py` ;
- enrichir le message dans `greetings.py` ;
- ajouter un faux script meteo dans `weather_fake.py` ;
- ajouter un test pour chaque nouvelle fonction.

## Regles de contribution proposees

1. Creer une branche par fonctionnalite.
2. Faire des commits courts et lisibles.
3. Ajouter ou modifier les tests si le comportement change.
4. Ouvrir une Pull Request.
5. Attendre que la CI soit verte avant de merger.
