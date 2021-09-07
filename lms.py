# library management system using Tkinter
# 1. login
# 2. loan
# 3. return
# 4. new book
# 5. new Student
# 6. Student record
# 7. delete student
# 8. delete Book


import mysql.connector as c
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

con = c.connect(host="localhost", user="root", password="*******", database="lms")
cursor = con.cursor()

main = Tk()
main.geometry('800x500')
main.title('LIBRARY MANAGEMENT SYSTEM')
main.iconbitmap(r'D:\\RISHABH KADAM\\Programming\\Python\\titleicon.ico')

def raise_frame(frame):
    frame.tkraise()

DelSt_frame = Frame(main)
DelSt_frame.place(width=800,height=500)
DelSt_frame.configure(bg='#b3fff0')

DelBk_frame = Frame(main)
DelBk_frame.place(width=800,height=500)
DelBk_frame.configure(bg='#b3fff0')

StDetail_frame = Frame(main)
StDetail_frame.place(width=800, height=500)
StDetail_frame.configure(bg='#b3fff0')

Loan_frame = Frame(main)
Loan_frame.place(width=800, height=500)
Loan_frame.configure(bg='#b3fff0')

Return_frame = Frame(main)
Return_frame.place(width=800, height=500)
Return_frame.configure(bg='#b3fff0')

NB_Frame = Frame(main)
NB_Frame.place(width=800, height=500)
NB_Frame.configure(bg='#b3fff0')

Stu_Frame = Frame(main)
Stu_Frame.place(width=800, height=500)
Stu_Frame.configure(bg='#b3fff0')

menu = Frame(main)
menu.place(width=800, height=500)
menu.configure(bg='skyblue')


login_frame = Frame(main)
login_frame.place(width=800, height=500)
login_frame.configure(bg='skyblue')

Label(login_frame, text='developed by RISHABH KADAM', bg='skyblue').pack(side=BOTTOM)
# =============================================================== #
# LOGIN
username = StringVar()
pwd = StringVar()
l = ['rishabh', 'kadam']
Label(login_frame, text='LOGIN', font=("OCR A Extended", 60), background='skyblue').place(x=280, y=40)

user = Entry(login_frame, textvariable=username, font=("Arial Unicode MS", 15), width=20)
user.insert(0, "Enter Username")
user.place(x=290, y=160)

pw = Entry(login_frame, textvariable=pwd, font=("Arial Unicode MS", 15), width=20)
pw.insert(0, "Enter Password")
pw.place(x=290, y=200)


def checkID():
    if username.get() == l[0] and pwd.get() == l[1]:
        return raise_frame(menu)

    else:
        Label(login_frame, text='Incorrect! Try again.', bg='skyblue', fg='#cc0000', font=20).place(x=290, y=135)
        messagebox.showerror("Incorrect","Username or Password Incorrect! try again!")


def userClick(a):
    user.delete(0, 'end')


def pwdClick(b):
    pw.delete(0, 'end')


user.bind('<Button-1>', userClick)
pw.bind('<Button-1>', pwdClick)

loginIcon = PhotoImage(file=r'D:\\RISHABH KADAM\\Programming\\Python\\loginicon.png')
Button(login_frame, text='login', image=loginIcon, background='skyblue', border=0,
       command=checkID).place(x=350, y=250)
# ================================================================ #
# BACK BUTTON
backIcon = PhotoImage(file=r'D:\\RISHABH KADAM\\Programming\\Python\\backicon.png')
def back(curFrame,frame):
    Button(curFrame, text='Back', image=backIcon, height=50, width=50, border=0, bg='#b3fff0',
           command=lambda: raise_frame(frame)).place(x=10, y=10)
# ================================================================ #
# MENU BUTTONS
bd_color = Frame(menu, background="black")
Label(bd_color, text='WELCOME TO LIBRARY MANAGEMENT SYSTEM', fg='black',bg='#c1bebe',bd=10,
      font=("Lucida Sans", 20)).place(x=5, y=6)
bd_color.place(relx=0.1,rely=0,relwidth=.82,relheight=.13)

buttonL = Button(menu, text='Loan', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                 command=lambda: raise_frame(Loan_frame)).place(x=285, y=90)

buttonR = Button(menu, text='Return', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                 command=lambda: raise_frame(Return_frame)).place(x=285,
                                                                  y=140)

buttonNBook = Button(menu, text='New Book', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                     command=lambda: raise_frame(NB_Frame)).place(x=285, y=190)

