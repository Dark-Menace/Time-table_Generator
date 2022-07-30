def Home_screen():
    master=Tk()
    master.geometry("300x150")
    master.minsize(350,150)
    master.maxsize(350,150)
    master.title("Timetable generator")
    Label(text="").pack()
    Button(text="Continue",height="2",width=30,command=Main_pg,relief="solid").pack()    
    master.mainloop()

def Main_pg():
    global Main
    Main=Toplevel(master)
    Main.geometry("300x150")
    Main.minsize(300,150)
    Main.maxsize(300,150)
    Label(Main,text="").pack()
    Button(Main,text="Login",height="2",width=30,command=lambda:[Login_window(),Main.destroy()],relief="solid").pack()
    Label(Main,text="").pack()
    Button(Main,text="Register",height="2",width=30,command=lambda:[Register_window(),Main.destroy()],relief="solid").pack()

def Login_window():
    global lgin
    lgin=Toplevel(master)
    lgin.geometry("360x250")
    lgin.minsize(450,250)
    lgin.maxsize(450,250)
    lgin.title("Login")
    Label(lgin,text="").pack()
    Label(lgin,text="User Name").pack()
    global username2
    global password2
    username2=Entry(lgin,bd=5,relief="ridge")
    username2.pack()
    Label(lgin,text="Password").pack()
    password2=Entry(lgin,bd=5,show="*",relief="ridge")
    password2.pack()
    Button(lgin,text="Home",height="2",width=16,command=lgin.destroy,relief="ridge").pack(side=LEFT)
    Button(lgin,text="Back",height="2",width=16,command=lambda:[Main_pg(),lgin.destroy()],relief="ridge").pack(side=LEFT)
    Button(lgin,text="Enter",height="2",width=16,command=lambda:[decide(),lgin.destroy()],relief="ridge").pack(side=LEFT)

def Register_window():
    global rgstr
    rgstr=Toplevel(master)
    rgstr.geometry("200x200")
    rgstr.minsize(280,200)
    rgstr.maxsize(280,200)
    rgstr.title("Register")
    Label(rgstr,text="").pack()
    Label(rgstr,text="User Name").pack()
    global username1
    global password1
    username1=Entry(rgstr,bd=5,relief="ridge")
    username1.pack()
    Label(rgstr,text="Password").pack()
    password1=Entry(rgstr,bd=5,show="*",relief="ridge")
    password1.pack()
    Button(rgstr,text="Home",height="2",width=8,command=rgstr.destroy,relief="ridge").pack(side=LEFT)
    Button(rgstr,text="Back",height="2",width=8,command=lambda:[Main_pg(),rgstr.destroy()],relief="ridge").pack(side=LEFT)
    Button(rgstr,text="Enter",height="2",width=8,command=lambda:[register_admin(),rgstr.destroy(),Main_pg()],relief="ridge").pack(side=LEFT)    

def Content_window():
    global cont
    cont=Toplevel(master)
    cont.geometry("300x200")
    cont.minsize(400,200)
    cont.maxsize(400,200)
    cont.title("Timetable generator")
    Label(cont,text="").pack()
    Button(cont,text="Generate Timetable",height="2",width=20,relief="ridge",command=lambda:[sec_finder(),cont.destroy()]).pack()
    Label(cont,text="").pack()
    Button(cont,text="Register Teacher",height="2",width=20,relief="ridge",command=lambda:[register_teacher(),cont.destroy()]).pack()
    Button(cont,text="Home",height="2",width=13,relief="ridge",command=cont.destroy).pack(side=LEFT)
    Button(cont,text="Back",height="2",width=13,command=lambda:[Login_window(),cont.destroy()],relief="ridge").pack(side=LEFT)
    Button(cont,text="Sign out",height="2",width=13,command=lambda:[Main_pg(),cont.destroy()] ,relief="ridge").pack(side=LEFT)

