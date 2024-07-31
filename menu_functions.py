import main
import hero


def initialize_new_game():
    hero_name = str(input("Enter a name for your hero!:"))
    main.day = 1
    main.hero = hero.Hero(hero_name)
    main.hero_position = (0,0)  # Based on (x,y) coordinates
    main.game_map = [['H/T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]


#HERO Statistics
def statistics():
    print("\n{}'s stats".format(main.hero.name))
    print("  Damage: {}".format(main.hero.attack_power))
    print(" Defence: {}".format(main.hero.defence))
    print("      HP: {}".format(main.hero.health))
    # if damage1 >= 7 : #If damage more than or equal to 7 means hero already have Orb of Power
    #     print("You are holding the Orb of Power")


### MAP FUNCTIONS ###

def show_map(): #Prints the world map
    
    print("\n  ====== WORLD MAP ======  ")
    print("H - HERO | T - TOWN \ K - RATKING")
    for row in range(len(main.game_map)):
        print("\n+---+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(len(main.game_map[row])) :
            print("{:^3}".format(main.game_map[row][col]),end = "")
            print("|", end="")
    print()
    print("+---+---+---+---+---+---+---+---+")
    print()


def move():
    print("W = Up; S = Down; A = Left; D = Right")
    movement_input = input("Where do you want to move? :")


### END OF MAP FUNCTIONS ###


#Resting in town
def rest() :
    print("\nAs you jumped on the inn's bed, you slowly closed your eyes...")
    print("The sun is out and is a new day, you are fully healed to 20 HP!")
    main.hero.health = 20 #Set hero hp to 20 after healing
    main.day += 1
