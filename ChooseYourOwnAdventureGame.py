name =  input("Type your name ")
print("Welcome", name, "to this adventure!") # dont need to put spaces when concatinating using commas

print("You are on a dirt road.. It has come to an end to a cliff. You can either go to your left or to your right.")
answer = input("Which way would you like to go??(left/right): ").lower()

if answer =="left":
    print("After walking for a mile, you came to a deep blue lake! You can walk around it or swim across it.")
    answer = input("(walk/swim): ").lower()

    if answer == "walk":
        print("You walked for few miles.. but still couldn't cross the pond and ultimately reached to a drier stretch of pond!")
        print("Would you like to cross the swamp or keep walking untill you get to the edge of it?")
        answer = input("cross/walk): ").lower()

        if answer == "walk":
            print("You kept walking and after few miles reached the edge of the lake! There is a house on the side.")
            answer = input("Would you like to cross the lake or rest in the house for sometime?(rest/cross): ").lower()

            if answer == "cross":
                print("You have successfully reached your destination! You WON!")

            elif answer == "rest":
                print("The house seemed empty at first so you entered it went to sleep!")
                print("Unfortunetly it was the resting spot of bandits who returned while you were asleep and captured you!")
                answer = input("You can either fight the bandits or play dead and run when they throw you out!(fight/dead): ").lower()

                if answer == "fight":
                    print("You fought but the bandits out-numbered you! They beat you to a pulp.. now you are dead.")
                    print("You LOST!")

                elif answer == "dead":
                    print("Playing dead after getting beaten up made them throw you outside the house!")
                    print("You ran as fast as you could and crossed the lake and reached your destination! You WON!")
                
                else:
                    print("Invalid option. GAME OVER!")
            
            else:
                    print("Invalid option. GAME OVER!")
        
        elif answer == "cross":
            print("Though the patch seemed dry because of being continuously being exposed to water it had turned into quick sand!")
            print("You are being sucked inside the wetland! You LOST!")

        else:
            print("Invalid option. GAME OVER!")

    elif answer == "swim":
        print("There were alligators in the lake!")
        print("You LOST :(")
    else:
        print("Invalid option. GAME OVER!")

elif answer == "right":
    print("You came to a river.. There's a bridge, but it looks very wobbly!")
    print("Do you wanna cross the river using the bridge?")
    answer = input("Or wanna jump on the big high river stones to cross the path?(bridge/stones): ").lower()

    if answer == "bridge":
        print("You crossed the river tripping once/twice on the bridge in the process!")
        print("You have safely reached your destination! You WON!")
    
    elif answer == "stones":
        print("You slipped while jumpimg on stones to cross the river! YOU ARE DROWNING!")
        answer = input("Do you know how to swim? (Yes/No): ").lower()

        if answer == 'yes':
            print("You swim across the river and successfully reach your destination! You WIN!")

        elif answer == 'no':
            print("You drown in the river and LOSE!")

        else:
            print("Invalid option. GAME OVER!")
    
    else:
            print("Invalid option. GAME OVER!")

else:
    print("Invalid option. GAME OVER!")

print("Thank you for playing! Bye", name, "!")