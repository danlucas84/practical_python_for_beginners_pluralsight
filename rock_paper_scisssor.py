computer_choice = "scissors"

user_choice = input ("What do you want rock, paper or scissors?")

if computer_choice == user_choice:
    print ("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print("WIN the computer has" + computer_choice)
elif user_choice == "paper" and computer_choice == "rock":
    print("WIN WIN the computer has" + computer_choice)
elif user_choice == "scissors" and computer_choice == "paper":
    print("WIN WIN the computer has" + computer_choice)
else:
    print("You lose - computer wins:D")