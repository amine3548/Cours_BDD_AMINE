import pymongo
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["Game"]
db_heroes = db["heroes"]

heroes = [
    {"name": "Knight", "ATK": 20, "DEF": 10, "HP": 100},
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

monsters = [
    {"name": "Goblin", "ATK": 5, "DEF": 2, "HP": 20},
    {"name": "Orc", "ATK": 10, "DEF": 5, "HP": 40},
    {"name": "Troll", "ATK": 15, "DEF": 10, "HP": 50},
    {"name": "Dragon", "ATK": 30, "DEF": 20, "HP": 300},
    {"name": "Vampire", "ATK": 20, "DEF": 15, "HP": 40}
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

           
def recup_heroes_disponible(liste_joueur):
    heroes_liste = heroes
    # pour chaque personnage de la liste
    for i in heroes_liste:
        # si le perso est dans la liste du joueur
        if i in liste_joueur:
            # on le supprime de la liste
            heroes_liste.remove(i)
    # retourne la liste des hero disponible
    return heroes_liste

def afficher_personnage_choix(liste):
    print(" ")
    n = 1
    for personnage in liste:
        print(f"{n} {personnage}")
        n += 1
    print(" ")

def afficher_personnage(liste):
    for personnage in liste:
        print(personnage)

def choix_heroes(liste_hero):
    # tant que vrai
    while True:
        # afficher les hero disponible
        afficher_personnage_choix(liste_hero)
        # demande au joueur de choisir un perso
        perso = input(f"Entrer un personnage (1, {len(liste_hero)}): ")
        # si la saisi est valider
        if saisie_is_valide(perso, 1, len(liste_hero)) is True:
            # on return perso
            return perso

def creation_equipe():
    # initialiser une liste qui va contenir les heros du joueur
    liste_heroes_joueur = []
    # tant que le joueur n'a pas choisi 3 heroes
    while len(liste_heroes_joueur) < 3:
        # on recupere les hero disponible 
        liste_hero = recup_heroes_disponible(liste_heroes_joueur)
        # choisir un hero
        heroes_joueur = int(choix_heroes(liste_hero))
        # ajoute les hero dans l'equipe
        liste_heroes_joueur.append(heroes[heroes_joueur -1])
    return liste_heroes_joueur

def equipe_is_alive(equipe):
    # si l'equipe est composer d'au moins un hero
    if len(equipe) > 0:
        # retourne vrai
        return True
    # retourne faux
    else:
        return False

def monstre_is_dead(monstre):
    # si HP du monstre sont inferieur a 0
    if monstre["HP"] <= 0:
        # retourne vrai
        return True
    # sinon retourne faux
    return False

def attaquer(attaquant, victime):
    # verifier si l'attaque final est <= 0
    if attaquant["ATK"] - victime["DEF"] <= 0:
        # l'attaque est ineficace
        print(f"L'attaque de {attaquant["name"]} est ineficace!!")
        return victime["HP"]
    # sinon
    else:
        # additionner les HP et la DEF du monstre et soustrai l'ATK du hero
        new_HP = victime["HP"] + victime["DEF"] - attaquant["ATK"]
        # retourner le nouveau HP
        return new_HP

def hero_is_dead(hero):
    # si les HP du hero <= 0
    if hero["HP"] <= 0:
        # retourne vrai
        return True
    # sinon retourne faux
    else:
        return False

def choix_auto_hero(equipe):
    # choisir au hasard un element de la liste de l'equipe
    hero = random.choice(equipe)
    return hero

def apparition_monstre():
    # choisir au hasard un monstre de la liste monsters
    monstre = random.choice(monsters)
    # retourner le monstre
    return monstre

def sup_hero(equipe, hero):
    equipe.remove(hero)
    
def tour(equipe, monstre):
    # chaque personnage de l'equipe
    for hero in equipe:
        # attaque le monstre
        monstre["HP"] = attaquer(hero, monstre)
        # verifie si le monstre est mort
        if monstre_is_dead(monstre) is True:
            # retourne
            return True
    
    # verifie si l'equipe est vivant
    if equipe_is_alive(equipe) is False:    
        return
    
    # choisi auto un hero de l'equipe a attaque
    hero_victime = choix_auto_hero(equipe)
    # monstre attaque ce hero
    hero_victime["HP"] = attaquer(monstre, hero_victime)
    print(monstre)
    afficher_personnage(equipe)
    # verifi si le hero est mort
    if hero_is_dead(hero_victime) is True:
        # suprimme le hero de l'equipe
        sup_hero(equipe, hero_victime)
        
        
    
def commencer_manche(equipe, monstre):
    score = 0
    # tant que le monstre n'est pas mort
    while monstre_is_dead(monstre) is not True:
        # on fait un tour
        tour(equipe, monstre)
        # on incremente le score
        score +=1
    # retourne le score
    return score
        
def commencer_jeu(equipe):
    conteur = 0
    # tant que tout les hero de l'equipe sont vivant
    while equipe_is_alive(equipe) is True:
        conteur += 1
        # choisi au hasard un monstre
        monstre_manche = apparition_monstre()
        # commencer la manche
        score = commencer_manche(equipe, monstre_manche)        
    return score

def play_game():
    # demande a l'utilisateur d'entrer un nom
    nom_choisi = name_team()
    # utilisateur choisi ses hero
    equipe = creation_equipe()
    # le jeu commence
    score = commencer_jeu(equipe)
    print(f"Nom: {nom_choisi} \nScore: {score}")

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
        afficher_top_score()
    # si choix 3 quitter
    if int(choix) == 3:
        quitter()
    
    
main()