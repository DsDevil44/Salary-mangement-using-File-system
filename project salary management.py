print("________________________________________________________________________________________________________________________________________")
print("   ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("##################################################......WELCOME TO RADIANT  SALARY MANAGEMENT SYSTEM......################################################")
print("_________________________________________________________________________________________________________________________________________")
print("    ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("******************************************************************************************************************************************************************************************************")

print("please login or sign.up")

print('press 1 for login')

print('press 2 for sign.up')

option=int(input("enter 1,2:"))

if option==1:

     print("write a user name to continue")

     username=input("enter your username :")

else:

     f=open("Emp.txt","a")

     nname=input("enter name of new employee:")

     #entered name will be saved in a new file

     npost=input("enter post of new employee:")

     #entered name will be saved in a new file

     nsalary=int(input("enter salary of new employee:"))

     #entered name will be saved in a new file

     ncompany=input("enter company name of new employee :")

     #entered name will be saved in a new file

     f.write(nname),f.write(npost),f.write (ncompany)

     f.close()
     

print("enter 1 for enter in salary mangement system")            

print("enter 2 for exit")

n=int(input("enter 1or 2:"))

def Salary():

     print("enter option 1,2,3,4,5 ")

     print('press option 1 for  show all data in the file')

     print('press option 2 for adding new employee details')

     print('press option 3 for increase the salary')

     print('press option 4 for check about the salary details')

     print('press option 5 for delete all data')

     option=int(input("enter 1,2,3,4,5:"))

     if  option==1:

         f=open("employee.txt","r")

         r=f.read()

         print(r)

         f.close()

         

     elif option==2:

         f=open("employee.txt","a")

         enumber=int(input("enter employee number :"))  

         name=input("after a space enter name of new employee:")

         #after a space write the values for mantaining the table

         post=input("after 3 times space enter post of new employee:")

         #after 3 times  space write the values for mantaining the table

         salary=int(input("after 11 times space enter salary of new employee:"))

         #after 11 times  space write the values for mantaining the table


         company=input(" after 3 times enter company name of new employee:")

         #after  3 times space write the values for mantaining the table

         f.write('%d' % enumber),f.write( name),f.write(   post),f.write(           '%d'%salary),f.write(   company)
         f.close()

     elif option==3:

          a=int(input("enter the value of salary that you have to replace:"))

          replace("employee.txt",'%'%a)

     elif option ==4:

         import  csv

         fields = []

         rows = []

         f=open("salaryaugust.csv","r")

         ###user should write the name of csv file where the salary details is stored of  given month

         csvReader=csv.reader(f)

         for row in csvReader:

                    rows.append(row)

         for i in rows:

              for  j  in  i :

                     print(j,end=",")

              print('\n')

         h=open("salaryaugust","r",newlines='\r\n')

         sreader=csv.reader(h)

         for i in sreader:

              print(i)


     
     
     else:

         import os

         print("CAUTION! THIS WILL DELETE ALL YOUR STORED DATA")

         print("CAUTION! THIS WILL DELETE ALL YOUR STORED DATA")

         print("CAUTION! THIS WILL DELETE ALL YOUR STORED DATA")

         if os.path.exists("employee.txt"):

             os.remove("employee.txt")

         else:

             print("file doesnot exist !!")

               #your file name does not exits

if n==1:

    password=int(input("enter your password:"))

    if password==12342:

       Salary()

       print("type yes of repeat the program")

       print("type no for exit the program")

       a=input("type yes or no  :  ")

       while a=='yes' :

            Salary()

       else :

         print("_________________________________________________________THANKING YOU________________________________________________________")

         print("________________________________________________________PLEASE VISIT AGAIN____________________________________________________")
         
         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

         print("#################################################################################################")

         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

         print("*****************************************************************************THANKING YOU*************************************************************") 
            
    else:

        print("your password is incorrect")

else:

    print("_________________________________________________________THANKING YOU________________________________________________________")

    print("________________________________________________________PLEASE VISIT AGAIN____________________________________________________")

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    print("#################################################################################################")

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    print("*****************************************************************************THANKING YOU*************************************************************") 
