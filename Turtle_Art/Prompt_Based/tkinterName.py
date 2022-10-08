from tkinter import *
from tkinter import messagebox
from turtle import *
win=Tk()
win.title('Writing any word')
win.geometry('300x250')
win.configure(background='cyan')
l=Label(win,text='Enter a word\nTo see it on computer',fg='midnight blue',bg='cyan',font=('Berlin Sans FB ',15))
l.grid(column=0,row=0)
t=Entry(win,width=12,bg='ivory2',font=('Georgia',15))
t.grid(column=0,row=1)
t.focus()
def func():
    n=t.get().upper()
    nlist=list(n)
    getscreen()
    title('Writing words on Computer Screen')
    bgcolor('pale turquoise')
    speed(-1)
    width(5)
    up()
    goto(-600,0)
    down()
    for i in range(len(nlist)):
        u=i+1
        if nlist[i]==' ':
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='A':
            color('dark violet')
            lt(75)
            fd(200)
            rt(150)
            fd(200)
            rt(180)
            fd(100)
            lt(78)
            fd(50)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(177)
            down()
        elif  nlist[i]=='B':
            color('navy')
            rt(-90)
            fd(200)
            rt(90)
            lt(180)
            circle(50,-180)
            rt(-180)
            circle(50,-180)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif  nlist[i]=='C':
            up()
            fd(100)
            down()
            color('lime green')
            rt(180)
            circle(-100,180)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='D':
            color('tomato')
            rt(-90)
            fd(200)
            rt(90)
            lt(180)
            circle(100,-180)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='E':
            color('royal blue')
            fd(100)
            rt(-180)
            fd(100)
            lt(-90)
            fd(200)
            rt(90)
            fd(100)
            rt(180)
            fd(100)
            rt(-90)
            fd(100)
            lt(90)
            fd(70)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='F':
            color('orange red')
            rt(-90)
            fd(200)
            rt(90)
            fd(100)
            backward(100)
            lt(-90)
            fd(100)
            rt(-90)
            fd(70)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='G':
            color('forest green')
            up()
            fd(100)
            down()
            rt(-90)
            fd(50)
            lt(90)
            fd(40)
            rt(-90)
            fd(50)
            rt(90)
            fd(60)
            rt(90)
            fd(200)
            rt(90)
            fd(100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='H':
            color('gold')
            rt(-90)
            fd(200)
            fd(-100)
            rt(90)
            fd(80)
            rt(-90)
            fd(100)
            fd(-100)
            rt(180)
            fd(100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(-90)
            down()
        elif nlist[i]=='I':
            color('hot pink')
            fd(100)
            fd(-50)
            lt(90)
            fd(200)
            lt(90)
            fd(50)
            rt(180)
            fd(100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='J':
            color('coral')
            up()
            rt(-90)
            fd(40)
            rt(180)
            down()
            circle(50,180)
            fd(150)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(90)
            down()
        elif nlist[i]=='K':
            color('indian red')
            lt(90)
            fd(200)
            fd(-100)
            rt(30)
            fd(110)
            fd(-110)
            rt(120)
            fd(110)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(-60)
            down()
        elif nlist[i]=='L':
            color('maroon')
            lt(90)
            fd(200)
            fd(-200)
            rt(90)
            fd(100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='M':
            color('light sea green')
            lt(90)
            fd(200)
            rt(150)
            fd(100)
            rt(-120)
            fd(100)
            rt(60)
            rt(90)
            fd(200)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(90)
            down()
        elif nlist[i]=='N':
            color('violet red')
            lt(90)
            fd(200)
            rt(160)
            fd(210)
            lt(160)
            fd(200)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(-90)
            down()
        elif nlist[i]=='O':
            color('medium spring green')
            fd(100)
            lt(90)
            fd(200)
            lt(90)
            fd(100)
            lt(90)
            fd(200)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(90)
            down()
        elif nlist[i]=='P':
            color('yellow green')
            lt(90)
            fd(200)
            rt(90)
            fd(80)
            rt(90)
            fd(70)
            rt(90)
            fd(80)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(-180)
            down()
        elif nlist[i]=='Q':
            color('steel blue')
            fd(100)
            lt(90)
            fd(200)
            lt(90)
            fd(100)
            lt(90)
            fd(200)
            lt(90)
            fd(30)
            lt(90)
            fd(30)
            rt(150)
            fd(60)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(60)
            down()
        elif nlist[i]=='R':
            color('orchid')
            lt(90)
            fd(200)
            rt(90)
            fd(80)
            rt(90)
            fd(80)
            rt(90)
            fd(80)
            rt(-120)
            fd(140)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(60)
            down()
        elif nlist[i]=='S':
            color('light coral')
            fd(100)
            lt(90)
            fd(100)
            lt(90)
            fd(100)
            rt(90)
            fd(100)
            rt(90)
            fd(100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            down()
        elif nlist[i]=='T':
            color('cornflower blue')
            up()
            fd(50)
            down()
            lt(90)
            fd(200)
            lt(90)
            fd(50)
            fd(-100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(180)
            down()
        elif nlist[i]=='U':
            color('goldenrod')
            up()
            lt(90)
            fd(45)
            rt(180)
            down()
            circle(45,180)
            fd(145)
            rt(180)
            fd(145)
            circle(-45,180)
            fd(145)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(-90)
            down()
        elif nlist[i]=='V':
            color('dark khaki')
            up()
            fd(45)
            down()
            lt(105)
            fd(205)
            fd(-205)
            rt(30)
            fd(205)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(-75)
            down()
        elif nlist[i]=='W':
            color('rosy brown')
            lt(90)
            fd(200)
            fd(-200)
            rt(30)
            fd(100)
            rt(120)
            fd(100)
            rt(-60)
            rt(-90)
            fd(200)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            lt(-90)
            down()
        elif nlist[i]=='X':
            color('dark violet')
            lt(60)
            fd(200)
            fd(-100)
            lt(60)
            fd(100)
            fd(-200)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(120)
            down()
        elif nlist[i]=='Y':
            color('orange red')
            up()
            fd(45)
            down()
            lt(90)
            fd(100)
            rt(30)
            fd(120)
            fd(-120)
            lt(60)
            fd(120)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(120)
            down()
        elif nlist[i]=='Z':
            color('dim grey')
            fd(100)
            fd(-100)
            lt(60)
            fd(200)
            lt(120)
            fd(100)
            up()
            goto(0,0)
            goto(-600+u*120,0)
            rt(180)
            down()
def main():
    if len(t.get())>11:
        messagebox.showerror('Disclaimer','The word limit for\ndisplaying words is 11 letters')
    else:
        reset()
        func()
        ht()
b=Button(win,text='Click Here',command=main,relief=RIDGE,bg='steel blue',fg='midnight blue',font=('CooperBlack',10))
b.grid(column=0,row=2)
c=Button(win,text='EXIT',command=win.destroy,relief=RIDGE,bg='orange',fg='blue',font=('CooperBlack',10))
c.grid(column=1,row=3)
win.mainloop()
