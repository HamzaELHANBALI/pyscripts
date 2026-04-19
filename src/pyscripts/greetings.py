"""Messages d'accueil pour les exercices de branches et conflits."""


def welcome_message(name: str) -> str:
    clean_name = name.strip() or "etudiant"
    return f"Bonjour {clean_name}, bienvenue dans le TP Git du CNAM !"


def goodbye_message(name: str) -> str:
    clean_name = name.strip() or "etudiant"
    return f"A bientot {clean_name}, pense a pousser ta branche."
