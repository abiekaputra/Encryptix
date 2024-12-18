import tkinter as tk

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x) if x != "=" else calculate()
    tk.Button(root, text=button, width=7, height=2, bg="#4CAF50" if button == "=" else "#FFFFFF",
              fg="#333333", font=("Arial", 14, "bold"), relief="raised", command=action).grid(
              row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="Clear", width=7, height=2, bg="#f44336", fg="white",
          font=("Arial", 14, "bold"), relief="raised", command=clear).grid(row=row_val, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
