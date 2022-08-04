#This script to open a file and read
x = open("file1", "a")
#x.write(input("enter the number to add in file :  ", "\n"))
x.write("\n")
x.write(input("enter the a number:=   "))
x.close()

#display added numbers in the file
x = open("file1", "r")
#print (x.readlines()[-1])
print ("added last line in the file: = ", x.readlines()[-1])
