from tkinter import *
from math import sin,cos,tan,log

operators=['7','8','9','C','AC','sin','4','5','6','+','/','cos','1','2','3','-','*','tan','0','.','=','(',')','ln']
evaluate=''

def add(operator):

    global evaluate,expression

    if operator is 'C':
        evaluate=evaluate[:-1]
        expression.delete(0,END)
        expression.insert(0, evaluate)

    elif operator is 'AC':
        evaluate=''
        expression.delete(0, END)
        expression.insert(0, evaluate)

    elif operator is '=':
        expression.delete(0, END)

        try:
            eval(evaluate)
            expression.insert(0, eval(evaluate))

        except :
            evaluate='Error'
            expression.insert(0, evaluate)

    else:

        if operator is (('sin')or('cos')or('tan')):
            evaluate=evaluate+operator+'('

        elif operator is 'ln':
            evaluate=evaluate+'log'+'('

        else:
            evaluate = evaluate + operator

        expression.delete(0,END)
        expression.insert(0, evaluate)

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
expression.place(x=80,y=8)


'''----------------------------------------------- Button Bottom to Top --------------------------------------------'''
k=0

for y in range(1,5):

    for x in range(0,6):

        i = operators[k]

        if x<3 :

            button = Button(panel,text=operators[k],command=lambda i=i:add(i))
            button.configure(bg='grey80', fg='grey10', borderwidth=0, width=3, height=1,
                          font=('courier new', '25', 'bold'))
            button.place(x=68*x,y=63*y)

        elif x is 5 :
            button = Button(panel, text=operators[k], command=lambda i=i: add(i))
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

