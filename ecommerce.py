class Ecommerce:
    def __init__(self,pname,pcategory,pprice,pcolor,pweight):
        self.name=pname 
        self.category=pcategory
        self.price=pprice
        self.color=pcolor
        self.weight=pweight
    def display_details(self):
        print("name:",self.name)
        print("category:",self.category)
        print("price:",self.price)
        print("color:",self.color)
        print("weight:",self.weight)
iphone=Ecommerce("iphone13","phone","75000","black","250")
iphone.display_details()