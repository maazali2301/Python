import random

def rps():

    print("\nRules: R for Rock, P for Paper, S for Scissors...")
    user_choice = input("Enter Your Pick: ")
    computer_choice = random.choice(["R", "P", "S"])

    print("\nComputer Chose: " + computer_choice)
    if user_choice == computer_choice:
        print("\nIt's a Tie!\n")
        return

    if win(user_choice, computer_choice):
        print("\nUser Has Won!\n")

    else:
        print("\nComputer Has Won!\n")

def win(user, comp):
    if (user== "R" and comp=="S"):
        return True
    if (user== "S" and comp=="P"):
        return True
    if (user== "P" and comp=="R"):
        return True

def display():
        print("*"*20)
        print("ROCK-PAPER-SCISSORS")
        print("*"*20)


def main():
    
    display()
    ch = "yes"
    while (ch == "yes" or ch=="Yes" or ch=="YES"):
        rps()
        ch = input("\nPlay Again?(yes/no) ")



if __name__ == "__main__":
    main()
