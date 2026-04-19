from pyscripts.text_tools import count_words, normalize_spaces, reverse_text


def test_count_words():
    assert count_words("Git est utile") == 3


def test_reverse_text():
    assert reverse_text("CNAM") == "MANC"


def test_normalize_spaces():
    assert normalize_spaces("Git    puis   GitHub") == "Git puis GitHub"
