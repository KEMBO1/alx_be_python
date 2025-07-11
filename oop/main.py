# oop/main.py

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected output: 1984 by George Orwell, published in 1949

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected output: Book('1984', 'George Orwell', 1949)

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
