"""Petits outils de manipulation de texte."""


def count_words(text: str) -> int:
    return len(text.split())


def reverse_text(text: str) -> str:
    return text[::-1]


def normalize_spaces(text: str) -> str:
    return " ".join(text.split())
