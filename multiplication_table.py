#*************pgm to print multiplication table of a number using for loop*************************

a=int(input("enter a number"))

x=1
for y in range (x,11):
    print(y,"*",a,"=",y*a)

#*************pgm to print multiplication table of a number using while loop*************************
a=int(input("enter a number"))

x=1
while(x<=10):
    print(x,"*",a,"=",x*a)
    x=x+1
