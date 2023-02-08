
from math import factorial, log, sin, cos
def predef():
    """
    • Ecrire un script permettant de rentrer 1 caractères et un entier
    • Afficher la variables sous forme d'entiers et de caractères
    """

    while True:
        # Saisie des variables
        carac = input("Entrer un caractère : ")

        if not carac.isalpha() or len(carac) > 1:
            print("Erreur, mauvais input")
            continue
        
        entier = input("Entrer un entier : ")
        if not entier.isdigit():
            print("Erreur, mauvais input")
            continue 

        entier = int(entier)

        # Affichage des variables
        print(f'{carac} vaut {ord(carac)}')
        print(f'{entier} vaut {chr(entier)}')

        if input("Voulez-vous recommencer ? (o/n) : ") == 'n':
            print("Merci a bientôt")
            break

def trapeze():
    """
    • Programme qui calcule la surface d’un trapèze 
    """
    
    # Saisie des variables
    a = input("Entrer la longueur du côté a : ")
    b = input("Entrer la longueur du côté b : ")
    h = input("Entrer la hauteur h : ")

    if not all([a.isdigit(), b.isdigit(), h.isdigit()]):
        print("Erreur, mauvais input")
        return

    a, b, h = int(a), int(b), int(h)

    # Calcul de la surface
    surface = (a + b) * h * 0.5

    # Affichage de la surface
    print(f"La surface du trapèze est de {surface} m")


def somme_factoriel():
    """
    Algorithme qui demande un nombre entier positif de départ, et qui calcule la somme et le factoriel de l’entiers
    """

    while True:

        number = input("Entrer un entier positif : ")

        if not number.isdigit():
            print("Erreur, vous n'avez pas entré un entier")
            continue

        number = int(number)

        somme, factoriel = 0, factorial(number)
        list_number = []

        
        # Calcul de la somme et de la factoriel
        for i in range(1, number + 1):
            somme += i
            list_number.append(str(i))

        # Affichage de la somme
        print(" + ".join(list_number), "=", somme)
        print(somme, "=", " + ".join(list_number), "\n")

        # Affichage de la factoriel
        print(" * ".join(list_number), "=", factoriel)
        print(factoriel, "=", " * ".join(list_number))

        if input("Voulez-vous recommencer ? (o/n) : ") == 'n':
            print("Merci a bientôt")
            break

def arbre():
    """
    Afficher un arbre de Noel en utilisant les symboles = et *. La hauteur de l’arbre sera donnée
    par l’utilisateur, et l’affichage devra ressembler aux lignes cidessous
    """

    # Saisie de la hauteur de l'arbre
    hauteur = input("Hauteur de l'arbre : ")

    if not hauteur.isdigit():
        print("Erreur, mauvais input")
        return

    hauteur = int(hauteur)

    # Dessin de l'arbre entouré de =
    for i in range(hauteur):
        print(f"{'=' * (hauteur - i)}{'*' * (2 * i + 1)}{'=' * (hauteur - i)}")

    # Dessin de la base de l'arbre
    print("="*hauteur + "*" + "="*hauteur)
    print("="*(hauteur-1) + "***" + "="*(hauteur-1))

def mathe():
    """
    • Script permettant de saisir un entier au clavier et d’afficher :
        – Le logarithme népérien de l’entier
        – Le sinus de l’entier
        – Le cosinus de l’entier
    """
    entier = input("Entrer un entier : ")

    if not entier.isdigit():
        print("Erreur, mauvais input")
        return

    print(f"log({entier}) = {log(int(entier))}")
    print(f"sin({entier}) = {sin(int(entier))}")
    print(f"cos({entier}) = {cos(int(entier))}")


def menu():
    print("Menu:")
    print("1. Types prédéfinis")
    print("2. Calcul d’une surface")
    print("3. Somme & factoriel")
    print("4. Arbre de noël")
    print("5. Math")
    choice = int(input("Choisissez une option : "))
    if choice == 1:
        predef()
    elif choice == 2:
        trapeze()
    elif choice == 3:
        somme_factoriel()
    elif choice == 4:
        arbre()
    elif choice == 5:
        mathe()
    else:
        print("Option non valide.")

menu()
