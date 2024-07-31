import menu

global hero
global hero_position
global day
global game_map

def main():
    try: 
        menu.main_menu()
    
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()