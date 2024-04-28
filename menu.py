import main
import sys
import menu_functions

def main_menu():
    print("Welcome to Ratventure!")
    print("----------------------")
    print("1) New Game \n2) Resume Game \n3) View Leaderboard \n4) Exit Game")
    choice = int(input("\nEnter choice :"))

    if choice == 1 : # If user choose New game, display Town Menu and initialize new Hero
        menu_functions.initialize_new_game()
        town_menu()
    elif choice == 2 : #Loads the game
        pass
    
    elif choice == 3 : #preview the top 5 shortest day to complete the game
        pass

    elif choice == 4 : #Exit the game
        sys.exit("See you next time!")


def town_menu():
    print("\nHello {}! Let's go!".format(main.hero.name))
    print("Day {} : You are in a town.".format(main.day))
    print("1) View Character \n2) View Map \n3) Move \n4) Rest \n5) Save Game \n6) Exit Game")
    choice = int(input("Enter choice:"))
    if choice == 1 : 
        menu_functions.statistics()
        town_menu()
    elif choice == 2 :
        menu_functions.show_map()
        town_menu()
    elif choice == 3 :
        printMap()
        movement()
    elif choice == 4 :
        print()
        rest()
    elif choice == 5 :
        savingGame()
        print("Game saved successfully!")
        print()
        town_text()
    elif choice == 6 :
        print()
        sys.exit("See you next time!")