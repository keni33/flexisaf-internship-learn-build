from dataclasses import dataclass
from collections.abc import Sequence
from typing import TypedDict


class BookData(TypedDict):
    title: str
    author: str
    pages: int


@dataclass
class Book:
    title: str
    author: str
    pages: int

    def description(self) -> str:
        return f"{self.title} by {self.author} ({self.pages} pages)"


def create_book(data: BookData) -> Book:
    return Book(
        title=data["title"],
        author=data["author"],
        pages=data["pages"],
    )


def longest_book(books: Sequence[Book]) -> Book:
    return max(books, key=lambda book: book.pages)


raw_books: list[BookData] = [
    {
        "title": "The First Book",
        "author": "Alice",
        "pages": 250,
    },
    {
        "title": "The Second Book",
        "author": "Bob",
        "pages": 410,
    },
    {
        "title": "The Third Book",
        "author": "Charlie",
        "pages": 320,
    },
]


books: list[Book] = [
    create_book(data)
    for data in raw_books
]

for book in books:
    print(book.description())


largest = longest_book(books)

print("\nLongest book:")
print(largest.description())