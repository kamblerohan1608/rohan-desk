import mysql.connector as db
import pandas as pd
import time
import random

class Connection:
    def __init__(self):
        
        mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123")
        cur = mydb.cursor()
        query = """create database if not exists library"""
        cur.execute(query)
        mydb.close()

        mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
        cur = mydb.cursor()
        query = """create table if not exists library_system (SrNo int not null auto_increment , book_code varchar(50) not null unique , book_name varchar(50) not null , author_name varchar(50) not null , status varchar(25) not null default "Available" , primary key(SrNo))"""
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()

        self.issue_book_flag = False
        self.return_book_flag = False

    def read_data(self):
        mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
        cur = mydb.cursor()
        query = """select * from library_system"""
        cur.execute(query)
        data = cur.fetchall()
        return data
        

    def add_book(self,b_name,a_name):
        b_code = self.b_code_otp()
        b_code = str(b_code)  
        b_code = "SL000"+b_code
        
        mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
        cur = mydb.cursor()
        query = f"""insert into library_system (book_code,book_name,author_name) values ("{b_code}","{b_name}","{a_name}")"""
        cur.execute(query)
        cur.execute("commit;")
        mydb.close()
        print("--------------------------------------------------------------------------------------")
        print(f" {b_name} book added successfully ".center(80))                                    
        print("--------------------------------------------------------------------------------------")

        
    def b_code_otp(self):
        
        b_code = random.randint(1000,9999)  
        return b_code


    def issue_book(self,b_name,s_name):

        date_data =  time.strftime(f"%d/%m/%Y %I:%M:%S %p")

        mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
        cur = mydb.cursor()
        query = """select * from library_system"""
        cur.execute(query)
        data = cur.fetchall()
        # print(data)
        for data1 in data:
            # print(data1)
            if b_name in data1[2]:
                ind = data.index(data1)
                # print(ind)
                if "Available" in data1[4]: 
                    mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
                    cur = mydb.cursor()
                    query = f"""update library_system set status = "Book Issued" where book_name = "{b_name}";"""
                    cur.execute(query)
                    cur.execute("commit;")
                    mydb.close()
                    self.issue_book_flag = True
                    print("˜”*°•.˜”*°• Book Issued Succesfully •°*”˜.•°*”˜")
                    break

                elif "Book Issued" in data1[4]:
                    print("˜”*°•.˜”*°• Book Already Issued By Someone or Library Does Not have the Book You Are Looking for •°*”˜.•°*”˜")
                    self.issue_book_flag = True
                    break
                else:
                    print("--------------------------------------------------------------------------------------")
                    print(f"""      {b_name} Book Issued Successfully to {s_name} on {date_data} 
                                !!! Return After 30 Days !!!""")
                    print("--------------------------------------------------------------------------------------")
                    self.issue_book_flag = True
                    break
        return self.issue_book_flag


        
    def return_book(self,b_name,s_name):
        
        date_data =  time.strftime(f"Date:-%d/%m/%Y  Time:-%I:%M:%S %p")
        mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
        cur = mydb.cursor()
        query = """select * from library_system"""
        cur.execute(query)
        data = cur.fetchall()
        mydb.close()
        for data1 in data:
            # print(data1)
            if b_name in data1[2]:
                ind = data.index(data1)
                # print(ind)
                if "Book Issued" in data1[4]:
                    mydb = db.connect(host = "localhost", user = "root", passwd = "c0d3r123", database = "library")
                    cur = mydb.cursor()
                    query = f"""update library_system set status = "Available" where book_name = "{b_name}";"""
                    cur.execute(query)
                    cur.execute("commit;")
                    mydb.close()
                    self.return_book_flag= True
                    print("˜”*°•.˜”*°• Book Returned Succesfully •°*”˜.•°*”˜")
                    break

                elif "Available" in  data1[4]:
                    self.return_book_flag = True
                    print("˜”*°•.˜”*°• Already Available!! •°*”˜.•°*”˜")
                    break
                
                else:
                    print("--------------------------------------------------------------------------------------")
                    print(f"           *********** Returned {b_name} book Successfully ************")
                    print(f"                  By {s_name} On {date_data}")
                    print("--------------------------------------------------------------------------------------")
                    self.return_book_flag = True
                    break

        return self.return_book_flag

        
        
            
