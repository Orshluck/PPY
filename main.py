# zadanie 1
import random
import getpass
numbers = input("Give me number! : ")
list_of_numbers = numbers.split(',')
max = list_of_numbers[0]
min = list_of_numbers[0]
for number in list_of_numbers:
    if  number < min :
        min = number
    if number > max:
        max = number
print(f"Biggest number is :{max} ")
print(f"Smallest number is :{min}")

# 2 zadanie
# I will read from file, because i need to relearn it
file = open("List_of_cities.txt",'r',encoding="utf8") # "r" to read
cities = file.readlines()
selected_cities = random.sample(cities,10)
for i in range (10):
    print(f"For {i+1} city i recomend goint to {selected_cities[i].strip()}")

def printSumOfGames(list):
    sum = 0
    for i in range (len(list)):
        sum += int(list[i])
    return sum
# Zadanie 3
def computer_round(round):
    print(f"This is round {round} prepare to play")
    choice = int(input("What do you choose 1- rock 2 - paper 3-scissors : "))
    computerMove = random.randint(1,3)
    if computerMove == choice:
        print("This is a draw")
        return 0
    if (computerMove == 1 and choice == 2 ) or (computerMove == 2 and choice == 3 ) or (computerMove == 3 and choice == 1 ):
        print("You have won ")
        return 1;
    else:
        print("You lost")
        return -1;

def printScores(roundScores, Player):
    for i in range(len(roundScores)):
        outcome = roundScores[i]
        if Player:
            outcome = -outcome
        if outcome == -1:
            print(f"\tRound {i+1} was a draw")
        if outcome == 1:
            print(f"\tRound {i+1} was a victory")
        if outcome == 0:
            print(f"\tRound {i+1} was a defeat")
def player_round(round, playerA, playerB):

    print(f"This is round {round} prepare to play")
    choiceA = getpass.getpass(f"{playerA} what do you choose 1- rock 2 - paper 3-scissors : ")
    choiceB = getpass.getpass(f"{playerB} what do you choose 1- rock 2 - paper 3-scissors : ")
    if(choiceB == choiceA):
        print("This is a draw")
        return 0
    if (choiceA == 1 and choiceB == 2) or (choiceA == 2 and choiceB == 3) or (choiceA == 3 and choiceB == 1):
        print(f"{playerA} have won")
        return 1
    else:
        print(f"{playerB} have won")
        return 0

number_of_rounds = int(input("How many rounds do you want to play : "))
game_mode = int(input("What game mode do you want to play \n1-vs computer \n2-vs human\nChoice: "))
roundScores = [None] * number_of_rounds
if(game_mode == 1):
    for i in range (number_of_rounds):
        roundScores[i] = computer_round(i)
    printScores(roundScores)

if game_mode == 2:
    playerA = input("What is the name for player 1: ")
    playerB = input("What is the name for player 2: ")
    playerAScore = [None] * number_of_rounds
    playerBScore = [None] * number_of_rounds
    for i in range(number_of_rounds):
        outcome = player_round(i+1,playerA,playerB)
        playerAScore[i] = outcome
        playerBScore[i] = -outcome


    print(f"{playerA} have this outcomes :")
    printScores(playerAScore,False)
    print(f"At the end has {sum(playerAScore)} points")

    print(f"{playerB} have this outcomes :")
    printScores(playerBScore, True)
    print(f"At the end has {sum(playerBScore)} points")
    if sum(playerAScore) > sum(playerBScore):
        print(f"{playerA} has WON CONGRATS")
    elif sum(playerAScore) < sum(playerBScore):
        print(f"{playerB} has WON CONGRATS")
    else:
        print("Game has ended in a draw wow")