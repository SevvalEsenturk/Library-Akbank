
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"""{self.title} by {self.author} (ISBN: {self.isbn})"""


class EBook(Book):
    """Represents an electronic book that inherits from Book."""
    def __init__(self, title, author, isbn, file_format="EPUB"):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        return f"""{self.title} by {self.author} (ISBN: {self.isbn}) [Format: {self.file_format}]"""


class AudioBook(Book):
    """Represents an audio book that inherits from Book."""
    def __init__(self, title, author, isbn, duration_in_minutes=0):
        super().__init__(title, author, isbn)
        self.duration = duration_in_minutes

    def __str__(self):
        return f"""{self.title} by {self.author} (ISBN: {self.isbn}) [Duration: {self.duration} mins]"""