buttonNStudent = Button(menu, text='New Student', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                        command=lambda: raise_frame(Stu_Frame)).place(x=285, y=240)

buttonStDt = Button(menu, text='Student Detail', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                    command=lambda: raise_frame(StDetail_frame)).place(x=285, y=290)

buttonDelBk = Button(menu, text='Delete Book', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                        command=lambda: raise_frame(DelBk_frame)).place(x=285, y=340)

buttonDelSt = Button(menu, text='Delete Student', height=1, width=20, font=("Helvetica", 15), background='LightCoral',
                        command=lambda: raise_frame(DelSt_frame)).place(x=285, y=390)

Button(menu, text='', image=backIcon, height=50, width=50, border=0,background='skyblue',
           command=lambda: raise_frame(login_frame)).place(x=10, y=10)
# ==================================================================== #
# NEW STUDENT
rollno = StringVar()
name = StringVar()
branch = StringVar()
Label(Stu_Frame, text='Add New Student', font=("", 30), background='#b3fff0').place(x=250, y=20)

Label(Stu_Frame, text='Name :', font=12, background='#b3fff0').place(x=40, y=150)
Entry(Stu_Frame, textvariable=name, font=12).place(x=120, y=150)

Label(Stu_Frame, text='Roll No. :', font=12, background='#b3fff0').place(x=40, y=200)
Entry(Stu_Frame, textvariable=rollno, font=12).place(x=120, y=200)

Label(Stu_Frame, text='Branch :', font=12, background='#b3fff0').place(x=40, y=250)
Entry(Stu_Frame, textvariable=branch, font=12).place(x=120, y=250)


def bt():
    try:
        libid = f"lib{branch.get()+str(datetime.datetime.now().year)+rollno.get()[-2:]}".upper()
        query = "insert into student values('{}','{}','{}','{}')".format(rollno.get(),libid,name.get().upper(),branch.get().upper())
        cursor.execute(query)
        con.commit()
        Label(Stu_Frame, text='Name : ' + (name.get().upper()), font=12, background='#b3fff0').place(x=400, y=150)
        Label(Stu_Frame, text='Roll No. : ' + (rollno.get()), font=12, background='#b3fff0').place(x=400, y=200)
        Label(Stu_Frame, text='Branch : ' + (branch.get().upper()), font=12, background='#b3fff0').place(x=400, y=250)
        Label(Stu_Frame, text='Lib ID : ' + libid, font=12, background='#b3fff0').place(x=400, y=300)
        messagebox.showinfo("Student", "Student Added Successfully.")
    except:
        messagebox.showerror("Error","Something went wrong!")

Button(Stu_Frame, text='Generate', font=30, height=1, width=19, background='grey', command=bt).place(x=120, y=300)

back(Stu_Frame,menu)

# -------------------------------------------------------------------------------------------------#
# NEW BOOK
bookno = StringVar()
bname = StringVar()
noofbooks = StringVar()
Label(NB_Frame, text='Add New Book', font=('', 30), background='#b3fff0').place(x=250, y=20)

Label(NB_Frame, text='Book No. :', font=12, background='#b3fff0').place(x=40, y=150)
Entry(NB_Frame, textvariable=bookno, font=12).place(x=150,y=150)

Label(NB_Frame, text='Book Name :', font=12, background='#b3fff0').place(x=40, y=200)
Entry(NB_Frame, textvariable=bname, font=12).place(x=150, y=200)

Label(NB_Frame, text='No. of Books :', font=12, background='#b3fff0').place(x=40, y=250)
Entry(NB_Frame, textvariable=noofbooks, font=12).place(x=150, y=250)

def bt():
    try:
        query = "insert into book values('{}','{}','{}')".format(bookno.get(), bname.get(),noofbooks.get())
        cursor.execute(query)
        con.commit()
        Label(NB_Frame, text='Book Name : ' + bname.get(), font=12, background='#b3fff0').place(x=400, y=150)
        Label(NB_Frame, text='Book No. : ' + (bookno.get()), font=12, background='#b3fff0').place(x=400, y=200)
        Label(NB_Frame, text='No. of Book : ' + (noofbooks.get()), font=12, background='#b3fff0').place(x=400, y=250)
        messagebox.showinfo("Book","Book Added Successfully.")
    except:
        messagebox.showerror("Error","Something went wrong!")

Button(NB_Frame, text='Add Book', font=30, height=1, width=19, background='grey', command=bt).place(x=150, y=300)

