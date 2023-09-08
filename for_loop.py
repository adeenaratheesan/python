# for i in range(6):
#     for j in range(i):
#         print("*",end="  ")
#     print('\n')


# o/p

# *

# *  *

# *  *  *

# *  *  *  *

# *  *  *  *  *


# for i in range(5):
#     for j in range(i,5):
#         print("*",end="  ")
#     print('\n')

# o/p

# *  *  *  *  *  

# *  *  *  *

# *  *  *

# *  *

# *

# find length of array



#************************ swap 2 values in front and back of the  array**************************

#marks=[11,52,78,1,178]
#limit=len(marks)
#temp=0
#temp=marks[0]
#marks[0] = marks[limit-1]
#marks[limit-1]=temp
#print(marks)
#************************************
#*****to append 52 the array marks/************
#marks.append(52)
#print(marks)
#marks.clear()

# marks1=marks.copy()
# print(marks1)

# a=marks.count(5)
# print(a)

# b=[1,2]
# marks.extend(b)
# print(marks)

# marks.insert(0,7878787)
# print(marks)

# # index =marks.index[787878]
# # print(index)

# marks.pop(0)
# print(marks)

# marks.remove(52)
# print(marks)
# marks.reverse()
# print(marks)

# marks.sort()
# print(marks)






# ****************************replacing text baabtra with world and printing in to array******************************
# txt="welcome to baabtra"
# x=txt.replace("baabtra","world")
# print(x)

# y=txt.split()
# print(y)
#*******************print data in a list using for loop********************************************************
#file=['jocker.mp4','memories.mp4','honey mist.mp4']
#for x in file:
    #print(x)
    #*******to print name of the movie without .mp4 use code  print(x[0:-4])**
    #print(x[0:-4])
#**********************to print number with in a range******************************************************
#for x in range(5,10):
 #   print(x)
    #*****************************************************************************************************
#************************************************to print numbers with same difference**************************
#for x in range(10,50,2):
   # print(x)

    #here number starts from 10 and ends in 50 with difference 2 ie multiplication table of 2
    #*************************************************************************************************************************
#************************************to print number in reverse order************************
for i in range(30,10,-1):
    print(i)