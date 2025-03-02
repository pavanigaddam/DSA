"""
print("Hello, World")

num_1 = 3
num_2 = 5
print("3 + 5 = ", num_1+num_2)


#miles to kms

miles = input("Enter number of miles : ")
miles = int(miles)
kms = miles * 1.60934
print("Entered Miles in Kilometers is ", kms)


num1,oper,num2 = input("Enter the operation to be executed").split()
num1 = int(num1)
num2 = int(num2)

if oper == "+":
    print ("{} + {} = {}".format(num1, num2, num1+num2))
elif oper == "-":
    print ("{} - {} = {}".format(num1,num2,num1-num2))
elif oper == "*":
    print ("{} * {} = {}".format(num1,num2,num1*num2))
elif oper == "/":
    print ("{} / {} = {}".format(num1,num2,num1/num2))
elif oper == "%":
    print ("{} % {} = {}".format(num1,num2,num1%num2))
else:
    print ("Invalid")

age = int(input("Enter age:"))
if (age>=1) and (age<=18):
    print("Important")
elif (age==21) or (age==50):
    print("Important")
elif age>65:
    print("Important")
else:
    print("Not Important")

age = int(input("Enter age:"))
if (age == 5):
    print("Go to Kindergarten")
elif (age<5):
    print("Too Young")
elif (age>17):
    print("Go to College")
elif (age>5) and (age<=17):
    print("Go to Grade", age-5)


for i in range(20):
    if (i%2==1):
        print("i = ", i)


invst = float(input("Enter Investment amount: "))
intrt = float(input("Enter Interest rate: "))*0.01

for i in range(10):
    invst = invst + (invst*intrt)

print ("Earnings after 10 years is: ", invst)


n = 5
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print("-", end="")
    # Print stars with gaps
    for k in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line

"""


'''
#1
n = 5
for i in range(n):
    for j in range(n):
        print("*", end='')
    print()

#2
n = 5
for i in range(n+1):
    for j in range(i):
        print("*", end='')
    print()
    

#2
n = 5
for i in range(0, n, +1):
    print("*" * i)


#3
n = 5
for i in range(n, 0, -1):
    print("*" * i)

#3
n = 5
for i in range(n):
    j = 0
    while j<n-i:
        print("*", end='')
        j=j+1
    print()

#4
n = 5
for i in range(n+1):
    for j in range(i):
        print("",j+1, end='')
    print()

'''

#5
n = 5
for i in range(n+1):
    for j in range(i):
        print("*", end='')
    print()
n = 4
for i in range(n):
    j = 0
    while j<n-i:
        print("*", end='')
        j=j+1
    print()

#6







