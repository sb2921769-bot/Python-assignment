'''Q.1 Write a Python program to check if a number is positive
num=?
if num>0:
    print('the number is positive')
Q.2 Print "Eligible to vote" if age is 18 or above.
age=?
if age>=18:
    print('eligible to vote')
Q.3 Check if a number is divisible by 7.
num=?
if num%7==0:
    print('devisal by seven ')
Q.4 Print "Pass" if marks are greater than 40
marks=?
if marks>40:
    print('pass')
Q.5 Check if a number is greater than 100
if num>100:
    print('greater than 100')
Q.6 Display a message if temperature exceeds 45°C.
tem=?
if tem>45:
    print('Temperature exceeds 45')
Q.7 Check if a string length is more than 8 characters.
str=len('Jethalal champak lal gada')
if str>8:
    print('more than 8')
Q.8 Print "Logged In" if password matches "admin123"
ps=("admin123")
if ps is ('admin123'):
    print('logged in')
Q.9 Check if a number is a multiple of 10.
num=?
if num%10==0:
    print('multiple of 10')
Q.10 Print a warning if balance is below minimum limit.
balance=?
if balance<1000:
    print('balance is below minimum limit')
Q.11  Check whether a number is even or odd.
num=21
if num%2==0:
    print('even')
else:
    print('odd')
Q.12 Find the largest of two numbers
a=?
b=?
if a>b:
    print('A is largest number')
else:
    print('B is largest number')

Q.13 Check whether a person is eligible for driving license
age=?
if age>=18:
    print('eligible for driving')
else:
    print('not eligible')
Q.14 Print "Pass" or "Fail" based on marks.
mks=?
if mks>40:
    print('PASS')
else:
    print('fail')
Q.15  Check whether a number is positive or negative.
num=?
if num>0:
    print('positive')
else:
    if num==0:
        print('zero')
    else:
        print('negative')
Q.16 Check whether a character is a vowel or consonant.
ch=input('enter A character : ')
if ch=='a':
    print('vowel')
else:
    if ch=='e':
        print('vowel')
    else:
        if ch=='i':
            print('vowel')
        else:
            if ch=='o':
                print('vowel')
            else:
                if ch=='u':
                    print('vowel')
                else:
                    print('consonant')
Q.17 Check if a year is leap or not.
>>> Hold
Q.18  Print "Valid Password" or "Invalid Password".
ps=("Shubham@123")
if ps is ("Shubham@123"):
    print('valid password')
else:
    print('invalid password')
Q.19 Determine whether salary is taxable or not.
salary=
if salary<500000:
    print('not taxable')
else:
    print('taxable')
Q.20 Check whether a number is greater than 50 or not.
num=?
if num>50:
    print('greater than 50')
else:
    print('not greater than 50')
Q.21 Find the largest of three numbers
a=20
b=30
c=50
if a>b:
    if a>c:
        print('greater is a',a)
    else:
        print('greater is c',c)
else:
    if b>c:
        print('greater is b',b)
    else:
        print('greater is c',c)
Q.22 Check whether a number is positive, negative, or zero.
num=?
if num>0:
    print('positive')
else:
    if num==0:
        print('zero')
    else:
        print('negative')
Q.23 Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60
mrks=62
if mrks>=90:
    print("grade A")
else:
    if mrks>=75:
        print('grade B')
    else:
        if mrks>=60:
            print('grade C')
        else:
            if mrks<60:
                print('fail')
Q.24 Check whether a triangle is equilateral, isosceles, or scalene.
>>> Hold

Q.25  Check whether a character is uppercase, lowercase, digit, or special character.
ch = input("Enter a character: ")

if len(ch) == 1:
    if ch >= 'A' and ch <= 'Z':
        print("Uppercase letter")
    else:
        if ch >= 'a' and ch <= 'z':
            print("Lowercase letter")
        else:
            if ch >= '0' and ch <= '9':
                print("Digit")
            else:
                print("Special character")
else:
    print("Please enter only one character")
Q.26 Calculate electricity bill using slab-wise rates. 
units = int(input("Enter electricity units consumed: "))
bill = 0

if units <= 100:
    bill = units * 1.5

else:
    if units <= 200:
        bill = (100 * 1.5) + (units - 100) * 2.5
    
    else:
        if units <= 300:
            bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
        
        else:
            bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (units - 300) * 6

print("Total Electricity Bill = ₹", bill)
Q.27 Validate login using username and password.
correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful ")
    else:
        print("Wrong Password ")
else:
    print("Wrong Username ")
Q.28 Check student result using marks of 3 subjects. 
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
avg = total / 3

if m1 >= 33 and m2 >= 33 and m3 >= 33:
    if avg >= 75:
        print("Pass - Distinction ")
    else:
        if avg >= 60:
            print("Pass - First Division")
        else:
            if avg >= 50:
                print("Pass - Second Division")
            else:
                if avg >= 33:
                    print("Pass - Third Division")
else:
    print("Fail ")

print("Total =", total)
print("Average =", avg)
Q.29 Find the second largest number among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a < c:
        second = a
    else:
        if b > c:
            second = b
        else:
            second = c
else:
    if b < c:
        second = b
    else:
        if a > c:
            second = a
        else:
            second = c

print("Second largest number is:", second)
Q.30 Check loan eligibility using age, salary, and credit score. 
age = int(input("Enter your age: "))
salary = int(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))

if age >= 21:
    if salary >= 20000:
        if credit_score >= 650:
            print("Loan Approved ")
        else:
            print("Loan Rejected (Low Credit Score)")
    else:
        print("Loan Rejected (Low Salary)")
else:
    print("Loan Rejected (Age not eligible)")
Q.31 Print day name using day number (1–7)
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input")
Q.32 Print month name using month number
month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid input")
Q.33 Display grade based on percentage
per = float(input("Enter percentage: "))

if per >= 90:
    print("Grade A+")
elif per >= 75:
    print("Grade A")
elif per >= 60:
    print("Grade B")
elif per >= 50:
    print("Grade C")
elif per >= 33:
    print("Grade D")
else:
    print("Fail")
Q.34 Display bonus percentage based on experience
exp = int(input("Enter years of experience: "))

if exp >= 10:
    print("Bonus = 20%")
elif exp >= 5:
    print("Bonus = 10%")
elif exp >= 2:
    print("Bonus = 5%")
else:
    print("No Bonus")
Q.35 Identify traffic signal meaning
color = input("Enter traffic signal color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready / Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
Q.36 Categorize temperature
temp = float(input("Enter temperature: "))

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")
Q.37 Categorize employee based on salary
salary = int(input("Enter salary: "))

if salary >= 50000:
    print("High Salary")
elif salary >= 25000:
    print("Medium Salary")
else:
    print("Low Salary")
Q.38 Print discount based on purchase amount
amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    print("Discount = 20%")
elif amount >= 3000:
    print("Discount = 15%")
elif amount >= 1000:
    print("Discount = 10%")
else:
    print("No Discount")
Q.39 Identify number type
num = int(input("Enter a number: "))

if -9 <= num <= 9:
    print("Single-digit")
elif -99 <= num <= 99:
    print("Double-digit")
else:
    print("Multi-digit")
Q.40 Assign performance rating
score = int(input("Enter performance score: "))

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Average")
else:
    print("Poor")
Q.41 Number divisible by 5 and 11
num = int(input("Enter number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")
Q.42 Loan eligibility
age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
credit = int(input("Enter credit score: "))

if age >= 21 and salary >= 25000 and credit >= 700:
    print("Loan Approved ")
else:
    print("Loan Rejected ")
Q.43 Validate login (username AND password)
user = input("Enter username: ")
pwd = input("Enter password: ")

if user == "admin" and pwd == "1234":
    print("Login Successful ")
else:
    print("Invalid Login ")
Q.44 Student pass condition
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))

avg = (m1 + m2 + m3) / 3

if m1 >= 40 and m2 >= 40 and m3 >= 40 and avg >= 50:
    print("Pass ")
else:
    print("Fail ")
Q.45 Number between 10 and 100
num = int(input("Enter number: "))

if num > 10 and num < 100:
    print("Number is between 10 and 100")
else:
    print("Not in range")
Q.46 Exam eligibility (OR condition)
attendance = int(input("Enter attendance %: "))
medical = input("Medical certificate (yes/no): ")

if attendance >= 75 or medical == "yes":
    print("Eligible for exam ")
else:
    print("Not eligible ")
Q.47 Validate a date
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if (1 <= month <= 12) and (1 <= day <= 31):
    print("Valid Date ")
else:
    print("Invalid Date ")
Q.48 Email format validation
email = input("Enter email: ")

if "@" in email and "." in email and not email.startswith("@"):
    print("Valid Email ")
else:
    print("Invalid Email ")
Q.49 Insurance eligibility
age = int(input("Enter age: "))
health = input("Health status (good/bad): ")
income = int(input("Enter income: "))

if age >= 18 and age <= 60 and health == "good" and income >= 20000:
    print("Eligible for insurance ")
else:
    print("Not eligible ")
Q.50 Leap year (complete logic)
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year ")
else:
    print("Not a Leap Year ")
Q.51 Income tax using slabs
income = int(input("Enter your income: "))
tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.2
else:
    tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3

print("Total Tax =", tax)
Q.52 ATM withdrawal with balance check
balance = 10000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        balance -= amount
        print("Withdraw Successful ")
        print("Remaining Balance =", balance)
    else:
        print("Enter amount in multiples of 100 ")
else:
    print("Insufficient Balance ")
Q.53 Promotion eligibility
exp = int(input("Enter experience (years): "))
performance = input("Enter performance (good/average): ")

if exp >= 5 and performance == "good":
    print("Eligible for Promotion ")
else:
    print("Not Eligible ")
Q.54 Grading system (nested if-else)
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 75:
        print("Distinction")
    else:
        if marks >= 60:
            print("First Division")
        else:
            print("Pass")
else:
    print("Fail")
Q.55 Strong password validation
pwd = input("Enter password: ")

if len(pwd) >= 8 and any(c.isupper() for c in pwd) and any(c.islower() for c in pwd) and any(c.isdigit() for c in pwd):
    print("Strong Password ")
else:
    print("Weak Password ")
Q.56 Delivery charges
amount = int(input("Enter order amount: "))
location = input("Enter location (local/outstation): ")

if location == "local":
    if amount >= 500:
        print("Free Delivery")
    else:
        print("Delivery Charge = 50")
else:
    if amount >= 1000:
        print("Free Delivery")
    else:
        print("Delivery Charge = 100")
Q.57 Online exam qualification
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance %: "))

if marks >= 50 and attendance >= 75:
    print("Qualified for Online Exam ")
else:
    print("Not Qualified ")
Q.58 Movie ticket pricing
age = int(input("Enter age: "))
time = input("Show time (morning/evening): ")

if age < 18:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150

if time == "morning":
    price -= 50

print("Ticket Price =", price)
Q.59 Bank account type based on balance
balance = int(input("Enter balance: "))

if balance >= 100000:
    print("Premium Account")
elif balance >= 50000:
    print("Gold Account")
elif balance >= 10000:
    print("Savings Account")
else:
    print("Basic Account")
Q.60 Menu-driven program
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero ")
else:
    print("Invalid choice")

