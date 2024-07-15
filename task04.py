def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:  
            return "Contact already exists."
        else:
            contacts[name] = phone
            return "Contact added."
    except ValueError:
        return "Wrong data. Please check that your input contains name and phone"

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        return f"{name} phone is {contacts[name]}"
    else:
        return "Contact does not exist."
    
def show_all (contacts):
    return f"List of stored contacts:\n {contacts}"

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts: 
            contacts[name] = phone
            return "Phone was changed."
        else:
            return "Contact does not exist. Please add contact"
    except ValueError:
        return "Wrong data. Please check that your input contains name and phone"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
