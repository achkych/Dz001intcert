import json
import datetime
from Note import Note

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                notes = []
                for note_data in notes_data:
                    note = Note(
                        note_data['id'],
                        note_data['title'],
                        note_data['body'],
                        datetime.datetime.strptime(note_data['created_at'], '%Y-%m-%d %H:%M:%S'),
                        datetime.datetime.strptime(note_data['last_updated_at'], '%Y-%m-%d %H:%M:%S')
                    )
                    notes.append(note)
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        notes_data = []
        for note in self.notes:
            note_data = {
                'id': note.id,
                'title': note.title,
                'body': note.body,
                'created_at': note.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'last_updated_at': note.last_updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            notes_data.append(note_data)
        with open(self.file_path, 'w') as file:
            json.dump(notes_data, file)

    def create_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def find_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def delete_note(self, note):
        self.notes.remove(note)
        self.save_notes()

    def filter_notes_by_date(self, date):
        filtered_notes = []
        for note in self.notes:
            if note.created_at.date() == date or note.last_updated_at.date() == date:
                filtered_notes.append(note)
        return filtered_notes