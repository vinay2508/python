#Q.NO.1

a=3
if a<4:
    
    try:
        a=a/(a-3)
        print(a)
    except ZeroDivisionError as v:
        print(v)

#ZeroDivisionError exception is occured here.

#Q.no.2

try:
    l=[1,2,3] 
    print(l[3]) 
except IndexError as ie:
    print(ie)

#IndexError exception is occured here.

    
#Q.NO.3
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise 
# NameError: Hi there


#Q.NO.4

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#The output of this code is -5.0
#a/b result in 0


#Q.NO.5
#IMPORT ERROR

import sys
try:
    from time import datetime
except Exception as e:
    print(e)
#VALUE ERROR

while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print (" That was no valid number.  Try again...")

#Index Error

x=[12,11,77]
try:
    for i in range(5):
        print(x[i])
except IndexError as ab:
    print(ab)
