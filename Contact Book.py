import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def add():
    name = nameEntry.get()
    phone = phoneEntry.get()
    email = emailEntry.get()
    address = addressEntry.get()
    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        listBox.insert(tk.END, f"{name} ({phone})")
        clear()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def view():
    try:
        index = listBox.curselection()[0]
        contact = contacts[index]
        clear()
        nameEntry.insert(0, contact["Name"])
        phoneEntry.insert(0, contact["Phone"])
        emailEntry.insert(0, contact["Email"])
        addressEntry.insert(0, contact["Address"])
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def delete():
    try:
        index = listBox.curselection()[0]
        contacts.pop(index)
        listBox.delete(index)
        clear()
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def search():
    query = simpledialog.askstring("Search", "Enter name or phone to search:")
    if query:
        listBox.delete(0, tk.END)
        for contact in contacts:
            if query.lower() in contact["Name"].lower() or query in contact["Phone"]:
                listBox.insert(tk.END, f"{contact['Name']} ({contact['Phone']})")

def update():
    try:
        index = listBox.curselection()[0]
        contacts[index] = {
            "Name": nameEntry.get(),
            "Phone": phoneEntry.get(),
            "Email": emailEntry.get(),
            "Address": addressEntry.get()
        }
        listBox.delete(index)
        listBox.insert(index, f"{contacts[index]['Name']} ({contacts[index]['Phone']})")
        clear()
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear():
    nameEntry.delete(0, tk.END)
    phoneEntry.delete(0, tk.END)
    emailEntry.delete(0, tk.END)
    addressEntry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Name:", bg="#f0f0f0").pack(pady=2)
nameEntry = tk.Entry(root, font=("Arial", 12))
nameEntry.pack(pady=2)

tk.Label(root, text="Phone:", bg="#f0f0f0").pack(pady=2)
phoneEntry = tk.Entry(root, font=("Arial", 12))
phoneEntry.pack(pady=2)

tk.Label(root, text="Email:", bg="#f0f0f0").pack(pady=2)
emailEntry = tk.Entry(root, font=("Arial", 12))
emailEntry.pack(pady=2)

tk.Label(root, text="Address:", bg="#f0f0f0").pack(pady=2)
addressEntry = tk.Entry(root, font=("Arial", 12))
addressEntry.pack(pady=2)

tk.Button(root, text="Add", bg="#4CAF50", fg="white", command=add).pack(pady=5)
tk.Button(root, text="View", bg="#2196F3", fg="white", command=view).pack(pady=5)
tk.Button(root, text="Update", bg="#FFC107", fg="white", command=update).pack(pady=5)
tk.Button(root, text="Delete", bg="#f44336", fg="white", command=delete).pack(pady=5)
tk.Button(root, text="Search", bg="#9C27B0", fg="white", command=search).pack(pady=5)

listBox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listBox.pack(pady=10)

root.mainloop()