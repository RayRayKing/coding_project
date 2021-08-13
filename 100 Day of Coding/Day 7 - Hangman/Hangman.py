import random
import hangman_art
import hangman_words

## Stages for each lives + lives
stages = hangman_art.stages
lives = len(hangman_art.stages)
print(hangman_art.logo)

## List of word and the chosen word
word_list = hangman_words.word_list
word_choice = random.choice(word_list)
# print(f"Your word choice is {word_choice}")


# Create display Blank list 
display = list()

word_len = len(word_choice)
for space in range(len(word_choice)):
    display.append('_')

print(f"It's a {word_len} lettre mot!")

#user guesses
guesses = dict()
guess_list = list()

#game conditions
end_of_game = False
while not end_of_game:
    print(f"{' '.join(display)}")

    #Ask for input
    guess = input("Guess a letter!\n").lower()
    #check if letter is guessed
    if guess in guesses:
        print(f"You've already guessed {guess} letter!")
        pass
    else:
        guesses[guess] = 0
        guess_list.append(guess)
    #check if word exists, if it does replace the blanks with letter found. 
        if guess in word_choice:
            for idx,ltr in enumerate(word_choice):
                if guess == ltr:
                    display[idx] = ltr
        else:
            lives -= 1
            print(f"The letter {guess} is not in the word!")

    # show remaining lives
    print(guess_list)

    print(f"{' '.join(display)}")
    print(stages[lives])

    #winning/losing conditions

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    elif lives == 0:
        end_of_game = True
        print(f"You Lose!\nThe word was {word_choice}!")

        
# check input against variable