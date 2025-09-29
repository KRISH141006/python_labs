class Book :
    def __init__(self,title,author,price) :
        self.title = title
        self.author = author
        self.price = price

    def displayBook(self) :
        print(f"{self.title} By {self.author} - {self.price} rupees")

    def applyDiscount(self,discount) :
        print(f"applying {discount} % discount")
        self.price = self.price - self.price*(discount/100)
        print(f"new price is {self.price}")

book1 =Book("Sapiens: A Brief History of Humankind","Yuval Noah Harari",200)
book2 =Book("Thinking, Fast and Slow","Daniel Kahneman",300)

book1.displayBook()
print()
book2.displayBook()
print()
book1.applyDiscount(20)
print()
book1.displayBook()