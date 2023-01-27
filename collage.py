# Sum of two numbers
a,b = 10,20
c = a + b
print("sum = ", c)

a = int (input("Enter the value : ")) 
b = int (input("Enter the value : ")) 
c = a + b
print("sum = ", c)

# Print name
ch = "Ankush Paul \n"
print(ch*5)


# Swapping of 2 variables
a = int (input("Enter the value of a : ")) 
b = int (input("Enter the value of b : ")) 
c = a
a = b
b = c
print("value of a : ", a)
print("value of b : ", b)


# Average of 3 numbers
a = int (input("Enter the value1 : ")) 
b = int (input("Enter the value2 : ")) 
c = int (input("Enter the value3 : ")) 
avg = (a + b + c)/3
print("average : ", avg)


# Celsius to Farhenite
c = int (input("Enter the value in C : ")) 
f = (c * 9 / 5) +32
print(f)


# Area of a triangle
import math
a = int (input("Enter the value : ")) 
b = int (input("Enter the value : ")) 
c = int (input("Enter the value : ")) 

s = (a + b + c)/2
area = math.sqrt(s*(s-a)*(s - b)*(s-c))
print(area)


# unicode code of a specified character
import math
print(ord('A'))


# Upper case to lower case and vise-versa
ch = 'ankush'
print(ch.upper())
chh = 'ANKUSH'
print(chh.lower())



# Odd or Even
a = int (input("Enter a number : "))
if(a % 2 == 0) :
    print("{0} is even". format(a))
else:
    print("{0} is odd". format(a))


# Leap year or not
year = int(input("Enter a year : "))
if(year % 400 == 0):
    print("{0} is a leap year!".format(year))
elif(year % 4 == 0 and year % 100 != 0):
    print(year,"is a leap year!") 
else:
    print("{0} isn't a leap year!".format(year)) 


# Searching
char = str(input("Enter a word : "))
if('h' in char):
    print("true")
else:
    print("false")


# Largest number
num1 = int (input("Enter 1st number : "))
num2 = int (input("Enter 2nd number : "))
num3 = int (input("Enter 3rd number : "))
if(num1 >= num2 and num1 >= num3):
    print(num1, "is the largest number.")
elif(num2 >= num1 and num2 >= num3):
    print(num2, "is the largest number.")
elif(num3 >= num1 and num3 >= num2):
    print(num3, "is the largest number.")
else:
    print("Each number is equal!!")


# Average of a student's marks
char = str(input("Enter student's name : "))
a = int(input("Enter the 1st subject mark: "))
b = int(input("Enter the 2nd subject mark: "))
c = int(input("Enter the 3rd subject mark: "))
d = int(input("Enter the 4th subject mark: "))
e = int(input("Enter the 5th subject mark: "))

avg = (a + b + c + d + e) / 5

if(avg >= 90 and avg <= 100):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is O")
elif(avg >= 80 and avg <= 89):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is E")
elif(avg >= 70 and avg <= 79):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is A")
elif(avg >= 60 and avg <= 69):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is B")
elif(avg >= 50 and avg <= 59):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is C")
elif(avg >= 40 and avg <= 49):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is D")
elif(avg < 40):
    print("Student's name is : " , char , "......" , "Avg marks: ", avg, "......." , "Grade is Fail")
else:
    print("Invalid details!")


# String
n = int(input("Enter a number : "))
s = str(n)
l = len(s)
print("Number of digit in n :", l)


# Employee
name = str(input("Enter Employee code : "))
salary = int(input("Enter total salary : "))
year = int(input("Enter year of service: "))
if(year > 5):  
    netpay = salary * (1+(5/100))**(year-5)
    bonas = netpay - salary
else:
    bonas = 0
    netpay = salary
print("Employee code: ", name,"  Bonas amount: ", bonas, "  Net salary amount: ", netpay)



# Loop
for i in range(10,0,-1):    # FOR LOOP
    print(i, end = ' ')   


n = 3
while (n >= 6):   #WHILE LOOP
    print(n)
    n += 1
else:
    print("Out of loop")



# Sun of n natural number
n = int(input("Enter limit: "))
for i in range(1,n+1,1):
    print(i)

n = int(input("Enter limit: "))
sum = 0
for i in range(1,n+1,1):
    sum += i
print(sum)




# Factorial of a number
n = int(input("Enter limit: "))
fact = 1
for i in range(1,n+1,1):
    fact *= i
print(fact)



