#Calculator program
from tkinter import *
from tkinter import ttk

#global variable
Expression = ""

#updating expression in entry box
def press(num):
    global Expression
    Expression = Expression + str(num)
    Equation.set(Expression)

#setting the equals function
def Equals():
    #using 'try' and 'except' statements to catch errors (eg. div by 0)
    try: 
        global Expression
        #Eval just evaluates the function
        Total = str(eval(Expression))
        Equation.set(Total)
        Expression = ""
    except:
        Equation.set(" ERROR ")
        Expression = ""

#clearing the entry field
def Clear():
    global Expression
    Expression = ""
    Equation.set("")

#GUI setup
if __name__ == '__main__':
    #creates window
    base = Tk()
    #background colour
    base.configure(background='#8BCAFF')
    #padding of frame - does not seem to influence 
    #ttk.Frame(base, padding=(10, 10, 12, 12))
    #naming the window
    base.title("Calculator.")
    #setting window size
    base.geometry()
    #
    Equation = StringVar()
    #text-box for showing the expression
    ExpressionField = Entry(base, textvariable=Equation)
    #placing the entry field
    ExpressionField.grid(columnspan=(3), ipadx=15)
    #buttons: 
    #'1'
    Button1 = Button(base, text='1', fg='black', bg='#CECECE', command=lambda: press(1), height=2, width=6)
    Button1.grid(row=4, column=0)
    #'2'
    Button2 = Button(base, text='2', fg='black', bg='#CECECE', command=lambda: press(2), height=2, width=6)
    Button2.grid(row=4, column=1)
    #'3'
    Button3 = Button(base, text='3', fg='black', bg='#CECECE', command=lambda: press(3), height=2, width=6)
    Button3.grid(row=4, column=2)
    #'+'
    Plus = Button(base, text='+', fg='black', bg='#CECECE', command=lambda: press('+'), height=2, width=6)
    Plus.grid(row=4, column=3)
    #'4'
    Button4 = Button(base, text='4', fg='black', bg='#CECECE', command=lambda: press(4), height=2, width=6)
    Button4.grid(row=5, column=0)
    #'5'
    Button5 = Button(base, text='5', fg='black', bg='#CECECE', command=lambda: press(5), height=2, width=6)
    Button5.grid(row=5, column=1)
    #'6'
    Button6 = Button(base, text='6', fg='black', bg='#CECECE', command=lambda: press(6), height=2, width=6)
    Button6.grid(row=5, column=2)
    #'-'
    Minus = Button(base, text='-', fg='black', bg='#CECECE', command=lambda: press('-'), height=2, width=6)
    Minus.grid(row=5, column=3)
    #'7'
    Button7 = Button(base, text='7', fg='black', bg='#CECECE', command=lambda: press(7), height=2, width=6)
    Button7.grid(row=6, column=0)
    #'8'
    Button8 = Button(base, text='8', fg='black', bg='#CECECE', command=lambda: press(8), height=2, width=6)
    Button8.grid(row=6, column=1)
    #'9'
    Button9 = Button(base, text='9', fg='black', bg='#CECECE', command=lambda: press(9), height=2, width=6)
    Button9.grid(row=6, column=2)
    #'*'
    Times = Button(base, text='*', fg='black', bg='#CECECE', command=lambda: press('*'), height=2, width=6)
    Times.grid(row=6, column=3)
    #'0'
    Zero = Button(base, text='0', fg='black', bg='#CECECE', command=lambda: press(0), height=2, width=6)
    Zero.grid(row=7, column=1)
    #'.'
    Decimal = Button(base, text='.', fg='black', bg='#CECECE', command=lambda: press('.'), height=2, width=6)
    Decimal.grid(row=8, column=3)
    #'/'
    Divide = Button(base, text='/', fg='black', bg='#CECECE', command=lambda: press('/'), height=2, width=6)
    Divide.grid(row=7, column=3)
    #Clear
    Clear = Button(base, text='Clear', fg='black', bg='#CECECE', command=Clear, height=2, width=6)
    Clear.grid(row=8, column=0)
    #Equal
    Equal = Button(base, text='=', fg='black', bg='#CECECE', command=Equals, height=2, width=6)
    Equal.grid(row=8, column=4)
    
    #start the GUI
    base.mainloop()