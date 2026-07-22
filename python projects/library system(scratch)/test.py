class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True          # available by default

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []                    # collection of Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book.title}")
                return
        print(f"No book found with ISBN {isbn}.")

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print(f"\nBooks matching '{title}':")
            for book in results:
                print(f"  {book}")
        else:
            print(f"No books found with title containing '{title}'.")
        return results

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is currently borrowed.")
                return
        print(f"No book found with ISBN {isbn}.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    book.is_available = True
                    print(f"Thank you for returning '{book.title}'.")
                else:
                    print(f"'{book.title}' was not borrowed.")
                return
        print(f"No book found with ISBN {isbn}.")


# ===== Testing the system =====
lib = Library()

# Add some books
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
b2 = Book("1984", "George Orwell", "978-0-452-28423-4")
b3 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
b4 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)

# Search by title
lib.search_by_title("1984")
lib.search_by_title("the")    # should show multiple matches

# Borrow a book
print("\n--- Borrowing ---")
lib.borrow_book("978-0-452-28423-4")   # borrow 1984
lib.borrow_book("978-0-452-28423-4")   # try to borrow again → should say already borrowed

# Return a book
print("\n--- Returning ---")
lib.return_book("978-0-452-28423-4")   # return 1984
lib.return_book("978-0-452-28423-4")   # return again → not borrowed

# Remove a book
print("\n--- Removing ---")
lib.remove_book("978-0-316-76948-0")   # remove Catcher in the Rye
lib.remove_book("000-0-000-00000-0")   # non-existent ISBN

# Search again to see updated availability
lib.search_by_title("1984")