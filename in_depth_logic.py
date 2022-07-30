from tabulate import tabulate
import random
#user entering the subjects for one class in the timetable for a week

print("Enter 1 to add Maths")
print("Enter 2 to add Chemistry")
print("Enter 3 to add Physics")
print("Enter 4 to add Comp science")
print("Enter 5 to add English")
Monday=[]
Tuesday=[]
Wednesday=[]
Thursday=[]
Friday=[]


print("Enter the subjects for Monday:")
for i in range(1,7):
    print("Enter period",i,":")
    temp=input()
    Monday.append(temp)

Mon=["Monday"]   
for i in Monday:
    if i=="1":
        s=i.replace("1","Maths")
    if i=="2":
        s=i.replace("2","Chemistry")
    if i=="3":
        s=i.replace("3","Physics")
    if i=="4":
        s=i.replace("4","Comp Science")
    if i=="5":
        s=i.replace("5","English")
    Mon.append(s)

print("Enter 1 to add Maths")
print("Enter 2 to add Chemistry")
print("Enter 3 to add Physics")
print("Enter 4 to add Comp science")
print("Enter 5 to add English")
print("Enter the subjects for Tuesday:")
for i in range(1,7):
    print("Enter period",i,":")
    temp=input()
    Tuesday.append(temp)
Tue=["Tuesday"]   
for i in Tuesday:
    if i=="1":
        s=i.replace("1","Maths")
    if i=="2":
        s=i.replace("2","Chemistry")
    if i=="3":
        s=i.replace("3","Physics")
    if i=="4":
        s=i.replace("4","Comp Science")
    if i=="5":
        s=i.replace("5","English")
    Tue.append(s)    


print("Enter 1 to add Maths")
print("Enter 2 to add Chemistry")
print("Enter 3 to add Physics")
print("Enter 4 to add Comp science")
print("Enter 5 to add English")
print("Enter the subjects for Wednesday:")
for i in range(1,7):
    print("Enter period",i,":")
    temp=input()
    Wednesday.append(temp)
Wed=["Wednesday"]   
for i in Wednesday:
    if i=="1":
        s=i.replace("1","Maths")
    if i=="2":
        s=i.replace("2","Chemistry")
    if i=="3":
        s=i.replace("3","Physics")
    if i=="4":
        s=i.replace("4","Comp Science")
    if i=="5":
        s=i.replace("5","English")
    Wed.append(s)

print("Enter 1 to add Maths")
print("Enter 2 to add Chemistry")
print("Enter 3 to add Physics")
print("Enter 4 to add Comp science")
print("Enter 5 to add English")    
print("Enter the subjects for Thursday:")
for i in range(1,7):
    print("Enter period",i,":")
    temp=input()
    Thursday.append(temp)
Thurs=["Thursday"]   
for i in Thursday:
    if i=="1":
        s=i.replace("1","Maths")
    if i=="2":
        s=i.replace("2","Chemistry")
    if i=="3":
        s=i.replace("3","Physics")
    if i=="4":
        s=i.replace("4","Comp Science")
    if i=="5":
        s=i.replace("5","English")
    Thurs.append(s)

print("Enter 1 to add Maths")
print("Enter 2 to add Chemistry")
print("Enter 3 to add Physics")
print("Enter 4 to add Comp science")
print("Enter 5 to add English") 
print("Enter the subjects for Friday:")
for i in range(1,7):
    print("Enter period",i,":")
    temp=input()
    Friday.append(temp)    
Fri=["Friday"]   
for i in Friday:
    if i=="1":
        s=i.replace("1","Maths")
    if i=="2":
        s=i.replace("2","Chemistry")
    if i=="3":
        s=i.replace("3","Physics")
    if i=="4":
        s=i.replace("4","Comp Science")
    if i=="5":
        s=i.replace("5","English")
    Fri.append(s)
Tmtble=[Mon,Tue,Wed,Thurs,Fri]

print(tabulate(Tmtble, headers=["","1","2","3","4","5","6"], tablefmt="grid"))
 #Computer auto entering subjects in second section

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

Monday2=["1","2","3","4","5"]
rep=[]
ch='n'
flag=0
while ch!='y':
    dig=random.randint(1,5)
    if str(dig) in rep:
        continue
    Monday2.append(str(dig))
    random.shuffle(Monday2)
    for j in range(0,6):
        if  Monday[j] == Monday2[j]:
            Monday2=["1","2","3","4","5"]
            flag=0
            break
        else:
            flag+=1
    if flag==6:    
        ch="y"
rep.append(str(dig))
Tuesday2=["1","2","3","4","5"]
ch='n'
flag=0
while ch!='y':
    dig=random.randint(1,5)
    if str(dig) in rep:
        continue
    Tuesday2.append(str(dig))
    random.shuffle(Tuesday2)
    for j in range(0,6):
        if  Tuesday[j] == Tuesday2[j]:
            Tuesday2=["1","2","3","4","5"]
            flag=0
            break
        else:
            flag+=1
    if flag==6:    
        ch="y"
rep.append(str(dig))
Wednesday2=["1","2","3","4","5"]
ch='n'
flag=0
while ch!='y':
    dig=random.randint(1,5)
    if str(dig) in rep:
        continue
    Wednesday2.append(str(dig))
    random.shuffle(Wednesday2)
    for j in range(0,6):
        if  Wednesday[j] == Wednesday2[j]:
            Wednesday2=["1","2","3","4","5"]
            flag=0
            break
        else:
            flag+=1
    if flag==6:    
        ch="y"
rep.append(str(dig))
Thursday2=["1","2","3","4","5"]
ch='n'
flag=0
while ch!='y':
    dig=random.randint(1,5)
    if str(dig) in rep:
        continue
    Thursday2.append(str(dig))
    random.shuffle(Thursday2)
    for j in range(0,6):
        if  Thursday[j] == Thursday2[j]:
            Thursday2=["1","2","3","4","5"]
            flag=0
            break
        else:
            flag+=1
    if flag==6:    
        ch="y" 
rep.append(str(dig))
Friday2=["1","2","3","4","5"]
ch='n'
flag=0
while ch!='y':
    dig=random.randint(1,5)
    if str(dig) in rep:
        continue
    Friday2.append(str(dig))
    random.shuffle(Friday2)
    for j in range(0,6):
        if  Friday[j] == Friday2[j]:
            Friday2=["1","2","3","4","5"]
            flag=0
            break
        else:
            flag+=1
    if flag==6:    
        ch="y"  
Mon2=["Monday"]
Tue2=["Tuesday"]
Wed2=["Wednesday"] 
Thurs2=["Thursday"]
Fri2=["Friday"] 

Mon2=switch(Monday2,Mon2)
Tue2=switch(Tuesday2,Tue2)
Wed2=switch(Wednesday2,Wed2) 
Thurs2=switch(Thursday2,Thurs2)
Fri2=switch(Friday2,Fri2)       
Tmtble2=[Mon2,Tue2,Wed2,Thurs2,Fri2]

print(tabulate(Tmtble2, headers=["","1","2","3","4","5","6"], tablefmt="grid"))  




