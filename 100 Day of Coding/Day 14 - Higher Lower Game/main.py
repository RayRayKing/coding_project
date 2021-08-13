##Game to do higher or lower

## Game works by having a rolling score, it compares the number of followers
## you choose a or b. then right you continue, wrong you stop.
## if you continue, B becomes A. 
## produce a new B 
## and it continues to loop through until you get it wrong.
## A and b comes from the data file in data.
import art, data, random, os
INFO = data.data

## Checking user if they are correct, find the correct answer, then compare to user. returns true - when user is correct. else false.
def check_ans(user_choice,compare_a,compare_b):
    """user's decisions, option A, option b. Find the greater of option a and b then compares to the users choice. returns true if user is correct"""
    if compare_a["follower_count"] > compare_b["follower_count"]:
        winner = "a"
    else:
        winner = "b"
    return user_choice == winner

## create a function choose a new random data.
def choose_data():
    choice = random.choice(INFO)
    return choice

def vs_message(score,option1,option2):
    print(f"""
Compare A: {option1["name"]}, a {option1["description"]}, from {option1["country"]}.{art.vs}Compare B: {option2["name"]}, a {option2["description"]}, from {option2["country"]}.
    """)

##Counter for number of score
##intialization_ game setup

is_playing = True
current_score = 0
option_a = choose_data()
option_b = choose_data()
#game start
while is_playing:
 
    # print(option_a,option_b)
    print(f"Current score is {current_score}")
    vs_message(current_score,option_a,option_b)
    user_ans = input("Who has more followers? Type A or B: ")
    if check_ans(user_ans,option_a,option_b):
        current_score += 1
        print(f"Yay one Point. Current score is {current_score}")
        option_a = option_b
        while option_a == option_b:
            option_b = choose_data()
        os.system("cls") # Windows
    else:
        os.system("cls") # Windows
        print(f"Sorry, that is wrong! Final score {current_score}")
        is_playing = False
## deciding if the movement is ongoing


#populate the data in format  { name}, "a" {description}, "from" {country}