#day 1
print("hello users")
#day2
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=a+b
print("The sum of two numbers is:",c)
#day 3 - pro 1
rad=float(input("Enter the radius of circle="))
Area=3.14*r**2
print("Area of circle =",Area)
# day 3 - pro 2
num1=float(input("Enter the first number for addtion:"))
num2=float(input("Enter the second number for addtion:"))
sum_result=num1+num2
print(f"Sum:{num1}+{num2}={sum_result})
#day 4 - pro 3
num3=float(input("Enter the first number for division:"))
num4=float(input("Enter the second number for division:"))
if num4==0:
print("Error: Division error ")
else:
div_result=num3/num4
print("The quotient of the division =",div_result)
#day 5-pro 1
L=[1,2,3,4,5,6,7,8,9,10]
for n in range(1,11):
    for i in L:
        print(n,"x",i,"=",n*i) 
#day 5 - pro 2 
base=float(input("Enter the value of base:"))
height=float(input("Enter the value of height:"))
area=0.5*base*height
print("The area of the triangle=",area)
#day 5- pro 3
n=int(input("Enter the value of n:"))
n=str(n)
nn=(n+n)
nnn=(n+n+n)
Sum=int(n)+int(nn)+int(nnn)
print(Sum)
#day 5 - pro 4
n=int(input("Enter the value of n:"))
n=str(n)
nn=(n+n)
nnn=(n+n+n)
Sum=(n)+(nn)+(nnn)
print(Sum)
#day 5 - pro 5
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
Sum=a+b
Product=a*b
if(Product<=1000):
    print("The given product of numbers is lesser than 1000 and the product is",product)
else:
    print("The given product of numbers is greater than 1000 and the sum is",Sum)

#day 6 - pro 1
L=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for i in L:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("The number of even numbers are",even)
print("The number of odd numbers are",odd)
#day 6-pro 2
input_str=input("Enter the value of a string in hyphen seperated way")
input_lis=input_str.split('-')
input_lis.sort()
input_join='-'.join(input_lis)
print(input_join)
#day 7 - pro 1
w=input("Enter the sentence =")
lc=0
uc=0
sp=0
for i in w:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
    elif i.isspace():
        sp+=1
    else:
        pass
toggle_case=w.swapcase()
print(lc)
print(uc)
print(sp)
print(toggle_case)
#day 7 - pro 2
s={"Name":"Lisha","Age":18,"Gender":"Female"}
print(s)
s.update({"Age":19})
print(s)
s.update({"Status":"Single"})
print(s)
#day 7 - pro 3
s={12,14,85,6,4,8,2,54,5,5}
print("Original set:",s)
item=int(input("Enter the value to be removed:"))
if item in s:
    s.remove(item)
    print(s)
else:
    print("NOT FOUND")
#day 7 - pro 4
t=(1,2,5,4,5,6,9,8,5,6,3,2,1,7,9,5,1,2)
print(t)
repeated_items=[]
for item in t:
    if t.count(item)>1 and item not in repeated_items:
        repeated_items.append(item)
if repeated_items:
    print(repeated_items)
else:
    print("NO REPEATED ITEMS")
#day 8-pro 1    
file_name='untitled.txt'
count=0
with open (file_name,"r") as file:
    for l in file:
        count+=1
print(count) 
#day 8 - pro 2
fp=open('lis.txt','w')
L=["They were happy\n"]
fp.writelines(L)
fp.close()
fp=open('lis.txt','r')
print(fp.readlines())
fp.close()
fp=open('lis.txt','a')
P=["not good\n"]
fp.writelines(P)
fp.close()
fp=open('lis.txt','r')
print(fp.readlines())
fp.close()
#day 8 - pro 3
import string 
for letter in string.ascii_uppercase:
    with open (letter+".txt","w") as f:
        f.writelines("love lisha")
#day 8 - pro 4
def DivExp(a,b):
    assert a>0,"Assertion failed: 'a' must be greater than zero"
    if b==0:
        raise ZeroDivisionError("Division by zero is not allowed")
    c=a/b
    return c 
try:
    a=int(input("Enter the value a "))
    b=int(input("Enter the value of b"))
    result= DivExp(a,b)
    print(result)
except AssertionError as e :
    print("Error:",e)
except ZeroDivisionError as e :
    print("Error:",e)   
except ValueError as e :
    print("Error:Please enter the valid integer")
# day 9 - pro 1 
import random

number = random.randint(1, 100)
attempts = 5

for i in range(attempts):
    guess = int(input("Enter your guess (1-100): "))

    if guess == number:
        print("Correct! You won 🎉")
        break
    elif guess > number:
        print("Too high!")
    else:

        print("Too low!")

    print("Attempts left:", attempts - i - 1)

if guess != number:
    print("You lost! The number was:", number)
# day 9 - pro 2
num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# day 9 - pro 3
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print(add(a, b))
elif op == '-':
    print(sub(a, b))
elif op == '*':
    print(mul(a, b))
elif op == '/':
    print(div(a, b))
else:
    print("Invalid operator")
# day 9 - pro 4
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
 # day 9 - pro 5
 marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Average marks:", sum(marks)/len(marks))
#day 10 - pro 1
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
 #day 10 - pro 2
 s = input("Enter a string: ").lower()
vowels = "aeiou"
v = c = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
 #day 10 - pro 3
 nums = list(map(int, input("Enter numbers: ").split()))
print("Largest:", max(nums))
#day 10 - pro 4
n = int(input("Enter n: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#day 10 - pro 5
pwd = input("Enter password: ")

if len(pwd) >= 8 and any(c.isdigit() for c in pwd):
    print("Strong Password")
else:
    print("Weak Password")
#day 11 - pro 1
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
#day 11 - pro 2
nums = list(map(int, input("Enter numbers: ").split()))

nums = list(set(nums))  # remove duplicates
nums.sort()

print("Second largest:", nums[-2])
#day 11 - pro 3
nums = list(map(int, input("Enter numbers: ").split()))
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print("Without duplicates:", unique)
#day 11 - pro 4
string = input("Enter string: ")
freq = {}

for ch in string:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
#day 11 - pro 5
num = int(input("Enter number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect number")
else:
    print("Not perfect")
#day 12- pro 1
nums = list(map(int, input("Enter numbers: ").split()))

unique_nums = list(set(nums))
unique_nums.sort()

print("Second largest:", unique_nums[-2])
#day 12- pro 2
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
#day 12- pro 3
nums = list(map(int, input("Enter numbers: ").split()))
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
#day 12- pro 4
nums = list(map(int, input("Enter numbers: ").split()))
n = len(nums) + 1

total = n * (n + 1) // 2
print("Missing number:", total - sum(nums))

#day 13- pro 1
str1 = input("Enter string: ")

if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#day 13- pro 2
f = float(input("Enter temperature in Fahrenheit: "))
c = (5/9) * (f - 32)
print("Celsius:", c)
#day 13- pro 3
lst = list(map(int, input("Enter list: ").split()))
count = lst.count(2)
print("2 appears", count, "times")
#day 13- pro 4
str1 = input("Enter string: ")
char = input("Enter character to remove: ")

result = str1.replace(char, "")
print(result)
#day 14 - pro 1
amount = float(input("Enter original amount: "))
gst_rate = float(input("Enter GST rate (%): "))

gst = (amount * gst_rate) / 100
total = amount + gst

print("GST Amount:", gst)
print("Total Amount:", total)
#day 14 - pro 2 
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
#day 15 - pro 1
def long_words(words, k):
    result = [word for word in words if len(word) > k]
    return result

words = input("Enter words: ").split()
k = int(input("Enter length k: "))
print(long_words(words, k))
#day 15- pro 2
s = input("Enter string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates:", result)
#day 15 - pro 3
n = 5

# Upper part
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower part
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
#day 15 - pro 4
n = 9

for i in range(3):
    for j in range(n):
        if ((i + j) % 4 == 0) or (i == 1 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
 #day 15 - pro 5
 arr = [10, 45, 23, 67, 67, 89, 34]

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)
#day 16 - pro 1
def first_unique_char(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char

    return None

print(first_unique_char("aabbccdeff"))  
#day 16 - pro 2
def substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            result.append(s[i:j])
    return result

print(substrings("abc"))
#day 16 - pro 3
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

print(is_rotation("abcd", "cdab"))  # True
#day 16 - pro 4
def missing_number(arr, n):
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

print(missing_number([1, 2, 4, 5], 5))  # Output: 3
#day 16- pro 5
def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

print(flatten([1, [2, [3, 4], 5], 6]))
#day 17 - pro 1
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
        else:
            print("Insufficient Balance!")

    def show_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")
        print("Transactions:")
        for t in self.transactions:
            print("-", t)


# Object creation
acc1 = BankAccount("Lish", 1000)

acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(1500)

acc1.show_details()
#day 17 - pro 2
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"{title} issued successfully!")
                return
        print(f"{title} not available!")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"{title} returned!")
                return


# Objects
lib = Library()

b1 = Book("Python Basics")
b2 = Book("Data Structures")

lib.add_book(b1)
lib.add_book(b2)

lib.issue_book("Python Basics")
lib.issue_book("Python Basics")  # tricky case
lib.return_book("Python Basics")
lib.issue_book("Python Basics")
#day 18- pro 1
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass  # to be overridden


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


# Polymorphism in action
employees = [
    FullTimeEmployee("Lish", 50000),
    PartTimeEmployee("Alex", 5, 500)
]

for emp in employees:
    print(f"{emp.name}'s Salary:", emp.calculate_salary())
