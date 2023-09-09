import tkinter as tk 
from tkinter import messagebox

a = tk.Tk()
a.title("Contact Book")

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name:
        contacts[name] = {"Phone": phone, "Email": email}
        contact_list.insert(tk.END, name)
    else:
        messagebox.showwarning("Name cannot be empty!")

def view_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if selected_contact:
        contact_details = contacts[selected_contact]
        messagebox.showinfo(selected_contact, f"Phone: {contact_details['Phone']}\nEmail: {contact_details['Email']}")
    else:
        messagebox.showwarning("Select a contact to view.")

def del_contact():
    select_contact = contact_list.curselection()
    if select_contact:
        contact_list.delete(select_contact)
    else:
        messagebox.showwarning("Select a contact to delete.")


name_label = tk.Label(a, text="Name:")
name_label.pack()
name_entry = tk.Entry(a)
name_entry.pack()

phone_label = tk.Label(a, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(a)
phone_entry.pack()

email_label = tk.Label(a, text="Email:")
email_label.pack()
email_entry = tk.Entry(a)
email_entry.pack()

add_button = tk.Button(a, text="Add Contact", command=add_contact)
add_button.pack()

contact_list = tk.Listbox(a)
contact_list.pack()

view_button = tk.Button(a, text="View Contact", command=view_contact)
view_button.pack()

del_button = tk.Button(a, text="Delete Contact", command=del_contact)
del_button.pack()

a.mainloop()
