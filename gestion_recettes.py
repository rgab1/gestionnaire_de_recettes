import os
import json

recettes_file = "recettes.json"

def afficher_menu(recettes):
    while True:
        print("Menu:")
        print("1. Ajouter une recette")
        print("2. Voir toutes les recettes")
        print("3. Rechercher une recette par ingrédient")
        print("4. Quitter le programme")
        user_choice = input("Que voulez-vous faire ? : ")
        if user_choice == "1":
            ajouter_recette(recettes)
        elif user_choice == "2":
            voir_toutes_recettes(recettes)
        elif user_choice == "3":
            rechercher_par_ingredient(recettes)
        elif user_choice == "4":
            print("Bye bye")
            break
        else:
            print("Veuillez entrer l'une des options proposées")

def ajouter_recette(recettes):
    titre = input("Entrez le titre de la recette : ")
    ingredients = input("Entrez la liste d'ingrédients (séparés par des virgules) : ").split(',')
    methode = input("Entrez la méthode de préparation : ")
    recette = {"titre": titre, "ingredients": ingredients, "methode": methode}
    recettes.append(recette)
    sauvegarder_recettes(recettes)
    print("Recette ajoutée avec succès!")

import json

def sauvegarder_recettes(recettes):
    try:
        with open(recettes_file, 'r') as f:
            existing_data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        existing_data = []
    existing_data.extend(recettes)
    with open(recettes_file, 'w') as f:
        json.dump(existing_data, f, indent=2)


def charger_recettes():
    if os.path.exists(recettes_file):
        with open(recettes_file, 'r') as f:
            try:
                recettes = json.load(f)
                if isinstance(recettes, list):
                    return recettes
                else:
                    print("Le fichier JSON ne contient pas une liste valide.")
                    return []
            except json.JSONDecodeError:
                print("Erreur de décodage JSON. Le fichier est probablement vide.")
                return []
    else:
        print("Le fichier JSON n'existe pas.")
        return []


def voir_toutes_recettes(recettes):
    print("Toutes les recettes :")
    for i, recette in enumerate(recettes, 1):
        print(f"{i}. {recette['titre']}")

def recette_exist(titre, recettes):
    for recette in recettes:
        if recette['titre'] == titre:
            return True
    return False

def rechercher_par_ingredient(recettes):
    ingredient_recherche = input("Entrez l'ingrédient à rechercher : ")
    recettes_trouvees = []

    for recette in recettes:
        if ingredient_recherche.lower() in [i.lower() for i in recette['ingredients']]:
            recettes_trouvees.append(recette)

    if recettes_trouvees:
        print("\nRecettes contenant l'ingrédient recherché :")
        for i, recette in enumerate(recettes_trouvees, 1):
            print(f"{i}. {recette['titre']}")
    else:
        print(f"Aucune recette ne contient l'ingrédient : {ingredient_recherche}")

def main():
    recettes = charger_recettes()
    afficher_menu(recettes)
    print(recettes)

if __name__ == "__main__":
    main()
