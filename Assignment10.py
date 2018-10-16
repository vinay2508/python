#Q.1

f=open(r"c:\python\rahul.txt","r")
f1=f.readlines()
for i in f1:
    print(i)
f.close()

#Q.2
f=open(r"c:\python\r2.txt","r")
f1=f.read()
x=input("enter a word to count its occurence: ")
c=0
for i in f1:
    if i==x:
        c+=1
f.close()
print(x,"occurs",c,"times.")

#Q.3
f=open(r"c:\python\r2.txt","r")
f1=f.read()
f.close()
f2=open(r"c:\python\rahul.txt","w")
f2.write(f1)
f2.close()

#Q.No.4
f=open(r"c:\python\rahul.txt","r")
f1=open(r"c:\python\r2.txt","r+")
for i,j in zip(f,f1):
    f1.write(i+j)
f.close()
f1.close()

#Q.5
import random
f=open(r"c:\python\r3.txt","w+")
for i in range(10):
    num=random.randint(1,10)
    f.write(str(num))
f.close()
f=open(r"c:\python\r3.txt","r")
f1=f.read()
l=[]
for i in f1:
    i=int(i)
    l.append(i)
l.sort()
f2=open(r"c:\python\r4.txt","w")
for j in l:
    f2.write(str(j))
f2.close()
f.close()

