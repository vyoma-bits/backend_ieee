
import mysql.connector
class BANKING:
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
        cursor.execute("select ac from em1 where acno=acno")
        if (len(cursor.fetchall)=0):
            print("account not found")
            break
        


        
        dp=int(input("Enter amount to be deposited:"))
        dot=str(input("Enter date of Transaction: YYYY-MM-DD "))
        ttype="d"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("money has been deposited successully!!!")
    def updation_withdrawl():
       
        
        acno=str(input("Enter account number:"))
        cursor.execute("select ac from em1 where acno=acno")
        if (len(cursor.fetchall)=0):
            print("account not found")
            break
        wd=int(input("Enter amount to be withdrawn:"))
        dot=str(input("enter date of transaction: YYYY-MM-DD "))
        ttype="w"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
        mydb.commit()
    def display():
        
        acno=str(input("Enter account number:"))
        cursor.execute("select ac from em1 where acno=acno")
        if (len(cursor.fetchall)=0):
            print("account not found")
            break
        mycursor.execute("select * from bank_master where acno='"+acno+"'")
        for i in mycursor:
            print(i)
        
        
    
    mydb=mysql.connector.connect (host="localhost",user="root", passwd="admin")
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists bank")
    mycursor.execute("use bank")
    mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
    mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
    mydb.commit()
    while(True):
    
        print("1=Create account")
        print("2=Deposit ")
        print("3=Withdraw ")
        print("4=account summary")
        print("5=Exit")
        ch=int(input("Enter your choice:"))
    

        if(ch==1):
           new_account()
           

        elif(ch==2):
            updation_adding()
           


        elif(ch==3):
            updation_withdrawl()


        elif(ch==4):
            display()
        else:
            print("THank You")
            break
        
