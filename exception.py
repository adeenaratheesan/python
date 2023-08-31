# writing to a file
# try:
#     f=open('sample.txt','r')
   
#     a= f.write("writing")

# except IOError:
#     print("cant write")




try:
    f=open('sample.txt','a')
    # a=f.read()
    a= f.write("writing")
    print(a)
except FileNotFoundError:
    print("file not found")
except IOError:
    print("cant write")