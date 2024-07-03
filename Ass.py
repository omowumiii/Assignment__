1 
# Create a Class called BankAccount 
# def the  _init_ attributes
# Then create three class methods that would 
# *deposit 
# *Withdraw
# *CheckBalance
# Deposit and withdraw would make changes to the account balance, but CheckBalance would
# just give you the current balance at the time for checking


# class BankAccount:
#     def __init__(self, name,account_number,account_balance):
#         self.name=name
#         self.account_number=account_number
#         self.account_balance=account_balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.account_balance += amount
#             return f"Deposit has enter {self.name}'s account balance is {self.account_balance}"
    
#     def withdraw(self, amount):
#         if amount>0:
#             self.account_balance -= amount
#             return f"Withdrawal has been sucessful {self.name}'s account balance is {self.account_balance}"

#     def check_balance(self):
#         return f"your current  account balance is {self.account_balance}"
        


# wallet1 = BankAccount('Ambali Ajarah', '2089230678', 5000)
# wallet2 = BankAccount('Adekunle tobi', '231324423', 2000)

# print(wallet1.deposit(500))
# print(wallet1.withdraw(200))
# print(wallet1.check_balance())
# print(wallet2.deposit(500))
# print(wallet2.withdraw(200))
# print(wallet2.check_balance())

# Question two 
# Create a Class named Person 
# And Create two other classes that would inherit from it 
# Which are
# Student
# Lecturer

class Person:
   def __init__(self, name, age,address):
        self.name = name
        self.age = age
        self.address=address
   def person_info(self):
         return(f"Hi there, this is {self.name}, and my {self.age},with {self.address}")
class Student(Person):
    def student_infor(self, course):
        self.course= course
        print (f" my name is {self.name}, and my age is  {self.age},  with address {self.address},and my course is {self.course}")
class Lecturer(Person):
    def lecturer_infor(self,departmrnt):
        self.department=departmrnt
def lecturer_info(self):
       print (f"this is mr  {self.name},and his  {self.age} years old ,and his ID is department of {self.department}")

Persons=Person("tosin",34,"Ilorin")
student =Student("Adekunle", 35, "lagos")
lecturer =Lecturer("Dr. Ambali", 45, "Abuja")

Persons=Person()
student.student_infor("Accounting")
lecturer.lecturer_infor("computer science")




        

   
