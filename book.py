import json
class ContactBook:
    def __init__(self, filename="cbook.json"):
        self.filename = filename 
        try:
            with open(self.filename, "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}
    def save(self):
        with open(self.filename, "w") as f:
            
            json.dump(self.contacts, f, indent=4)
    def list(self):
        print("Contacts List:")
        for name, number in self.contacts.items():
            print(f"{name}: {number}")
    def add_contact(self):
        name = input("Please enter the name of the contact: ").strip()
        number = input("please enter the contact's number: ").strip()
        if name in self.contacts:
            print("this contact name already exist")
        else:
            self.contacts[name] = number
            self.save()
            print("Contact saved")
    def display_contact(self):
        name = input("Enter the name of the contact: ").strip()
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")  
        else:
            print("This contact name does not exist")
    def delete_contact(self):
        name = input("Enter the name of the contact you would like to delete: ").strip()
        if name in self.contacts:
            confirm = input(f"Are you sure you would like to delete {name} contact?(Yes/No): ").strip() 
            if confirm == "yes":    
                self.contacts.pop(name)
                self.save()
                print("Contact deleted") 
            else:
                return
        else:
            print("this contact name does not exist")
    def change_contact(self):
        name = input("Enter the name of the contact you would like to change: ").strip()
        if name in self.contacts:    
            option = input("Would you like to change (1 or 2): \n"
                        "1. name of the contact\n"
                        "2. contact's number\n").strip()
            if option == "1":
                new_name = input("Enter the new name: ").strip()
                if new_name in self.contacts:
                    print("This name already exists.")
                else:
                    value = self.contacts[name]
                    self.contacts[new_name] = value
                    self.contacts.pop(name)
                    self.save()
                    print(f"the contact has been updated to {new_name}: {self.contacts[new_name]}")
            elif option == "2":
                new_num = input("Enter the new contact number: ").strip()
                self.contacts[name] = new_num
                self.save()
                print(f"the contact has been updated to {name}: {self.contacts[name]}")
            else:
                print("Invalid choice, please pick between 1 or 2!")
        else:
            print("this contact name does not exist")
            return
def main():
    book = ContactBook()
    
    while True:   
        print("------Contact Book------ -\n"
            "1. Contact list\n"
            "2. Add new contact\n"
            "3. View Contact\n"
            "4. Delete contact\n"
            "5. Change contact\n"
            "6. Exit\n")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            book.list()
        elif choice == "2":
            book.add_contact()
        elif choice == "3":
            book.display_contact()
        elif choice == "4":
            book.delete_contact()
        elif choice == "5":
            book.change_contact()
        elif choice == "6":
            print("Goodbye!")
            break
main()
                   
    