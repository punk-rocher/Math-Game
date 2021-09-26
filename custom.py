import easy
import medium
import hard

#custom menu
def Custom_game():
    while True:
        print("1.Easy game mode")
        print("2.Medium game mode")
        print("3.Hard game mode")
        print("4.Return to main menu")
        option=input("Enter your dificultty.")
        if option == "1":
            easy.Easy_game_mode()
        elif option == "4":
            break
        elif option == "2":
            medium.Medium_game_mode()
        elif option == "3":
            hard.Hard_game_mode()
      
            

        
    

    
