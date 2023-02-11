#This script to open a file and read
x = open("file1", "a+")
#x.write(input("enter the number to add in file :  ", "\n"))
x.write("\n")
x.write(input("enter the a number:=   "))
x.close()

#Mandatory to use "r" to display added numbers in the file
x = open("file1", "r")
#print (x.readlines()[-1])
#x.close()
print ("added last line in the file: = ", x.readlines()[-1])
x.close()
print()
print ("Transaction Completed")
