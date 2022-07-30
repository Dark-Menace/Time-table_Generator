#Importing required modules
import pyfiglet
from tabulate import tabulate
import random
#user entering the subjects for the first section in a  class
#Definition of required variables

Monday=[]
Tuesday=[]
Wednesday=[]
Thursday=[]
Friday=[]
Mon=["Monday"]
Tue=["Tuesday"]
Wed=["Wednesday"] 
Thurs=["Thursday"]
Fri=["Friday"]
 
#definition of required functions

def inperiod(s):
    print("Enter 1 to add Maths.")
    print("Enter 2 to add Chemistry.")
    print("Enter 3 to add Physics.")
    print("Enter 4 to add Comp science.")
    print("Enter 5 to add English.")
    for i in range(1,7):
        print("Enter period",i,":")
        temp=input()
        s.append(temp)
    return s   

def switch(t,Final):         
    for i in t:
        if i=="1":
            st=i.replace("1","Maths")
        if i=="2":
            st=i.replace("2","Chemistry")
        if i=="3":
            st=i.replace("3","Physics")
        if i=="4":
            st=i.replace("4","Comp Science")
        if i=="5":
            st=i.replace("5","English")
        Final.append(st) 
    return Final


#Invoking the required functions
out=pyfiglet.figlet_format("TIMETABLE\nGENERATOR",font="slant")
print(out)
print()
print("Enter the number of sections:")
sec=int(input())
choice="y"    
while(choice=="y" or choice=="Y"):

    print("Enter the subjects for Monday:")
    print()
    Monday=inperiod(Monday)
    Mon=switch(Monday,Mon)
    print("2.To Enter the subjects for Tuesday:")
    print()
    Tuesday=inperiod(Tuesday)
    Tue=switch(Tuesday,Tue)
    print("3.To Enter the subjects for Wednesday:")
    print()
    Wednesday=inperiod(Wednesday)
    Wed=switch(Wednesday,Wed)
    print("4.To Enter the subjects for Thursday:")
    print()
    Thursday=inperiod(Thursday)
    Thurs=switch(Thursday,Thurs)
    print("5.To Enter the subjects for Friday:")
    print()
    Friday=inperiod(Friday)
    Fri=switch(Friday,Fri)    
    choice="n"

#output 1   
Tmtble=[Monday,Tuesday,Wednesday,Thursday,Friday]
Timetable=[Mon,Tue,Wed,Thurs,Fri]
print("The timetable for 1st section is:")
print()
print(tabulate(Timetable, headers=["","1","2","3","4","5","6"], tablefmt="grid"))
print()


for i in range(1,sec):
    rep=[] 
    Timetable=[] 
    Mon=["Monday"]
    Tue=["Tuesday"]
    Wed=["Wednesday"] 
    Thurs=["Thursday"]
    Fri=["Friday"]
    for j in range(5):
        t2=["1","2","3","4","5"]
        ch='n'
        flag=0
        while ch!='y':
            dig=random.randint(1,5)
            if str(dig) in rep:
                continue
            t2.append(str(dig))
            random.shuffle(t2)
            for k in range(j,(i)*5,5):
                for x in range(0,6):
                    if  t2[x] == Tmtble[k][x]:
                        t2=["1","2","3","4","5"]
                        flag=0
                        test=False
                        break
                    else:
                        flag+=1
                        test=True
                if test==False:
                    break        
            if flag==i*6:
                ch="y"
                rep.append(str(dig))
        Tmtble.append(t2)
        if j==0:
            t2=switch(t2,Mon)
        if j==1:
            t2=switch(t2,Tue)
        if j==2:
            t2=switch(t2,Wed)
        if j==3:
            t2=switch(t2,Thurs)
        if j==4:
            t2=switch(t2,Fri)
        Timetable.append(t2)
   
    print()       
    print("The timetable for ",(i+1), "section is : ")
    print()
    print(tabulate(Timetable, headers=["","1","2","3","4","5","6"], tablefmt="grid"))
    print()




