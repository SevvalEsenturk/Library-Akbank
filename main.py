from library import Library
from book import Book

def main():
    lib = Library()

    while True:
        print("\n--- Kütüphane Menüsü ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın (1-5): ")

        if choice == '1':
            isbn = input("Eklenecek kitabın ISBN numarasını girin: ")
            if isbn:
                lib.add_book(isbn)
            else:
                print("ISBN alanı boş bırakılamaz.")
        elif choice == '2':
            isbn = input("Silinecek kitabın ISBN numarasını girin: ")
            lib.remove_book(isbn)
        elif choice == '3':
            lib.list_books()
        elif choice == '4':
            isbn = input("Aranacak kitabın ISBN numarasını girin: ")
            book = lib.find_book(isbn)
            if book:
                print("\nKitap bulundu:")
                print(book)
            else:
                print("Bu ISBN ile eşleşen bir kitap bulunamadı.")
        elif choice == '5':
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir numara girin.")

if __name__ == "__main__":
    main()
