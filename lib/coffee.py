class Coffee:
    """
    Represents a coffee order with a size and price.
    Provides functionality to tip, which increases the price.
    """

    # Valid size options for coffee
    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        """
        Initialize a new Coffee instance.

        Args:
            size (str): The size of the coffee (Small, Medium, or Large).
            price (float): The price of the coffee.
        """
        self.size = size
        self.price = price

    @property
    def size(self):
        """Get the current size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size with validation.
        Ensures the size is one of the valid options: Small, Medium, or Large.
        """
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """
        Add a tip to the coffee order.
        Increases the price by 1 and prints a thank you message.
        """
        print("This coffee is great, here\u2019s a tip!")
        self.price += 1