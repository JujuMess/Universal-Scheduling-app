from app.universal_scheduling_app import normalise
import pytest

def test_normalise():
    assert normalise("Je suis-un deveLoppeur") == "je_suis_un_developpeur"