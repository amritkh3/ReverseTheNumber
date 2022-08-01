"""ask user to input he four digit no and print the reverse
1.ask user to input the four digit number and assign it to the variable userno with integer value.
2.declare a variable reverseno and assign it with value 0.
3. run while loop util the value of userno is greater than 0
4. under while loop override the value of userno and reverse no
    ie . reverseno=reverseno*10+userno%10
         userno=userno//10
5.print value of reverseno after loop is done.         
"""
userno=int(input("enter any four digit no "))
reverseno=0
while userno>0:
    reverseno=reverseno*10+userno%10
    userno=userno//10

print("the reverse of this no is",reverseno)   



"""let see how it works 
suppose user input the number 1234
userno=1234
reverseno=0
under while loop 
 reverseno=0*10+1234%10=0+4=4
 user no=1234//10=123

 now again 
 userno is 123 which greater than 0
 reverseno=4*10+123%10=40+3=43
 userno=123//10=12
 again userno is 12 which is greater than 0
 reverseno=43*10+12%10=430+2=432
 userno=12//10=1
  again userno is greater than 0
  so reverseno=432*10+1%10=4230+1=4321
  userno=1//10=0
  now the user no is not greater than o so the loop will stop.

  and the fine reverse value is 4321



"""