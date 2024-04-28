import menu

global hero
global day
global game_map

def main():
    try: 
        menu.main_menu()
    
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()