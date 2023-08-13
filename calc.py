from tkinter import *



def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set("")


def btnEquals():
    global val
    result = str(eval(val))
    data.set(result)






root=Tk()

root.title("My Calci")
root.geometry("365x400+500+200")
val=""
data=StringVar()
display=Entry(root,bd=29,justify="right",textvariable=data,bg="powder blue" ,font=("ariel",20))
display.grid(row=0,columnspan=4)


btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7),bg="red",fg="white")
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8),bg="red",fg="white")
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9),bg="red",fg="white")
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('+'),bg="red",fg="white")
btn_add.grid(row=1,column=3)


btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4),bg="red",fg="white")
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5),bg="red",fg="white")
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6),bg="red",fg="white")
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'),bg="red",fg="white")
btn_sub.grid(row=2,column=3)


btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1),bg="red",fg="white")
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2),bg="red",fg="white")
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3),bg="red",fg="white")
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'),bg="red",fg="white")
btn_mul.grid(row=3,column=3)


btnc=Button(root,text="C",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnClear,bg="red",fg="white")
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0),bg="red",fg="white")
btn0.grid(row=4,column=1)
btn_div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('/'),bg="red",fg="white")
btn_div.grid(row=4,column=2)
btn_equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals,bg="red",fg="white")
btn_equal.grid(row=4,column=3)

root.mainloop()



