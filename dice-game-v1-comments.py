# builtin fuction that need to be called
from random import randint
from time import sleep
from datetime import datetime
from csv import reader, DictWriter
from sys import exit
from os.path import isfile
from operator import itemgetter

# counter for the nume of rounds for each player
rounds = 0
# scores for players
score1 = 0
score2 = 0
#  scores for tie breaker
score1_tb = 0
score2_tb = 0
# dictionary to store users
users = {"raylin": "1234", "tommy": "1234", "luke": "1234"}

# set up the date for the game
# grad the date and time now
date = datetime.now()
# formats the date DD-MM-YYYY
game_date = (date.strftime("%d-%b-%Y"))

# ------------Welcome screen--------------------------------
# when the program first runs this check if the scores.csv exists if it exists it will print the menu
# because if you try to check the scores and this file is not there the program will crash
# CSV stands for comma seperated values
if isfile("scores.csv"):
    print("\n--------Welcome to Dice Game---------")
    print("1. Please enter 'n' to add new player")
    print("2. Please enter 'p' to play Dice Game")
    print("3. Please enter 's' to display top 5 players")
    print("4. Please enter 'q' to quit game")
else:
    # if scores.csv does not exist it creates the file and then prints menu
    # open file called scores.csv to append information to the file.
    with open("scores.csv", "a") as file:
        # set the headers for the csv file
        headers = ["Name", "Score", "Date"]
        # Writes the headers for the CSV file
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        # Writes the data for the CSV file
        csv_writer.writerow({
            "Name": "Raylin",
            "Score": "77",
            "Date": "06-Nov-2020"
        })
        print("\n--------Welcome to Dice Game---------")
        print("1. Please enter 'N' to add new player")
        print("2. Please enter 'P' to play Dice Game")
        print("3. Please enter 'S' to display top 5 players")
        print("4. Please enter 'Q' to quit game")

# if you thpe capital letter it will set to lower case3go
menu = input("\nPlease select option from menu: ").lower()
# checks that user has selected valid option from menu.
# while loop will run till valid option selected.
while menu not in ["n", "p", "s", "q"]:
    print(f"\n{menu}: is not a valid option ")
    menu = input("\nPlease select option from menu: ").lower()

if menu == "q":
    print("You have ended the game")
    exit()

if menu == "s":
    # opens the scores.csv file
    with open("scores.csv") as file:
        csv_reader = reader(file)
        # skips the frist row so headers are not printed on the scores
        next(csv_reader)
        # create the scores screen
        print("\n*****************TOP FIVE PLAYERS***************")
        print("*****Player****    ****Score****   \t****Date*****\n")
        # sorts the scores list in descending order
        # itemgetter used to pick point to sort om
        scores = sorted(csv_reader, reverse=True, key=itemgetter(1))
        # slices scores list with onlu top five scores
        top = scores[0:5]
        # goes throught the list of scores and prints the top 5 players
        for t in top:
            print(f"{t[0]}\t\t\t{t[1]}\t\t{t[2]}")

        input("\nPress 'enter' to play Dice Game")

if menu == "n":
    username = input("Please enter username: ")
    pword1 = input("Please enter password: ")
    pword2 = input("Please re-enter password: ")
    # compares password1 to password2 to see if the match
    if pword1 == pword2:
        # if the match prints account created
        print("-------------------------------------------")
        print("User account successfully created")
        print("-------------------------------------------")
        # saves user to users dictionary
        users[username] = pword2
        input("\nPress 'enter' to play Dice Game")
    # if password1 and password2 dont match it take password one as
    # the correct password and asks for password2 again
    if pword1 != pword2:
        # takes password1 as correct password
        correct_pword = (pword1)
        # while True:
        print("Passwords did not match")
        pword2 = input("Enter password again: ")
        if pword2 == correct_pword:
            # print("Correct password has been entered")
            print("-------------------------------------------")
            print("User account successfully created")
            print("-------------------------------------------")
            users[username] = pword2
            input("\nPress 'enter' to play Dice Game")
        else:
            print("Incorrect password, please start again")
            exit()

check_failed = True
while check_failed:
    print("Player 1 enter their username and password")
    username1 = input("Please enter your username ")
    pword = input("Please enter your password ")
    for u, p in users.items():
        if u == username1 and p == pword:
            player1 = username1.title()
            print("-------------------------------------------")
            print(f"Player #1 is {player1}")
            print("-------------------------------------------")
            check_failed = False
            check_failed = True
            while check_failed:
                print("Player 2 enter their username and password")
                username2 = input("Please enter your username ")
                pword = input("Please enter your password ")
                for u, p in users.items():
                    if u == username2 and p == pword:
                        player2 = username2.title()
                        print("-------------------------------------------")
                        print(f"Player #2 is {player2}")
                        print("-------------------------------------------")
                        check_failed = False
                        sleep(2)
                        print("-------------------------------------------")
                        print("Dice Game Starting.......")
                        print("-------------------------------------------")
                        sleep(2)

# ------------Dice Game-------------------------------------

