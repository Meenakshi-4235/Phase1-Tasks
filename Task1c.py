class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._royalty = 0

    # Getter and Setter for title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    # Getter and Setter for author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    # Getter and Setter for publisher
    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    # Getter and Setter for price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    # Method to calculate royalty
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._royalty = 0.10 * self._price * copies_sold
        elif copies_sold <= 1500:
            self._royalty = (0.10 * self._price * 500) + (0.125 * self._price * (copies_sold - 500))
        else:
            self._royalty = (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (copies_sold - 1500))
        return self._royalty


class EBook(Book):
    def __init__(self, title, author, publisher, price, format):
        super().__init__(title, author, publisher, price)
        self._format = format

    # Getter and Setter for format
    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, format):
        self._format = format

    # Override royalty method to account for GST
    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        gst = 0.12 * base_royalty
        return base_royalty - gst


# Example usage
book = Book("Sample Book", "John Doe", "XYZ Publishers", 100)
ebook = EBook("Sample EBook", "Jane Doe", "ABC Publishers", 100, "EPUB")

# Calculate royalty for a book
print(f"Book Royalty for 2000 copies: {book.royalty(2000)}")

# Calculate royalty for an ebook
print(f"EBook Royalty for 2000 copies: {ebook.royalty(2000)}")
