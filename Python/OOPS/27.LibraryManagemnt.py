class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self):
        return f'Title: "{self.title}", Author: {self.author}, Price: ${self.price}'


class FictionBook(Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre

    def get_book_info(self):
        return f'{super().get_book_info()}, Genre: {self.genre}'


class NonFictionBook(Book):
    def __init__(self, title, author, price, topic):
        super().__init__(title, author, price)
        self.topic = topic

    def get_book_info(self):
        return f'{super().get_book_info()}, Topic: {self.topic}'


fiction_book = FictionBook("To Kill a Mockingbird", "Harper Lee", 14.99, "Drama")
non_fiction_book = NonFictionBook("A Brief History of Time", "Stephen Hawking", 19.99, "Cosmology")

# Display book information
print("Book Info:", fiction_book.get_book_info())
print("Book Info:", non_fiction_book.get_book_info())
