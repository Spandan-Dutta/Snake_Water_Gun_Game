"""
So the game is all about that:
1) If you choose Snake and computer choose Gun, you loose as computer shots the snake with a gun.
2) If you choose Gun and computer choose water, you loose as gun is thrown in the water.
3) If you choose Snake and computer choose Water, you wins as Snake drinks the water. 
"""
import random
print("Welcome to Snake, Water and Gun Game")
print("Total number of attempts is 10")
attempts = 1
human_score = 0
computer_score = 0

while (attempts <= 10):
    print("Choices are: Snake, Water and Gun")
    inp = input("Enter your choice: ")
    l = ["Snake", "Water", "Gun"]
    ran = random.choice(l)
    if inp == "Snake" and ran == "Snake":
        print("It's a Tie....")
        print("You and computer both chose Snake!")

    elif inp == "Water" and ran == "Water":
        print("It's a Tie....")
        print("You and computer both chose Water!")

    elif inp == "Gun" and ran == "Gun":
        print("It's a Tie....")
        print("You and computer both chose Gun!")

    elif inp == "Gun" and ran == "Snake":
        human_score = human_score + 1
        print("Congratulations!!!! You Won....")
        print("You chose Gun and computer chose Snake")
        print("You got 1 point")

    elif inp == "Gun" and ran == "Water":
        computer_score = computer_score + 1
        print("You Loose!!!")
        print("You chose Gun and computer chose Water")
        print("Computer gets 1 point")

    elif inp == "Snake" and ran == "Gun":
        computer_score = computer_score + 1
        print("You Loose!!!")
        print("You chose Snake and computer chose Gun")
        print("Computer gets 1 point")

    elif inp == "Snake" and ran == "Water":
        human_score = human_score + 1
        print("Congratulations!!!! You Won....")
        print("You chose Snake and computer chose Water")
        print("You got 1 point")
        
    elif inp == "Water" and ran == "Snake":
        computer_score = computer_score + 1
        print("You Loose!!!")
        print("You choose Water and computer chose Snake")
        print("Computer gets 1 point")

    elif inp == "Water" and ran == "Gun":
        human_score = human_score + 1
        print("Congratulations!!!! You Won....")
        print("You choose Water and computer chose Gun")
        print("You got 1 point")
        
    else:
        print("Invalid Input")
        print("Type the first digit as capital")
        continue

# Logic to tell how many attempts are left
    print(f"Number of attempts left are {10-attempts}")
    attempts = attempts + 1
    
    if attempts > 10:
        print("Game Over")
    

    print(f"Your Score:{human_score}", end = ",")
    print(f"Computer Score:{computer_score}")

if computer_score > human_score:
    print("Computer wins")
elif human_score > computer_score:
    print("You Win this game buddy!!!!")
else:
    print("It was Tie!!!")
    