def register_teacher():
    global teach
    teach=Toplevel(master)
    teach.geometry("300x500")
    teach.minsize(400,600)
    teach.maxsize(400,600)
    teach.title("Timetable generator")
    global tchr_name
    global age
    global gend
    global subject
    global clss
    global sect
    global stream1
    Label(teach,text="").pack()
    Label(teach,text="Teacher's name").pack()
    tchr_name=Entry(teach,master,bd=10,relief="ridge")
    tchr_name.pack()
    Label(teach,text="Age").pack()
    age=Entry(teach,master,bd=10,relief="ridge")
    age.pack()
    Label(teach,text="Gender").pack()
    gend=Entry(teach,bd=10,relief="ridge")
    gend.pack()
    Label(teach,text="Subject").pack()
    subject=Entry(teach,master,bd=10,relief="ridge")
    subject.pack()
    Label(teach,text="Class").pack()
    clss=Entry(teach,master,bd=10,relief="ridge")
    clss.pack()
    Label(teach,text="Section").pack()
    sect=Entry(teach,master,bd=10,relief="ridge")
    sect.pack()
    Label(teach,text="Stream").pack()
    stream1=Entry(teach,master,bd=10,relief="ridge")
    stream1.pack()
    Label(teach,text="").pack()
    Button(teach,text="Submit",height="2",width=13,command=lambda:[teacher_regstr_sql(),Content_window(),teach.destroy()],relief="ridge").pack()
    Button(teach,text="Home",height="2",width=13,relief="ridge",command=teach.destroy).pack(side=LEFT)
    Button(teach,text="Back",height="2",width=13,command=lambda:[Content_window(),teach.destroy()] ,relief="ridge").pack(side=LEFT)
    Button(teach,text="Sign out",height="2",width=13,command=lambda:[Main_pg(),teach.destroy()],relief="ridge").pack(side=LEFT)

def teacher_regstr_sql():
    mycon=ms.connect(host="localhost",user="root",passwd="mysql@123",database="timetable_generator")
    mycur=mycon.cursor()
    a=tchr_name.get()
    b=age.get()
    c=gend.get()
    d=subject.get()
    e=clss.get()
    f=sect.get()
    g1=stream1.get()
    g=g1.lower()
    st="Insert into Teachers Values('{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g)
    mycur.execute(st)
    mycon.commit()
    mycon.close()    

def sec_finder():
    global scfind
    scfind=Toplevel(master)
    scfind.geometry("290x340")
    scfind.title("Timetable generator")
    Label(scfind,text="").pack()
    global cs
    global num
    global stream
    Label(scfind,text="Class:").pack()
    cs=Entry(scfind,bd=10,relief="ridge")
    cs.pack()
    Label(scfind,text="Number of sections:").pack()
    num=Entry(scfind,bd=10,relief="ridge")
    num.pack()
    Label(scfind,text="Stream:").pack()
    stream=Entry(scfind,bd=10,relief="ridge")
    stream.pack()
    Label(scfind,text="").pack()
    Button(scfind,text="Submit",height="2",width=8,command=lambda:[timetable_generate_1()],relief="ridge").pack()
    Button(scfind,text="Home",height="2",width=8,relief="ridge",command=scfind.destroy).pack(side=LEFT)
    Button(scfind,text="Back",height="2",width=8,command=lambda:[Content_window(),scfind.detroy()],relief="ridge").pack(side=LEFT)
    Button(scfind,text="Sign out",height="2",width=8,command=lambda:[Main_pg(),scfind.detroy()] ,relief="ridge").pack(side=LEFT)
    
  
def timetable_generate_1():
    p=stream.get()
    if p.lower()=="science":
        Science_1()
    if p.lower()=="commerce":
        Commerce_1()    

