from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')  

def get_operator(op):
    global first_number,operator
    
    first_number = int(result_label['text'])
    operator = op
    clear()
    return first_number,operator
def get_result():
    global first_number,second_number,operator
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number+second_number))
         
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
         
    elif operator == '*':
        result_label.config(text=str(first_number*second_number))
         
    elif operator:
        if second_number == 0:
            result_label['text'] = 'Error'
        else:
            result_label.config(text=str(round(first_number/second_number,2)))
         
def changeOnHover(*buttons, colorOnHover='#323232', colorOnLeave='#3B3B3B'):
    for btn in buttons:
        btn.bind("<Enter>", func=lambda e, hover=colorOnHover: e.widget.config(background=hover))
        btn.bind("<Leave>", func=lambda e, leave=colorOnLeave: e.widget.config(background=leave))
    
root = Tk()

root.title('Calculator')
app_icon = PhotoImage(file='myicon.ico')
root.iconphoto(True,app_icon)
root.geometry('272x374')
root.resizable(0,0)
root.configure(background='#202020')

result_label = Label(root,text='',bg='#202020',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='e')
result_label.config(font=('verdana',30,'bold'))

btn7 = Button(root,text='7',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(7),bd=1,relief=SOLID)
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))
 
btn8 = Button(root,text='8',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(8),bd=1,relief=SOLID)
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))
 
btn9 = Button(root,text='9',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(9),bd=1,relief=SOLID)
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))
 
btn_add = Button(root,text='+',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_operator('+'),bd=1,relief=SOLID)
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))
 
btn4 = Button(root,text='4',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(4),bd=1,relief=SOLID)
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))
 
btn5 = Button(root,text='5',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(5),bd=1,relief=SOLID)
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))
 
btn6 = Button(root,text='6',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(6),bd=1,relief=SOLID)
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))
 
btn_sub = Button(root,text='−',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_operator('-'),bd=1,relief=SOLID)
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))
 
btn1 = Button(root,text='1',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(1),bd=1,relief=SOLID)
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))
 
btn2 = Button(root,text='2',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(2),bd=1,relief=SOLID)
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))
 
btn3 = Button(root,text='3',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(3),bd=1,relief=SOLID)
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))
 
btn_mul = Button(root,text='×',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_operator('*'),bd=1,relief=SOLID)
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))
 
btn_clr = Button(root,text='C',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:clear(),bd=1,relief=SOLID)
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14))
 
btn0 = Button(root,text='0',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_digit(0),bd=1,relief=SOLID)
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))
 
btn_equals = Button(root,text='=',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_result(),bd=1,relief=SOLID)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('verdana',14))
 
btn_div = Button(root,text='÷',bg='#3B3B3B',fg='white',width=5,height=2,command=lambda:get_operator('/'),bd=1,relief=SOLID)
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))
 
changeOnHover(btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn_add,btn_sub,btn_mul,btn_div,btn_clr,btn_equals) 


root.mainloop()