from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import hashlib  # For password hashing

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Functionality Part'
def forget_pass():
    def change_password():
        if user_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Passwords do not match', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='root', database='userdata')
            mycursor = con.cursor()
            query = 'SELECT * FROM data WHERE username=%s'
            mycursor.execute(query, (user_entry.get(),))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                hashed_password = hash_password(newpass_entry.get())
                query = 'UPDATE data SET password=%s WHERE username=%s'
                mycursor.execute(query, (hashed_password, user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset. Please login with the new password.', parent=window)
                window.destroy()
    window = Toplevel()
    window.title("Change Password")
    
    # GUI elements for reset password window
    bgpic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgpic)
    bglabel.grid()
    heading_label = Label(window, text='Reset Password', font=('aerial', 18, 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)
    
    user_label = Label(window, text='Username', font=('aerial', 12, 'bold'), bg='white', fg='red')
    user_label.place(x=470, y=130)
    user_entry = Entry(window, width=25, fg='red', font=('aerial', 11, 'bold'), bd=0)
    user_entry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)
    
    password_label = Label(window, text='New Password', font=('aerial', 12, 'bold'), bg='white', fg='red')
    password_label.place(x=470, y=210)
    newpass_entry = Entry(window, width=25, fg='red', font=('aerial', 11, 'bold'), bd=0, show='*')
    newpass_entry.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)
    
    confirmpass_label = Label(window, text='Confirm New Password', font=('aerial', 12, 'bold'), bg='white', fg='red')
    confirmpass_label.place(x=470, y=290)
    confirmpass_entry = Entry(window, width=25, fg='red', font=('aerial', 11, 'bold'), bd=0, show='*')
    confirmpass_entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submit_button = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('Open Sans', '16', 'bold'),
                           width=19, cursor='hand2', activebackground='magenta2', activeforeground='white',
                           command=change_password)
    submit_button.place(x=470, y=390)
    
    window.mainloop()


def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All inputs are compulsory')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Unable to connect to database')
            return
        query = 'USE userdata'
        mycursor.execute(query)
        query = 'SELECT * FROM data WHERE username=%s'
        mycursor.execute(query, (usernameEntry.get(),))
        row = mycursor.fetchone()
        if row is None or row[2] != hash_password(passwordEntry.get()):  # Compare hashed password
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Success', 'Login successful')

def signup_page():
    login_window.destroy()
    import signup
def hide():
    openeye.config(file=r"C:\Users\ahuja\Desktop\Project\background.jpg")
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file=r'C:\Users\ahuja\Desktop\Project\openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


# GUI Part
# (Existing GUI code remains unchanged)
login_window = Tk()
login_window.geometry('790x512+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file=r"C:\Users\ahuja\Desktop\Project\background.jpg")
bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading = Label(login_window, text='USER LOGIN',font=('Microsoft Yahei UI Light',20,'bold'),
                bg='white')
heading.place(x=520,y=60)

usernameEntry = Entry(login_window, width=25,font=('Microsoft Yahei UI Light',11,'bold'),
                      bd=0,fg='firebrick1')

usernameEntry.place(x=500,y=140)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter) 

frame1 = Frame(login_window,width=200,height=2,bg='firebrick1')
frame1.place(x=500,y=160)

passwordEntry = Entry(login_window, width=25,font=('Microsoft Yahei UI Light',11,'bold'),
                      bd=0,fg='firebrick1')

passwordEntry.place(x=500,y=180)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_window,width=200,height=2,bg='firebrick1')
frame2.place(x=500,y=200)


openeye = PhotoImage(file=r"C:\Users\ahuja\Desktop\Project\openeye.png")


eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                   ,cursor='hand2',command=hide)
eyeButton.place(x=700,y=176)


forgetButton = Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white'
                   ,cursor='hand2', font=('Microsoft Yahei UI Light',7,'bold'), fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=650,y=207)


loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white'
                    ,activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=475,y=250)


signupLabel = Label(login_window,text='Do not have an account?',font=('Open Sans',8,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=475,y=300)


newaccountButton=Button(login_window,text='Create New Account',font=('Open Sans',8,'bold underline'),fg='firebrick1',bg='white',activeforeground='firebrick1'
                    ,activebackground='white',cursor='hand2',bd=0,width=19,command=signup_page)
newaccountButton.place(x=613,y=300)


login_window.mainloop()