def Science_1():
    global sci1
    sci1=Toplevel(master)
    sci1.geometry("450x280")
    sci1.minsize(600,330)
    sci1.maxsize(600,330)
    sci1.title("Timetable generator")

    global a11,a12,a13,a14,a15,a16
    global a21,a22,a23,a24,a25,a26
    global a31,a32,a33,a34,a35,a36
    global a41,a42,a43,a44,a45,a46
    global a51,a52,a53,a54,a55,a56
    Label(sci1,text=" ",relief="ridge",width=8,bd=2).grid(row=0,column=0)
    Label(sci1,text="1",relief="ridge",width=8,bd=2).grid(row=0,column=1)
    Label(sci1,text="2",relief="ridge",width=8,bd=2).grid(row=0,column=2)
    Label(sci1,text="3",relief="ridge",width=8,bd=2).grid(row=0,column=3)
    Label(sci1,text="4",relief="ridge",width=8,bd=2).grid(row=0,column=4)
    Label(sci1,text="5",relief="ridge",width=8,bd=2).grid(row=0,column=5)
    Label(sci1,text="6",relief="ridge",width=8,bd=2).grid(row=0,column=6)
    Label(sci1,text="Mon",relief="ridge",width=8,bd=6).grid(row=1,column=0)
    Label(sci1,text="Tue",relief="ridge",width=8,bd=6).grid(row=2,column=0)
    Label(sci1,text="Wed",relief="ridge",width=8,bd=6).grid(row=3,column=0)
    Label(sci1,text="Thurs",relief="ridge",width=8,bd=6).grid(row=4,column=0)
    Label(sci1,text="Fri",relief="ridge",width=8,bd=6).grid(row=5,column=0)

    a11=Entry(sci1,bd=6,width=8,relief="ridge")
    a11.grid(row=1,column=1)
    a12=Entry(sci1,bd=6,width=8,relief="ridge")
    a12.grid(row=1,column=2)
    a13=Entry(sci1,bd=6,width=8,relief="ridge")
    a13.grid(row=1,column=3)
    a14=Entry(sci1,bd=6,width=8,relief="ridge")
    a14.grid(row=1,column=4)
    a15=Entry(sci1,bd=6,width=8,relief="ridge")
    a15.grid(row=1,column=5)
    a16=Entry(sci1,bd=6,width=8,relief="ridge")
    a16.grid(row=1,column=6)

    a21=Entry(sci1,bd=6,width=8,relief="ridge")
    a21.grid(row=2,column=1)
    a22=Entry(sci1,bd=6,width=8,relief="ridge")
    a22.grid(row=2,column=2)
    a23=Entry(sci1,bd=6,width=8,relief="ridge")
    a23.grid(row=2,column=3)
    a24=Entry(sci1,bd=6,width=8,relief="ridge")
    a24.grid(row=2,column=4)
    a25=Entry(sci1,bd=6,width=8,relief="ridge")
    a25.grid(row=2,column=5)
    a26=Entry(sci1,bd=6,width=8,relief="ridge")
    a26.grid(row=2,column=6)

    a31=Entry(sci1,bd=6,width=8,relief="ridge")
    a31.grid(row=3,column=1)
    a32=Entry(sci1,bd=6,width=8,relief="ridge")
    a32.grid(row=3,column=2)
    a33=Entry(sci1,bd=6,width=8,relief="ridge")
    a33.grid(row=3,column=3)
    a34=Entry(sci1,bd=6,width=8,relief="ridge")
    a34.grid(row=3,column=4)
    a35=Entry(sci1,bd=6,width=8,relief="ridge")
    a35.grid(row=3,column=5)
    a36=Entry(sci1,bd=6,width=8,relief="ridge")
    a36.grid(row=3,column=6)

    a41=Entry(sci1,bd=6,width=8,relief="ridge")
    a41.grid(row=4,column=1)
    a42=Entry(sci1,bd=6,width=8,relief="ridge")
    a42.grid(row=4,column=2)
    a43=Entry(sci1,bd=6,width=8,relief="ridge")
    a43.grid(row=4,column=3)
    a44=Entry(sci1,bd=6,width=8,relief="ridge")
    a44.grid(row=4,column=4)
    a45=Entry(sci1,bd=6,width=8,relief="ridge")
    a45.grid(row=4,column=5)
    a46=Entry(sci1,bd=6,width=8,relief="ridge")
    a46.grid(row=4,column=6)

    a51=Entry(sci1,bd=6,width=8,relief="ridge")
    a51.grid(row=5,column=1)
    a52=Entry(sci1,bd=6,width=8,relief="ridge")
    a52.grid(row=5,column=2)
    a53=Entry(sci1,bd=6,width=8,relief="ridge")
    a53.grid(row=5,column=3)
    a54=Entry(sci1,bd=6,width=8,relief="ridge")
    a54.grid(row=5,column=4)
    a55=Entry(sci1,bd=6,width=8,relief="ridge")
    a55.grid(row=5,column=5)
    a56=Entry(sci1,bd=6,width=8,relief="ridge")
    a56.grid(row=5,column=6)

    Label(sci1,text="""Enter the subjects for section:A
    Enter:
    1 to add Maths.
    2 to add Chemistry.
    3 to add Physics.
    4 to add Comp science/Biology.
    5 to add English.""",width=27,relief="ridge",justify=LEFT).grid(row=6,column=0,columnspan=3)
    Button(sci1,text="Submit",height="2",width=8,command=lambda:[timetable_generate_sci(),sci1.destroy()],relief="ridge").grid(row=6,column=3,sticky=N)
    Button(sci1,text="Home",height="2",width=8,relief="ridge",command=sci1.destroy).grid(row=6,column=4,sticky=N)
    Button(sci1,text="Back",height="2",width=8,command=lambda:[sec_finder(),sci1.destroy()],relief="ridge").grid(row=6,column=3)
    Button(sci1,text="Sign out",height="2",width=8,command=lambda:[Main_pg(),sci1.destroy()] ,relief="ridge").grid(row=6,column=4)

