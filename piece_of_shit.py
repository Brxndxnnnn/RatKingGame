#Name : Chu Wee How Brandon
#Student ID : S10194173
#Class : P07

#Hi! Welcome to ratventure! The goal of the game is to defeat the Rat King
#that awaits you at the bottom right of the map. However, getting there won't
#be easy. his minions will be everywhere on the map to stop you from getting
#to the King. On the map somewhere there will be a Orb Of Power which you need
#to find in order to increase your power and fight the Rat King. Try your best
#and beat the game in the shortest amount of day possible. Good Luck! :)


import random
import sys

# +------------------------
# | Text for various menus 
# +------------------------


def main():
    print('test')


if __name__ == "__main__":
    main()


#Days in the game
days = 1
#Hero statistics
damage1 = 2
damage2 = 4
defence = 1
hp = 20
#Rat statistics
rDamage1 = 1
rDamage2 = 3
rDefence = 1
rHp = 10
#Rat King Statistics
kDamage1 = 6
kDamage2 = 10
kDefence = 5
kHp = 25
#Leaderboard
ranking = ["1st", "2nd", "3rd", "4th", "5th"]
#World Map
world_map = [['H/T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
hero_row = 0
hero_col = 0

#Randomise orb Location.

orb_row = random.randint(0,7)
orb_col = random.randint(0,7)
if orb_row > 3 :
    orb_col = random.randint(0,7)
    world_map[orb_row][orb_col] = ""
elif orb_row <= 3 :
    orb_col = random.randint(4,7)
    world_map[orb_row][orb_col] = ""
elif orb_col > 3 :
    orb_row = random.randint(0,7)
    world_map[orb_row][orb_col] = ""
elif orb_col <= 3 :
    orb_row = random.randint(4,7)
    world_map[orb_row][orb_col] = ""

    
    

#MAP FUNCTIONS#
def printMap() : #Prints the world map
    for row in range(len(world_map)) :
        print()
        print("+---+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(len(world_map[row])) :
            print("{:^3}".format(world_map[row][col]),end = "")
            print("|", end="")
    print()
    print("+---+---+---+---+---+---+---+---+")
    print()
    #return

def movement() :
    print("W = Up; S = Down; A = Left; D = Right")
    m = input("Where do you want to move? :")
    global hero_col
    global hero_row
    global rHp
    rHp = 10
    #Remove previous location
    if world_map[hero_row][hero_col] == "H" :
        world_map[hero_row][hero_col] = ""
    elif world_map[hero_row][hero_col] == "H/T" :
        world_map[hero_row][hero_col] ="T"
        
    #Update postion hero is going
    if m.upper() == "S" :
        hero_row += 1
    elif m.upper() == "W" :
        hero_row -= 1
    elif m.upper() == "A" :
        hero_col -= 1
    elif m.upper() == "D" :
        hero_col += 1
    else :
        movement() #Prompt user for choice in case of human error
    #Increase day after moving    
    global days
    days += 1

    #If location hero is going have town, print H/T and call town_text function
    if world_map[hero_row][hero_col] == "T":
        world_map[hero_row][hero_col] = "H/T"
        print()
        town_text()
        
    #If location hero is going have King, print H/K and call attacking King function
    elif world_map[hero_row][hero_col] == "K" :
        world_map[hero_row][hero_col] = "H/K"
        print()
        print("Day {}: You see the Rat King!".format(days))
        attacking3()
    
    #If location hero is going have orb of power, call getOrb function
    elif world_map[orb_row][orb_col] == world_map[hero_row][hero_col] :
        if damage1 > 5 :
            world_map[hero_row][hero_col] = "H"
            print() 
            print("Day {} : You are out in the open.".format(days))
            attacking1()
        else :
            world_map[hero_row][hero_col] = "H"
            getOrb()
            print("Day {} : You are out in the open.".format(days))
            open_text()
            
    #Location hero is going is out in the open, call fighting rat function    
    else :
        world_map[hero_row][hero_col] = "H"
        print() 
        print("Day {} : You are out in the open.".format(days))
        attacking1()
        
    #prints the map for user to see current location
    for row in range(len(world_map)) :
        print()
        print("+---+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(len(world_map[row])) :
            print("{:^3}".format(world_map[row][col]),end = "")
            print("|", end="")
    print()
    print("+---+---+---+---+---+---+---+---+")
    print()
    #return

#MENU FUNCTIONS#
#In town menu        
def town_text() :
    print("Day {} : You are in a town.".format(days))
    print("1) View Character \n2) View Map \n3) Move \n4) Rest \n5) Save Game \n6) Exit Game")
    choice = int(input("Enter choice:"))
    if choice == 1 : 
        print()
        statistics()
        town_text()
    elif choice == 2 :
        print()
        printMap()
        town_text()
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
    #return  

#Out in the open menu  
def open_text() :
    print("1) View Character \n2) View Map \n3) Move \n4) Sense Orb \n5) Exit Game")
    choice = int(input("Enter choice :"))
    if choice == 1 :
        statistics()
        open_text()
    elif choice == 2 :
        printMap()
        open_text()
    elif choice == 3 :
        printMap()
        movement()
    elif choice == 4 :
        senseOrb()
    elif choice == 5 :
        quit()
    #return


#OTHERS#
#HERO Statistics
def statistics() :
    print("The Hero")
    print("  Damage: {}-{}".format(damage1, damage2))
    print(" Defence: {}".format(defence))
    print("      HP: {}".format(hp))
    if damage1 >= 7 : #If damage more than or equal to 7 means hero already have Orb of Power
        print("You are holding the Orb of Power")
    print()
    
#Resting in town
def rest() :
    print("You are fully healed")
    global hp
    hp = 20 #Set hero hp to 20 after healing
    global days
    days += 1
    print()
    town_text()


#Orb of Power#
def senseOrb() :
    if damage2 < 5 :
        if hero_row < orb_row and hero_col < orb_col :
            print("You sense that the Orb of Power is to the South-East")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row == orb_row and hero_col < orb_col :
            print("You sense that the Orb of Power is to the East")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row > orb_row and hero_col < orb_col :
            print("You sense that the Orb of Power is to the North-East")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row > orb_row and hero_col == orb_col :
            print("You sense that the Orb of Power is to the North")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row > orb_row and hero_col > orb_col :
            print("You sense that the Orb of Power is to the North-West")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row == orb_row and hero_col > orb_col :
            print("You sense that the Orb of Power is to the West")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row < orb_row and hero_col > orb_col :
            print("You sense that the Orb of Power is to the South-West")
            print("Day {} : You are out in the open.".format(days))
            open_text()
        elif hero_row < orb_row and hero_col == orb_col :
            print("You sense that the Orb of Power is to the South")
            print("Day {} : You are out in the open.".format(days))
            open_text()
    else :
        print("You already have the Orb Of Power")
        print("Day {} : You are out in the open.".format(days))
        open_text()
        
               
#When hero finds the Orb       
def getOrb() :
    print("You found the Orb of Power!")
    print("Your attack increases by 5!")
    global damage1
    global damage2
    damage1 += 5
    damage2 += 5
    print("Your defence increases by 5!")
    global defence
    defence += 5
    print()

#FIGHTING FUNCTIONS#
#Encountering the Rat
def attacking1() :
    print("Encounter! - Rat")
    print("Damage: {}-{}".format(rDamage1, rDamage2))
    print("Defence: {}".format(rDefence))
    print("HP: {}".format(rHp))
    print("1) Attack \n2) Run")
    choice = int(input("Enter choice:"))
    if choice == 1 : #attack the rat
        print()
        attacking2()
    if choice == 2 : #run from the rat
        print()
        print("You run away and hide")
        print()
        print("1) View Character \n2) View Map \n3) Move \n4) Sense Orb \n5) Exit Game")
        choice = int(input("Enter choice :"))
        if choice == 3 :
            printMap()
            movement()
        elif choice == 5 :
            quit()
        else : #Only option 3 and 5 will work if hero run away
            attacking1()
                  

#Fighting the Rat
def attacking2() :
    damagetohero = random.randint(rDamage1, rDamage2)
    damagetorat = random.randint(damage1, damage2)
    print("You deal {} damage to the Rat".format(damagetorat)) #show damage dealt to the rat
    global rHp
    global hp
    rHp = rHp - damagetorat
    if rHp <= 0 : #If rat hp is 0 or below, print that it is dead
        print("The Rat is dead! You are victorious!")
        rHp = 10
        open_text()
    else : 
        if damagetohero <= defence : #If rat damage to hero is lesser or equal to heros defense, block the attack
            print("You blocked the attack!")
        else : #Else hero hp decrease
            hp = hp - damagetohero
            print("Ouch! The Rat hit you for {} damage!".format(damagetohero))
    print("You have {} HP left.".format(hp)) #Show hero hp
    if hp > 0 : #If hero hp is still above 0 and not rat not dead yet
        attacking1()
    else : #Else if hero hp fall below 0, game over hero is dead
        sys.exit("GAME OVER! Your HP reached 0! You are DEAD!")
        
#Encountering Rat King
def attacking3() :
    print("Encounter! - Rat King")
    print("Damage: {}-{}".format(kDamage1, kDamage2))
    print("Defence: {}".format(kDefence))
    print("HP: {}".format(kHp))
    print("1) Attack \n2) Run")
    choice = int(input("Enter choice:"))
    if choice == 1 : #attack the rat king
        print()
        attacking4()
    if choice == 2 : #run from the rat king
        print()
        print("1) View Character \n2) View Map \n3) Move \n4) Sense Orb \n5) Exit Game")
        choice = int(input("Enter choice :"))
        if choice == 3 :
            printMap()
            movement()
        elif choice == 5 :
            quit()
        else :
            attacking3()
            
#Attacking the Rat King
def attacking4() :
    kDamagetohero = random.randint(kDamage1, kDamage2)
    damagetoKingrat = random.randint(damage1, damage2)
    if damage1 < 6 : #Checks if Hero has orb of power, if not Rat King is immune
        print("You do not have the Orb of Power - the Rat King is immune")
        print("You deal 0 damage to the Rat King")
    else : #Else just damage the King
        print("You deal {} damage to the King Rat".format(damagetoKingrat))
    global kHp
    global hp
    kHp = kHp - damagetoKingrat
    if kHp <= 0 : #If Ratking HP is 0 or below means you win
        file = open("leaderboard.txt", "a")
        file.write(str(days) + "\n")
        file.close()
        sys.exit("The Rat King is dead! You are victorious! \nCongratulations, you have defeated the Rat King! \nThe world is saved! You win!")
        
    else :
        if kDamagetohero <= defence : #If King Damage is lesser or equal to hero defense, block it
            print("You blocked the attack!")
        else : #Else hero take damage from King
            hp = hp - kDamagetohero 
            print("Ouch! The King Rat hit you for {} damage!".format(kDamagetohero))
    print("You have {} HP left.".format(hp))
    if hp > 0 : #If Hero hp is still above 0, keep attacking till King is dead
        attacking3()
    else : #Else if hero hp drops below 0, hero dies and you lose
        sys.exit("GAME OVER! Your HP reached 0! You are DEAD!")
      
    
#SAVING AND LOADING#
#Saves progress like Hero current stats, postion etc
def savingGame() :
    herosavedLocation = [hero_row, hero_col]
    orbsavedLocation = [orb_row, orb_col]
    try :
        file = open("savedata.txt", "w+")
        file.write(str(hp) + "\n") #save hero current hp to file
        file.write(str(damage1) + "\n") #save hero curent damage1 to file
        file.write(str(damage2) + "\n") #save hero current damage1 to file
        file.write(str(defence) + "\n") #save hero current defence to file
        file.write(str(herosavedLocation[0]) + "\n") #save hero current row location to file
        file.write(str(herosavedLocation[1]) + "\n") #save hero current col location to file
        file.write(str(orbsavedLocation[0]) + "\n") #save orb row location to file
        file.write(str(orbsavedLocation[1]) + "\n") #save orb col location to file
        file.write(str(days) + "\n")

        file.close()
        
    except FileNotFoundError :
        print("File not Found")



#Load heros previously saved stats, postion etc
def loadGame() :
    global hp
    global damage1
    global damage2
    global defence
    global hero_row
    global hero_col
    global orb_row
    global orb_col
    global days
    try :
        file = open("savedata.txt", "r")
        line = file.readline() #Reads hero saved hp
        hp = int(line)
        
        line = file.readline() #Read hero saved damage1
        damage1 = int(line)
        
        line = file.readline() #Read hero saved damage2
        damage2 = int(line)
        
        line = file.readline() #Read hero saved defence
        defence = int(line)
        
        line = file.readline() #Read hero saved row position
        hero_row = int(line)
        
        line = file.readline() #Read hero saved col position
        hero_col = int(line)
        
        line = file.readline() #Read orb saved row position
        orb_row = int(line)
        
        line = file.readline() #Read horb saved col position
        orb_col = int(line)
        
        line = file.readline() #Read saved days
        days = int(line)

        file.close()
        
    except :
        print("No save data")
        print("Welcome to Ratventure!")
        print("----------------------")
        print("1) New Game \n2) Resume Game \n3) View Leaderboard \n4) Exit Game")
        starting()

#Code your main program here
print("Welcome to Ratventure!")
print("----------------------")
print("1) New Game \n2) Resume Game \n3) View Leaderboard \n4) Exit Game")
starting()

    
