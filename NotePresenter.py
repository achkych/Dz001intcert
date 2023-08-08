from Note import Note
import datetime

class NotePresenter:
    def __init__(self, note_manager, note_view):
        self.note_manager = note_manager
        self.note_view = note_view

    def create_note(self, title, body):
        id = len(self.note_manager.notes) + 1
        note = Note(id, title, body)
        self.note_manager.create_note(note)
        self.note_view.display_success_message("Note created successfully.")

    def read_notes(self, filter_date=None):
        if filter_date:
            filtered_notes = self.note_manager.filter_notes_by_date(filter_date)
            self.note_view.display_notes(filtered_notes)
        else:
            self.note_view.display_notes(self.note_manager.notes)

    def edit_note(self, id, title, body):
        note = self.note_manager.find_note_by_id(id)
        if note:
            note.title = title
            note.body = body
            note.last_updated_at = datetime.datetime.now()
            self.note_manager.save_notes()
            self.note_view.display_success_message("Note edited successfully.")
        else:
            self.note_view.display_error_message("Note not found.")

    def delete_note(self, id):
        note = self.note_manager.find_note_by_id(id)
        if note:
            self.note_manager.delete_note(note)
            self.note_view.display_success_message("Note deleted successfully.")
        else:
            self.note_view.display_error_message("Note not found.")