while rounds < 1:
    # player one
    input(f"\n{player1} hit 'enter' roll dice")
    print("\nrolling......")
    print(f"\n--------{player1} Rolling Round #{rounds + 1}-----\n")
    dice1 = randint(1, 6)
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    dice2 = randint(1, 6)
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    total = dice1 + dice2
    if dice1 == dice2:
        print("Adding 10 points for even total.")
        total += 10
        print("Rolling dice again for double")
        dice3 = randint(1, 6)
        print(f"Extra roll total: {dice3}")
        total += dice3
    elif total % 2 == 0:
        total += 10
        print("Adding 10 points for even total.")
    else:
        total -= 5
        print("Subtracting 5 points for odd total.")
    print(f"Round total is: {total}")
    # print(score1)
    # score1 += total
    score1 = 100
    print(f"Player score is: {score1}")
    print("-------------------------------------------")
    if score1 <= 0:
        print("-------------------------------------------")
        print(f"{player1} your score is 0 or less")
        print(f"{player1} you have lost the game")
        print("-------------------------------------------")
        exit()

    # player 2
    input(f"\n{player2} hit 'enter' roll dice")
    print("\nrolling......")
    print(f"\n--------{player2} Rolling Round #{rounds + 1}-----\n")
    dice1 = randint(1, 6)
    print(f"Dice #1 this round is: {dice1}")
    sleep(2)
    dice2 = randint(1, 6)
    print(f"Dice #2 this round is: {dice2}")
    sleep(2)
    total = dice1 + dice2
    if dice1 == dice2:
        print("Adding 10 points for even total.")
        total += 10
        print("Rolling dice again for double")
        dice3 = randint(1, 6)
        print(f"Extra roll total: {dice3}")
        total += dice3
    elif total % 2 == 0:
        total += 10
        print("Adding 10 points for even total.")
    else:
        total -= 5
        print("Subtracting 5 points for odd total.")
    print(f"Round total is: {total}")
    # print(score2)
    # score2 += total
    score2 = 100
    print(f"Player score is: {score2}")
    print("-------------------------------------------")
    if score2 <= 0:
        print("-------------------------------------------")
        print(f"{player2} your score is 0 or less")
        print(f"{player2} you have lost the game")
        print("-------------------------------------------")
        exit()
    rounds += 1


print("\n")
print("-------------------------------------------")
print(f"Total score for player 1 - {player1} is", score1)
print("-------------------------------------------")
print(f"Total score for player 2 - {player2} is", score2)
print("-------------------------------------------")

# ------------Tie break-------------------------------------

if score1 == score2:
    print("Game Drawn")
    print("-------------------------------------------")
    print("\n************************TIE BREAK****************************")
    print("Each player rolls one die again to see who scores the highest")
    sleep(2)
    no_win = True
    while no_win:
        input(f"\n{player1} hit 'enter' roll dice")
        print("\nrolling......")
        sleep(2)
        dice_tb1 = randint(1, 6)
        print(f"\n--------{player1} Tie Break--------\n")
        score1_tb = dice_tb1
        # score1_tb = 2
        print(f"{username1} rolled: {score1_tb}")
        if score1_tb % 2 == 0:
            score1_tb += 10
            print("Adding 10 points for even total.")
            print(f"{player1} score is: {score1_tb}")
        else:
            score1_tb -= 5
            print("Subtracting 5 points for odd total.")
            print(f"{player1} score is: {score1_tb}")
        if score1_tb <= 0:
            print("-------------------------------------------")
            print(f"{player1} your score is 0 or less")
            print(f"{player1} you have lost the game")
            print("-------------------------------------------")
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player2,
                    "Score": score2,
                    "Date": game_date
                })
                exit()

        input(f"\n{username2} hit 'enter' roll dice")
        print("\nrolling......")
        sleep(2)
        dice_tb2 = randint(1, 6)
        print(f"\n--------{player2} Tie Break--------\n")
        score2_tb = dice_tb2
        # score2_tb = 6
        print(f"{player2} rolled: {score2_tb}")
        if score2_tb % 2 == 0:
            score2_tb += 10
            print("Adding 10 points for even total.")
            print(f"{player2} score is: {score2_tb}")
        else:
            score2_tb -= 5
            print("Subtracting 5 points for odd total.")
            print(f"{player2} score is: {score2_tb}")
        if score2_tb <= 0:
            print("-------------------------------------------")
            print(f"{player2} your score is 0 or less")
            print(f"{player2} you have lost the game")
            print("-------------------------------------------")
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player1,
                    "Score": score1,
                    "Date": game_date
                })
                exit()
        if score1_tb == score2_tb:
            print("-------------------------------------------")
            print("Still no winner you will have to roll again")
            print("-------------------------------------------")
        elif score1_tb > score2_tb:
            no_win = False
            print("-------------------------------------------")
            print(f"{player1} has won the Tie Break.")
            print("-------------------------------------------")
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player1,
                    "Score": score1,
                    "Date": game_date
                })
                sys.exit()
        else:
            no_win = False
            print("-------------------------------------------")
            print(f"{player2} has won the Tie Break.")
            print("-------------------------------------------")
            with open("scores.csv", "a") as file:
                headers = ["Name", "Score", "Date"]
                csv_writer = DictWriter(file, fieldnames=headers)
                csv_writer.writerow({
                    "Name": player2,
                    "Score": score2,
                    "Date": game_date
                })
                exit()

elif score1 > score2:
    print(f"{player1} is the winner of this game.")
    print("-------------------------------------------")
    with open("scores.csv", "a") as file:
        headers = ["Name", "Score", "Date"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            "Name": player1,
            "Score": score1,
            "Date": game_date
        })
        exit()
else:
    print(f"{player2} is the winner of this game.")
    print("-------------------------------------------")
    with open("scores.csv", "a") as file:
        headers = ["Name", "Score", "Date"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            "Name": player2,
            "Score": score2,
            "Date": game_date
        })
        exit()
