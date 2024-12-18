from tkinter import *
import os

tasks = []

def load():
    if os.path.exists("allTasks.txt"):
        with open("allTasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
                listBox.insert(END, line.strip())

def save():
    with open("allTasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add():
    task = entry.get()
    if task:
        tasks.append(task)
        listBox.insert(END, task)
        entry.delete(0, END)
        save()
        print(f"Task '{task}' has been added successfully!")

def delete():
    try:
        index = listBox.curselection()[0]
        removed = listBox.get(index)
        tasks.remove(removed)
        listBox.delete(index)
        save()
        print(f"Task '{removed}' has been deleted.")
    except IndexError:
        print("Please select a task to delete.")

def display():
    print("\nTO-DO LIST")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

titleLabel = Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333333")
titleLabel.pack(pady=10)

entryFrame = Frame(root, bg="#f0f0f0")
entryFrame.pack(pady=10)

entry = Entry(entryFrame, width=25, font=("Arial", 12), bd=2, relief=SOLID)
entry.grid(row=0, column=0, padx=10, pady=5)

addButton = Button(entryFrame, text="Add Task", command=add, bg="#4CAF50", fg="white", font=("Arial", 10), relief=FLAT)
addButton.grid(row=0, column=1, padx=5)

listFrame = Frame(root, bg="#f0f0f0")
listFrame.pack(pady=10)

scrollbar = Scrollbar(listFrame)
scrollbar.pack(side=RIGHT, fill=Y)

listBox = Listbox(listFrame, width=40, height=15, font=("Arial", 12), bd=2, relief=SOLID, yscrollcommand=scrollbar.set)
listBox.pack()

scrollbar.config(command=listBox.yview)

buttonFrame = Frame(root, bg="#f0f0f0")
buttonFrame.pack(pady=10)

deleteButton = Button(buttonFrame, text="Delete Task", command=delete, bg="#f44336", fg="white", font=("Arial", 10), relief=FLAT)
deleteButton.grid(row=0, column=0, padx=10)

showButton = Button(buttonFrame, text="Show Tasks (CLI)", command=display, bg="#2196F3", fg="white", font=("Arial", 10), relief=FLAT)
showButton.grid(row=0, column=1, padx=10)

load()

root.mainloop()