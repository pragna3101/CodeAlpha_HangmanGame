# CodeAlpha Python Programming Internship - Task 1: Hangman Game

## 📝 Project Overview
This repository contains a premium, interactive, console-based **Hangman Game** developed in Python. It randomly selects a word from a predefined pool of words, handles guess validations, displays a detailed visual progression using ASCII hangman stages, and tracks player stats in real-time.

## 🎯 Objective
The objective of this project is to implement standard Python programming structures (functions, collections, user interaction, strings, loops, and condition checks) within a complete, clean, and interactive environment. It serves as an exemplary project demonstrating foundational software development principles.

---

## ✨ Features
- **Smart Game Engine**: Random word selection from an extensive collection.
- **Detailed Visualizations**: 7 custom ASCII-art hangman stages reflecting wrong attempt progression.
- **Input Validation**: Rejects invalid characters, numeric values, multiple inputs, and repeated guesses with clear, helpful alerts.
- **Real-Time Trackers**: Displays word progress masked with underscores, remaining incorrect guesses, and alphabetical lists of guessed letters.
- **Replay Option**: Keeps players engaged by prompting to restart another game immediately upon win or loss.
- **Highly Readability**: Fully PEP8 compliant structure with comprehensive comments.

---

## 🛠️ Technologies Used
- **Language**: Python 3
- **Core Modules**: `random`

---

## 📂 Folder Structure
```text
CodeAlpha_HangmanGame/
│
├── hangman.py          # Core Game Script (Execution Entrypoint)
├── README.md           # Project Documentation
└── screenshots/        # Directory containing sample run previews
```

---

## 🚀 Installation & Getting Started

### Prerequisites
- **Python**: Make sure Python 3.x is installed. You can check your version in a command prompt or terminal using:
  ```bash
  python --version
  ```

### Installation Steps
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/CodeAlpha_HangmanGame.git
   ```
2. Navigate into the project folder:
   ```bash
   cd CodeAlpha_HangmanGame
   ```

---

## 🎮 How to Run
Execute the main script via terminal or command prompt:
```bash
python hangman.py
```

---

## 📸 Sample Console Output

```text
========================================
        WELCOME TO HANGMAN GAME!        
========================================
Try to guess the secret word letter by letter.

       +---+
       |   |
           |
           |
           |
           |
    =========
    
Word: _ _ _ _ _ _ _ _ _ _
Remaining Incorrect Attempts: 6
Guessed Letters: None
----------------------------------------
Enter a letter to guess: E

Good job! 'E' is in the secret word!

       +---+
       |   |
           |
           |
           |
           |
    =========
    
Word: _ E _ E _ _ _ E _
Remaining Incorrect Attempts: 6
Guessed Letters: E
----------------------------------------
Enter a letter to guess: X
Oops! 'X' is NOT in the secret word.
```

---

## 📈 Future Improvements
- **Difficulty Settings**: Add game difficulty modes (Easy, Medium, Hard) that adjust the word lengths and allowed guess counts.
- **Category Selection**: Allow players to choose custom categories (e.g., Animals, Movies, Tech).
- **GUI Version**: Develop a desktop graphical interface using `tkinter` or a web version using Flask.
- **Score System**: Maintain high-score statistics and win streaks inside a persistent local JSON file.
