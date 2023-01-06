import mysql.connector
def user_choice():
    while True:
        choice=input("Enter Book Name : ")
        if choice:
            break
        else:
            print("You Didn't Entered")
    return choice
def check_quntity(name):
    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="Library")
    cursor=conn.cursor()
    query="select quntity from book where name=%s"
    values=(name,)
    cursor.execute(query,values)
    my_data=cursor.fetchall()
    conn.commit()
    conn.close()
    return my_data[0][0]>=1  
def show_book(Type):
    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="Library")
    cursor=conn.cursor()
    query="select name from book where type=%s"
    values=(Type,)
    cursor.execute(query,values)
    my_data=cursor.fetchall()
    conn.commit()
    conn.close()
    return my_data
def select_ask(Type,Id):
    print("-------------------Choose From Below Option----------------------+")
    print("--------------------------(A): RETRY-----------------------------|")
    print("--------------------------(B): REDIRECT TO LEND BOOK-------------|")
    print("--------------------------PRESS ANY KEY TO RETURN TO MENU--------+")
    choice=input("Enter From Above Choice : ")
    if choice.capitalize()=="A":
        select(Type,Id)
    elif choice.lower()=="b":
        Lend()
    else:
        Ask()           
def update(book,Id,Task):
    conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='Library')
    cursor=conn.cursor()
    query="UPDATE user SET book=%s where id=%s"
    if Task==1:
        query_2="UPDATE book SET quntity=quntity-1 where name=%s"
    else:
        query_2="UPDATE book SET quntity=quntity+1 where name=%s"
    values=(book,Id)
    val=(book,)
    cursor.execute(query,values)
    cursor.execute(query_2,val)
    conn.commit()
    conn.close()
def your_id():
    conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='Library')
    cursor=conn.cursor()
    query="select id from user where id=(select max(id) from user)"
    cursor.execute(query)
    my_data=cursor.fetchall()
    conn.commit()
    conn.close()
    return my_data[0][0]
def select(Type,Id):
    book=show_book(Type)
    print("-------------------Choose From Below Option----------------------+")
    print("--------------------------(A): Choose Book-----------------------|")
    print("--------------------------(B): Find Book-------------------------+")
    choice=input("Enter From Above Choice : ")
    if choice=="A" or choice=="a":
        for i in book:
            print(i[0])
        userchoice=user_choice()
        for i in book:
                if userchoice.capitalize()==i[0].capitalize():
                    if check_quntity(userchoice):
                        update(userchoice,Id,-1)
                        print("Sucssesfully Lended")
                        break
                    else:
                        print("Sorry This Book Isn't Available At The Moment")
                        select_ask(Type,Id)
        else:
            print("Sorry Book Not Found")
            select_ask(Type,Id)
    elif choice=="B" or choice=="b":
        userchoice=user_choice()
        for i in book:
                if userchoice.capitalize()==i[0].capitalize():
                    if check_quntity(userchoice):
                        update(userchoice,Id,-1)
                        print("Sucssesfully Lended")
                        break
                    else:
                        print("Sorry This Book Isn't Available At The Moment")
                        select_ask(Type,Id)
        else:
            print("Sorry Book Not Found")
            select_ask(Type,Id)
    else:
        print("Invalid Choice Enter Again")
        select(Type,Id)                   
def checker(Pass):
     conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='Library')
     cursor=conn.cursor()
     query="select id from user"
     cursor.execute(query)
     my_data=cursor.fetchall()
     conn.commit()
     conn.close()
     for Id in my_data:
          if Pass in Id:
              return True  
def endscreen():
     print("--------------------------------------------------------------------------------+")
     print("---------------------**Enter any given options**--------------------------------|")
     print("--------------------------------(A): Main Menu----------------------------------|")
     print("--------------------------------(B): Exit---------------------------------------|")
     print("--------------------------------------------------------------------------------+")
     choice=input("Enter Any Of Above Option : ")
     if choice.capitalize()=="A":
          print("Please Wait......")
          Ask()
     elif choice.capitalize()=="B":
          print("#","THANKS FOR USIN LIBRARY MANAGMENT SYSTEM".center(80,"_"),"#")
     else:
          print("Invalid Choice Enter Again")
          endscreen()
def Do_u():
    print("--------------------------------(A): REDIRECT TO LEND BOOK-----------------------|")
    print("--------------------------------(B): REDIRECT TO MAIN PAGE-----------------------|")
    choice=input("Enter From Above Choice : ")
    if choice.capitalize()=="A":
        Lend()
    elif choice.capitalize()=="B":
        Ask()
    else:
        print("Invalid Choice Enter Again")
        Do_u()
