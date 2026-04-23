from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

a = Tk()
a.geometry("425x195")
a.title=("MagicSquareGame")

glid = [
    [0,0,0],
    [0,5,0],
    [0,0,0]
]

test = random.randint(1,4)
if test == 1:
    x = 0
    y = 0
elif test == 2:
    x = 2
    y = 0
elif test == 3:
    x = 0
    y = 2
elif test == 4:
    x = 2
    y = 2
num = [2,4,6,8]
glid[x][y] = random.choice(num)

button_style = {"width": 5, "padding": 5}

style = ttk.Style()
style.configure("Selected.TButton", background="#f7b2b2")
style.configure("Normal.TButton", background="#ffffff")

set_value = 0
test = str(x) + str(y)
print(test)

def d1c():
    global set_value,test
    if test != "00":
        set_value = 1
        d1.config(style="Selected.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Normal.TButton")
d1 = ttk.Button(a, text=str(glid[0][0]), **button_style, command=d1c)
d1.place(x=25, y=25, height=50)

def d2c():
    global set_value,test
    if test != "01":
        set_value = 2
        d1.config(style="Normal.TButton")
        d2.config(style="Selected.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Normal.TButton")
d2 = ttk.Button(a, text=str(glid[0][1]), **button_style, command=d2c)
d2.place(x=75, y=25, height=50)

def d3c():
    global set_value,test
    if test != "02":
        set_value = 3
        d1.config(style="Normal.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Selected.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Normal.TButton")
d3 = ttk.Button(a, text=str(glid[0][2]), **button_style, command=d3c)
d3.place(x=125, y=25, height=50)

def d4c():
    global set_value,test
    if test != "10":
        set_value = 4
        d1.config(style="Normal.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Selected.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Normal.TButton")
d4 = ttk.Button(a, text=str(glid[1][0]), **button_style, command=d4c)
d4.place(x=25, y=75, height=50)


d5 = ttk.Button(a, text=str(glid[1][1]), **button_style)
d5.place(x=75, y=75, height=50)

def d6c():
    global set_value,test
    if test != "12":
        set_value = 6
        d1.config(style="Normal.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Selected.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Normal.TButton")
d6 = ttk.Button(a, text=str(glid[1][2]), **button_style, command=d6c)
d6.place(x=125, y=75, height=50)

def d7c():
    global set_value,test
    if test != "20":
        set_value = 7
        d1.config(style="Normal.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Selected.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Normal.TButton")
d7 = ttk.Button(a, text=str(glid[2][0]), **button_style, command=d7c)
d7.place(x=25, y=125, height=50)

def d8c():
    global set_value,test
    if test != "21":
        set_value = 8
        d1.config(style="Normal.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Selected.TButton")
        d9.config(style="Normal.TButton")
d8 = ttk.Button(a, text=str(glid[2][1]), **button_style, command=d8c)
d8.place(x=75, y=125, height=50)

def d9c():
    global set_value,test
    if test != "22":
        set_value = 9
        d1.config(style="Normal.TButton")
        d2.config(style="Normal.TButton")
        d3.config(style="Normal.TButton")
        d4.config(style="Normal.TButton")
        d5.config(style="Normal.TButton")
        d6.config(style="Normal.TButton")
        d7.config(style="Normal.TButton")
        d8.config(style="Normal.TButton")
        d9.config(style="Selected.TButton")
d9 = ttk.Button(a, text=str(glid[2][2]), **button_style, command=d9c)
d9.place(x=125, y=125, height=50)

def fillin(x):
    global glid,set_value
    print("Fillin : Debug : {} : {}".format(glid,set_value))
    if set_value == 1:
        glid[0][0] = x
        d1.config(text=x)
    elif set_value == 2:
        glid[0][1] = x
        d2.config(text=x)
    elif set_value == 3:
        d3.config(text=x)
        glid[0][2] = x
    elif set_value == 4:
        d4.config(text=x)
        glid[1][0] = x
    elif set_value == 5:
        d5.config(text=x)
        glid[1][1] = x
    elif set_value == 6:
        d6.config(text=x)
        glid[1][2] = x
    elif set_value == 7:
        d7.config(text=x)
        glid[2][0] = x
    elif set_value == 8:
        d8.config(text=x)
        glid[2][1] = x
    elif set_value == 9:
        d9.config(text=x)
        glid[2][2] = x
    print("Filled : Debug : {} : {}".format(glid,set_value))

def c1c():
   fillin(1) 
c1 = ttk.Button(a, text="1", **button_style,command=c1c)
c1.place(x=200, y=25, height=50)
def c2c():
   fillin(2) 
c2 = ttk.Button(a, text="2", **button_style,command=c2c)
c2.place(x=200, y=75, height=50)
def c3c():
   fillin(3) 
c3 = ttk.Button(a, text="3", **button_style,command=c3c)
c3.place(x=200, y=125, height=50)

def c4c():
   fillin(4) 
c4 = ttk.Button(a, text="4", **button_style,command=c4c)
c4.place(x=250, y=25, height=50)
def c5c():
   fillin(5) 
c5 = ttk.Button(a, text="5", **button_style,command=c5c)
c5.place(x=250, y=75, height=50)
def c6c():
   fillin(6) 
c6 = ttk.Button(a, text="6", **button_style,command=c6c)
c6.place(x=250, y=125, height=50)

def c7c():
   fillin(7) 
c7 = ttk.Button(a, text="7", **button_style,command=c7c)
c7.place(x=300, y=25, height=50)
def c8c():
   fillin(8) 
c8 = ttk.Button(a, text="8", **button_style,command=c8c)
c8.place(x=300, y=75, height=50)
def c9c():
   fillin(9) 
c9 = ttk.Button(a, text="9", **button_style,command=c9c)
c9.place(x=300, y=125, height=50)
def c10c():
   fillin(0) 
c10 = ttk.Button(a, text="⌫", **button_style,command=c10c)
c10.place(x=350, y=25, height=50)

def c11c():
    global glid

    print("check : debug")
    print(glid)
    ans = 0

    if glid[0][0] + glid[0][1] + glid[0][2] == 15:
        ans += 1
        if glid[1][0] + glid[1][1] + glid[1][2] == 15:
            ans += 1
            if glid[2][0] + glid[2][1] + glid[2][2] == 15:
                ans += 1
    if glid[0][0] + glid[1][0] + glid[2][0] == 15:
        ans += 1
        if glid[0][1] + glid[1][1] + glid[2][1] == 15:
            ans += 1
            if glid[0][2] + glid[1][2] + glid[2][2] == 15:
                ans += 1
    if glid[0][0] + glid[1][1] + glid[2][2] == 15:
        ans += 1
        if glid[2][0] + glid[1][1] + glid[0][2] == 15:
            ans += 1
    print("Check : Debug : {}".format(ans))
    print("Ans : Debug : {} : {}".format(glid,set_value))
    if ans == 8:
        messagebox. showinfo(title="Result",message="This is a magic square!")
    else:
        messagebox. showinfo(title="Result",message="You are wrong!") 
        
c11 = ttk.Button(a, text="Ans", **button_style,command=c11c)
c11.place(x=350, y=75, height=100)

a.mainloop()