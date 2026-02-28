from library import librarian

def main():
    library_data = {}
    librarian.add_book(library_data, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    librarian.add_book(library_data, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    librarian.add_book(library_data, "1984", "George Orwell", "9780451524935")

    librarian.display_books(library_data)
    print()

    librarian.check_out_book(library_data, "9780316769174")

    librarian.display_books(library_data)
    print()

    librarian.return_book(library_data, "9780316769174")

    librarian.display_books(library_data)

if __name__ == "__main__":
    main()