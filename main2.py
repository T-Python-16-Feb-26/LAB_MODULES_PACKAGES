from library.librarian import add_book, display_books,check_out_book,remove_book

# إنشاء مكتبة فارغة (dictionary)
library = {}

# -------------------------
# Add books
# -------------------------
add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
add_book(library, "1984", "George Orwell", "9780451524935")

print("Library after adding books:")
display_books(library)
print()

# -------------------------
# Checkout book
# -------------------------
check_out_book(library, "9780316769174")

print("Library after checkout:")
display_books(library)
print()

# -------------------------
# Remove book
# -------------------------
remove_book(library, "9780446310789")

print("Library after removing a book:")
display_books(library)