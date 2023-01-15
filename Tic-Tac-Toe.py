#Created By @KunnalDayaRoy


from tkinter import *
from tkinter import messagebox
import random as r

def button(frame):

    b=Button(frame,padx=2,bg="#6A5ACD",width=3,font=('Segoe Script',42,'bold'),relief="solid",bd=1)
    return b
def change_a():
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break


def reset():

    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"]=" "
            b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])

def check():
    for i in range(3):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
            messagebox.showinfo("Winner !","Player "+a)
            reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Winner","Player "+a)
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","Try Again")
        reset()


def click(row,col):
    b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
    check()
    change_a()
    label.config(text="Player "+a+"'s chance")

root=Tk()
root.geometry('375x525')
root.title("Tic-Tac-Toe")
a=r.choice(['O','X'])
colour={'O':"lavender",'X':"white"}                                                              #X AND 0's color
b=[[],[],[]]
for i in range(3):
    for j in range(3):
        b[i].append(button(root))
        b[i][j].config(cursor='hand2',command= lambda row=i,col=j:click(row,col))
        b[i][j].grid(row=i,column=j)
label=Label(text="Player " +a+"'s chance",font=('Comic Sans MS',17))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()
#%%
