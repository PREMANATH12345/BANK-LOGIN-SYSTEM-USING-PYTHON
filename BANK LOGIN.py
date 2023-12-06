from tkinter import *
from tkinter import messagebox
import tkinter

import pymysql


def sign():
    w=tkinter.Tk()
    w.config(bg='#D3D3D3')
    w.geometry("1920x1080")
    Label(w,text='MAARIYAMMAN INDIAN BANK',font=('Times New Roman',20,'bold'),fg='brown',bg='#D3D3D3').place(relx=0.32,rely=0.05)
    
    Label(w,text='NAME',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.10,rely=0.2)
    Label(w,text='AGE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.60,rely=0.2)
    Label(w,text='GENDER',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.10,rely=0.3)
    Label(w,text='ACCOUNT NUMBER',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.60,rely=0.3)
    Label(w,text='IFSC CODE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.10,rely=0.4)
    Label(w,text='CIF CODE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.60,rely=0.4)
    Label(w,text='CARD NUMBER',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.10,rely=0.5)
    Label(w,text='PIN NUMBER',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.60,rely=0.5)
    Label(w,text='BRANCH NAME',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.10,rely=0.6)
    Label(w,text='BARNCH CODE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.60,rely=0.6)
    Label(w,text='CREATE PASSWORD',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.10,rely=0.7)
    Label(w,text='CONFORM PASSWORD',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.60,rely=0.7)

    name=Entry(w)
    name.place(relx=0.30,rely=0.2)
    Entry(w).place(relx=0.80,rely=0.2)
    Radiobutton(w,text='MALE',value=1,bg='#D3D3D3').place(relx=0.30,rely=0.3)
    Radiobutton(w,text='FEMALE',value=2,bg='#D3D3D3').place(relx=0.40,rely=0.3)
    Entry(w).place(relx=0.80,rely=0.3)
    Entry(w).place(relx=0.30,rely=0.4)
    Entry(w).place(relx=0.80,rely=0.4)
    Entry(w).place(relx=0.30,rely=0.5)
    Entry(w).place(relx=0.80,rely=0.5)
    Entry(w).place(relx=0.30,rely=0.6)
    Entry(w).place(relx=0.80,rely=0.6)
    pas=Entry(w)
    pas.place(relx=0.30,rely=0.7)
    Entry(w).place(relx=0.80,rely=0.7)
    
    Button(w,text='LOGIN',font=('Times New Roman',11,'bold'),command=logi,bg='red',fg='white').place(relx=0.40,rely=0.8)
    def dd():
        messagebox.showinfo('info','SIGNED SUCCESFULLY') 
        db=pymysql.connect(
        host='localhost',
        user='root',
        password='prem',
        database='prem'
        )
        mydb=db.cursor()
        print("CONNECTED WITH DATABASE")
        sql="INSERT INTO mainproject(NAME,PASS) value(%s,%s)"
        value=(name.get(),pas.get())
        mydb.execute(sql,value)
        db.commit()
    Button(w,text='SUBMIT',font=('Times New Roman',11,'bold'),command=dd,bg='green',fg='white').place(relx=0.50,rely=0.8)

    w.mainloop()

def logi():
    
    win=tkinter.Tk()
    win.config(bg='#D3D3D3')
    win.geometry("1920x1080")

    Label(win,text='MAARIYAMMAN INDIAN BANK',font=('Times New Roman',20,'bold'),fg='brown',bg='#D3D3D3').place(relx=0.46,rely=0.3,anchor=CENTER)

    Label(win,text="USERNAME",bg='#D3D3D3').place(relx=0.4,rely=0.4,anchor=CENTER)
    Label(win,text="PASSWORD",bg='#D3D3D3').place(relx=0.4,rely=0.5,anchor=CENTER)

    name=Entry(win)
    pas=Entry(win)
    name.place(relx=0.5,rely=0.4,anchor=CENTER)
    pas.place(relx=0.5,rely=0.5,anchor=CENTER)
                
    def log():
        db=pymysql.connect(
        host='localhost',
        user='root',
        password='prem',
        database='prem'
        )
        mydb=db.cursor()
        sql="SELECT * FROM mainproject"
        mydb.execute(sql)
        aa=mydb.fetchall()
        bb=[]
        for i in aa:
            bb.append(i)
        n=name.get()
        p=pas.get()
        bbb=(n,p)
        if bbb in bb:
            wi=tkinter.Tk()
            wi.config(bg='#D3D3D3')
            wi.geometry('1920x1080')
            
            Label(wi,text='MAARIYAMMAN INDIAN BANK',font=('Times New Roman',20,'bold'),fg='brown',bg='#D3D3D3').place(relx=0.32,rely=0.03)
            Label(wi,text='WELCOME MR.PREMANATH S',font=('Times New Roman',15),fg='blue',bg='#D3D3D3').place(relx=0.37,rely=0.1)

            Label(wi,text='ACCOUNT DETIALS',font=('Times New Roman',12,'bold'),fg='green',bg='#D3D3D3').place(relx=0.10,rely=0.33)

            Label(wi,text='NAME',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.40)
            Label(wi,text='PREMANATH S',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.40)
            Label(wi,text='ACCOUNT NUMBER',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.45)
            Label(wi,text='123456789',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.45)
            Label(wi,text='IFSC CODE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.50)
            Label(wi,text='IBI00023',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.50)
            Label(wi,text='CIF CODE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.55)
            Label(wi,text='1235678',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.55)
            Label(wi,text='ACCOUNT OPENIN DATE',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.60)
            Label(wi,text='28/02/2002',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.60)
            Label(wi,text='PASSWORD',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.65)
            Label(wi,text='123',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.65)
            Label(wi,text='BRANCH NAME',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.05,rely=0.70)
            Label(wi,text='METTUPPATI',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.20,rely=0.70)


            Label(wi,text='ACCOUNT BALANCE',font=('Times New Roman',10,'bold'),bg='#D3D3D3').place(relx=0.70,rely=0.20)
            Label(wi,text='10000',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.85,rely=0.20)  

            Label(wi,text='AVAILABLE BALANCE',font=('Times New Roman',10,'bold'),bg='#D3D3D3').place(relx=0.70,rely=0.25)
            Label(wi,text='8000',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.85,rely=0.25)  

            

            Label(wi,text='TRANSACTION DETIALS',font=('Times New Roman',12,'bold'),fg='green',bg='#D3D3D3').place(relx=0.60,rely=0.33)

            Label(wi,text='ACCOUNT NUMBER',font=('Times New Roman',10,'bold'),bg='#D3D3D3').place(relx=0.40,rely=0.40)
            Label(wi,text='TYPE',font=('Times New Roman',10,'bold'),bg='#D3D3D3').place(relx=0.70,rely=0.40)
            Label(wi,text='AMOUNT',font=('Times New Roman',10,'bold'),bg='#D3D3D3').place(relx=0.90,rely=0.40)

            Label(wi,text='856723210',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.45)
            Label(wi,text='CREDIT',font=('Times New Roman',10),fg='dark green',bg='#D3D3D3').place(relx=0.70,rely=0.45)
            Label(wi,text='257',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.45)

            Label(wi,text='874567870',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.50)
            Label(wi,text='DEPIT',font=('Times New Roman',10),bg='#D3D3D3',fg='red').place(relx=0.70,rely=0.50)
            Label(wi,text='356',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.50)

            Label(wi,text='876545875',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.55)
            Label(wi,text='CREDIT',font=('Times New Roman',10),fg='dark green',bg='#D3D3D3').place(relx=0.70,rely=0.55)
            Label(wi,text='674',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.55)

            Label(wi,text='876507540',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.60)
            Label(wi,text='DEPIT',font=('Times New Roman',10),bg='#D3D3D3',fg='red').place(relx=0.70,rely=0.60)
            Label(wi,text='432',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.60)


            Label(wi,text='876543210',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.65)
            Label(wi,text='CREDIT',font=('Times New Roman',10),fg='dark green',bg='#D3D3D3').place(relx=0.70,rely=0.65)
            Label(wi,text='1000',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.65)

            Label(wi,text='856723210',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.70)
            Label(wi,text='CREDIT',font=('Times New Roman',10),bg='#D3D3D3',fg='dark green').place(relx=0.70,rely=0.70)
            Label(wi,text='257',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.70)

            Label(wi,text='874567870',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.42,rely=0.75)
            Label(wi,text='DEPIT',font=('Times New Roman',10),fg='red',bg='#D3D3D3').place(relx=0.70,rely=0.75)
            Label(wi,text='356',font=('Times New Roman',10),bg='#D3D3D3').place(relx=0.91,rely=0.75)

            Button(wi,text='TRANSFER',font=('Times New Roman',11,'bold'),bg='blue',fg='white').place(relx=0.68,rely=0.82)



            wi.mainloop
        else:
            messagebox.showwarning("WARNING","INCORRECT USER NAME OR PASSWORD")


    Button(win,text="SIGNIN",command=sign,font=('Times New Roman',11),bg='red',fg='white').place(relx=0.4,rely=0.6,anchor=CENTER)
    Button(win,text="SUBMIT",command=log,font=('Times New Roman',11),bg='green',fg='white').place(relx=0.5,rely=0.6,anchor=CENTER)


    
    win.mainloop()
logi()
