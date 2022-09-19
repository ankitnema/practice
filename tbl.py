#program is for  creating tables from 1-10
for row in range(1,11):
 for col in range(1,11):
  product = row*col
  if product <10:
   print ('',product,'',end=' ')
  else:
   print (product,'',end=' ')
 print ()

