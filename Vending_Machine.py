import tkinter as tk

from tkinter import Label,CENTER,PhotoImage,Button,Entry,BOTTOM,S,messagebox

root= tk.Tk() 

canvas1 = tk.Canvas(root, width = 950, height = 600)

canvas1.pack()

# title of the frame

root.title('Vending Machine')

root.iconbitmap("images/vm.ico")

canvas1.configure(bg='black')


label1 = tk.Label(root, text='Automatic Vending Machine',font="none 35 bold")

label1.config(anchor=CENTER)

canvas1.create_window(470, 30, window=label1)



label1 = tk.Label(root, text='Press on the machine to buy or CLOSE to quit the order',font="none 16 bold")

canvas1.create_window(480,80, window=label1)



# click on machine

def display():

    messagebox.showwarning("Warning", "Please insert the coins") 

    

cof = PhotoImage(file="images/vm.png")

b1 = tk.Button(root, image = cof,command=display,bg="black")

canvas1.create_window(260, 350, window=b1)



# function calculates the no. of the coin 1

root.counter1 = 0

def clicked1():

    root.counter1 += 1

    L['text'] = 'Coin 1 inserted: ' + str(root.counter1)

    alpha = tk.Label(root, text= root.counter1, bg='yellow',font="none 19 bold")

    canvas1.create_window(650, 380, window=alpha)

img = PhotoImage(file="images/one.png")

btn = tk.Button(root, image = img,command=clicked1,bg="black")

canvas1.create_window(650, 300, window = btn)



# function calculates the no. of the coin 2

root.counter2 = 0

def clicked2():

    root.counter2 += 1

    L['text'] = 'Coin 2 inserted: ' + str(root.counter2)

    alpha = tk.Label(root, text= root.counter2, bg='yellow',font="none 19 bold")

    canvas1.create_window(750, 380, window=alpha)

img2 = PhotoImage(file="images/two.png")

btn1 = tk.Button(root, image = img2,command=clicked2,bg="black")

canvas1.create_window(750, 300, window = btn1)



# function calculates the no. of the coin 5

root.counter5 = 0

def clicked5():

    root.counter5 += 1

    L['text'] = 'Coin 5 inserted: ' + str(root.counter5)

    alpha = tk.Label(root, text= root.counter5, bg='yellow',font="none 19 bold")

    canvas1.create_window(850, 380, window=alpha)

img3 = PhotoImage(file="images/five.png")

btn2 = tk.Button(root, image = img3,command=clicked5,bg="black")

canvas1.create_window(850, 300, window = btn2)



# when no coin is inserted

L = Label(root, text="No coins inserted yet.")

L.pack()



# function calculates the total amount of the money and states the condition i.e. 

# DFA that accepts set of all strings whose individual input symbol summation is greater than or equal to 5 

root.total = 0

def submit():

    root.total = root.counter1 + 2*root.counter2 + 5*root.counter5

    if root.total >= 5:

        Success = ("Your item is being dispensed.\n Thank you and have a nice day!!") # Item is finally bought

        label_success = tk.Label(root, text= Success, bg='yellow',font="none 18 bold")

        canvas1.create_window(750, 530, window=label_success)

    else:

        messagebox.showerror("Error", "Insufficient money. Please insert more coins !") # insufficient money as amount is less than 5



# click to buy the desired item

submit_btn = tk.Button(root, text='Buy the item', command=submit,font="none 16 bold")

canvas1.create_window(750, 450, window=submit_btn)



# click to close the application

button=Button(root,text='CLOSE',command=root.quit,font="none 13 bold")

button.pack(side="bottom")



root.mainloop()
