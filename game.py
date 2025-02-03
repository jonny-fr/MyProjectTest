import random

choosable = ["Rock", "Paper", "Scissors"]
while True:
    chosen = input("Choose Rock,Paper or Scissors: ")
    if chosen in ["Rock", "Paper", "Scissors"]:
        break

computerschoice = random.choice(choosable)


if chosen == computerschoice:
    print("It's a tie!")
elif chosen == "Rock":
    if computerschoice == "Paper":
        print("You lose!", computerschoice, "covers", chosen)
    else:
        print("You win!", chosen, "smashes", computerschoice)
elif chosen == "Paper":
    if computerschoice == "Scissors":
        print("You lose!", computerschoice, "cuts", chosen)
    else:
        print("You win!", chosen, "covers", computerschoice)
elif chosen == "Scissors":
    if computerschoice == "Rock":
        print("You lose...", computerschoice, "smashes", chosen)
    else:
        print("You win!", chosen, "cuts", computerschoice)


print("You chose: ", chosen, "Computer chose: ", computerschoice)




