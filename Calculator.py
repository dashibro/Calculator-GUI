import tkinter
root = tkinter.Tk()
root.title("Calculator")
root.geometry("300x292")
root.configure(background="black")
root.wm_iconbitmap("calculator.ico")

def evaluate():
    if not calculate.get():
        calculate.set("Error")
        return

    elif calculate.get()[0] in ["+","X","%"]:
        calculate.set("Error")
        return

    elif calculate.get() [-1] in ["+","-","X","%"]:
        calculate.set("Error") 
        return
    try:
        expression = calculate.get()
        expression = expression.replace("X", "*")
        result = eval(expression)
        calculate.set(str(result))
    except Exception:
        calculate.set("Error")
            

def button_click(value):
    current = calculate.get()
    calculate.set(current + value)

def clear():
    calculate.set("")
# Screen
calculate = tkinter.StringVar()
tkinter.Entry(root,width=25,font="Arial 15 bold",bg="black",fg="white",textvariable=calculate).grid(row=0,column=0,columnspan=4,padx=5,pady=5)

# Black line
canvas = tkinter.Canvas(root, width=300, height=2, bg="black", highlightthickness=0)
canvas.grid(row=1,column=0,columnspan=4)


# Buttons
tkinter.Button(root,text="7",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("7")).grid(row=2,column=0)
tkinter.Button(root,text="8",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("8")).grid(row=2,column=1)
tkinter.Button(root,text="9",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("9")).grid(row=2,column=2)
tkinter.Button(root,text="AC",width=5,height=2,bg="red",fg="white",font="courier 16 bold",command=clear).grid(row=2,column=3)
tkinter.Button(root,text="4",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("4")).grid(row=3,column=0)
tkinter.Button(root,text="5",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("5")).grid(row=3,column=1)
tkinter.Button(root,text="6",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("6")).grid(row=3,column=2)
tkinter.Button(root,text="%",width=5,height=2,bg="orange",fg="white",font="courier 16 bold",command=lambda: button_click("%")).grid(row=3,column=3)
tkinter.Button(root,text="1",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("1")).grid(row=4,column=0)
tkinter.Button(root,text="2",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("2")).grid(row=4,column=1)
tkinter.Button(root,text="3",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("3")).grid(row=4,column=2)
tkinter.Button(root,text="X",width=5,height=2,bg="orange",fg="white",font="courier 16 bold",command=lambda: button_click("X")).grid(row=4,column=3)
tkinter.Button(root,text="0",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("0")).grid(row=5,column=0)
tkinter.Button(root,text="+",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=lambda: button_click("+")).grid(row=5,column=1)
tkinter.Button(root,text="=",width=5,height=2,bg="black",fg="white",font="courier 16 bold",command=evaluate).grid(row=5,column=2)
tkinter.Button(root,text="-",width=5,height=2,bg="orange",fg="white",font="courier 16 bold",command=lambda: button_click("-")).grid(row=5,column=3)

root.mainloop()