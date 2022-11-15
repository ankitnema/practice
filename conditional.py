#import statement
import os
import pathlib


#Check file is exits in the folder
#import pathlib
file = pathlib.Path("outfile1")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")
    print ()
    print ("creatinng file ********* ")
    x= open("outfile1", "w+")
    print ()
    print ("****file is created******")
    x.close()

#check file is empty
if os.stat("outfile1").st_size == 0:
  print ("file is empty ")
  print ("Owner id of the file:", os.stat(file).st_uid)
  print ("Group id of the file:", os.stat(file).st_gid)
else:
  print ("Owner id of the file:", os.stat(file).st_uid)
  print ("Group id of the file:", os.stat(file).st_gid)
  print ("continue with the process")
  x = open("outfile1", "r+")
  print ("added last line in the file: = ", x.readlines()[-1])


#This script to open a file and read
x = open("outfile1", "a+")
#x.write(input("enter the number to add in file :  ", "\n"))
#print ("added last line in the file: = ", x.readlines()[-1])

#x.write("\n")
#x.write(input("enter the a number:=   "))
input_num =input ('enter the new number : ')
x.write(input_num + '\n')
#x.write('\n')


#Mandatory to use "r" to display added numbers in the file
#x = open("outfile1", "r")
#print (x.readlines()[-1])
x.close()
#read the file as LIST to display last line [-1]
with open("outfile1", "r") as y:
 last_line = y.readlines()[-1]
 print ("last line added in the file : " , last_line)
 x.close()
#count the digit of the number added in the file


print ()
print ("Transaction Completed")

