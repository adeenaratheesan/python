class A:
    def __init__(self):
        print('parent class A ')
    
    def display1(self):
        print('class A display 1') 

    def __init__(self):
        print('parent class A ')
    
    def display2(self):
        print('class A display 2') 

    def __init__(self):
        print('parent class A ')
    
    def display3(self):
        print('class A display 3') 
    
    def __init__(self):
        print('parent class A ')
    
     

# B inherit A
class B(A):
    def __init__(self):
        super().__init__()
        print ('child class B')   
    
    def display3(self):
        print('class B display 4')



class C(B):
    def __init__(self):
        super().__init__()
        print('child class C')
    
    def display5(self):
        print('class C display 5')
# object of class A
a=A()
# object of class B
b=B().display3()