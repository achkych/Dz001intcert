import json
import datetime
class Note:
    def __init__(self, id, title, body, created_at=None, last_updated_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.datetime.now()
        self.last_updated_at = last_updated_at or datetime.datetime.now()