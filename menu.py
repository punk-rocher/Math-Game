import sys
import gameplay
import custom
import ppdetails
#intro
print("""$$$---------<***Game 2020***>---------$$$""")

while True:
    print("1.Quick game")
    print("2.Custom game")
    print("3.Display past game details")
    print("4.Exit")
    option=input("Enter your option.")
    if option == "1":
        gameplay.Quick_game()
    elif option == "4":
        break
    elif option == "2":
        custom.Custom_game()
    elif option == "3":
        ppdetails.ppd()
      
