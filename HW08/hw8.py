# Zhenhao Zhang 11/13/23


from dataclasses import dataclass

@dataclass
class Book:
    title: str # The title of the book.
    author: str # The author of the book.
    publication_year: int # The year the book was published.
    isbn: str # The International Standard Book Number of the book.


    def __init__(self,title,author,publication_year,isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.publication_year

    def get_isbn(self):
        return self.isbn

    # to str: Return a string representation of the book in the format
    # ”Title by Author (Year)”.
    def to_str(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


    # is published recently(current year): Return True if the book was published
    # within the last 10 years based on the current year;
    # otherwise, return False.
    def is_published_recently(self, current_year):
        if current_year - self.publication_year <= 10:
            return True
        else:
            return False


def enter_book_data():
    user_input_title = input("Enter book title: ")
    user_input_author = input("Enter author: ")
    user_input_year = int(input("Publication year: "))
    user_input_isbn = input("ISBN: ")
    return Book(user_input_title, user_input_author, user_input_year, user_input_isbn)


def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-3-16-148410-0")
    print(book1.to_str())
    print(book1.is_published_recently(2023))
    print(book1.get_isbn())
    print(book1.get_year())

    print()

    book2 = Book("The Last Wish", "Andrzej Sapkowski", 1993, "0-575-07192-1")
    print(book2.to_str())
    print(book2.is_published_recently(2023))
    print(book2.get_title())
    print(book2.get_author())

    print()

    book3 = enter_book_data()
    print(book3.to_str())

if __name__ == "__main__":
    main()


















































