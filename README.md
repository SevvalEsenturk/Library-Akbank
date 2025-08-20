-->Kütüphane Yönetim Sistemi

Python ile geliştirilmiş modern bir kütüphane yönetim sistemi. Bu proje Global AI Hub Python 202 Bootcamp kapsamında geliştirilmiştir ve OOP, API entegrasyonu ve FastAPI kullanımını birleştirir.

^^ Özellikler
Nesne Yönelimli Programlama (OOP) ile modüler yapı
Farklı kitap türleri desteği:
-Fiziksel Kitaplar
-E-Kitaplar (EPUB formatı)
-Sesli Kitaplar (süre bilgisi ile)
Open Library API entegrasyonu ile otomatik kitap bilgisi çekme
FastAPI ile modern RESTful API
JSON tabanlı veri saklama
Otomatik API dokümantasyonu (Swagger UI)
***Gereksinimler
Python 3.8+
İnternet bağlantısı (Open Library API için)
🛠Kurulum
Projeyi klonlayın:
git clone https://github.com/SevvalEsenturk/Library-Akbank
cd kutuphane-yonetim-sistemi
Gerekli paketleri yükleyin:
pip install -r requirements.txt
-->Kullanım
1. Konsol Uygulaması
Basit menü tabanlı terminal uygulaması:

python main.py

Menü seçenekleri:

Kitap Ekle (ISBN ile otomatik bilgi çekme)
Kitap Sil
Kitapları Listele
Kitap Ara
Çıkış

2. Web API Servisi
Modern REST API servisi:
uvicorn api:app --reload
API Endpoints:
GET /books - Tüm kitapları listele
POST /books - Yeni kitap ekle
DELETE /books/{isbn} - Kitap sil
API Dokümantasyonu: http://localhost:8000/docs

***API Kullanımı
Kitap Ekleme
curl -X POST "http://localhost:8000/books" \
     -H "Content-Type: application/json" \
     -d '{
       "isbn": "9780140449136",
       "book_type": "physical"
     }'
Kitap Türleri
"physical" - Fiziksel kitap
"ebook" - E-kitap (file_format ile)
"audiobook" - Sesli kitap (duration ile)
E-Kitap Ekleme
{
  "isbn": "9780140449136",
  "book_type": "ebook",
  "file_format": "EPUB"
}
Sesli Kitap Ekleme
{
  "isbn": "9780140449136",
  "book_type": "audiobook",
  "duration": 540
}
--> Proje Yapısı
kutuphane-yonetim-sistemi/
├── api.py              # FastAPI web servisi
├── book.py             # Book sınıfları (Book, EBook, AudioBook)
├── library.py          # Library sınıfı (ana mantık)
├── main.py             # Konsol uygulaması
├── requirements.txt    # Python bağımlılıkları
├── library.json        # Kitap veritabanı (otomatik oluşur)
└── README.md          # Bu dosya
Örnek Kullanım
Web Arayüzü ile Test
API'yi başlatın: uvicorn api:app --reload
Tarayıcıda açın: http://localhost:8000/docs
"Try it out" butonları ile test edin
Programatik Kullanım
from library import Library
from book import Book, EBook, AudioBook

# Kütüphane oluştur
lib = Library()

# ISBN ile kitap ekle
book = lib.add_book("9780140449136")
if book:
    print(f"Eklenen kitap: {book}")

# E-kitap ekle
ebook = lib.add_book_with_type("9780451524935", "ebook", "EPUB")

# Kitapları listele
lib.list_books()
🔧 Teknik Detaylar
Kullanılan Teknolojiler
Python 3.8+
FastAPI - Modern web framework
Pydantic - Veri doğrulama
httpx - HTTP client
uvicorn - ASGI server
Veri Modeli
class Book:
    - title: str
    - author: str  
    - isbn: str

class EBook(Book):
    - file_format: str

class AudioBook(Book):
    - duration: int
API Referansı
Method	Endpoint	Açıklama
GET	/books	Tüm kitapları listele
POST	/books	Yeni kitap ekle
DELETE	/books/{isbn}	Kitap sil
GET	/docs	API dokümantasyonu
**->Eğitim Hedefleri
Bu proje aşağıdaki konuları kapsamaktadır:

OOP Prensipleri: Encapsulation, Inheritance, Polymorphism
API Entegrasyonu: Open Library REST API kullanımı
Web API Geliştirme: FastAPI ile modern API tasarımı
Veri Yönetimi: JSON tabanlı veri saklama
Hata Yönetimi: try-except blokları
Type Hints: Modern Python yazım stilleri
!!-->Katkıda Bulunma
Fork edin
Feature branch oluşturun (git checkout -b feature/amazing-feature)
Commit edin (git commit -m 'Add amazing feature')
Push edin (git push origin feature/amazing-feature)
Pull Request oluşturun
Lisans
Bu proje eğitim amaçlı geliştirilmiştir.

Geliştirici
Global AI Hub Python 202 Bootcamp Projesi
Eğer bu proje işinize yaradıysa, lütfen yıldızlamayı unutmayın!
