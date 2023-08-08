from Note import Note
from NoteView import NoteView
from NotePresenter import NotePresenter
from NoteManager import NoteManager
import datetime

def main():
    file_path = 'notes.json'
    note_manager = NoteManager(file_path)
    note_view = NoteView()
    note_presenter = NotePresenter(note_manager, note_view)

    while True:
        print("Choose an option:")
        print("1. Create a note")
        print("2. Read notes")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Exit")

        choice = input("Enter the option number: ")

        if choice == '1':
            title = input("Enter the note title: ")
            body = input("Enter the note body: ")
            note_presenter.create_note(title, body)
        elif choice == '2':
            filter_date_str = input("Enter the filter date (YYYY-MM-DD) (leave empty for all notes): ")
            if filter_date_str:
                filter_date = datetime.datetime.strptime(filter_date_str, '%Y-%m-%d').date()
                note_presenter.read_notes(filter_date)
            else:
                note_presenter.read_notes()
        elif choice == '3':
            id = int(input("Enter the note ID: "))
            title = input("Enter the new note title: ")
            body = input("Enter the new note body: ")
            note_presenter.edit_note(id, title, body)
        elif choice == '4':
            id = int(input("Enter the note ID: "))
            note_presenter.delete_note(id)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()