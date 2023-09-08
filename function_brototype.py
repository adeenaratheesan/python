#***********************pgm to pass values as argument in function *******************
#def hey(name,age):
#    print("My name is "+name+"age is "+str(age))
#values="python"
#hey(values,1)



#***********************to pass multiple arguments in function***********************************
#def hello(*values):
 #   print("first value:"+values[0]+" second value: "+values[1]+" third value: "+values[2])
#hello("python","java","css")
#here *values can pass multiple arguments



#******************global and local variable*************************
#here value =10 is global variable
value=10
def fun(arg):
    #value=30 is local variable .and can only be accessed inside function fun 
    value=30
    print("local variable",value)

def hello(value):
    #here access global variable value =10.because this function doesnot have local function
    print(value)

def add():
    s=value+1
    print("added value",s)
fun(value)

hello(value)
add()
print("global variable",value)