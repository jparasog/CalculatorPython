from tkinter import*
window=Tk()
import math

window.title("Calculator")
window.geometry('400x244')
var=StringVar()
result= ""

def press(num):
    global result
    result=result + str(num)
    var.set(result)
def clear():
    global result
    result=""
    var.set("")
def equalpress():
    try:
        global result
        total=str(eval(result))
        var.set(total)
        result=""
    except:
        var.set("Error")
        result= ""

txt=Entry(window,width=30,font=("Arial",15),text=var)
txt.grid(column=0,row=0,columnspan=4)

btn1=Button(window,text="clear",width=10,font=("Arial",12),command= clear)
btn1.grid(column=0,row=1)
btn2=Button(window,text="(",width=10,font=("Arial",12),command=lambda: press("("))
btn2.grid(column=1,row=1)
btn3=Button(window,text=")",width=10,font=("Arial",12),command=lambda: press(")"))
btn3.grid(column=2,row=1)
btn4=Button(window,text="/",width=10,font=("Arial",12),command=lambda: press("/"))
btn4.grid(column=3,row=1)

btn5=Button(window,text="7",width=10,font=("Arial",12),command=lambda: press(7))
btn5.grid(column=0,row=2)
btn6=Button(window,text="8",width=10,font=("Arial",12),command=lambda: press(8))
btn6.grid(column=1,row=2)
btn7=Button(window,text="9",width=10,font=("Arial",12),command=lambda: press(9))
btn7.grid(column=2,row=2)
btn8=Button(window,text="*",width=10,font=("Arial",12),command=lambda: press("*"))
btn8.grid(column=3,row=2)

btn9=Button(window,text="4",width=10,font=("Arial",12),command=lambda: press(4))
btn9.grid(column=0,row=3)
btn10=Button(window,text="5",width=10,font=("Arial",12),command=lambda: press(5))
btn10.grid(column=1,row=3)
btn11=Button(window,text="6",width=10,font=("Arial",12),command=lambda: press(6))
btn11.grid(column=2,row=3)
btn12=Button(window,text="-",width=10,font=("Arial",12),command=lambda: press("-"))
btn12.grid(column=3,row=3)

btn13=Button(window,text="1",width=10,font=("Arial",12),command=lambda: press(1))
btn13.grid(column=0,row=4)
btn14=Button(window,text="2",width=10,font=("Arial",12),command=lambda: press(2))
btn14.grid(column=1,row=4)
btn15=Button(window,text="3",width=10,font=("Arial",12),command=lambda: press(3))
btn15.grid(column=2,row=4)
btn16=Button(window,text="+",width=10,font=("Arial",12),command=lambda: press("+"))
btn16.grid(column=3,row=4)

btn13=Button(window,text="0",width=10,font=("Arial",12),command=lambda: press(0))
btn13.grid(column=0,row=5)
btn14=Button(window,text="^",width=10,font=("Arial",12),command=lambda: press("**"))
btn14.grid(column=1,row=5)
btn15=Button(window,text=",",width=10,font=("Arial",12),command=lambda: press("."))
btn15.grid(column=2,row=5)
btn16=Button(window,text="=",width=10,font=("Arial",12),command=equalpress)
btn16.grid(column=3,row=5)

btn17=Button(window,text="√",width=10,font=("Arial",12),command=lambda: press("math. sqrt("))
btn17.grid(column=0,row=6)
btn18=Button(window,text="!",width=10,font=("Arial",12),command=lambda: press("math.factorial("))
btn18.grid(column=1,row=6)

window.mainloop()