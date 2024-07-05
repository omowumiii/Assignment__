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
#     def withdraw(self,amount):
#         if self.account_balance< amount:
#             print("insufficient funds")
#             return
#         print(f"withdrawal of {amount} sucessful and your new balance is {self.account_balance}")
#         self.account_balance-=amount
    
#     def withdraw(self, amount):
#         if amount>0:
#             self.account_balance -= amount
#             return f"Withdrawal has been sucessful {self.name}'s account balance is {self.account_balance}"

    # def check_balance(self):
#         return f"your current  account balance is {self.account_balance}"
        


# wallet1 = BankAccount('Ambali Ajarah', '2089230678', 5000)
# wallet2 = BankAccount('Adekunle tobi', '231324423', 2000)

# print(wallet1.deposit(500))
# print(wallet1.withdraw(22000))
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

# class Person:
#    def __init__(self, name, age,address):
#         self.name = name
#         self.age = age
#         self.address=address
#    def person_info(self):
#          return(f"Hi there, this is {self.name}, and my {self.age},with {self.address}")
# class Student(Person):
#     def student_infor(self, course):
#         self.course= course
#         print (f" my name is {self.name}, and my age is  {self.age},  with address {self.address},and my course is {self.course}")
# class Lecturer(Person):
#     def lecturer_infor(self,department):
#         self.department=department
#         print (f"this is mr  {self.name},and his  {self.age} years old ,and his is department of {self.department}")

# Persons=Person("tobi",67,"aj")
# student =Student("Adekunle", 35, "lagos")
# lecturer =Lecturer("Dr. Ambali", 45, "Abuja")

# Persons.person_info()
# student.student_infor("Accounting")
# lecturer.lecturer_infor("computer science")

# question 3
# create a Class name Parent and create two others
# classes children and grandchildren. The children must 
# inherit from their parents, and the grandchildren must inherit from both parents and children.
# to create atleast two instances and methods for each class using python



        
class Parent:
    def __init__(self, family_name, eye_color):
        self.family_name= family_name
        self.eye_color=eye_color
        
    def display(self):
        return f"my name is {self.family_name}, and the color of his eyes is  {self.eye_color}"

class Children(Parent):
    def __init__(self, family_name,eye_color,  height):
        super().__init__(family_name, eye_color)
        self.height=height
    def display(self):
        super().display()
        return f"my family name is {self.family_name} and my eyes color is  {self.eye_color}, and my height is  {self.height} feet"



class GrandChildren(Children):
    def __init__(self, family_name,eye_color,  height, intelligence ):
        super().__init__(family_name, eye_color,height)
        self.intelligence = intelligence
    def display(self):
        super().display()
        return f"my family name is {self.family_name}, and my eyes  color is  {self.eye_color}, my height is {self.height} feet, and my  intelligence is very {self.intelligence}"



parent= Parent("Amabali","brown")
print(parent.display())
children= Children("Ambali","brown", 5.8)
print(children.display())

grandchildren= GrandChildren("Ambali","Brown",5.8,"High")
print(grandchildren.display())
   
