import pytest
import pandas as pd
from app.modules.mon_module import add, sub, square, print_data

#1. La Paramétrisation (pour les fonctions mathématiques)
#Au lieu d'écrire trois fonctions pour tester add, on en écrit une seule qui reçoit une liste de scénarios.
# On test plusieurs cas (positifs, negatifs, zero) en une seule fois
@pytest.mark.parametrize("a,b, expected", [
    (10, 2, 12),
    (20, 2, 22),
    (0, 2, 2),
    (-1, -1, -2)
])

def test_add_parametrized(a, b, expected):
    assert add(a,b) == expected

def test_sub():
    assert sub(10, 5) == 5

def test_square():
    assert square(4) == 16


#2. La Fixture (pour le test de DataFrame)
#Le TP précise : ne pas lire le vrai fichier CSV. Pourquoi ? Parce qu'un test doit être rapide et ne pas dépendre d'un fichier externe qui pourrait être supprimé.
#On crée une Fixture : une fonction qui prépare des données "jetables" pour le test

@pytest.fixture
def fake_df():
    """Génère un DataFrame temporaire pour les tests."""
    data = {
        "nom" : ["Alice", "Bob", "Charlie"],
        "score" : [10,20,30]
    }
    return pd.DataFrame(data)

def test_print_data(fake_df):
    """Test la fonction print_data en utilisant la fixture fake_df."""
    # La fonction print_data doit retourner le nombre de lignes
    result = print_data(fake_df)
    assert result == 3
    assert isinstance(fake_df, pd.DataFrame)