
import mysql.connector
mydb=mysql.connector.connect (host="localhost",user="root", passwd="admin")
mycursor=mydb.cursor(buffered=True)
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")

mydb.commit()
class Bank:
    

    def new_account():
        
        print("All information prompted are mandatory to be filled")
        acno=str(input("Enter account number:"))
        name=input("Enter name:")
        city=str(input("Enter city name:"))
        mn=str(input("Enter mobile no.:"))
        balance=0
        mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
        mydb.commit()
        print("Account is successfully created!!!")
    def updation_adding():
        
        acno=str(input("Enter account number:"))
        mycursor.execute("select acno from bank_master where acno={}".format(acno))
        mycursor.fetchall()
        if(mycursor.rowcount==0):
            print("wrong account number")
    
    
        


        else:
            dp=int(input("Enter amount to be deposited:"))
       
        
       
            mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno={}".format(acno))
            mydb.commit()
            print("money has been deposited successully!!!")
    def updation_withdrawl():
       
        
        acn=str(input("Enter account number:"))
        mycursor.execute("select acno from bank_master where acno={}".format(acn))
        mycursor.fetchall()
        if(mycursor.rowcount==0):
            print("wrong account number")
    
        else:
            wd=int(input("Enter amount to be withdrawn:"))
        
            ttype="w"
      
            mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno={}".format(acn))
            print("Money withdrawn successfully")
            mydb.commit()
    def display():
        
        acn=str(input("Enter account number:"))
        mycursor.execute("select acno from bank_master where acno={}".format(acn))
        mycursor.fetchall()
        if(mycursor.rowcount==0):
            print("wrong account number")
        else:
            mycursor.execute("select * from bank_master where acno={}".format(acn))
            for i in mycursor:
                print(i)
        
        
    


print("1=Create account")
print("2=Deposit ")
print("3=Withdraw ")
print("4=account summary")
print("5=Exit")
ch=int(input("Enter your choice:"))
    

if(ch==1):
    Bank.new_account()
           

elif(ch==2):
    Bank.updation_adding()
           


elif(ch==3):
    Bank.updation_withdrawl()


elif(ch==4):
    Bank.display()
else:
    print("THank You")
          
        
