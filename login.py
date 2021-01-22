from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from datetime import *

db = mysql.connector.connect(
    user="lifechoices",
    password="@Lifechoices1234",
    host="localhost",
    database="lifechoicesOnline",
    auth_plugin="mysql_native_password"
    )

cursor = db.cursor()

window = Tk()
window.resizable(False,False)
window.title("Login")
window.geometry("400x150")
usrlb = Label(window, text="Username:")
passlb = Label(window, text="Password:")
usrame = Entry(window)
pss = Entry(window, show = '*')


def adminIn():
    usr = usrame.get()
    p = pss.get()
    
    sql = "select * from admin where username=%s and password=%s"
    cursor.execute(sql,[(usr), (p)])
    datab = cursor.fetchall()
    if datab:
        window2 = Tk()
        window2.geometry("700x600")
        window2.resizable(False,False)
        window2.title("Admin Page")
        liLb = Label(window2, text="ID:")
        liName = Listbox(window2, width=20)
        li2Lb = Label(window2, text="Fullname:")
        liD = Listbox(window2, width=20)
        liTL = Label(window2,text="Username")
        liT = Listbox(window2, width=20)
        liLp = Label(window2, text="Password:")
        liP = Listbox(window2, width=20)
        #######################################
        lbU = Label(window2, text="Username:")
        Liu = Listbox(window2, width=20)
        lbD = Label(window2, text="Date:")
        Lid = Listbox(window2, width=20)
        LiTiL = Label(window2, text="Login Time:")
        LiTi = Listbox(window2, width=20)
        LiOl = Label(window2, text="Logout Time:")
        LiT0 =Listbox(window2, width=20)
        def s():
            cursor.execute("SELECT id FROM users")
            
            id = cursor.fetchall()

            for x in id:
                liName.insert(END, x)
        
            liName.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT full_name FROM users")
            
            name = cursor.fetchall()

            for x in name:
                liD.insert(END, x)
        
            liD.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT username FROM users")
            
            uName = cursor.fetchall()
            for x in uName:
                liT.insert(END, x)
            liT.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT password FROM users")
            
            pas = cursor.fetchall()
            for x in pas:
                liP.insert(END, x)
            liP.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT username FROM time_register")
            
            tUn = cursor.fetchall()
            for x in tUn:
                Liu.insert(END, x)
            Liu.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT date FROM time_register")
            
            d = cursor.fetchall()
            for x in d:
                Lid.insert(END, x)
            Lid.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT login_time FROM time_register")
            
            timeIn = cursor.fetchall()
            for x in timeIn:
                LiTi.insert(END, x)
            LiTi.insert(END, str(cursor.rowcount) + " rows")
            
            cursor.execute("SELECT logout_time FROM time_register")
            
            timeIn = cursor.fetchall()
            for x in timeIn:
                LiT0.insert(END, x)
            LiT0.insert(END, str(cursor.rowcount) + " rows")
        showbtn = Button(window2, text="show database content", command=s)
        
        liLb.place(x=0, y=0)
        liName.place(x=0, y=50)
        li2Lb.place(x=50, y=0)
        liD.place(x=50, y=50)
        liTL.place(x=150, y=0)
        liT.place(x=150, y=50)
        liLp.place(x=300, y=0)
        liP.place(x=300, y=50)
        lbU.place(x = 0, y = 250)
        Liu.place(x=0, y =300)
        lbD.place(x=150, y=250)
        Lid.place(x=150, y = 300)
        LiTiL.place(x = 300, y = 250)
        LiTi.place(x = 300, y =300)
        LiOl.place(x = 450, y = 250)
        LiT0.place(x = 450, y = 300)
        showbtn.place(x=0, y=500)
        window2.mainloop()

adBtn = Button(window, text="Login as Admin", command=adminIn)
shVar = IntVar()

def shP():
    pss.config(show="")

shwPss = Checkbutton(window, text="Show Password", onvalue=1, offvalue=0, command=shP)

