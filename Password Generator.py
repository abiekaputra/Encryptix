import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entryLength.get())
        if length > 0:
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))
            resultLabel.config(text=f"Password: {password}", fg="#4CAF50")
        else:
            resultLabel.config(text="Please enter a positive number.", fg="red")
    except:
        resultLabel.config(text="Invalid input. Enter a valid number.", fg="red")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text="Enter password length:", bg="#f0f0f0").pack()

entryLength = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
entryLength.pack(pady=5)

tk.Button(root, text="Generate", bg="#4CAF50", fg="white", font=("Arial", 12), command=generate_password).pack(pady=10)

resultLabel = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333333")
resultLabel.pack(pady=10)

root.mainloop()