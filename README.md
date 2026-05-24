# Number Guessing Game 🎯

A simple yet engaging Python command-line game where players try to guess a randomly generated number between 1 and 100. Perfect for beginners learning Python fundamentals!

## 🎮 Game Overview

In this game, the computer generates a secret random number, and you have to guess it. The computer provides hints after each guess, telling you whether your guess is too high or too low. The game ends when you correctly guess the number, and it displays how many attempts it took you to win.

## ✨ Features

- **Random Number Generation**: Each game generates a unique random number between 1 and 100
- **Input Validation**: Ensures guesses are within the valid range (1-100)
- **Error Handling**: Gracefully handles invalid inputs (non-numeric values)
- **Feedback System**: Provides clear feedback indicating if guess is too high or too low
- **Attempt Counter**: Tracks the number of attempts taken to guess the correct number
- **Infinite Gameplay**: Play as many rounds as you want without restarting

## 🚀 How to Use

### Prerequisites
- Python 3.x installed on your system

### Running the Game

1. **Clone the repository** (if applicable):
```bash
git clone https://github.com/shivrajwakle/Number-Guess-Game.git
cd number-guessing-game
```

2. **Run the game**:
```bash
python number_guessing_game.py
```

3. **Follow the prompts**:
   - Enter your guess when prompted
   - The game will tell you if your guess is too high or too low
   - Continue guessing until you find the correct number
   - View your final score (number of attempts)

## 📋 Game Instructions

1. The computer thinks of a random number between 1 and 100
2. Enter your guess when prompted with "Guess the number (1-100): "
3. Read the feedback:
   - **"Too high!"** - Your guess is higher than the secret number
   - **"Too low!"** - Your guess is lower than the secret number
   - **"Correct! The number was X."** - You found it! 🎉
4. The game displays how many attempts it took you to win
5. Exit by pressing `Ctrl+C` or close the terminal

## 💡 Example Gameplay

```
Guess the number (1-100): 50
Too low!
Guess the number (1-100): 75
Too high!
Guess the number (1-100): 62
Too high!
Guess the number (1-100): 56
Too low!
Guess the number (1-100): 59
Correct! The number was 59.
You guessed it in 5 attempts.
```

## 🔧 Technical Details

### Code Structure

- **`random.randint(1, 100)`** - Generates the secret number
- **`while True` loop** - Continues game until correct guess
- **Try-Except block** - Handles invalid input gracefully
- **Input validation** - Checks if guess is in range (1-100)
- **Counter variable** - Tracks number of attempts

### Key Functions Used
- `random.randint()` - Generate random integer
- `int()` - Convert string input to integer
- `input()` - Get user input from command line
- `print()` - Display messages to user

## 🎓 Learning Objectives

This project demonstrates:
- Basic Python syntax and flow control
- Working with the `random` module
- Input/Output operations
- Error handling with try-except blocks
- While loops and conditional statements
- Variable management and counters

## 📈 Difficulty Levels (Potential Enhancement)

You can enhance this game by adding difficulty levels:
- **Easy**: 1-50 range
- **Medium**: 1-100 range (current)
- **Hard**: 1-500 range

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new features
- Submit pull requests

### Ideas for Enhancement
- Add a scoring system based on attempts
- Implement difficulty levels
- Add a hint system
- Track high scores
- Create a graphical UI version using tkinter
- Add multiplayer functionality

## 📝 License

This project is open source and available under the MIT License. See the LICENSE file for more details.

## 👨‍💻 Author

Created as a beginner-friendly Python project to learn game development basics.

## 📧 Feedback

If you have any questions or suggestions, feel free to open an issue or contact the project maintainer.

---

**Happy Guessing! 🎲**
