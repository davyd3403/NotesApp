print("\n=== Notes Manager ===")

notes = []

while True:

    print("1. Add note")
    print("2. Show notes")
    print("3. Delete note")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note here: ")
        notes.append(note)
    elif choice == "2":
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")
    elif choice == "3":
        index = int(input("Enter the index of the note to delete: "))
        notes.pop(index)
    elif choice == "4":
        break
    else:
        print("Invalid option.")

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