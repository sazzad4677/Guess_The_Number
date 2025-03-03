from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(user_answer, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_answer > actual_answer:
        print("TOO HIGH!!!!!!!")
        return turns - 1
    elif user_answer < actual_answer:
        print("TOO LOW!!!!!!!")
        return turns - 1
    else:
        print("CORRECT, You got it. The actual answer is: ", actual_answer)


def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("Welcome to Guess the Number.")
    print("I'm thinking of a number between 1 and 100.")
    turns = set_difficulty()
    answer = randint(1, 100)
    print("Shhhh! Answer is {}.".format(answer))
    guess = 0
    while guess != answer:
        print("You have {} turns left.".format(turns))
        guess = int(input("Guess a number between 1 and 100: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Sorry, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
