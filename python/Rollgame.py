import random

def roll():
    min_value = 1
    max_value = 6
    game = random.randint(min_value,max_value)
    return game

while True:
    player = input("Please enter number of player (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2<= player <= 4:
            break
        else:
            print("Must be between (2-4) player.")
    else:
        print("Invalid answer, try again")


max_score = 50
player_score = [0 for i in range(player)] #[0,0]

while max(player_score) < max_score:
    for index in range(player):
        print("\nPlayer", index + 1, "just started!\n")
        score = 0
        while True:
            current_roll = input("would you like to roll (y/n): ")
            if current_roll.lower() != "y":
                break
            else:
            
                value = roll()
                if value == 1:
                    print("You roll is 1")
                    score = 0
                    break
                else:
                    score += value
                    print("Your roll is:",value)
                
                print("Your score is:",score)
        player_score[index] += score
    print("Your totoal score is: ",player_score[index])


        


