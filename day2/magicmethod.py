#magic_method= dunder method __init__ and __str__,__eq__
#they are automatically called by many of python's built-in functions and operators
#they are used to define the behavior of objects in python
class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # magic method to define the string representation of the object
    def __str__(self):
        return f"'{self.title}' by {self.author}, priced at ${self.price:.2f}"

    # magic method to define equality between two objects
    def __eq__(self, other):
      
            return self.title == other.title and self.author == other.author and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __add__(self, other):
        return self.price + other.price
    def __sub__(self, other):
        return self.price - other.price
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key=="title":
            return self.title
        elif key=="author":
            return self.author
        elif key=="price":
            return self.price
        else:
            raise f"'{key}' not found in book object"
book1 = book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
print(book1)  # Output: 'The Great Gatsby' by F. Scott Fitzgerald, priced at $10.99 IF we dont have __str__ method it will return the memory address of the object
book2 = book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
print(book1 == book2)  # Output: True
#__eq__ method is used to compare two objects of the same class
# it is used to define the behavior of the equality operator (==) for objects of the class
book3 = book("To Kill a Mockingbird", "Harper Lee", 12.99)
print(book1 < book3) 
print(book1 > book3)
print(book1 + book3)  # Output: 23.98 
print(book1 - book3)  # Output: -2.00
print("The" in book1)  # Output: True
print("F. Scott" in book1)  # Output: True
print(book1["title"])  # Output: The Great Gatsby
print(book1["author"])  # Output: F. Scott Fitzgerald
print(book1["price"])  # Output: 10.99
