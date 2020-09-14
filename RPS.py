import random
human = ""
human_wins = 0
computer_wins = 0

while human_wins < 3 and computer_wins < 3:
    computer = random.choice(["rock", "paper", "scissors"])
    human = input("Please choose: rock, paper or scissors?")
    if computer == "rock" and human == "paper" or computer == "paper" and human == "scissors" or computer == "scissors" and human == "rock" :
        print("Computer chose: " + computer)
        print("Human chose: " + human)
        print("Human wins!")
        human_wins += 1
        print("Human: " + str(human_wins) + " Computer: " + str(computer_wins))
    elif computer == "rock" and human == "scissors"or computer == "paper" and human == "rock" or computer == "scissors" and human == "paper":
        print("Computer chose: " + computer)
        print("Human chose: " + human)
        print("Computer wins!")
        computer_wins += 1
        print("Human: " + str(human_wins) + " Computer: " + str(computer_wins))
    elif computer and human == "rock" or computer and human == "paper" or computer and human =="scissors":
        print("Computer chose: " + computer)
        print("Human chose: " + human)
        print("Its a tie!")
        print("Human: " + str(human_wins) + " Computer: " + str(computer_wins))
    else:
        print("Not a valid option, please pick rock, paper or scissors!")

if human_wins >=3:
    print("Congrats! You Win!")
if computer_wins >=3:
    print("Sorry, you lose, please try again")
