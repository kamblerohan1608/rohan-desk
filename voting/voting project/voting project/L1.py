import mysql.connector as db
import re

class Vote:
    def __init__(self):
        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123")
        
        cur = mydb.cursor()
        query1 = '''create database if not exists voter_db;'''
        cur.execute(query1)
        cur.execute("commit;")
        mydb.close()

        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123", database = "voter_db")
        cur = mydb.cursor()
        query2 = '''show tables;'''
        cur.execute(query2)
        data = cur.fetchall()
        print(data)
        data_new = []
        for i in range(len(data)):
            data_new.append(data[i][0])
        print(data_new)

        if "voter_records" in data_new:
            pass
        else:
            query3 = '''create table voter_records(email varchar(100),password varchar(100));'''
            cur.execute(query3)
            cur.execute("commit;")
        mydb.close()

    def add_voter(self,email,password):
        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123", database = "voter_db")
        cur = mydb.cursor()
        query1 = f'''insert into voter_records(email,password) values("{email}","{password}");'''
        cur.execute(query1)
        cur.execute("commit;")
        mydb.close()
    
    def check_voters(self):
        mydb = db.connect(host = "localhost",user = "root",password = "c0d3r123", database = "voter_db")
        cur = mydb.cursor()
        query = '''select email from voter_records;'''
        cur.execute(query)
        voters_id = cur.fetchall()
        # print('voters data table already created',voters_id)
        cur.execute("commit;")

        query5 = '''select password from voter_records;'''
        cur.execute(query5)
        password_data = cur.fetchall() 
        # print('password data table already created',password_data)
        cur.execute("commit;")
        return [voters_id,password_data]



if __name__ == "__main__":
    app = Vote()
    print("\n\n************ WELCOME TO VOTING SYSTEM **************\n")
    menu1 = "Press 1 : Add Voters Data.\nPress 2 : Go To Voting Panel.\nPress 3: Exit\n"
    print(menu1)
    s=0
    while True:
        if s==1:
            break
        else:
            ch = int(input("Enter Your Choice: "))
            if ch == 1:
                voter = input("Enter Your Email ID :")
                voter = voter.strip()
                valid_voter = re.match(r'\b[a-zA-Z0-9.*_*-*]+@[a-zA-Z]+\.[a-zA-Z]{2,}\b',voter)
                if valid_voter:
                    password = input("Enter your password : ")
                    app.add_voter(voter,password)
                    print("\n********** Information Added Succesfully... ************\n")
                    print(menu1)
                else:
                    print("\n*************** Invalid Email Address ****************\n")
                    print(menu1)

            elif ch ==2:
                print("\n************ WELCOME TO VOTING SYSTEM **************\n")
                print("!!!!!!! Give The Names Of Candidates For Voting !!!!!!!!!!\n")
                print()


                candidates1 = input("Enter 1st candidate Name :")
                candidates2 = input("Enter 2nd candidate Name :")
                candidates3 = input("Enter 3rd candidate Name :")

                cand1_votes = 0
                cand2_votes = 0
                cand3_votes = 0


                records = app.check_voters()
                # print('records ',records)
                voters_id1 = records[0]
                # print('voters_id1', voters_id1)
                password_record1 = records[1]
                # print('password_record1',password_record1)
                if voters_id1:
                    # print(voters_id1)
                    voters_id = []
                    for i in range(len(voters_id1)):
                        voters_id.append(voters_id1[i][0])
                    # print(voters_id)
                    password_record = [] 
                    for i in range(len(password_record1)):
                        password_record.append(password_record1[i][0])
                    # print(password_record)
                    no_voter_id = len(voters_id)
                    print()
                    print(f"###### Numbers of voters {no_voter_id} ########")
                    print()
                    voted = []
                    while True:
                        if voters_id == []:
                            print("*************!! Voting is Over !!************\n")
                            if cand1_votes>cand2_votes and  cand1_votes>cand3_votes:
                                print(f"************* {candidates1} Won the Election With {cand1_votes} Votes *************")
                                print()

                            elif cand2_votes>cand3_votes and cand2_votes>cand1_votes:
                                print(f"************* {candidates2} Won The Election With {cand2_votes} Votes *************")
                                print()

                            elif cand3_votes>cand1_votes and cand3_votes>cand2_votes :
                                print(f"************* {candidates3} Won The Election With {cand3_votes} Votes *************")
                                print()

                            elif cand1_votes == cand2_votes :
                                print(f"********* Voting Tied Between {candidates1} and {candidates2} *******!!!!!")
                                print()

                            elif cand2_votes == cand3_votes :
                                print(f"********* Voting Tied Between {candidates2} and {candidates3} *******!!!!!")
                                print()

                            elif cand3_votes == cand1_votes :
                                print(f"********* Voting Tied Between {candidates3} and {candidates1} *******!!!!!")
                                print()
                            s=1
                            break
                        
                        else:
                            voter = input("Enter Your Email ID :")
                            password = input("Enter your password : ")
                            # print(voters_id)
                            # print(password_record)
                            if voter in voters_id and voters_id.index(voter) == password_record.index(password):
                                print(f"\nVote Your candidate : \n1.{candidates1}\n2.{candidates2}\n3.{candidates3}\n")
                                choice = int(input("Enter Your Choice :"))
                                if choice == 1:
                                    cand1_votes+=1
                                    print(f"\nYou Voted To {candidates1}\n")
                                elif choice == 2:
                                    cand2_votes+=1
                                    print(f"\nYou Voted To {candidates2}\n")
                                elif choice == 3:
                                    cand3_votes+=1
                                    print(f"\nYou Voted To {candidates3}\n")
                                voters_id.remove(voter)
                                password_record.remove(password)
                                voted.append(voter)
                  
                            elif voter in voted:
                                print("\n!!!You Already Voted !!!!\n")
                            else:
                                print("\n************ Invalid Email Id Or Password ***************\n")
                else:
                    print("\n*********************** There are no registed voters -- Add Voters First !!! ***********************\n")
                    print(menu1)



            elif ch == 3:
                print("\n*************** Thank you for using the application ***************\n")
                break

            else:
                print("\n*************** Invalid Input Inter Proper Input ***************\n")
                print(menu1)

                        
