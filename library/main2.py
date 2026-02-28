import librarian
books = {}
librarian .add_book(books, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
librarian.add_book(books, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(books, "1984", "George Orwell", "9780451524935")


librarian.display_books(books)
print()
librarian.check_out_book(books, "9780316769174")
librarian.display_books(books)
print()
librarian.return_book(books, "9780316769174")
librarian.display_books(books)

'''
librarian.remove_book(books,"9780451524935")
librarian.display_books(books)
'''