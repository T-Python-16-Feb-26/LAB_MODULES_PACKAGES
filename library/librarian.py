def add_book(library, title, author, isbn):
    if isbn in library:
        return False, "Book already exists."

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }
    return True, "Book added successfully."


def remove_book(library, isbn):
    if isbn not in library:
        return False, "Book not found."

    library.pop(isbn)
    return True, "Book removed successfully."


def check_out_book(library, isbn):
    if isbn not in library:
        return False, "Book not found."

    if not library[isbn]["available"]:
        return False, "Book is already checked out."

    library[isbn]["available"] = False
    return True, "Book checked out successfully."


def return_book(library, isbn):
    if isbn not in library:
        return False, "Book not found."

    library[isbn]["available"] = True
    return True, "Book returned successfully."


def display_books(library):
    if not library:
        return False, []

    books_output = []

    for book in library.values():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        books_output.append(
            f'{book["title"]} by {book["author"]} (ISBN: {book["isbn"]}) - {status}'
        )

    return True, books_output