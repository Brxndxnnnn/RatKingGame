import main
import hero


def initialize_new_game():
    hero_name = str(input("Enter a name for your hero!:"))
    main.day = 1
    main.hero = hero.Hero(hero_name)
    main.hero_position = (0,0)  # Based on (x,y) coordinates
    main.game_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
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
    for y in range(len(main.game_map)):
        print("\n+---+---+---+---+---+---+---+---+")
        print("|", end="")
        for x in range(len(main.game_map[y])) :
            # Print "H" if matches the current hero_pos coordinate
            if (x, y) == main.hero_position:
                # If Hero is in Town, print "H/T"
                if main.game_map[y][x].upper() == "T":
                    print("{:^3}".format("H/T"),end = "")
                # Else just print "H"
                else:
                    print("{:^3}".format("H"),end = "")
            # Else just print as per normal
            else:
                print("{:^3}".format(main.game_map[y][x]),end = "")
            print("|", end="")
    print()
    print("+---+---+---+---+---+---+---+---+")
    print()


def move():
    print("W = Up; S = Down; A = Left; D = Right; X = Back")
    movement_input = input("Where do you want to move? :")

    ### NEED TO ENSURE X AND Y COORDINATE IS NOT 0 if they try to exceed the map size

    hero_x_coordinate = main.hero_position[0]
    hero_y_coordinate = main.hero_position[1]

    if is_valid_move(movement_input, hero_x_coordinate, hero_y_coordinate):
        # If user wants to go up
        if movement_input.upper() == "W":
            hero_y_coordinate -= 1
        # If user wants to go left
        elif movement_input.upper() == "A":
            hero_x_coordinate -= 1
        # If user wants to go down
        elif movement_input.upper() == "S":
            hero_y_coordinate += 1
        # If user wants to go right
        elif movement_input.upper() == "D":
            hero_x_coordinate += 1
        
        # Update the final hero coordinates
        main.hero_position = (hero_x_coordinate, hero_y_coordinate)

    else:
        print("Invalid move! You can't go out of the map!")


def is_valid_move(movement_input, hero_x, hero_y):

    # Cant go UP any further
    if movement_input.upper() == "W" and hero_y == 0:
        return False
    
    # Cant go LEFT any further
    elif movement_input.upper() == "A" and hero_x == 0:
        return False
    
    # Cant go DOWN any further
    elif movement_input.upper() == "S" and hero_y == 7: #! TODO: MAKE THIS DYNAMIC
        return False
    
    # Cant go RIGHT any further
    elif movement_input.upper() == "D" and hero_x == 7: #! TODO MAKE THIS DYNAMIC
        return False
    
    return True

### END OF MAP FUNCTIONS ###


#Resting in town
def rest() :
    print("\nAs you jumped on the inn's bed, you slowly closed your eyes...")
    print("The sun is out and is a new day, you are fully healed to 20 HP!")
    main.hero.health = 20 #Set hero hp to 20 after healing
    main.day += 1
