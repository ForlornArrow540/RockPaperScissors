import random




#create some varieables
userName = input("Enter your name: ")

userInput = int(input("enter 1-Rock, 2-Paper, 3-Scissors: "))
if userInput == 1: 
    userText = "Rock"
elif userInput == 2:
    userText = "Paper"
else:
    userText = "Scissors"
print (f"User Selection is: {userText}")

computerInput = random.randint(1,3)
if computerInput == 1: 
    computerText = "Rock"
elif computerInput == 2:
    computerText = "Paper"
else:
    computerText = "Scissors"
print (f"Computer Selection is: {computerText}")

if computerInput == userInput: 
    print ("The result is a Tie!")

#computer = rock and user = scissors, computer wins
if computerInput == 1 and userInput == 3:
    print (f"Computer Wins!")

#computer = rock and user = paper, user wins
if computerInput == 1 and userInput == 2:
    print (f"{userName} Wins!")
    
#computer = paper and user has scissors = user wins 
if computerInput == 2 and userInput ==3:
    print (f"{userName} Wins!")

#computer = paper and user has rock = computer wins 
if computerInput == 2 and userInput ==1:
    print (f"Computer Wins!")

#computer = scissors and user has paper, computer wins
if computerInput == 3 and userInput ==2:
    print (f"Computer Wins!")

#computer = scissors and user has rock, user wins
if computerInput == 3 and userInput ==1:
    print (f"{userName} Wins!")
