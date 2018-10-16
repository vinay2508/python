#Q.1- Create a function to calculate the area of a sphere by taking radius from user. 
def sphere(r):
    pi=3.14
    area=4*pi*r*r
    return area
r=int(input("Enter the radius : "))
print('Area of sqaure is :',sphere(r))

#Q.2-Prints All the Perfect Numbers Between 1 and 1000
l=[]
def perfect(n):
    p=0
    
    for i in range(1,n):
        if n%i==0:
            p=p+i
    if p==n:
        l.append(p)
    return l
for j in range(1,1000):
    a=perfect(j)

print(a)

#Q.3-Print Multiplication Table of a User Defined Number
n=int(input('Enter the number:'))
if n>=1:
    for x in range (1,11):
        y=n * x
        print(y)

#Q.4-Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
       

                                