def Eligiblity(Id):
    conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='Library')
    cursor=conn.cursor()
    query="select Book from user where id=%s"
    values=(Id,)
    cursor.execute(query,values)
    my_data=cursor.fetchall()
    conn.commit()
    conn.close()
    if my_data:
        return my_data[0][0]
    else:
        return False
    
def Submit():
    ask=ID()
    if Eligiblity(ask):
        print(Eligiblity(ask))
        update(None,ask,1)
        print("Succesfully Submitted")
    else:
        print("Sorry But U Have Not Lended Any Book")
def ID():
    while True:
        try:
            user_pass=int(input("Enter Your Pass Id : "))
        except:
            print("Error You Have Entered Wrong DataType\nTry Again!")
        else:
            break
    return user_pass
def Lend():
    user_pass=ID()
    if checker(user_pass):
        print("--------------------------------------------------------------------------------+")
        print("---------------------**Select The Type OF Book U Want**-------------------------|")
        print("--------------------------(A): Fairy Tail---------------------------------------|")
        print("--------------------------(B): AutoBiography------------------------------------|")
        print("--------------------------(C): Refreshers---------------------------------------|")
        print("--------------------------(D): Encylophedia And Genius Book of Word Record------|")
        print("--------------------------------------------------------------------------------+")
        userchoice=input("Enter From Above Choice : ")
        if userchoice.capitalize()=="A":
            if Eligiblity(user_pass)==None:
                select("Fairy Tail",user_pass)
            else:
                print("You Have Already Lended A Book First Return That")
                Do_u()
        elif userchoice.capitalize()=="B":
            if Eligiblity(user_pass)==None:
                select("AutoBiography",user_pass)
            else:
                print("You Have Already Lended A Book First Return That")
                Do_u()
        elif userchoice.capitalize()=="C":
            if Eligiblity(user_pass)==None:
                    select("Refresher",user_pass)
            else:
                print("You Have Already Lended A Book First Return That")
                Do_u()
        elif userchoice.capitalize()=="D":
            if Eligiblity(user_pass)==None:
                select("Encylophedia And Genius Book of Word Record",user_pass)
            else:
                print("You Have Already Lended A Book First Return That")
                Do_u()
        else:
            print("Invalid Choice Enter Again")
            Lend()
    else:
        print("This Id Dosen't Exist")
        Do_u()
def create(NAME,CLASS,TYPE):
    conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='Library')
    cursor=conn.cursor()
    query="INSERT INTO user(name,class,type) VALUES(%s,%s,%s)"
    values=(NAME,CLASS,TYPE)
    cursor.execute(query,values)
    conn.commit()
    conn.close()
def Ask():
    print("---------------------------------------------------------------------------------+")
    print("----------------------------WELCOME TO LIBRARY-----------------------------------|")
    print("--------------------------------(A): SUBMIT BOOK---------------------------------|")
    print("--------------------------------(B): LEND BOOK-----------------------------------|")
    print("--------------------------------(C): CREATE ID-----------------------------------|")
    print("---------------------------------------------------------------------------------+")
    choice=input("Enter From Above Choice : ")
    if choice.capitalize()=="A":
        Submit()
    elif choice.capitalize()=="B":
        Lend()
    elif choice.capitalize()=="C":
        information()
    else:
        print("Invalid Choice Enter Again")
        Ask()
    endscreen()
def NAME():
   while True:
        Name=input("Enter Your Name : ")
        if Name:
            break
        else:
            print("You Didn't Entered\nTry Again")
   return Name
def CLASS():
    while True:
        try:
            Class=int(input("Enter Your Class : "))
        except:
            print("You Have Entered Wrong DataType!\nTry Again!")
        else:
            break
    return Class
def Type():
    while True:
        print("---------------------------------------------------------------------------------+")
        print("----------------------------SELECT YOUR TYPE-------------------------------------|")
        print("--------------------------------(A): STUDENT-------------------------------------|")
        print("--------------------------------(B): TEACHER-------------------------------------|")
        print("---------------------------------------------------------------------------------+")
        TypE=input("Select Your Type : ")
        if TypE.lower()=="a" or TypE.lower()=="b":
            if TypE.lower()=="a":
                TypE="Student"
            elif TypE.lower()=="b":
                TypE="Teacher"
            break
        else:
            print("Invalid Choice\nTry Again!")
    return TypE
def information():
    Name=NAME()
    Class=CLASS()
    TYPE=Type()
    create(Name,Class,TYPE)
    print("Your ID Has Been Sucssfully Created".center(81,"="))
    print("Your ID is : ",end="")
    print(your_id())
    print("="*81)
Ask()
