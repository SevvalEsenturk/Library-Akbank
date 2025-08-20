
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Proje modüllerimizi import edelim
from library import Library
from book import Book, EBook, AudioBook

# --- Pydantic Veri Modelleri ---
# API'den dönecek kitap modeli
class BookModel(BaseModel):
    title: str
    author: str
    isbn: str
    book_type: str = "physical"  # "physical", "ebook", "audiobook"
    file_format: str = None  # EBook için
    duration: int = None  # AudioBook için (dakika)

# POST isteği ile gelecek kitap ekleme modeli
class AddBookModel(BaseModel):
    isbn: str
    book_type: str = "physical"  # "physical", "ebook", "audiobook"
    file_format: str = "EPUB"  # EBook için varsayılan
    duration: int = 0  # AudioBook için varsayılan dakika

# --- FastAPI Uygulaması ---
app = FastAPI(
    title="Kütüphane API",
    description="Kitapları yönetmek için basit bir API.",
    version="1.0.0"
)

# Library sınıfından bir nesne oluşturalım
# Not: Bu basit bir örnek olduğu için veriler bellekte tutulur.
# Sunucu yeniden başladığında library.json'dan yüklenir.
lib = Library()


# --- API Endpoint'leri ---

@app.get("/books", response_model=List[BookModel])
def get_all_books():
    """Kütüphanedeki tüm kitapları listeler."""
    books = []
    for book in lib.books:
        book_type = "physical"
        file_format = None
        duration = None
        
        if isinstance(book, EBook):
            book_type = "ebook"
            file_format = book.file_format
        elif isinstance(book, AudioBook):
            book_type = "audiobook"
            duration = book.duration
        
        books.append(BookModel(
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            book_type=book_type,
            file_format=file_format,
            duration=duration
        ))
    return books

@app.post("/books", response_model=BookModel)
def create_book(book_data: AddBookModel):
    """Verilen ISBN ile Open Library'den kitap bilgilerini çeker ve kütüphaneye ekler."""
    
    # Önce kitabın zaten var olup olmadığını kontrol edelim
    if any(b.isbn == book_data.isbn for b in lib.books):
        raise HTTPException(status_code=400, detail="Bu ISBN numaralı kitap zaten mevcut.")

    # Kitap türüne göre uygun sınıfı kullanarak kitap oluştur
    new_book = lib.add_book_with_type(book_data.isbn, book_data.book_type, 
                                      book_data.file_format, book_data.duration)
    
    if new_book is None:
        raise HTTPException(status_code=404, detail="Kitap Open Library'de bulunamadı veya eklenemedi.")
    
    # Return formatını BookModel'e uygun hale getir
    book_type = "physical"
    file_format = None
    duration = None
    
    if isinstance(new_book, EBook):
        book_type = "ebook"
        file_format = new_book.file_format
    elif isinstance(new_book, AudioBook):
        book_type = "audiobook"
        duration = new_book.duration
    
    return BookModel(
        title=new_book.title,
        author=new_book.author,
        isbn=new_book.isbn,
        book_type=book_type,
        file_format=file_format,
        duration=duration
    )

@app.delete("/books/{isbn}", response_model=dict)
def delete_book(isbn: str):
    """Verilen ISBN numarasına sahip kitabı kütüphaneden siler."""
    # remove_book metodunun da API'ye uygun şekilde güncellenmesi gerekiyor.
    if lib.remove_book(isbn):
        return {"message": f"ISBN {isbn} numaralı kitap başarıyla silindi."}
    else:
        raise HTTPException(status_code=404, detail="Silinecek kitap bulunamadı.")

