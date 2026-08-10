print("\n=== Notes Manager ===")

notes = []

def save_notes():
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")

def load_notes():
    try:
        with open("notes.txt", "r") as file:
            for line in file:
                notes.append(line.strip())
    except FileNotFoundError:
        pass

load_notes()

def delete_all_notes():
    confirm_deletion = input("Are you sure you want to delete all notes? (y/n): ")

    if confirm_deletion == "y":
        notes.clear()
        save_notes()
        print("All notes deleted.")
    else:
        print("Deletion canceled.")

while True:

    print("1. Add note")
    print("2. Add more notes")
    print("3. Show notes")
    print("4. Delete note")
    print("5. Delete all notes")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note here: ")
        notes.append(note)
        save_notes()

    elif choice == "2":
        while True:
            try:
                many_notes = int(input("How many notes do you want to add? "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        for i in range(many_notes):
            note = input("Enter your note here: ")
            notes.append(note)
        save_notes()
        print("Notes added successfully.")

    elif choice == "3":
        if len(notes) == 0:
            print("No notes found.")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "4":
        try:
            index = int(input("Enter the index of the note to delete: "))
            notes.pop(index - 1)
            save_notes()
            print("Note deleted successfully.")
        except ValueError:
            print("Invalid index. Please enter a valid note index.")
        except IndexError:
            print("Note does not exist.")

    elif choice == "5":
        delete_all_notes()
        
    elif choice == "6":
        confirm_exit = input("Are you sure you want to exit? (y/n): ")

        if confirm_exit == "y":
            print("The app is closed successfully.")
            break
        else:
            print("Exit canceled.")
    else:
        print("Invalid option.")