def Commerce_1():
    global com1
    com1=Toplevel(master)
    com1.geometry("450x280")
    com1.minsize(600,330)
    com1.maxsize(600,330)
    com1.title("Timetable generator")

    global a11,a12,a13,a14,a15,a16
    global a21,a22,a23,a24,a25,a26
    global a31,a32,a33,a34,a35,a36
    global a41,a42,a43,a44,a45,a46
    global a51,a52,a53,a54,a55,a56
    Label(com1,text=" ",relief="ridge",width=8,bd=2).grid(row=0,column=0)
    Label(com1,text="1",relief="ridge",width=8,bd=2).grid(row=0,column=1)
    Label(com1,text="2",relief="ridge",width=8,bd=2).grid(row=0,column=2)
    Label(com1,text="3",relief="ridge",width=8,bd=2).grid(row=0,column=3)
    Label(com1,text="4",relief="ridge",width=8,bd=2).grid(row=0,column=4)
    Label(com1,text="5",relief="ridge",width=8,bd=2).grid(row=0,column=5)
    Label(com1,text="6",relief="ridge",width=8,bd=2).grid(row=0,column=6)
    Label(com1,text="Mon",relief="ridge",width=8,bd=6).grid(row=1,column=0)
    Label(com1,text="Tue",relief="ridge",width=8,bd=6).grid(row=2,column=0)
    Label(com1,text="Wed",relief="ridge",width=8,bd=6).grid(row=3,column=0)
    Label(com1,text="Thurs",relief="ridge",width=8,bd=6).grid(row=4,column=0)
    Label(com1,text="Fri",relief="ridge",width=8,bd=6).grid(row=5,column=0)

    a11=Entry(com1,bd=6,width=8,relief="ridge")
    a11.grid(row=1,column=1)
    a12=Entry(com1,bd=6,width=8,relief="ridge")
    a12.grid(row=1,column=2)
    a13=Entry(com1,bd=6,width=8,relief="ridge")
    a13.grid(row=1,column=3)
    a14=Entry(com1,bd=6,width=8,relief="ridge")
    a14.grid(row=1,column=4)
    a15=Entry(com1,bd=6,width=8,relief="ridge")
    a15.grid(row=1,column=5)
    a16=Entry(com1,bd=6,width=8,relief="ridge")
    a16.grid(row=1,column=6)

    a21=Entry(com1,bd=6,width=8,relief="ridge")
    a21.grid(row=2,column=1)
    a22=Entry(com1,bd=6,width=8,relief="ridge")
    a22.grid(row=2,column=2)
    a23=Entry(com1,bd=6,width=8,relief="ridge")
    a23.grid(row=2,column=3)
    a24=Entry(com1,bd=6,width=8,relief="ridge")
    a24.grid(row=2,column=4)
    a25=Entry(com1,bd=6,width=8,relief="ridge")
    a25.grid(row=2,column=5)
    a26=Entry(com1,bd=6,width=8,relief="ridge")
    a26.grid(row=2,column=6)

    a31=Entry(com1,bd=6,width=8,relief="ridge")
    a31.grid(row=3,column=1)
    a32=Entry(com1,bd=6,width=8,relief="ridge")
    a32.grid(row=3,column=2)
    a33=Entry(com1,bd=6,width=8,relief="ridge")
    a33.grid(row=3,column=3)
    a34=Entry(com1,bd=6,width=8,relief="ridge")
    a34.grid(row=3,column=4)
    a35=Entry(com1,bd=6,width=8,relief="ridge")
    a35.grid(row=3,column=5)
    a36=Entry(com1,bd=6,width=8,relief="ridge")
    a36.grid(row=3,column=6)

    a41=Entry(com1,bd=6,width=8,relief="ridge")
    a41.grid(row=4,column=1)
    a42=Entry(com1,bd=6,width=8,relief="ridge")
    a42.grid(row=4,column=2)
    a43=Entry(com1,bd=6,width=8,relief="ridge")
    a43.grid(row=4,column=3)
    a44=Entry(com1,bd=6,width=8,relief="ridge")
    a44.grid(row=4,column=4)
    a45=Entry(com1,bd=6,width=8,relief="ridge")
    a45.grid(row=4,column=5)
    a46=Entry(com1,bd=6,width=8,relief="ridge")
    a46.grid(row=4,column=6)

    a51=Entry(com1,bd=6,width=8,relief="ridge")
    a51.grid(row=5,column=1)
    a52=Entry(com1,bd=6,width=8,relief="ridge")
    a52.grid(row=5,column=2)
    a53=Entry(com1,bd=6,width=8,relief="ridge")
    a53.grid(row=5,column=3)
    a54=Entry(com1,bd=6,width=8,relief="ridge")
    a54.grid(row=5,column=4)
    a55=Entry(com1,bd=6,width=8,relief="ridge")
    a55.grid(row=5,column=5)
    a56=Entry(com1,bd=6,width=8,relief="ridge")
    a56.grid(row=5,column=6)

    Label(com1,text="""Enter the subjects for section:A
    Enter:
    1 to add Statistics.
    2 to add Accounts.
    3 to add Business Studies.
    4 to add Economics.
    5 to add English.""",width=27,relief="ridge",justify=LEFT).grid(row=6,column=0,columnspan=3)
    Button(com1,text="Submit",height="2",width=8,command=lambda:[timetable_generate_com(),com1.destroy()],relief="ridge").grid(row=6,column=3,sticky=N)
    Button(com1,text="Home",height="2",width=8,relief="ridge",command=com1.destroy).grid(row=6,column=4,sticky=N)
    Button(com1,text="Back",height="2",width=8,command=lambda:[sec_finder(),com1.destroy()],relief="ridge").grid(row=6,column=3)
    Button(com1,text="Sign out",height="2",width=8,command=lambda:[Main_pg(),com1.destroy()] ,relief="ridge").grid(row=6,column=4)

