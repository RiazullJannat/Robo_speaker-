from tkinter import *
from PIL import ImageTk,Image
import random
import tkinter.messagebox as tmsg
app = Tk()
count = 0

# creating a function to generate a number.
def generate():
    global comp
    comp = random.randint(1,101)
    print(comp)
def restart():
    tmsg.showerror("Reset","Game reset!")
    generate()
def call1():
    str1 = 'This game is developed by Raizull Jannat.'
    tmsg.showinfo('About', str1)

def basic():
    # setup the window size, title, logo
    app.title("Number guessing game.")
    app.geometry("500x500")
    app.minsize(500,500)
    app.maxsize(500, 500)
    photo = PhotoImage(file='guess.png')
    app.iconphoto(False,photo)
    heading = Label(text = "Number guessing game", font= "Helvivata 18 bold",bg='black',fg='tomato', padx=170).pack()
    with open('score.txt', 'r') as f:
        hg = f.read()
    sc = Label(app, text = f'Previous score: {hg}', font='lucida 8 bold').pack(anchor=E,padx=25,pady=5)
    footer = Label(text= "Developed by Riazull Jannat",font="Helvicta 10 bold",bg='black',fg='tomato',padx=153).pack(side = BOTTOM)
    # setup Menu
    my_menu = Menu(app)
    filee = Menu(my_menu, tearoff= 0)
    my_menu.add_cascade(label="Start", menu=filee)
    my_menu.add_cascade(label='Restart',command=restart)
    my_menu.add_command(label='About',command=call1)
    my_menu.add_command(label='Quit',command=quit)
    app.config(menu=my_menu)
    generate()
def result():
    global count
    number = userv.get()
    if number == '':
        tmsg.showerror("Error", "Please enter a value.")
    else:
        n = int(number)
        count+=1
        if count == 10:
            a = tmsg.showinfo("Game over.","You loose the game!")
        elif comp == n:
            score = 11 - count
            a = tmsg.showinfo('Win',f'You guess right number!\nYour score {score}')
            show.config(text='Winn!', fg='green')
            with open('score.txt','w') as f:
                f.write(str(score))
            generate()
            tmsg.showinfo('Next number',f'click ok to guess another number.')
        elif comp>n:
            show.config(text='Select greater number',fg='red')
        else:
            show.config(text='Select smaller number',fg='red')




basic()


userv = StringVar()
user = Entry(app,textvariable=userv, justify=CENTER,relief=FLAT,borderwidth=2, font='Helvicta 18 bold').pack(pady=10)

i = Image.open('guess.png',mode='r')
img = ImageTk.PhotoImage(i)
l = Label(image=img).pack(pady=30,padx=30)

sub_button = Button(app,text='Submit',command=result).pack(pady=10)


show = Label(app,text='',font='Helvicta 12 bold')
show.pack(pady = 10)

app.mainloop()