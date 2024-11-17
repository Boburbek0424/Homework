# notebook.py

class Note:
    def __init__(self, note_id, text):
        self.id = note_id
        self.text = text

class Notebook:
    def __init__(self):
        self.notes = {}
        self.next_id = 1

    def show_all_notes(self):
        if not self.notes:
            print("No notes available.")
            return
        print("All Notes:")
        for note_id, note in self.notes.items():
            print(f"ID: {note_id}, Text: {note.text[:30]}...")  # Show preview (30 chars)

    def show_note_details(self, note_id):
        note = self.notes.get(note_id)
        if note:
            print(f"Note ID: {note_id}")
            print(f"Text: {note.text}")
        else:
            print(f"Note with ID {note_id} not found.")

    def create_note(self, text):
        note = Note(self.next_id, text)
        self.notes[self.next_id] = note
        print(f"Note created with ID {self.next_id}.")
        self.next_id += 1

    def update_note(self, note_id, new_text):
        note = self.notes.get(note_id)
        if note:
            note.text = new_text
            print(f"Note ID {note_id} updated.")
        else:
            print(f"Note with ID {note_id} not found.")

    def delete_note(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
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
    notebook = Notebook()
    show_menu()

    while True:
        choice = input("Enter your choice: ").strip().upper()
        if choice == '1':
            notebook.show_all_notes()
        elif choice == '2':
            note_id = int(input("Enter Note ID: "))
            notebook.show_note_details(note_id)
        elif choice == '3':
            text = input("Enter note text: ")
            notebook.create_note(text)
        elif choice == '4':
            note_id = int(input("Enter Note ID: "))
            new_text = input("Enter new note text: ")
            notebook.update_note(note_id, new_text)
        elif choice == '5':
            note_id = int(input("Enter Note ID: "))
            notebook.delete_note(note_id)
        elif choice == 'Q':
            print("Goodbye!")
            break
        elif choice == 'M':
            show_menu()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