if __name__ == "__main__":

    app = Connection()

    print()
    print()
    print("  ░W░e░l░c░o░m░e░ ░t░o░ ░S░q░u░a░d░ ░L░i░b░r░a░r░y░ ░M░a░n░a░g░e░m░e░n░t░  \n".center(120))
    
    while True:
        
        print("""
        +-------------------------------------+
        |  Display  Book     :      Press  1  |
        +-------------------------------------+
        |  Add BOOK          :      Press  2  |
        +-------------------------------------+
        |  Issue  Book       :      Press  3  |
        +-------------------------------------+
        |  return  Book      :      Press  4  |
        +-------------------------------------+
        |  Exit              :      Press  5  |
        +-------------------------------------+

        """.center(80))



        ch = int(input("Enter Your Choice =>> "))
        

        if ch == 1:
            print("--------------------------------------------------------------------------------------")
            print("                     【Ｓｑｕａｄ　Ｌｉｂｒａｒｙ　ｂｏｏｋｓ】")
            print("--------------------------------------------------------------------------------------")
            print()
            
            data = app.read_data()
            df = pd.DataFrame(data,columns=["SrNo","Book Code","Book Name","Author Name","Status"])
            print(df)
            print("--------------------------------------------------------------------------------------")

        elif ch == 2:

            print("--------------------------------------------------------------------------------------")
            print("                     【Ａｄｄ　Ｂｏｏｋｓ　Ｓｅｃｔｉｏｎ】")
            print("--------------------------------------------------------------------------------------")

            # b_code = input("Enter Book Code : ")
            b_name = input("Enter Book Name : ")
            a_name = input("Enter Author Name : ")
            
            # b_code = b_code.strip()
            b_name = b_name.strip()
            a_name = a_name.strip()

            app.add_book(b_name,a_name)
            # app.b_code_otp()


        elif ch == 3:
            print("--------------------------------------------------------------------------------------")
            print("                     【Ｉｓｓｕｅ　Ｂｏｏｋ　Ｓｅｃｔｉｏｎ】")
            print("--------------------------------------------------------------------------------------")
            print()
            
            b_name = input("Enter Book Name : ")
            s_name = input("Enter your Name : ")

            b_name = b_name.strip()
            s_name = s_name.strip()

            result = app.issue_book(b_name,s_name)
            if result == True:
                pass
            else:
                print("˜”*°•.˜”*°• Invalid •°*”˜.•°*”˜")

        
        elif ch == 4:
            print("--------------------------------------------------------------------------------------")
            print("                     【Ｒｅｔｕｒｎ　Ｂｏｏｋ　Ｓｅｃｔｉｏｎ】")
            print("--------------------------------------------------------------------------------------")
            print()

            b_name = input("Enter Book Name : ")
            s_name = input("Enter your Name : ")

            b_name = b_name.strip()
            s_name = s_name.strip()

            result = app.return_book(b_name,s_name)
            if result == True:
                pass
            else:
                print("˜”*°•.˜”*°• Invalid •°*”˜.•°*”˜")
        
        
        elif ch == 5:
            print()
            print("======================================================================================")
            print("         【Ｔｈａｎｋ　Ｙｏｕ　Ｆｏｒ　Ｕｓｉｎｇ　Ｓｑｕａｄ　Ｌｉｂｒａｒｙ】")
            print("======================================================================================")
            break


        else:
            print()
            print("˜”*°•.˜”*°• enter invalid choice •°*”˜.•°*”˜")
