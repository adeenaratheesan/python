a=10
def fun():
    global b
    b=14
    print("inside function")
    print(a)
    print(b)
fun()
print("outside function",a)
print("outside function",b)