back(NB_Frame, menu)
# ---------------------------------------------------------------------------------------------- #
# RETURN
R_libid = StringVar()
R_Bno = StringVar()
Label(Return_frame, text='Return Book', font=('', 30), background='#b3fff0').place(x=250, y=20)

Label(Return_frame, text='LIBID: ', font=12, background='#b3fff0').place(x=40, y=150)
Entry(Return_frame, textvariable=R_libid, font=12).place(x=150, y=150)

Label(Return_frame, text='Book No.: ', font=12, background='#b3fff0').place(x=40, y=200)
Entry(Return_frame, textvariable=R_Bno, font=12).place(x=150, y=200)


def bt():
    try:
        cursor.execute(f'select * from issuebook where bno = "{R_Bno.get()}"')
        getissebno = cursor.fetchall()
        getdetail = getissebno[0][0]
        cursor.execute(f'select * from book where bookno = "{R_Bno.get()}"')
        getbno = cursor.fetchall()
        cursor.execute(f'select * from student where libid = "{getdetail}"')
        getid = cursor.fetchall()
        cursor.execute(f'delete from issuebook where libid = "{R_libid.get()}" and bno = "{R_Bno.get()}"')
        cursor.execute(f'update book set noofbooks = "{int(getbno[0][2])+1}" where bookno = "{R_Bno.get()}"')
        con.commit()
        Label(Return_frame, text='Book Name : ' + getbno[0][1], font=12, background='#b3fff0').place(x=400, y=150)
        Label(Return_frame, text='Book No. : ' + R_Bno.get(), font=12, background='#b3fff0').place(x=400, y=200)
        Label(Return_frame, text='Issue By : ' + getid[0][2], font=12, background='#b3fff0').place(x=400, y=250)
        Label(Return_frame, text='Issue Lib ID : ' + getid[0][1], font=12, background='#b3fff0').place(x=400, y=300)
        Label(Return_frame, text='Book Successfully Return.', font=12, background='#b3fff0').place(x=150, y=300)
        messagebox.showinfo("Book Retuned","Book Return Successfully.")
    except:
        messagebox.showerror("Error","Something went wrong!")

Button(Return_frame, text='Return Book', font=30, height=1, width=19, background='grey', command=bt).place(x=150, y=250)

back(Return_frame,menu)
# ------------------------------------------------------------------------------------------------- #
# LOAN
libid = StringVar()
bno = StringVar()
dt = datetime.datetime.now()
date = dt.strftime('%d') + " " + dt.strftime('%b') + " " + dt.strftime('%Y')
time = dt.strftime('%I') + ":" + dt.strftime('%M') + ":" + dt.strftime('%S')

Label(Loan_frame, text='Loan A Book', font=('', 30), background='#b3fff0').place(x=250, y=20)

Label(Loan_frame, text='Lib ID : ', font=12, background='#b3fff0').place(x=40, y=100)
Entry(Loan_frame, textvariable=libid, font=12).place(x=100, y=100)


def issueBook():
        try:
            cursor.execute(f'select * from book where bookno = {bno.get()}')
            getNoofBOOK = cursor.fetchall()
            numBooks = getNoofBOOK[0][2]
            print(numBooks)
            if numBooks == '0':
                print("BOOK ARE NOT AVAILABLE YET.")
            else:
                cursor.execute(f'select * from book where bookno = {bno.get()}')
                getbookname = cursor.fetchall()
                query = "insert into issuebook values('{}','{}','{}','{}')".format(libid.get(), bno.get(), date + " " + time, getbookname[0][1])
                cursor.execute(query)

                cursor.execute(f'update book set noofbooks = "{int(getbookname[0][2])-1}" where bookno = "{bno.get()}"')
                con.commit()
        except:
            messagebox.showerror("Error", "Something Wrong!Try again!")
def bt():
    try:
        cursor.execute(f'select * from student where libid = "{libid.get()}"')
        getid = cursor.fetchall()
        Label(Loan_frame, text='Name : ' + getid[0][2], font=12, background='#b3fff0').place(x=400, y=100)
        Label(Loan_frame, text='Roll No.: ' + getid[0][0], font=12, background='#b3fff0').place(x=400, y=130)
        Label(Loan_frame, text='branch : ' + getid[0][3], font=12, background='#b3fff0').place(x=400, y=160)
        Label(Loan_frame, text='Book No.: ', font=12, background='#b3fff0').place(x=40, y=300)
        bnum = Entry(Loan_frame, textvariable=bno, font=12, width=13)
        bnum.place(x=120, y=300)

        def clean():
            bnum.delete(0, 'end')

        Button(Loan_frame, text='Add', font=30, height=1, width=10, background='grey', command=issueBook).place(x=250, y=300)
        Button(Loan_frame, text='Add More', font=30, height=1, width=10, background='grey', command=clean).place(x=360, y=300)

        Button(Loan_frame, text='Done', font=30, height=1, width=10, background='grey',
               command=lambda: raise_frame(menu)).place(x=500, y=300)
    except:
        messagebox.showerror("Error", "ID wrong not found!")

