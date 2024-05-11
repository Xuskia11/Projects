name = input("type your name here: ")
print(f"hello {name} in my adventure")

#mission to find treasure
question = input("your mission is to find a treasure,you are in a big jungle and you see 2 ways left and right,which way you like to go?: ")
if question == "right":
    question = input("you see big black cave,there are 2 choice go away,or go in,which choice you want to pick?: ")


    if question == "go in":
        print("you were eaten by huge snake and you lost the game")
    elif question == "go away":
        question = input("you see big river what you gonna do now swim or walk away?: ")
        if question == "swim":
            print("you were eaten by alligatoes and you lost")
        elif question == "walk away":
            print("you were eaten by monkey and you lost")
        else:
            print("ivalid answer,you lost")
elif question == "left":
    question = input("you see huge sea and over the sea big island,what you gonna do across or go back?: ")
    if question == "go back":
        print("you lost the game")
    elif question == "across":
        question = input("you see now 2 cave,first cave and second cave,which one you like to go?: ")
    
        if question == "first":
            print("you were eaten by dragon and you lost")
        elif question == "second":
            print("congratulation,you found a treasure and you won")
        else:
            print("invalid answer,you lost")
print("thanks for playing,Bye bye")


