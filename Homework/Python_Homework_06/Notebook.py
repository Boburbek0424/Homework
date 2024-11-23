from datetime import datetime

class Note:
    def __init__(self, note_id, content, created_date):
        self.id = note_id
        self.content = content
        self.created_date = created_date
    
    def display(self):
        print(f"ID: {self.id} | Created: {self.created_date} | Content: {self.content}")

    def to_file_format(self):
        # Representing the note in text format
        return f"{self.id} | {self.created_date} | {self.content}"

    @classmethod
    def from_file_format(cls, note_line):
        # Create a Note object from a line in the file
        note_id, created_date, content = note_line.split(" | ", 2)
        return cls(int(note_id), content, created_date)

class Notebook:
    def __init__(self, filename="demo.txt"):
        self.filename = filename
        self.notes = []
        self.current_id = 1  # Start with ID 1
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    note = Note.from_file_format(line.strip())
                    self.notes.append(note)
                    self.current_id = max(self.current_id, note.id + 1)
        except FileNotFoundError:
            print("\nNo existing notes found, starting a new notebook.")

    def save_notes(self):
        with open(self.filename, "w") as file:
            for note in self.notes:
                file.write(note.to_file_format() + "\n")

    def show_all_notes(self):
        if not self.notes:
            print("\nNo notes found.")
        else:
            print("\nAll Notes:")
            for note in self.notes:
                print(f"ID: {note.id} | Created: {note.created_date} | Content: {note.content}")

    def show_note_details(self):
        note_id = int(input("\nEnter the ID of the note: "))
        for note in self.notes:
            if note.id == note_id:
                note.display()  # Displays the ID, created date, and content of the note
                return
        print("\nNote not found.")

    def create_note(self):
        text = input("\nEnter the note content: ")
        new_note = Note(
            note_id=self.current_id,
            content=text,
            created_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.notes.append(new_note)
        self.current_id += 1  # Increment the ID for the next note
        self.save_notes()  # Save to file
        print("\nNote created successfully.")

    def update_note(self):
        note_id = int(input("\nEnter the ID of the note to update: "))
        for note in self.notes:
            if note.id == note_id:
                print(f"Current Content: {note.content}")
                note.content = input("Enter the new content: ")
                self.save_notes()  # Save to file
                print("\nNote updated successfully.")
                return
        print("\nNote not found.")

    def delete_note(self):
        note_id = int(input("\nEnter the ID of the note to delete: "))
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()  # Save to file
                print("\nNote deleted successfully.")
                return
        print("\nNote not found.")

    def menu(self):
        while True:
            print("\nNotebook Application")
            print("     1. Show All Notes")
            print("     2. Show Note Details")
            print("     3. Create Note")
            print("     4. Update Note")
            print("     5. Delete Note")
            print("     6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_all_notes()
            elif choice == "2":
                self.show_note_details()
            elif choice == "3":
                self.create_note()
            elif choice == "4":
                self.update_note()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                print("\nExiting application... \nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")


# Run the application
if __name__ == "__main__":
    notebook = Notebook()
    notebook.menu()
