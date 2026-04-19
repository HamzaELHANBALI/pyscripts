from pyscripts.greetings import goodbye_message, welcome_message


def test_welcome_message_uses_name():
    assert welcome_message("Alice") == (
        "Bonjour Alice, bienvenue dans le TP Git du CNAM !"
    )


def test_welcome_message_uses_default_name():
    assert welcome_message("   ") == (
        "Bonjour etudiant, bienvenue dans le TP Git du CNAM !"
    )


def test_goodbye_message():
    assert goodbye_message("Samir") == (
        "A bientot Samir, pense a pousser ta branche."
    )