def timetable_generate_sci():
    global sci2
    sci2=Toplevel(master)
    sci2.geometry("1500x1500")
    
    sci2.title("Timetable generator")
    Mon=["Monday"]
    Tue=["Tuesday"]
    Wed=["Wednesday"] 
    Thurs=["Thursday"]
    Fri=["Friday"]

    Monday=[a11.get(),a12.get(),a13.get(),a14.get(),a15.get(),a16.get()]
    Mon=switch_sci(Monday,Mon)
    Tuesday=[a21.get(),a22.get(),a23.get(),a24.get(),a25.get(),a26.get()]
    Tue=switch_sci(Tuesday,Tue)
    Wednesday=[a31.get(),a32.get(),a33.get(),a34.get(),a35.get(),a36.get()]
    Wed=switch_sci(Wednesday,Wed)
    Thursday=[a41.get(),a42.get(),a43.get(),a44.get(),a45.get(),a46.get()]
    Thurs=switch_sci(Thursday,Thurs)
    Friday=[a51.get(),a52.get(),a53.get(),a54.get(),a55.get(),a56.get()]
    Fri=switch_sci(Friday,Fri)

    Tmtble=[Monday,Tuesday,Wednesday,Thursday,Friday]
    Timetable=[Mon,Tue,Wed,Thurs,Fri]
    r=tabulate(Timetable, headers=[" ","1","2","3","4","5","6"], tablefmt="grid")
    o=cs.get()
    c="The timetable for class "+o+" A is:"

    Label(sci2,text=c,relief="ridge",width=120,bd=2,font=("Consolas",8)).grid(row=0,column=0)
    Label(sci2,text=r,relief="ridge",width=120,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=1,column=0,rowspan=30)
    sec=int(num.get())
    scfind.destroy()

    mycon=ms.connect(host="localhost",user="root",passwd="mysql@123",database="timetable_generator")
    mycur=mycon.cursor()    
    st="select * from Teachers where Class='{}' and Stream='{}'".format(o,"science")
    mycur.execute(st)
    result=mycur.fetchall()
    mycon.close()
    teacherdata=[]
    for i in result:
        if i[5]=="A":
            teacherdata.append(i)
    c="The teacher info for class "+o+" A is:"
    r=tabulate(teacherdata, headers=["Teacher Name ","Age","Gender","Subject","Class","Section","Stream"], tablefmt="grid")
    Label(sci2,text=c,relief="ridge",width=120,bd=2,font=("Consolas",8)).grid(row=0,column=1)
    Label(sci2,text=r,relief="ridge",width=120,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=1,column=1,rowspan=30)
    teacherdata.clear()
    sci2.minsize(sec*400,sec*400)
    Button(sci2,text="Home",height="3",width=30,relief="ridge",command=sci2.destroy,justify=CENTER).grid(row=500,column=0,sticky=NW)
    Button(sci2,text="Back",height="3",width=30,command=lambda:[Science_1(),sci2.destroy()],relief="ridge",justify=CENTER).grid(row=500,column=0)
    Button(sci2,text="Sign out",height="3",width=30,command=lambda:[Main_pg(),sci2.destroy()] ,relief="ridge",justify=CENTER).grid(row=500,column=0,sticky=E)
    Label(sci2,text="""An app by:
Abhinava Bayary
Shubham Pandey
shashank S""",relief="ridge",width=120,bd=4,font=("Consolas",8)).grid(row=500,column=1)
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
                t2=switch_sci(t2,Mon)
            if j==1:
                t2=switch_sci(t2,Tue)
            if j==2:
                t2=switch_sci(t2,Wed)
            if j==3:
                t2=switch_sci(t2,Thurs)
            if j==4:
                t2=switch_sci(t2,Fri)
            Timetable.append(t2)
        if i+1==2:
            a="B"
            row1=31
        if i+1==3:
            a="C"
            row1=133
        if i+1==4:
            a="D"
            row1=234
        if i+1==5:
            a="E"
            row1=335
        for y in result:
            if y[5]==a:
                teacherdata.append(y)    
        
        t="The timetable for class "+o+" "+a+" is:"
        ti="The teacher info for class "+o+" "+a+" is:"
        tm=tabulate(Timetable, headers=["","1","2","3","4","5","6"], tablefmt="grid")
        qw=tabulate(teacherdata, headers=["Teacher Name ","Age","Gender","Subject","Class","Section","Stream"], tablefmt="grid")
        Label(sci2,text=t,relief="ridge",width=120,bd=2,font=("Consolas",8)).grid(row=row1,column=0)
        Label(sci2,text=tm,relief="ridge",width=120,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=(row1+1),column=0,rowspan=30)
        Label(sci2,text=ti,relief="ridge",width=120,bd=2,font=("Consolas",8)).grid(row=row1,column=1)
        Label(sci2,text=qw,relief="ridge",width=120,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=(row1+1),column=1,rowspan=30)
        teacherdata.clear()
    
    
    
          
