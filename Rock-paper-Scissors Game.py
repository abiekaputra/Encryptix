import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score
    computer = random.choice(choices)
    if choice == computer:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    resultLabel.config(text=f"Computer chose: {computer}\n{result}", fg="#333333")
    scoreLabel.config(text=f"Your Score: {user_score}  |  Computer Score: {computer_score}")

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    resultLabel.config(text="")
    scoreLabel.config(text="Your Score: 0  |  Computer Score: 0")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

buttonsFrame = tk.Frame(root, bg="#f0f0f0")
buttonsFrame.pack()

for text in choices:
    tk.Button(buttonsFrame, text=text, font=("Arial", 12), width=10, bg="#4CAF50", fg="white",
              command=lambda x=text: play(x)).pack(side="left", padx=5)

resultLabel = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
resultLabel.pack(pady=20)

scoreLabel = tk.Label(root, text="Your Score: 0  |  Computer Score: 0", font=("Arial", 12), bg="#f0f0f0")
scoreLabel.pack(pady=10)

tk.Button(root, text="Play Again", font=("Arial", 12, "bold"), bg="#f44336", fg="white",
          width=15, command=reset).pack(pady=10)

root.mainloop()
