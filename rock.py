import random

def Get_user_input():
    userInput = int(input("enter 1-Rock, 2-Paper, 3-Scissors: ")) 
    while userInput != 1 and userInput != 2 and userInput != 3:
        userInput = int(input("enter 1-Rock, 2-Paper, 3-Scissors: ")) 
    return userInput

def Get_selection_text(SelectValue):
    if SelectValue == 1: 
       ReturnText = "Rock"    
    elif SelectValue == 2:
        ReturnText = "Paper"
    else:
      ReturnText = "Scissors"
    return ReturnText

def Determine_winner():
    if computerInput == userInput: 
      print ("The result is a Tie!")

#computer = rock and user = scissors, computer wins
    if computerInput == 1 and userInput == 3:
     print (f"Computer Wins!")
     computeWins =+ 1

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
  
#create some varieables
userName = ""
while userName == "":
    userName = input("Enter your name: ")


#userInput = Get_user_input()
gameCount = 0
gameCountMax = 5
computeWins = 0 
userWins = 0
while gameCount < gameCountMax:
    gameCount += 1
    userInput = Get_user_input()
    userText = Get_selection_text(userInput)
    print (f"User Selection is: {userText}")

    computerInput = random.randint(1,3)
    computerText = Get_selection_text(computerInput)
    print (f"Computer Selection is: {computerText}")

    Determine_winner()
    

print (f"We played {gameCountMax}")