def switch_sci(t,Final):         
    for i in t:
        if i=="1":
            st=i.replace("1","Maths")
        if i=="2":
            st=i.replace("2","Chemistry")
        if i=="3":
            st=i.replace("3","Physics")
        if i=="4":
            st=i.replace("4","Comp Science/Bio")
        if i=="5":
            st=i.replace("5","English")
        Final.append(st) 
    return Final


def timetable_generate_com():
    global com2
    com2=Toplevel(master)
    com2.geometry("1500x1500")
    
    com2.title("Timetable generator")
    
    Mon=["Monday"]
    Tue=["Tuesday"]
    Wed=["Wednesday"] 
    Thurs=["Thursday"]
    Fri=["Friday"]

    Monday=[a11.get(),a12.get(),a13.get(),a14.get(),a15.get(),a16.get()]
    Mon=switch_com(Monday,Mon)
    Tuesday=[a21.get(),a22.get(),a23.get(),a24.get(),a25.get(),a26.get()]
    Tue=switch_com(Tuesday,Tue)
    Wednesday=[a31.get(),a32.get(),a33.get(),a34.get(),a35.get(),a36.get()]
    Wed=switch_com(Wednesday,Wed)
    Thursday=[a41.get(),a42.get(),a43.get(),a44.get(),a45.get(),a46.get()]
    Thurs=switch_com(Thursday,Thurs)
    Friday=[a51.get(),a52.get(),a53.get(),a54.get(),a55.get(),a56.get()]
    Fri=switch_com(Friday,Fri)

    Tmtble=[Monday,Tuesday,Wednesday,Thursday,Friday]
    Timetable=[Mon,Tue,Wed,Thurs,Fri]
    r=tabulate(Timetable, headers=["","1","2","3","4","5","6"], tablefmt="grid")
    o=cs.get()
    c="The timetable for class "+o+" A is:"
    c1=c
    Label(com2,text=c1,relief="ridge",width=130,bd=2,font=("Consolas",8)).grid(row=0,column=0)
    Label(com2,text=r,relief="ridge",width=130,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=1,column=0,rowspan=30)
    sec=int(num.get())
    scfind.destroy()
    com2.minsize(sec*400,sec*400)
    
    mycon=ms.connect(host="localhost",user="root",passwd="mysql@123",database="timetable_generator")
    mycur=mycon.cursor()    
    st="select * from Teachers where Class='{}' and Stream='{}'".format(o,"commerce")
    mycur.execute(st)
    result=mycur.fetchall()
    mycon.close()
    teacherdata=[]
    for i in result:
        if i[5]=="A":
            teacherdata.append(i)
    c="The teacher info for class "+o+" A is:"
    r=tabulate(teacherdata, headers=["Teacher Name ","Age","Gender","Subject","Class","Section","Stream"], tablefmt="grid")
    Label(com2,text=c,relief="ridge",width=130,bd=2,font=("Consolas",8)).grid(row=0,column=1)
    Label(com2,text=r,relief="ridge",width=130,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=1,column=1,rowspan=30)
    teacherdata.clear()

    Button(com2,text="Home",height="3",width=30,relief="ridge",command=com2.destroy,justify=CENTER).grid(row=500,column=0,sticky=NW)
    Button(com2,text="Back",height="3",width=30,command=lambda:[Commerce_1(),com2.destroy()],relief="ridge",justify=CENTER).grid(row=500,column=0)
    Button(com2,text="Sign out",height="3",width=30,command=lambda:[Main_pg(),com2.destroy()] ,relief="ridge",justify=CENTER).grid(row=500,column=0,sticky=E)
    Label(com2,text="""An app by:
Abhinava Bayary
Shubham Pandey
shashank S""",relief="ridge",width=120,bd=4,font=("Consolas",8)).grid(row=500,column=1)
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
                t2=switch_com(t2,Mon)
            if j==1:
                t2=switch_com(t2,Tue)
            if j==2:
                t2=switch_com(t2,Wed)
            if j==3:
                t2=switch_com(t2,Thurs)
            if j==4:
                t2=switch_com(t2,Fri)
            Timetable.append(t2)
        if i+1==2:
            a="B"
            row1=31
        if i+1==3:
            a="C"
            row1=133
        if i+1==4:
            a="D"
            row1=234
        if i+1==5:
            a="E"
            row1=335   
        
        t="The timetable for class "+o+" "+a+" is:"
        ti="The teacher info for class "+o+" "+a+" is:"
        qw=tabulate(teacherdata, headers=["Teacher Name ","Age","Gender","Subject","Class","Section","Stream"], tablefmt="grid")
        tm=tabulate(Timetable, headers=["","1","2","3","4","5","6"], tablefmt="grid")
        Label(com2,text=t,relief="ridge",width=130,bd=2,font=("Consolas",8)).grid(row=row1,column=0)
        Label(com2,text=tm,relief="ridge",width=130,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=(row1+1),column=0,rowspan=30)
        Label(com2,text=ti,relief="ridge",width=130,bd=2,font=("Consolas",8)).grid(row=row1,column=1)
        Label(com2,text=qw,relief="ridge",width=130,bd=2,justify=LEFT,anchor="nw",font=("Consolas",8)).grid(row=(row1+1),column=1,rowspan=30)
        teacherdata.clear()
       

