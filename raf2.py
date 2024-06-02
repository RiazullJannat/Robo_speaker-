from tkinter import *
from PIL import ImageTk,Image
import random
import tkinter.messagebox as tmsg

'''root = Tk()
root.title("My app")
icon = PhotoImage(file='guess.png')
root.iconphoto(False,icon)
root.mainloop()'''
'''a = [2,7,11,15]
t = 9
dict = {}
n = len(a)
for i in range(n):

    dict[a[i]] = i


for i in range(n):
    gap = t - a[i]
    if gap in dict and dict[gap] != i:
        print(i,dict[gap])'''
'''import tkinter as tk
root = tk.Tk()
root.geometry('150x150')
root.title("StringVar Example")

string_variable = tk.StringVar(root,"Hello World!")
l = tk.Label(root,textvariable= string_variable, height=150)
l.pack()
root.mainloop()
'''
'''import tkinter as tk

master_window = tk.Tk()
master_window.geometry("300x300")
master_window.title("StringVar get() example")


def print_data():
    print(string_variable.get())


string_variable = tk.StringVar(master_window)

label = tk.Label(master_window, text="Enter Data: ")
label.grid(row=0, column=0)

entry = tk.Entry(master_window, textvariable=string_variable)
entry.grid(row=0, column=1)

button = tk.Button(master_window, text="Print data", command=print_data)
button.grid(row=1, column=0, columnspan=2)

master_window.mainloop()
'''

'''import tkinter as tk
root = tk.Tk()
root.geometry('600x400')

name_var = tk.StringVar()
passw_var = tk.StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()
    print(f'The name is : {name}')
    print(f'The password is : {password}')
    name_var.set("")
    passw_var.set("")


name_lebel = tk.Label(root,text="Username",font='calibre 10 bold')

name_entry = tk.Entry(root,textvariable=name_var, font='calibre 10 normal')

passw_label = tk.Label(root,text = "Password",font="calibre 10 bold")

passw_entry = tk.Entry(root,textvariable=passw_var,font='calibre 10 normal',show="*")

sub_btn = tk.Button(root,text="Submit",command=submit)

name_lebel.grid(row = 0,column = 0)
name_entry.grid(row = 0,column = 1)
passw_label.grid(row = 1,column = 0)
passw_entry.grid(row = 1,column = 1)
sub_btn.grid(row = 2,column = 1)

root.mainloop()
'''
'''def panildrome(a):
    a = str(a)
    b = a[::-1]
    if b == a:
        return True
    else:
        return False


print(panildrome(10))
print(panildrome('aba'))'''

from tkinter import *
from PIL import ImageTk, Image
import random
import tkinter.messagebox as tmsg

app = Tk()
count = 0


def generate():
    global comp
    comp = random.randint(1, 101)


def basic():
    # setup the window size, title, logo
    app.title("Number Guessing game")
    app.geometry("500x500")
    app.minsize(500, 500)
    app.maxsize(500, 500)
    photo = PhotoImage(file="guess.png")
    app.iconphoto(False, photo)
    heading = Label(text='Number Guessing game', font="Helvicta 18 bold",
                    bg='black', fg='tomato', padx=170).pack()
    with open('score.txt', 'r') as f:
        hg = f.read()
    sc = Label(app, text=f'Previous score: {hg}', font='lucida 8 bold ').pack(
        anchor=E, padx=25, pady=5)

    # footer
    footer = Label(text='Developed by Siddharth Dyamgond', font="Helvicta 8 bold",
                   bg='black', fg='tomato', padx=153).pack(side=BOTTOM)

    # Setup Menu
    mymenu = Menu(app)
    filee = Menu(mymenu, tearoff=0)
    mymenu.add_cascade(label='Start', menu=filee)
    mymenu.add_cascade(label='Restart', command=restart)
    mymenu.add_command(label='About', command=call1)
    mymenu.add_command(label='Quit', command=quit)
    app.config(menu=mymenu)
    generate()


def result():
    global count
    number = userv.get()
    if number == '':
        tmsg.showerror('Error', "Please enter a value")
    else:
        n = int(number)
        count += 1
        if count == 10:
            a = tmsg.showinfo('Game over', 'You loose the Game!')
        elif comp == n:
            score = 11 - count
            a = tmsg.showinfo(
                'Win', f'You guess right number!\nYour score {score}')
            show.config(text='Winn!', fg='green')
            with open('score.txt', 'w') as f:
                f.write(str(score))
            generate()
            tmsg.showinfo('Next number', f'click ok to Guess another number')
        elif comp > n:
            show.config(text='Select greater number', fg='red')
        else:
            show.config(text='Select smaller number', fg='red')


def restart():
    tmsg.showerror('Reset', "Game reset!")
    generate()


def call1():
    str1 = 'This game is developed by XD\n\ncopyright@2021-22 '
    tmsg.showinfo('About', str1)


basic()

print(comp)
userv = StringVar()
user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT,
             borderwidth=2, font='Helvicta 18 bold').pack(pady=10)
i = Image.open('guess.png', mode='r')
img = ImageTk.PhotoImage(i)
l = Label(image=img).pack(pady=30)


submit = Button(app, text='Submit', command=result,
                font='Helvicta 18 bold', relief=FLAT).pack(pady=10)
show = Label(app, text='', font='Helvicta 12 bold')
show.pack(pady=10)
app.mainloop()