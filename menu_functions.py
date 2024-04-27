import main
import hero

def initialize_new_game():
    hero_name = str(input("Enter a name for your hero!:"))
    main.day = 1
    main.hero = hero.Hero(hero_name)


#HERO Statistics
def statistics():
    print("\n{}'s stats".format(main.hero.name))
    print("  Damage: {}".format(main.hero.attack_power))
    print(" Defence: {}".format(main.hero.defence))
    print("      HP: {}".format(main.hero.health))
    # if damage1 >= 7 : #If damage more than or equal to 7 means hero already have Orb of Power
    #     print("You are holding the Orb of Power")