import pandas as pd
from modules.mon_module import add, print_data


def run():
    """ON lance le truc."""
    print("--- Démarrage de la Toolbox ---")

    # 1. Test des fonctions mathématiques
    result = add(10, 5)
    print(f"Test calcul : 10 + 5 = {result}")

    # 2. Test du traitement de données
    try:
        df = pd.read_csv("app/moncsv.csv")
        print("CSV chargé avec succès.")
        nb_lignes = print_data(df)
        print(f"Le fichier contient {nb_lignes} lignes.")
    except Exception as e:
        print(f"Erreur lors de la lecture du CSV : {e}")

if __name__ == "__main__":
    run()
