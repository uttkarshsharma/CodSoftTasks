#ImportingLibraries
import tkinter as tk
from tkinter import messagebox

#Creating_"Contact" Class
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
#Creating_"ContactManagerApp" using class
class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, sticky="w")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="w")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=5)

    #AddingContact
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact added successfully.")

        self.clear_entries()

    #ViewingContact
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join(f"{contact.name}: {contact.phone}" for contact in self.contacts)
            messagebox.showinfo("Contacts", contact_list)

    #SearchingContact
    def search_contact(self):
        search_term = self.name_entry.get().lower()
        found_contacts = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]

        if not found_contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join(f"{contact.name}: {contact.phone}" for contact in found_contacts)
            messagebox.showinfo("Search Results", contact_list)

    #DeletingContact
    def delete_contact(self):
        search_term = self.name_entry.get().lower()
        found_contact = None
        for contact in self.contacts:
            if search_term in contact.name.lower() or search_term in contact.phone:
                found_contact = contact
                break

        if not found_contact:
            messagebox.showinfo("Info", "No contact found.")
        else:
            self.contacts.remove(found_contact)
            messagebox.showinfo("Success", "Contact deleted successfully.")

        self.clear_entries()

    #ClearingContactEntries
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