btn = Button(Loan_frame, text='Search', font=30, height=1, width=19, background='grey',command=bt)
btn.place(x=100,y=150)

back(Loan_frame, menu)
# ------------------------------------------------------------------------------------------------- #
# STUDENT Detail
StD_libid = StringVar()
Label(StDetail_frame, text='Student Detail', font=('', 30), background='#b3fff0').place(x=250, y=20)
Label(StDetail_frame, text='Lib ID : ', font=12, background='#b3fff0').place(x=40, y=100)
Entry(StDetail_frame, textvariable=StD_libid, font=12).place(x=100, y=100)
def bt():
    try:
        cursor.execute(f'select * from student where libid = "{StD_libid.get()}"')
        StuDLibid = cursor.fetchall()

        Label(StDetail_frame, text='Name      : ' + StuDLibid[0][2], font=12, background='#b3fff0').place(x=400, y=100)
        Label(StDetail_frame, text='Roll No.  : ' + StuDLibid[0][0], font=12, background='#b3fff0').place(x=400, y=130)
        Label(StDetail_frame, text='branch    : ' + StuDLibid[0][3], font=12, background='#b3fff0').place(x=400, y=160)

        cursor.execute(f'select * from issuebook where libid = "{StD_libid.get()}"')
        get = cursor.fetchall()

        tree = ttk.Treeview(StDetail_frame, columns=("1", "2", "3"),show='headings')
        tree.place(x=100,y=250)
        tree.heading("1",text='Date/Time')
        tree.heading("2",text='book No.')
        tree.heading("3",text='Book Name')
        for i in get:
            tree.insert('',"end", values=(i[2],i[1],i[3]))
    except:
        messagebox.showerror("Error","Something went wrong!")

Button(StDetail_frame, text='Search', font=30, height=1, width=19, background='grey', command=bt).place(x=100, y=150)
back(StDetail_frame, menu)

# ------------------------------------------------------------------------------------------------- #
# DELETE BOOK
back(DelBk_frame, menu)

Label(DelBk_frame, text='Delete Book', font=('', 30), background='#b3fff0').place(x=250, y=20)
Dbno = StringVar()
Label(DelBk_frame, text='Book Number : ', font=12, background='#b3fff0').place(x=40, y=100)
Entry(DelBk_frame, textvariable=Dbno, font=12).place(x=160, y=100)

def bt():
    try:
        cursor.execute(f'delete from book where bookno = "{Dbno.get()}"')
        con.commit()
        Label(DelBk_frame,text="Book Delete Successfully.", font=12, background='#b3fff0').place(x=100,y=300)
        messagebox.showinfo("Deleted","Student delete Successfully.")
    except:
        messagebox.showerror("Error","Something went wrong!")

Button(DelBk_frame, text='Search', font=30, height=1, width=19, background='grey', command=bt).place(x=160, y=150)
# ------------------------------------------------------------------------------------------------- #
# DELETE STUDENT
back(DelSt_frame, menu)

Label(DelSt_frame, text='Delete Student', font=('', 30), background='#b3fff0').place(x=250, y=20)
DSid =StringVar()
Label(DelSt_frame, text='Lib ID : ', font=12, background='#b3fff0').place(x=40, y=100)
Entry(DelSt_frame, textvariable=DSid, font=12).place(x=100, y=100)

def bt():
    try:
        cursor.execute(f'delete from student where libid = "{DSid.get()}"')
        con.commit()
        Label(DelSt_frame,text="Student Delete Successfully.", font=12, background='#b3fff0').place(x=100,y=300)
        messagebox.showinfo("Deleted", "Book delete Successfully.")
    except:
        messagebox.showerror("Error","Something went wrong!")

Button(DelSt_frame, text='Search', font=30, height=1, width=19, background='grey', command=bt).place(x=100, y=150)

menu.mainloop()
