from library import librarian

# create empty library dictionary
my_library = {}

# add books
librarian.add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
librarian.add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(my_library, "1984", "George Orwell", "9780451524935")

# display all books
librarian.display_books(my_library)
print()

# check out a book
librarian.check_out_book(my_library, "9780316769174")

# display again
librarian.display_books(my_library)
print()

# return the book
librarian.return_book(my_library, "9780316769174")

# display again
librarian.display_books(my_library)