# 🎯 Guess the Number Game  

A simple Python-based number guessing game where you try to guess a randomly chosen number between **1 and 100**.

## 📌 How the Game Works  
1. The computer randomly selects a number between **1 and 100**.  
2. You choose a difficulty level:  
   - **Easy Mode**: 10 attempts  
   - **Hard Mode**: 5 attempts  
3. You enter guesses, and the game gives feedback:  
   - `"TOO HIGH!!!!!!!"` if your guess is too high.  
   - `"TOO LOW!!!!!!!"` if your guess is too low.  
   - `"CORRECT"` if you guessed the right number.  
4. You win if you guess correctly before running out of attempts.  
5. If you run out of attempts, you lose, and the game ends.  

## 🚀 How to Play  
1. Run the script in Python:  
   ```bash
   python guess_the_number.py
   ```
2. Follow the on-screen prompts to choose difficulty and enter guesses.  

## 🛠 Code Breakdown  
- **`check_answer(user_answer, actual_answer, turns)`**  
  - Compares the player's guess with the correct answer.  
  - Reduces remaining attempts if incorrect.  
- **`set_difficulty()`**  
  - Lets the user choose between **easy** and **hard** difficulty.  
- **`game()`**  
  - Controls the game flow, generates a random number, and handles user input.  

## 🎮 Example Gameplay  
```
Welcome to Guess the Number.
I'm thinking of a number between 1 and 100.
Choose a difficulty level. Type 'easy' or 'hard': easy
Shhhh! Answer is 42.
You have 10 turns left.
Guess a number between 1 and 100: 50
TOO HIGH!!!!!!!
Guess again.
You have 9 turns left.
Guess a number between 1 and 100: 30
TOO LOW!!!!!!!
Guess again.
...
CORRECT, You got it. The actual answer is: 42
```

Enjoy playing! 🔢🎉