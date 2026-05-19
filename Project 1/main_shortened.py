'''
1 for Rock
-1 for Paper
0 for Scissors
'''
import random


computer = random.choice([1, -1, 0])
youstr = (input("Enter your choice:  "))
youDict = {"R":1, "P": -1, "S": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}


younum = youDict[youstr]


print(f"Computer chose {reverseDict[computer]}\n and you chose {reverseDict[younum]}")

if(computer == younum):
    print("It's a tie!")
    
else:
    if((computer - younum) == -1 or (computer - younum) == 2):
        print("You Win!")


    # if(computer == 1 and younum == -1): (computer - younum) = 2
    #     print("You win!")
    # elif(computer == 1 and younum == 0): (computer - younum) = 1
    #     print("You Lose!")
    # elif(computer == -1 and younum == 1): (computer - younum) = -2
    #     print("You Lose!")
    # elif(computer == -1 and younum == 0): (computer - younum) = -1
    #     print("You Win!")
    # elif(computer == 0 and younum == 1): (computer - younum) = -1
    #     print("You Win!")
    # elif(computer == 0 and younum == -1): (computer - younum) = 1
    #     print("You Lose!")

    else:
        print("You Lose!")