# Sum of odd numbers and even numbers
n = int(input("Enter limit: "))
sumOdd = 0
sumEven = 0
for i in range(1,n+1,2):
    sumOdd += i
print("sum of odd numbers : ", sumOdd)

for i in range(2,n+1,2):
    sumEven += i
print("sum of even numbers : ", sumEven)




# Fibonacci Series
nterms = int(input("number of terms: "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Invalid input: ")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1





# Prime Number
num = int(input("Enter number: "))
flag = False
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")





# Armstrong number
n = int(input("Enter number: "))
sum = 0
m = n
while (n > 0):
    r = n % 10
    n = n // 10
    sum += r * r * r
if(sum == m) :
    print(m, "is a Armstrong number")
else:
    print(m, "isn't a Armstrong number")





# Krishnamurthy number
n = int(input("Enter your number: "))
sum = 0
m = n

while n > 0:
    r = n % 10
    fact = 1
    for i in range(1, r+1):
        fact *= i
    sum += fact
    n //= 10
if m == sum:
    print("Krishnamurthy number")
else:
    print("It is not a Krishnamurthy number")





# pattern
n = int(input("Enter number: "))
for i in range(1, n+1):
    print('* '* i)


row = 5
for i in range(row): 
    for j in range(i):
        print(" ", end="")
    for j in range(row - i):
        print("*", end=" ")
    print()





# List
n = int(input("Enter the number of elements: "))
list = []
for i in range(1, n+1):
    sq = i*i
    list.append(sq)
print(list)





# Max and min element of a list
n = int(input("Enter the number of elements you want to insert: "));
list = []
for i in range(0, n):
    num = int(input("Enter the element: "))
    list.append(num)
max = list[0]
min = list[0]

for i in range(1, n):
    if(list[i] > max):
        max = list[i]
    if(list[i] < min):
        min = list[i]
print(min)
print(max)







# Remove duplicates
n = int(input("Enter the number of elements you want to insert: "));
list = []
for i in range(0, n):
    num = int(input("Enter the element: "))
    list.append(num)
newList = []
newList.append(list[0])
for i in range(1, len(list)):
    if list[i] not in newList:
        newList.append(list[i])
print(newList)





# Searching element
n = int(input("Enter the number of elements you want to insert: "));
list = []
for i in range(0, n):
    num = int(input("Enter the element: "))
    list.append(num)
element = int(input("Enter the number you want to search: "));
flag = 0
for i in range(0, n):
    if element in list:
        id = list.index(element)
        flag = 1
        break
if(flag == 1):
    print("The element present in index", id)
else:
    print("The element is not present")





# Bubble sort
n = int(input("Enter the number of elements you want to insert: "));
list = []
for i in range(0, n):
    num = int(input("Enter the element: "))
    list.append(num)
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if(list[j] > list[j+1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print(list)







# Stack using list
list = []
while(1):
    print("1. Push\n2. Pop\n3. Display\n4. Exit\n")
    n = int(input("Enter the option: "));
    
    if(n == 1):
        num = int(input("Enter the number for push: "));
        list.append(num)
        print(num, "Inserted");
    elif(n == 2):
        print(list.pop(), "Deleted");
    elif(n == 3):
        print(list)
    else:
        exit




# Slice and Reverse
n = int(input("Enter the number of elements you want to insert: "));
list = []
for i in range(0, n):
    num = int(input("Enter the element: "))
    list.append(num)
for i in range(0, len(list), 3) :
    x = i
    print(list[x : x+3])
    list.reverse()






#2. Add two matrices
n1 = int(input("Enter the number of nested lists: "))
list1 = []
for i in range (0, n1):
    list2 = []
    for j in range (0, 3):
        m = int(input("Enter the number: "))
        list2.append(m)
    list1.append(list2)

n2 = int(input("Enter the number of nested lists: "))
list3 = []
for i in range (0, n2):
    list4 = []
    for j in range (0, 3):
        m = int(input("Enter the number: "))
        list4.append(m)
    list3.append(list4)
print(list1)
print(list3)
list5 = []
for i in range(0, 3):
    list6 = []
    for j in range(0, 3):
        sum = list1[i][j] + list3[i][j]
        list6.append(sum) 
    list5.append(list6)
print(list5)






#1. Sort a nested list according to the 2nd element of the nested list
#   for eg: [[2,5,7], [1,6,8], [4,3,2], [4,9,1]]
#   o/p:    [[4,3,2], [2,5,7], [1,6,8], [4,9,1]]

n = int(input("Enter the number of nested lists: "))
list = []
for i in range (0, n):
    list1 = []
    for j in range (0, 3):
        m = int(input("Enter the number: "))
        list1.append(m)
    list.append(list1)
list_sort = []
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if(list[j][1] > list[(j+1)][1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print(list)





#3. Print the sum of diagonal elements of a matrix
n1 = int(input("Enter the number of nested lists: "))
list1 = []
for i in range (0, n1):
    list2 = []
    for j in range (0, 3):
        m = int(input("Enter the number: "))
        list2.append(m)
    list1.append(list2)
print(list1)
sum = 0
for i in range(0, len(list1)):
    for j in range(0, len(list1[i])):
        if((i == j) or (i + j == 2)):
            sum = sum + list1[i][j]
print(sum)






# Merge 2 list sort the first
n1 = int(input("Enter the number of elements you want to insert: "))
list1 = []
for i in range(0, n1):
    num1 = int(input("Enter the element: "))
    list1.append(num1)


n2 = int(input("Enter the number of elements you want to insert: "))
list2 = []
for i in range(0, n2):
    num2 = int(input("Enter the element: "))
    list2.append(num2)

for i in range(n2):
    list1.append(list2[i])

for i in range(n1-1):
    for j in range(0, n1-i-1):
        if(list1[j] > list1[j+1]):
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
print(list1)


# Insert Element in Tuple
N1 = int(input("Enter the number of inputs in a tuple"))

list = []
for i in range(0,N1):
    num = int(input("Enter the number in a tuple"))
    list.append(num)
t1 = tuple(list)
print(t1)

num_1 = int(input("Enter the number in a tuple"))
pos_1 = int(input("Enter the position of the number in a tuple"))

list.insert(pos_1-1,num_1)
t2 = tuple(list)
print(t2)


# Repeated Element in Tuple
n1 = int(input("Enter the number of elements in a tuple: "))
list = []
for i in range(0, n1):
    num = int(input("Enter the element: "))
    list.append(num)
    
for i in range (n1):
    for j in range(i+1, n1):
        if list[i] == list[j]:
            print(list[i])
            break
 


# Sort element in a nested tuple according to it's second element
n = int(input("Enter the number of nested lists: "))
list = []
for i in range (0, n):
    list1 = []
    for j in range (0, 3):
        m = int(input("Enter the number: "))
        list1.append(m)
    list.append(list1)
list_sort = []
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if(list[j][1] > list[(j+1)][1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print(list)
print(tuple(list))



# Delete Duplicate elements from a tuple
n1 = int(input("Enter the number of elements in a tuple: "))
list = []
for i in range(0, n1):
    num = int(input("Enter the element: "))
    list.append(num)

res = []
for i in list:
    if i not in res:
        res.append(i)
print(tuple(res))




# Dictionary
employee = dict()
employees = int(input("Enter the number of employees: "))

for i in range(employees):
    accountNumber = input("Enter the account number: ")
    balance = input("Enter the balance: ")
    employee[accountNumber] = balance

print("1. Check balance for an existing account holder\n2. WithDraw amount\n3. Deposit amount\n4. Insert new Account holder\n")
option = int(input("Enter the option: "))

if(option == 1):
    accountNumber = input("Enter the account number: ")
    if accountNumber in employee.keys():
        print("Total balance : "+ employee[accountNumber])
    else:
        print("Account number invalid!")
elif(option == 2):
    accountNumber = input("Enter the account number: ")
    withdrawAmount = input("Enter the amount: ")
    presentAmount = employee[accountNumber]
    if(int(presentAmount) >= int(withdrawAmount)):
        print(withdrawAmount + " is withdraw")
        employee[accountNumber] = str(int(presentAmount) - int(withdrawAmount))
    else:
        print("You haven't enough balance!")
    print("Remaining balance : "+ employee[accountNumber])
elif(option == 3):
    accountNumber = input("Enter the account number: ")
    depositAmount = input("Enter the amount: ")
    presentAmount = employee[accountNumber]
    totalAmount = int(depositAmount) + int(presentAmount)
    employee[accountNumber] = str(totalAmount)
    print("New balance : "+ employee[accountNumber])
elif(option == 4):
    accountNumber = input("Enter the account number: ")
    balance = input("Enter the balance: ")
    employee.update({accountNumber:balance})
    print(employee)

