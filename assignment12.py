#Q.1
import datetime

today = datetime.date.today()
print (today)

#Q.2
import webbrowser
import time
total_breaks=3
break_count=0
while(break_count<total_breaks):
    print("This program started on"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=TKz5G8qVI-c")
    break_count +=1

    
#Q.3
import os 
path = r'C:\Users\Rahul\Desktop'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1     