def createUser():
    CuWindow = Tk()
    CuWindow.title("Create student")
    CuWindow.resizable(False,False)
    CuWindow.geometry("300x250")
    nameRegLb = Label(CuWindow, text="Full Name:")
    nameReg = Entry(CuWindow)
    usrNamelb = Label(CuWindow, text="Username:")
    psswrdlb = Label(CuWindow, text="Password:")
    
    usrName = Entry(CuWindow)
    psswrd = Entry(CuWindow, show = '*')
    
    def addUser():
        try:
            user_info = (nameReg.get() ,str(usrName.get()), str(psswrd.get()))
            comm = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"
            
            cursor.execute(comm, user_info)
            
            db.commit()
            mb.showinfo("Confirmation", "User Created Successfully")
            
        except:
            mb.showerror("error", "Username already exist")
        CuWindow.destroy()
    cBtn = Button(CuWindow, text="Create student", command=addUser)
    
    nameRegLb.place(x=0, y=0)
    nameReg.place(x=100, y=0)
    usrNamelb.place(x=0, y=75)
    usrName.place(x=100, y=75)
    psswrdlb.place(x=0, y=150)
    psswrd.place(x=100, y=150)
    cBtn.place(x=100, y=200)
    CuWindow.mainloop()


def addAdmin():
    master = Tk()
    master.title("Add User/Admin")
    master.resizable(False,False)
    
    nameLb = Label(master, text="Name:")
    name = Entry(master)
    usrAdLb = Label(master, text="User/Admin Name:")
    usrEnt = Entry(master)
    usrAdp = Label(master, text="Password")
    adUps = Entry(master)
    
    def creat():
        u = usrEnt.get()
        p = adUps.get()
        com1 = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(u, p);
        cursor.execute(com1)
        cursor.execute(comm3, user_info1)
        db.commit()
        mb.showinfo("Confirmation", "User/Admin Created Successfully")
        
    def priv():
        u = usrEnt.get()
        priv_com = "GRANT ALL PRIVILEGES ON books.authors  TO '%s'@'localhost'"%(u)
        cursor.execute(priv_com)
        mb.showinfo("Message", "Privileges Granted")
    user_info1 = name.get(), usrEnt.get(), adUps.get()
    comm3 = "INSERT INTO admin (full_name, username, password) VALUES (%s, %s, %s)"
        
    

    crteBtn = Button(master, text="Create Admin/User", command=creat)
    privBtn = Button(master, text="Grant Privileges", command=priv)
    nameLb.pack()
    name.pack()
    usrAdLb.pack()
    usrEnt.pack()
    usrAdp.pack()
    adUps.pack()
    privBtn.pack()
    crteBtn.pack()
    master.mainloop()


def showAdmin(): # Function to show admin
    addAdmin()
window.bind("<Alt-a>",lambda i: showAdmin())

def login(): # Function to login
    usr = usrame.get()
    p = pss.get()
    sql = "select * from users where username=%s and password=%s"
    cursor.execute(sql,[(usr), (p)])
    datab = cursor.fetchall()
    login = datetime.now()
    x = login.strftime("%H:%M:%S")
    dt = login.strftime("%d/%m/%y")
    
    if datab:
        mb.showinfo("Login", "login successful")
        hud = Tk()
        def sign():
            logout = datetime.now()
            y = logout.strftime("%H:%M:%S")
            time = usr, str(dt), str(x), str(y)
            comm_time = "INSERT INTO time_register(username, date, login_time, logout_time)VALUES (%s, %s, %s, %s)"
            cursor.execute(comm_time, time)
            db.commit()
            mb.showinfo("Message", "Logout successfully")
            hud.destroy()
            
        signOut = Button(hud, text="sign out", command=sign)
        signOut.pack()
        hud.mainloop()


btn = Button(window, text="register", command=createUser) # Button to create users

btnLogin = Button(window, text="login", command=login) # Button to login

# Placing widgets for Login window
usrlb.place(x=0, y=0)
usrame.place(x=75, y=0)
passlb.place(x=0, y=50)
pss.place(x=75, y=50)
shwPss.place(x=250, y=50)
btn.place(x=10, y=100)
btnLogin.place(x=100, y=100)
adBtn.place(x=175, y=100)
window.mainloop()