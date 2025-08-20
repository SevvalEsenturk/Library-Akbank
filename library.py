
import json
import os
import httpx
from book import Book, EBook, AudioBook

class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                books = []
                for book_data in data:
                    # Kitap türüne göre uygun sınıfı kullan
                    if 'file_format' in book_data:
                        books.append(EBook(book_data['title'], book_data['author'], 
                                         book_data['isbn'], book_data['file_format']))
                    elif 'duration' in book_data:
                        books.append(AudioBook(book_data['title'], book_data['author'], 
                                             book_data['isbn'], book_data['duration']))
                    else:
                        books.append(Book(book_data['title'], book_data['author'], book_data['isbn']))
                return books
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def add_book(self, isbn):
        if any(b.isbn == isbn for b in self.books):
            return None # Kitap zaten var

        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url, follow_redirects=True)
            response.raise_for_status()
            data = response.json()

            title = data.get('title', 'Başlık Bulunamadı')
            author_keys = [author['key'] for author in data.get('authors', [])]
            author_name = ", ".join(author_keys) if author_keys else "Yazar Bulunamadı"

            new_book = Book(title, author_name, isbn)
            self.books.append(new_book)
            self.save_books()
            return new_book
        except (httpx.HTTPStatusError, Exception):
            return None

    def add_book_with_type(self, isbn, book_type="physical", file_format="EPUB", duration=0):
        """Kitap türüne göre uygun sınıfı kullanarak kitap ekler"""
        if any(b.isbn == isbn for b in self.books):
            return None # Kitap zaten var

        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url, follow_redirects=True)
            response.raise_for_status()
            data = response.json()

            title = data.get('title', 'Başlık Bulunamadı')
            author_keys = [author['key'] for author in data.get('authors', [])]
            author_name = ", ".join(author_keys) if author_keys else "Yazar Bulunamadı"

            # Kitap türüne göre uygun sınıfı kullan
            if book_type == "ebook":
                new_book = EBook(title, author_name, isbn, file_format)
            elif book_type == "audiobook":
                new_book = AudioBook(title, author_name, isbn, duration)
            else:
                new_book = Book(title, author_name, isbn)

            self.books.append(new_book)
            self.save_books()
            return new_book
        except (httpx.HTTPStatusError, Exception):
            return None

    def remove_book(self, isbn):
        initial_count = len(self.books)
        self.books = [b for b in self.books if b.isbn != isbn]
        if len(self.books) < initial_count:
            self.save_books()
            return True # Başarıyla silindi
        else:
            return False # Kitap bulunamadı

    def list_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
            return
        print("--- Kütüphanedeki Kitaplar ---")
        for book in self.books:
            print(book)
        print("---------------------------")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
