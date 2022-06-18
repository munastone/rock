import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    player = input("Choose Rock, Paper or Scissors: ")
    if player in ["Rock", "rock", "r", "R"]:
        player = "R"
    elif player in ["Paper", "paper", "p", "P"]:
        player = "P"
    elif player in ["Scissors", "scissors", "s", "S"]:
        player = "S"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return player

def Computer_Option():
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "R"
    elif computer == 2:
        computer = "P"
    else:
        computer = "S"
    return computer


while True:
    print("")
    
    player = Choose_Option()
    computer = Computer_Option()

    print("")
    
    if player == computer:
            print('computer:',computer)
            print('player:',player)
            print('Tie!')
        
    elif computer == "P":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
            
    elif computer  == "S":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1

    elif player == "P":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1
        
        elif computer  == "P":
            print("You chose paper. The computer chose paper. You tied.")
            
            
        elif computer  == "S":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    elif player == "S":
        if computer  == "R":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
        
        elif computer  == "P":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1
            
        elif computer  == "S":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")
    
    player = input("Do you want to play again? (y/n)")
    if player in ["Y", "y", "yes", "Yes"]:
        pass
    elif player in ["N", "n", "no", "No"]:
        break
    else:
        break
