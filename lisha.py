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


