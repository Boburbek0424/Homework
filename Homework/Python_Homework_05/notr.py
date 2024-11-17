# notebook.py

def loading_notes():
    notes = {}
    try:
        with open('notes.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                note_id, text = line.strip().split(' - ', 1)
                notes[int(note_id)] = text.strip("'")
    except FileNotFoundError:
        # If the file does not exist, we'll create an empty notebook.
        pass
    return notes

def saving_notes(notes):
    with open('demo.txt', 'w') as file:
        for note_id, text in notes.items():
            file.write(f"{note_id} - '{text}'\n")

def show_all_notes(notes):
    if not notes:
        print("No notes available.")
        return
    print("All Notes:")
    for note_id, text in notes.items():
        print(f"{note_id} - '{text}'")

def show_note_details(notes, note_id):
    note = notes.get(note_id)
    if note:
        print(f"Note ID: {note_id}")
        print(f"Text: {note}")
    else:
        print(f"Note with ID {note_id} not found.")

def create_note(notes, text):
    # Find the next available ID
    note_id = max(notes.keys(), default=0) + 1
    notes[note_id] = text
    saving_notes(notes)
    print(f"Note created with ID {note_id}.")

def update_note(notes, note_id, new_text):
    if note_id in notes:
        notes[note_id] = new_text
        saving_notes(notes)
        print(f"Note ID {note_id} updated.")
    else:
        print(f"Note with ID {note_id} not found.")

def delete_note(notes, note_id):
    if note_id in notes:
        del notes[note_id]
        saving_notes(notes)
        print(f"Note ID {note_id} deleted.")
    else:
        print(f"Note with ID {note_id} not found.")

def show_menu():
    print("""
Select choices:
1. Show All Notes
2. Show Note Details
3. Create Note
4. Update Note
5. Delete Note
Q. Quit
M. Show Menu
""")

def main():
    notes = loading_notes()
    show_menu()

    while True:
        choice = input("Enter your choice: ").strip().upper()
        if choice == '1':
            show_all_notes(notes)
        elif choice == '2':
            try:
                note_id = int(input("Enter Note ID: "))
                show_note_details(notes, note_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric ID.")
        elif choice == '3':
            text = input("Enter note text: ")
            create_note(notes, text)
        elif choice == '4':
            try:
                note_id = int(input("Enter Note ID: "))
                new_text = input("Enter new note text: ")
                update_note(notes, note_id, new_text)
            except ValueError:
                print("Invalid ID. Please enter a numeric ID.")
        elif choice == '5':
            try:
                note_id = int(input("Enter Note ID: "))
                delete_note(notes, note_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric ID.")
        elif choice == 'Q':
            print("Goodbye!")
            break
        elif choice == 'M':
            show_menu()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
