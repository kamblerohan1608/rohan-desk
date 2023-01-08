

from atexit import register
from doctest import register_optionflag
import os


class loginregistration:
    def __init__(self):
        try:
            os.mkdir('EMPLOYEE DATA')
        except:
            pass
        with open("EMPLOYEE DATA/employee_data.txt",'a') as file:
            pass 
        self.register_flag=False
        self.login_flag=False
    def add_user(self,name,age,contact,location,email,pass1):
        user_data=f'{name},{age},{contact},{location},{email},{pass1},\n'
        with open("EMPLOYEE DATA/employee_data.txt",'a') as file:
            file.write(user_data)
        self.register_flag=True
        return self.register_flag

    def login (self,email,pass3):
        email=email.strip()
        pass3=pass3.strip()
        l_obj=f'{email},{pass3}'
        with open("EMPLOYEE DATA/employee_data.txt",'r') as file:
            data=file.readlines()
            for user in data:
                user=user.split(',')
                if email==user[4] and pass3==user[5]:
                    self.login_flag=True
        return self.login_flag





if __name__=='__main__':  #program will exicuted after the main function
    app=loginregistration()
    while True:
        print('1-REGISTRE')
        print('2-LOGIN')
        print('3-EXIT')
        app_ch=int(input('enter your choice '))

        if app_ch==1:
            print('~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^----WELCOME TO REGISTRATION FORM----~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~')
            name=input('enter your name ')
            age=int(input('enter your age '))
            contact=int(input('enter your mobile number '))
            location=input('enter your location ')
            email=input('enter your email id ')
            pass1=input("enter your password ")
            pass2=input('confirm password ')
            
            if name=='':
                print('please enteryour name')
            elif age=='':
                print('please enter your age ')
            elif contact=='':
                print('enter your name')
            elif location=='':
                print('please enter your location')
            elif email=='':
                print('pleas enter your email id')
            elif pass1=='':
                print('please enter your password')
            elif pass2=='':
                print('please enter your confirm password')
            
            
            
            pass1=pass1.strip()
            pass2=pass2.strip()
            if pass1!=pass2:
                print('**********************----please check your password----**********************\n')
            else:
                name=name.strip()
                location=location.strip()
                email=email.strip()
                obj=app.add_user(name,age,contact,location,email,pass1)
                if obj==True:
                    print('/*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*-----Registred Succesfully----/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/\n')
                else:
                    print('/*/*/*/*/*//*/*/*/*/*/*/*/*/*/----Somthing Went Wrong----*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*\n')


        elif app_ch==2:
            email=input('enter your email id ')
            pass3=input('enter your password ')
            lg_obj=app.login(email,pass3)
            if lg_obj==True:
                print('~*~*~*~*~*~*~*~~*~*~*~*~*~*~*~*~*----login succesfully----~*~*~*~*~*~*~*~~*~*~*~*~*~*~*~*~*\n')
            else:
                print('~*~*~*~*~*~*~*~~*~*~*~*~*~*~*~*~*-----somthing went wrong------~*~*~*~*~*~*~*~~*~*~*~*~*~*~*~*~*\n')

        elif app_ch==3:
            print('^*^*^*^*^*^*^^*^*^*^^*^*^*^^*----^thank you for using applicatin----^*^*^*^^^*^^*^*^*^*^*^*^*^*^*^*^*^\n')
        else:
            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~-----please enter correct choice----~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n')


