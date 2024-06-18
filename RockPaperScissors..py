import random

print("Welcome to rock,paper and scissors game !!!!")
choices = ["rock", "paper", "scissors"]
your_score = 0
finished = False

while not finished:
  user = input("What do you choose? (Rock,Paper or Scissors).\n")
  user_choice=user.lower()

  computer_choice = random.choice(choices)
  print("Computer chose:", computer_choice)

  if user_choice == computer_choice:
    print("Draw")
  
  elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
    print("User wins")
    your_score +=1
  
  else:
    print("Computer wins")
  
  playgame = input("do you want to continue the game (yes/no)")
  playgame.lower()
  if playgame  == "no":
    finished = True
    print(f"Your final score is {your_score}")
  elif playgame == "yes":
    finished = False
  else:
    print("The game has been ended!! ")
    print(f"Your final score is {your_score}")