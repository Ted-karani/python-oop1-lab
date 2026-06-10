class Book:
    """
    Represents a book with a title and page count.
    Provides functionality to track reading progress by turning pages.
    """

    def __init__(self, title, page_count):
        """
        Initialize a new Book instance.

        Args:
            title (str): The title of the book.
            page_count (int): The number of pages in the book.
        """
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Get the current page count of the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """
        Set the page count with validation.
        Ensures the page count is an integer.
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")