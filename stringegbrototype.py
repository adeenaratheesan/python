#*************** to print a letter in a string *************
#name="python programming"
#print(name[4])
#***********to replace space in a string*******************
#name="python programming"
#name[6]="r"
#print(name[5])
#it does not works TypeError: 'str' object does not support item assignment because string is immutable.ie,a letter in a string can not be changed
#**********to replace a string with another ***************
#name="python programming"
#name="backend programing"
#print(name)
#*************************to print a list***************************************
#values=["php","python","css"]
#print(values)
#********************to change value in a list*********************
#values=["php","python","css"]
#values[2]="java"
#print(values)
#print(len(values))
#values in a list is muttable.ie values can be changed
#print(values[-1])  
#to print values in last position
#print(values[-2:])
#to print all values after second position
#*****************to add a list to another list************************
values=["php","python","css"]
values=values+["programing",10]
print(values)

#*****************to add a value to last position of list**************
values=["php","python","css"]
values.append("hello")
print(values)
#*****************to append a user defined value to list*********
values=["php","python","css"]
values.append(input("enter a value"))
print(values)