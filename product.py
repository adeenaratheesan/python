class product:
    count=0
    def __init__(self,name,price,category):
        self.name=name   
        # self is ued to make variable "name" into instance variable so that we can access name from display_product
        self.price=price
        self.category=category
        product.count=product.count+1
    def display_product(self):
        print("name:",self.name)
        print("price:",self.price)
        print("category:",self.category)
    def product_count(self):
        print("total number of product %d" %product.count) 

        