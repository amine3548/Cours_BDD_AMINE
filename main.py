import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["Game"]
db_heroes = db["heroes"]

heroes = [
    { "name": "Knight", "ATK": 10, "DEF": 10, "HP": 100},
    {"name": "Archer", "ATK": 15, "DEF": 5, "HP": 80},
    {"name": "Mage", "ATK": 20, "DEF": 3, "HP": 60},
    {"name": "Assassin", "ATK": 25, "DEF": 2, "HP": 50},
    {"name": "Paladin", "ATK": 12, "DEF": 12, "HP": 120},
    {"name": "Berserker", "ATK": 30, "DEF": 0, "HP": 80},
    {"name": "Druid", "ATK": 18, "DEF": 8, "HP": 70},
    {"name": "Necromancer", "ATK": 22, "DEF": 4, "HP": 60},
    {"name": "Rogue", "ATK": 28, "DEF": 3, "HP": 55},
    {"name": "Monk", "ATK": 14, "DEF": 10, "HP": 90}
]

def afficher_menu():
    print("1. Lancer le jeux") 
    print("2. Afficher le score") 
    print("3. Quitter")    

def choix_option():
    # demande a l'utilisateur de choisir une option
    while True:
        saisie = input("Entrer votre choix: ")
        # verifier si la saisi est valide
   
        if saisie_is_valide(saisie, 1, 3) is True:
            # retourner la saisi
            return saisie
            
def saisie_is_valide(choix,min_val,max_val):
    # si le choix n'est pas numeric
    if not choix.isnumeric():
        #on affiche un message d'erreur 
        print(f"Saisi invalide entre {min_val} et {max_val}.")
        # on retourne faux
        return False
    # si le nombre n'est pas entre min_val et max_val
    if int(choix) < min_val or int(choix) > max_val:
        # affiche un mlessage d'erreur 
        print(f"Saisi invalide entre {min_val} et {max_val}.")
        # retourne faux 
        return False
    # retourne true
    return True

def name_team():
    # demande a l'utilisateur d'entrer un nom
    while True:
        name = input("Entrez un nom d'équipe (3-20): ")
        # verifie si il est valide
        if name_is_valide(name) is True:
            # retourn le nom
            return name
        
    
def name_is_valide(name):
    # si la taille du nom n'es pas entre 3 et 20
    if len(name) < 3 or len(name) > 20:
        #retourne faux
        return False
    #sinon on retourne vrai
    else:
        return True

# def recuperer_heroes(heroes):
#     for x in db_heroes.find():
#         heroes.append(x)
    
    
def afficher_heroes_disponible(liste_joueur):
    test = []
    liste_base = heroes
    # recuperer les heroes de base
    # recuperer_heroes(liste_base)
    # pour chaque element de la liste du joueur
    for i in liste_base:
        # si il est pas dans la liste du joueur
        if i not in liste_joueur:
            # on affiche ce qui reste
            print(i)
            test.append(i)
    return test

    

def choisir_heroes():
    # initialiser une liste qui va contenir les heros du joueur
    heroes_joueur = []
    # tant que le joueur n'a pas choisi 3 heroes
    while len(heroes_joueur) < 3:
        # on affiche les heroes disponible
        list_test = afficher_heroes_disponible(heroes_joueur)
        # tant que vrai
        while True:
            # demande a l'utilisateur d'entrer un index de hero a choisir
            heroes_choisi = input("Entrer le numero du personnage que vous voulez (): ")
            # si la saisi est valide
            if saisie_is_valide(heroes_choisi, 1, len(list_test)) is True:
                # retourne le choix d'heroes
                return heroes_choisi
        # ajoute le choix a sa liste
    # on l'enleve de la liste
    supprimer_element()

def play_game():
    # demande a l'utilisateur d'entrer un nom
    nom_choisi = name_team()
    # utilisateur choisi ses hero
    choisir_heroes()
    # le jeu commence
    start()
    

def main():
    # afficher le menu
    afficher_menu()
    # choix de l'option
    choix = choix_option()
    # si choix 1 lancer le jeux
    if int(choix) == 1:
        play_game()
    # si choix 2 afficher les score
    if int(choix) == 2:
        afficher_score()
    # si choix 3 quitter
    if int(choix) == 3:
        quitter()
    
main()