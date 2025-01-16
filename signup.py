
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
     

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror("Error", 'All fields are required')
    
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("Error", 'Password is not matching')
    else:
        try: 
            con = pymysql.connect(host="localhost",user="root",password="root")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error", 'Database connectivity issue, try again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Name already exists.')
        else:   
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','resgistration is done')
            clear()
            signup_window.destroy()
            import signin

            


def login_page():
    signup_window.destroy()
    import signin

signup_window = Tk()

signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file=r"C:\Users\ahuja\Desktop\Project\background.jpg")

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame= Frame(signup_window,bg='white')
frame.place(x=453,y=40)

heading = Label(frame, text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),
                bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)


emailLabel= Label(frame, text='Email', font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',9,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLabel= Label(frame, text='Username', font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25, pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',9,'bold'),bg='firebrick1',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel= Label(frame, text='Password', font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25, pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',9,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


confirmLabel= Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25, pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',9,'bold'),bg='firebrick1',fg='white')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

signupButton = Button(frame,text='Signup', font=('Open Sans',14,'bold'),bg='firebrick1',fg='white'
                ,activebackground='firebrick1',activeforeground='white', width=20,command = connect_database)
signupButton.grid(row=9,column=0,sticky='w',padx=25,pady=30)

alreadyAccount = Label(frame,text="Don't have an account?", font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
alreadyAccount.grid(row=10,column=0,sticky='w',padx=25)

loginButton= Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',
                    activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=372)

signup_window.mainloop()
