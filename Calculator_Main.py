from tkinter import *
from math import sin,cos,tan,log

# the collection of operators and digits
# entered in a Specific Order as they appear in Layout of Calculator
operators=['7','8','9','C','AC','sin','4','5','6','+','/','cos','1','2','3','-','*','tan','0','.','=','(',')','ln']
evaluate=''

# function bounded with buttons adds operators to "evaluate" string
def add(operator):

    global evaluate,expression

    if operator is 'C':
        evaluate=evaluate[:-1]                  ## removes the last entered character in 'evaluate' string
        expression.delete(0,END)
        expression.insert(0, evaluate)

    elif operator is 'AC':
        evaluate=''                             ## reassignes String hence cleanes all data
        expression.delete(0, END)               # Clears ENTRY and deletes all output
        expression.insert(0, evaluate)          # gives the new Output in ENTRY

    elif operator is '=':
        expression.delete(0, END)

        try:
            eval(evaluate)                # try is used to first check if eval() can operate over evaluate string
            expression.insert(0, eval(evaluate))

        except :                            # exception is handled with message on screen
            expression.insert(0, 'Error')

    else:

        if operator is (('sin')or('cos')or('tan')):
            evaluate=evaluate+operator+'('             # bracket is pre added in case of Trigonometric Functions

        elif operator is 'ln':
            evaluate=evaluate+'log'+'('                # similarly bracket added for ln function

        else:
            evaluate = evaluate + operator

        expression.delete(0,END)                        # Clears ENTRY and deletes all output
        expression.insert(0, evaluate)                  # gives the new Output in ENTRY

'''-----------------------------------------------------------------------------------------------------------------'''
def keyBoard(event):
                                                        # Keyboard Input
    global evaluate, expression,panel

    if event.char is not '=':
        evaluate = evaluate + event.char                # event.char carries info about the key pressed on keyboard

    else:
        expression.delete(0, END)
        expression.insert(0, eval(evaluate))
        evaluate = ''

def solver(event):                                      # as soon as ENTER key is hit from keyboard
                                                        # it gives output in ENTRY
    global evaluate, expression

    try:
        eval(evaluate)
        expression.delete(0, END)
        expression.insert(0, eval(evaluate))

    except:
        expression.delete(0, END)
        expression.insert(0, 'Error')

    finally:
        evaluate=''

''' ---------------------------------------  MAIN CALCULATOR SCREEN LAYOUT -----------------------------------------'''
panel=Tk()
panel.title('Py Calc')
panel.wm_minsize(405,313)
panel.wm_maxsize(405,313)
panel.iconbitmap('icon_main.ico')
panel.configure(bg='grey10')

'''------------------------------------------------Input Panel ------------------------------------------------------'''
expression=Entry(panel)
expression.configure(bg='grey10',fg='white',font=('courier new','15'),borderwidth=0,justify=RIGHT)
expression.bind('<Key>',keyBoard)           # binding ENTRY to KeyBoard Input
expression.bind('<Return>',solver)          # binding ENTRY to ENTER KEY OPERATION
expression.place(x=130,y=8)

'''----------------------------------------------- Button Top to Bottom ---------------------------------------------'''
k=0

'''Creates layout of the Calculator'''

for y in range(1,5):

    for x in range(0,6):

        i = operators[k]

        if x<3 :

            button = Button(panel,text=operators[k],command=lambda i=i:add(i))
            button.configure(bg='grey80', fg='grey10', borderwidth=0, width=3, height=1,
                          font=('courier new', '25', 'bold'))
            button.place(x=68*x,y=63*y)

        elif x is 5 :
            button = Button(panel, text=operators[k],command=lambda i=i:add(i))
            button.configure(bg='royalblue3', fg='white', borderwidth=0, width=3, height=1,
                             font=('courier new', '25','bold'))
            button.place(x=68 * x, y=63 * y)

        else :
            button = Button(panel,text=operators[k],command=lambda i=i:add(i))
            button.configure(bg='darkorange2', fg='white', borderwidth=0, width=3, height=1,
                             font=('courier new', '25', 'bold'))
            button.place(x=68*x,y=63*y)

        k=k+1
'''------------------------------------------------------------------------------------------------------------------'''

panel.mainloop()

