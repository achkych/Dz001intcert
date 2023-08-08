class NoteView:
    def display_notes(self, notes):
        for note in notes:
            print(f"ID: {note.id}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Created At: {note.created_at}")
            print(f"Last Updated At: {note.last_updated_at}")
            print()

    def display_success_message(self, message):
        print(message)

    def display_error_message(self, message):
        print(message)