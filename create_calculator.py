from tkinter import*
import math
from math import sqrt

window = Tk()
window.title('calculator')
window.iconbitmap('C:\\Users\\Shubham\\Documents\\GitHub\\Calculator\\Cal_icon.ico')

screen = Entry(window,bd=5,bg="#abbab1",justify= 'right',width = 45,borderwidth=7)
screen.grid(row=0,column=0,columnspan=4)

expression = 0

def btnclick(number):
    global expression
    if expression ==1:
        screen.delete(0,END)
        screen.insert(0,str(number))
        expression = 0
        return
    if number == 0:
        screenContent = screen.get()
        if screenContent == "":
            screen.insert(0,"")

        elif (screenContent[-1] == "+" or screenContent[-1] == "-" or screenContent[-1] == "*"  or screenContent[-1] == "%" ):
            screen.insert(0,"")

        else:
            current = screen.get()
            screen.delete(0,END)
            screen.insert(0,str(current)+str(number))


    else:

        current = screen.get()
        screen.delete(0,END)
        screen.insert(0,str(current)+str(number))


def symbol(number):
    global expression
    expression = 0
    screenContent = screen.get()
    if (screenContent[-1] == "+" or screenContent[-1] == "-" or screenContent[-1] == "*" or screenContent[-1] == "/" or screenContent[-1] == "%" or screenContent[-1] == "." ):
        new_content = str(screenContent[0:-1]) + str(number)
        Entry_len = len(screen.get())
        screen.delete(0,Entry_len)
        screen.insert(0,new_content)

    else:
        Entry_len = len(screen.get())
        screen.insert(Entry_len,str(number))
    
def point(number):
    global expression
    if expression == 1:
        screen.delete(0,END)
        screen.insert(0,"0.")
        expression = 0
        return

    screenContent = screen.get()
    i= -1
    length = 1
    Entry_len = len(screenContent)
    decimal = 0
    while (length <= Entry_len and screenContent[i] !="*" and screenContent[i] !="/" and screenContent[i] !="+" and screenContent[i] !="-" and screenContent[i] !="%"   ):  
        if screenContent[i] == ".":
            decimal = 1
            screen.insert(0,"")
            break
        i=i-1
        length = length+1
        
    if screenContent == (""):
        screen.insert(0,str("0."))


    elif (screenContent[-1] == "+" or screenContent[-1] == "-" or screenContent[-1] == "*" or screenContent[-1] == "/" or screenContent[-1] == "%" ): 
        screen.delete(0,END)
        screen.insert(0,str(screenContent)+str("0."))

    elif decimal != 1 and decimal == 0:
        current = screen.get()
        screen.delete(0,END)
        screen.insert(0,str(current)+str(number))


def btn_clear():
    screen.delete(0,END)

def Equal():
    global expression
    expression = 1
    screenContent = screen.get()
    if screenContent[-2] =="/" and screenContent[-1]=="0":
        screen.delete(0,END)
        screen.insert(0,"can't divide by zero")
        return

    if (screenContent[-1] == "+" or screenContent[-1] == "-" or screenContent[-1] == "*" or screenContent[-1] == "/" or screenContent[-1] == "%" or screenContent[-1] == "(" ):
        screen.delete(0,END)
        screen.insert(0,"Error")
        return


    result = eval(screen.get())
    screen.delete(0,END)
    screen.insert(0,str(result))

def backspace():
    lastdig = screen.get()[:-1]
    screen.delete(0,END)
    screen.insert(0,lastdig)


def Square_Root():
    global expression
    if expression == 1:
        screen.delete(0,END)
        screen.insert(0,"sqrt(")
        expression = 0
        return
    screenContent = screen.get()
    Entry_len = len(screenContent)
    if screenContent == "":
        screen.insert(0,"sqrt(")
 
    else:
        screen.insert(Entry_len,"sqrt(")


