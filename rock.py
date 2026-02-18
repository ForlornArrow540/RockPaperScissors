import random




#create some varieables
userInput = int(input("enter 1-Rock, 2-Paper, 3-Scissors: "))
if userInput == 1: 
    userText = "Rock"
elif userInput == 2:
    userText = "Paper"
else:
    userText = "Scissors"
print (userText)

computerInput = random.randint(1,3)
if computerInput == 1: 
    computerText = "Rock"
elif computerInput == 2:
    computerText = "Paper"
else:
    computerText = "Scissors"
print (computerText)

if computerInput == userInput: 
    print ("Tie")
else: 
    print ("Win")
#who wins

#computer = rock and user = scissors, computer wins
#computer = rock and user = paper, user wins
#computer = paper and user has scissors = computer wins 
#computer = paper and user has rock = computer wins 
#computer = scissors and user has paper, computer wins
#computer = scissors and user has rock, user wins