def switch_com(t,Final):         
    for i in t:
        if i=="1":
            st=i.replace("1","Statistics")
        if i=="2":
            st=i.replace("2","Accounts")
        if i=="3":
            st=i.replace("3","Business Studies")
        if i=="4":
            st=i.replace("4","Economics")
        if i=="5":
            st=i.replace("5","English")
        Final.append(st) 
    return Final         


def decide():
    mycon=ms.connect(host="localhost",user="root",passwd="mysql@123",database="timetable_generator")
    mycur=mycon.cursor() 
    st="select * from Entry"
    mycur.execute(st)
    data=mycur.fetchall()
    mycon.close()
    x=username2.get()
    y=password2.get()
    flag=0
    for i in data:
        if x==i[0]:
            flag=1
            if y==i[1]:
                lgin.destroy()
                Content_window()
                break
    

def register_admin():
    mycon=ms.connect(host="localhost",user="root",passwd="mysql@123",database="timetable_generator")
    mycur=mycon.cursor()
    x=username1.get()
    y=password1.get()
    st="Insert into Entry Values('{}','{}')".format(x,y)
    mycur.execute(st)
    mycon.commit()
    mycon.close()

from tkinter import*
import mysql.connector as ms
from tabulate import tabulate

import random
master=None   
Home_screen()
