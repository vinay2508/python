#Q.No.1

n=int(input("enter year: "))
def leap_year(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return "given year is a leap year"
    else:
        return "given year is not a leap year"
print(leap_year(n))

#Q.No.2

length=int(input("enter length: "))
breadth=int(input("enter breadth: "))
def dimensions(l,b):
    if l==b:
        return ("given dimensions are of square")
    else:
        return ("given dimensions are of rectangle")
print(dimensions(length, breadth))
      
#Q.No.3

a=int(input("enter age of first person: "))
b=int(input("enter age of second person: "))
c=int(input("enter age of third person: "))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
elif a==b and a>c:
    print("a and b are greater")
elif b==c and b>a:
    print("b and c are greater")
elif c==a and c>b:
    print("a and c are greater")

if a<b and a<c:
    print ("a is smaller")
elif b<c and b<a:
    print ("b is smaller")
elif c<a and c<b:
    print ("c is smaller")
elif a==b and a<c:
    print("a and b are smaller")
elif b==c and b<a:
    print("b and c are smaller")
elif c==a and c<b:
    print("a and c are smaller")
elif a==b and b==c:
    print ("all are equal")


#Q.No.4

age=int(input("enter age: "))
sex=input("enter sex(M or F): ")
marital_status=input("enter marital status(Y or N): ")
def job_area(a,s,m):
    if sex.upper()=="F":
        return("work only in urban areas")
    elif sex.upper()=="M" and age>=20 and age<40:
        return ("work anywhere")
    elif sex.upper()=="M" and age>=40 and age <=60:
        return ("work in urban areas only")
    elif age<20 or age>60:
        return ("ERROR")
print(job_area(age,sex,marital_status))

#Q.No.5

quantity=int(input("enter quantity: "))
cost=quantity*100
def quant(q):
    cost=quantity*100
    if cost>=1000:
        discount=(10/100)*cost
        total_cost=cost-discount
        return total_cost
    else:
        return cost
print("total cost is",quant(quantity))

#Q.No.6

for i in range(10):
    n=int(input("enter a number: "))
    print("number",i+1,"is",n)

#Q.No.7

while True:
    print("infinite loop")

#Q.No.8

n=int(input("enter total no of intger: "))
l=[]
for i in range(n):
    n1=int(input("enter integer: "))
    l.append(n1)
print("first list is",l)
l2=[]
for j in l:
    s=j**2
    l2.append(s)
print("list containig square of intigers is",l2)

#Q.No.9

l=[1,"ishita",2.3]
l1=[]
l2=[]
l3=[]
for i in l:
    if type(i)==int:
        l1.append(i)
        print(l1)
    elif type(i)==float:
        l2.append(i)
        print(l2)
    else:
        l3.append(i)
        print(l3)

#Q.No.10

l=[]
for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
print(l)

#Q.No.11

for i in range(1,5):
    print("*"*i)

#Q.No.12

n=int(input("enter total no of elements: "))
l=[]
for i in range(n):
    n1=int(input("enter number: "))
    l.append(n1)
print(l)
n2=int(input("enter element to be serached: "))
for j in l:
    if j==n2:
        k=l.index(j)
        l.pop(k)
print(l)
