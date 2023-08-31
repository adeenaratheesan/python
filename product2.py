class Product:
    def __init__(self,name,category,price):
        self.sname=name
        self.scategory=category
        self.__sprice=price
        

    def display_product(self):
        print("name",self.sname)
        print("category",self.scategory)
        # print("price",self.price)

    def set_sprice(self,price):
        self.__sprice=price
    
    def get_sprice(self):
        return self.__sprice
    
product1=Product("mobile","electronics",75000)
# product1.display_product()
# print(product1.sname)
# print(product1.__sprice)  here sprice cannot be accessed because its private 

# namemangling method
# print(product1._Product__sprice)  
# here sprice is private methode & cannot be accessed .it is  accessed only using namemangling method as below
# product1.__sprice=1000

# print(product1.__sprice)
# print(product1._Product__sprice)


# **************************************get/set method
product1.set_sprice(2)
print(product1.get_sprice())
print(product1._Product__sprice)