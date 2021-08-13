#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns`, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


##diffcultiy easy - 10; hard - guess 5 

##
import art,random
print(art.logo)
print(""" Welcome to the guessing game!
I'm thinking of a number from 1-100.
""")

is_playing = True
#test
while is_playing:
    is_wrong_guess = True
    #generating number list and choosing number
    nums_list = [x for x in range (0,101)]
    num_choice = random.choice(nums_list)
    print(f"test mode: Answer is {num_choice}")
    ##q: hard or easy
    diff = input("Do you want to play easy or hard? ").lower
    if diff == "hard":
        attempt = 5
    else:
        attempt = 10
    print(f"You have {attempt} attempts remaining to guess the number.")

    while is_wrong_guess:
        user_guess = int(input("Guess a number. "))
        # respond high or low, if correct, end game
        #function to check number, return the proper choice with game end. 
        if num_choice == user_guess:
            print("You guess it right!")
            is_wrong_guess = False
        elif user_guess > num_choice:
            print("Too high. Guess Again!")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print("Too low. Guess Again!")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")

        if attempt == 0:
            print("You've run out of guesses! Game Over!")
            is_wrong_guess = False
    play_again = input("Do you want to play again? y/n ")
    if play_again == "n":
        is_playing = False
    elif play_again =="y":
        is_wrong_guess = True

#function for checking high or low and returning