def get_last_num():
    screenContent = screen.get()
    Entry_len= len(screenContent)
    i= -1
    length = 1
    while (length<Entry_len and screenContent[-i] != "+" and screenContent[-i] != "-" and screenContent[-i] != "*" and screenContent[-i] != "/" and screenContent[-i] != "%"   ):
        i=i-1
        length=length+1
    temp = int(str(screenContent[i:Entry_len]))
    return temp

def square():
    global expression
    expression = 1
    num = get_last_num()
    screenContent = screen.get()
    Entry_len = len(screenContent)
    val = num**2
    num=str(num)
    length = len(num)
    screen.delete(Entry_len-length,END)
    screen.insert(Entry_len,val) 



def DivideByNumber():
    global expression 
    expression = 1
    num = get_last_num()
    screenContent = screen.get()
    Entry_len = len(screenContent)
    val = 1/(num)
    num=str(num)
    length = len(num)
    screen.delete(Entry_len-length,END)
    screen.insert(Entry_len,val)



one = Button(window,text = '1' ,width=8,height = 2, bd=4,fg = 'white',bg = '#333333',command = lambda:btnclick(1)) 
two = Button(window,text = '2' ,width=8,height = 2,  bd=4,fg = 'white',bg = "#333333",command =lambda:btnclick(2))
three = Button(window,text = '3' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(3))
four = Button(window,text = '4' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(4))
five = Button(window,text = '5' ,width=8,height = 2, bd=4, fg = 'white',bg ="#333333",command =lambda:btnclick(5))
six = Button(window,text = '6' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(6))
sevine = Button(window,text = '7' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(7))
eight = Button(window,text = '8' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(8))
nine = Button(window,text = '9' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(9))
zero = Button(window,text = '0' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:btnclick(0))

decimal = Button(window,text = '.' ,width=8,height = 2, bd=4, fg = 'white',bg = "#333333",command =lambda:point("."))

multyply = Button(window,text = '*' ,width=8,height = 2,bd=4, fg = 'black',bg = "#abbab1",command =lambda:symbol("*"))
devide = Button(window,text = '÷' ,width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:symbol("/"))
addition = Button(window,text = '+' ,width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:symbol("+"))
substrect = Button(window,text = '-' ,width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:symbol("-"))

clear = Button(window,text = 'AC' ,width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command = lambda:btn_clear())
equal = Button(window,text = '=' ,width=8,height = 2,bd=4, fg = 'black',bg = "#abbab1",command =lambda:Equal())
percentage = Button(window,text = '%',width = 8,height = 2,bd=4,fg = 'white',bg = "#333333",command =lambda:symbol("%"))

Backspace = Button(window,text = '⌫' ,width=8,height = 2, bd=4, fg ='black',bg = "#abbab1",command =lambda:backspace())
x_square = Button(window,text = "x²" ,width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:square())
squareRoot = Button(window,text ="√x",width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:Square_Root())
onebyx = Button(window,text ="1/x",width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:DivideByNumber())
open_bracket = Button(window,text ="(",width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:btnclick("("))
close_bracket = Button(window,text =")",width=8,height = 2, bd=4, fg = 'black',bg = "#abbab1",command =lambda:btnclick(")"))


open_bracket.grid(row = 1,column = 0)
close_bracket.grid(row = 1,column =1)
Backspace.grid(row = 1,column = 2)
clear.grid(row = 1,column=3)

squareRoot.grid(row = 2 , column = 0)
x_square.grid(row = 2,column = 1)   
onebyx.grid(row = 2,column = 2)
devide.grid(row =2,column =3)

sevine.grid(row = 3,column = 0)
eight.grid(row = 3,column = 1)
nine.grid(row = 3,column = 2)
multyply.grid(row = 3,column = 3)

four.grid(row=4,column = 0)
five.grid(row =4,column = 1 )
six.grid(row=4,column = 2)
substrect.grid(row = 4,column =3)

one.grid(row = 5,column = 0)
two.grid(row=5,column = 1)
three.grid(row = 5,column = 2)
addition.grid(row =5,column=3)

percentage.grid(row=6 ,column = 0)
zero.grid(row = 6,column = 1)
decimal.grid(row = 6,column = 2)
equal.grid(row =6,column = 3)

window.mainloop()
