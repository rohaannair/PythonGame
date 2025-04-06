import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors, lizard, Spock: )")
  options = ["rock", "paper", "scissors", "lizard", "Spock"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  #return player_choice
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == "paper" and computer == "rock":
    return "Paper covers rock! You win!"
  elif player == "paper" and computer =="scissors":
    return "Scissors cut paper! You lose!"
  elif player == "paper" and computer == "lizard":
    return "Lizard eats paper! You lose!"
  elif player == "paper" and computer == "Spock":
    return "Paper disproves Spock! You win!"
    
  elif player == "rock" and computer == "scissors":
    return "Rock smashes scissors! You win!"
  elif player == "rock" and computer == "paper":
    return "Paper covers rock! You lose."
  elif player == "rock" and computer == "lizard":
    return "Rock crushes lizard! You win!"
  elif player == "rock" and computer == "Spock":
    return "Spock vaporizes rock! You lose."

  elif player == "scissors" and computer == "paper":
    return "Scissors cut paper! You win!"
  elif player == "scissors" and computer == "rock":
    return "Rock smashes scissors! You lose."
  elif player == "scissors" and computer == "lizard":
    return "Scissors decapitates lizard! You win!"
  elif player == "scissors" and computer == "Spock":
    return "Spock smashes scissors! You lose."

  elif player == "lizard" and computer == "paper":
    return "Lizard eats paper! You win!"
  elif player == "lizard" and computer == "rock":  
    return "Rock crushes lizard! You lose."
  elif player == "lizard" and computer == "scissors":
    return "Scissors decapitates lizard! You lose."
  elif player == "lizard" and computer == "Spock":  
    return "Lizard poisons Spock! You win!"

  elif player == "Spock" and computer == "paper":
    return "Paper disproves Spock! You lose."
  elif player == "Spock" and computer == "rock":  
    return "Spock vaporizes rock! You win!"
  elif player == "Spock" and computer == "scissors":
    return "Spock smashes scissors! You win!"
  elif player == "Spock" and computer == "lizard":
    return "Lizard poisons Spock! You lose."
  
  else:
    return "It's a tie!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)