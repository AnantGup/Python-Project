print("Welcome to the brand new text adventure game")

name = input("What is your name: ")
print("Welcome", name)

age = int(input("What is your age: "))
if age >= 8 and age <= 115:
    print("You are eligible to play")
    wantToPlay = input("Do you want to play(y) or (n): ").lower()
    if wantToPlay == "y":
        print("Great let's start the game")
        left_right = input("Left(l) Or Right(r): ").lower()
        if left_right == "r":
            lake = input("Nice, you follow the path and reach a lake... Do you want to swim(s) or go around(a): ").lower()
            if lake == "a":
              house_school = input("Nice... You notice that there was a small house(h) and there was an big school but broken from somewhere(s)... Where you want to go: ").lower()
              if house_school == "h":
                  print("You managed to make food and you survived for that day")
                  L_M = input("Now you reached a place.... In the left there was a palace(l) and in the right there was also a palace(r). Where do you want to go: ").lower()
                  if L_M == "r":
                      print("The palace was of evils. They ate you and you lost")
                  elif L_M == "l":
                      print("You become the king of that palace and you won!!!!!")
                  else:
                      print("Enter something valid")
              elif house_school == "s":
                  print("There was a big hole and you didn't noticed, you fall and you lost")
              else:
                  print("Enter something valid")
            elif lake == "s":
                print("You were eaten by crocodiles and you lost")
            else:
                print("Enter something valid")
        elif left_right == "l":
            print("You fell down and lost")
        else:
            print("Enter something valid")
    elif wantToPlay == "n":
        print("Ok... Quitting")
    else:
        print("Enter something valid")
else:
    print("You are not eligible to play")
