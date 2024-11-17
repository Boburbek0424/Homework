# File to store notes
FILE_NAME = "notes.txt"

# Load notes from file
def load_notes():
    notes = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                note_id, text = line.strip().split("|")
                notes.append({"id": note_id, "text": text})
    except FileNotFoundError:
        pass  # No file exists yet; start with an empty list
    return notes

# Save notes to file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        for note in notes:
            file.write(f"{note['id']}|{note['text']}\n")

# Display all notes in the requested format
def display_notes(notes):
    if not notes:
        print("\nNo notes available.\n")
    else:
        print("\nNotebook:")
        for note in notes:
            print(f"{note['id']}- '{note['text']}'")
        print()

# Create a new note
def create_note(notes):
    text = input("Enter note content: ")
    note_id = str(len(notes) + 1)
    notes.append({"id": note_id, "text": text})
    save_notes(notes)
    print("Note created successfully.")
    display_notes(notes)

# Update a note
def update_note(notes):
    note_id = input("Enter note ID to update: ")
    for note in notes:
        if note["id"] == note_id:
            new_text = input("Enter new text: ")
            note["text"] = new_text
            save_notes(notes)
            print("Note updated successfully.")
            display_notes(notes)
            return
    print("Note not found.")

# Delete a note
def delete_note(notes):
    note_id = input("Enter note ID to delete: ")
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully.")
            display_notes(notes)
            return
    print("Note not found.")

# Main menu
def main_menu():
    print("\nNotebook Application")
    print("1. Create Note")
    print("2. Update Note")
    print("3. Delete Note")
    print("4. Show Note Details")
    print("5. Show All Notes")
    print("Q. Quit")
    print("M. Show Menu Again")

# Main application logic
def main():
    notes = load_notes()
    main_menu()
    while True:
        choice = input("Enter your choice: ").strip().upper()

        if choice == "1":
            create_note(notes)
        elif choice == "2":
            update_note(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            note_id = input("Enter note ID: ")
            for note in notes:
                if note["id"] == note_id:
                    print(f"ID: {note['id']}")
                    print(f"Text: {note['text']}")
                    break
            else:
                print("Note not found.")
        elif choice == "5":
            display_notes(notes)
        elif choice == "Q":
            print("Exiting... Goodbye!")
            break
        elif choice == "M":
            main_menu()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
