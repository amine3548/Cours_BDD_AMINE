def afficher_menu():
    print("1. Lancer le jeux") 
    print("2. Afficher le score") 
    print("3. Quitter")    

def choix_option():
    

def main():
    # afficher le menu
    afficher_menu()
    # choix de l'option
    choix = choix_option()
    # si choix 1 lancer le jeux
    if choix == 1:
        play_game() 
    # si choix 2 afficher les score
    if choix == 2:
        afficher_score()
    # si choix 3 quitter
    if choix == 3:
        quitter()
    
    
    

main()