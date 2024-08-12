import tkinter as tk

root = tk.Tk()
root.title('Calculator')

num1_printing = True
num2_printing = False

num1_list = []
num2_list = []
main_num1 = 0
main_num2 = 0

def num_switch1():
    global num1_printing
    global num2_printing
    num1_printing = True
    num2_printing = False

def num_switch2():
    global num1_printing
    global num2_printing
    num1_printing = False
    num2_printing = True

def num_1_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('1')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('1')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_2_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('2')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('2')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_3_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('3')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('3')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_4_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('4')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('4')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_5_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('5')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('5')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_6_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('6')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('6')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_7_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('7')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('7')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_8_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('8')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('8')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_9_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('9')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('9')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def num_0_app():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.append('0')
        main_num1 = int(''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.append('0')
        main_num2 = int(''.join(num2_list))
        num2_lab.config(text=main_num2)

def cleaner():
    global main_num1
    global main_num2
    if num1_printing is True:
        num1_list.clear()
        num1_list.append('0')
        main_num1 = (''.join(num1_list))
        num1_lab.config(text=main_num1)
    elif num2_printing is True:
        num2_list.clear()
        num2_list.append('0')
        main_num2 = (''.join(num2_list))
        num2_lab.config(text=main_num2)

def plus_equal():
    global main_num1
    global main_num2
    equal_lab.config(text=f'Result: {main_num1 + main_num2}')

def minus_equal():
    global main_num1
    global main_num2
    equal_lab.config(text=f'Result: {main_num1 - main_num2}')

def multiply_equal():
    global main_num1
    global main_num2
    equal_lab.config(text=f'Result: {main_num1 * main_num2}')

def division_equal():
    global main_num1
    global main_num2
    equal_lab.config(text=f'Result: {main_num1 / main_num2}')

num2_lab = tk.Label(text=main_num2)
num1_lab = tk.Label(text=main_num1)

equal_lab = tk.Label(text='Result: ')

b_1 = tk.Button(text='1',width=6, height=2, command=num_1_app)
b_2 = tk.Button(text='2',width=6, height=2, command=num_2_app)
b_3 = tk.Button(text='3',width=6, height=2, command=num_3_app)

b_4 = tk.Button(text='4',width=6, height=2, command=num_4_app)
b_5 = tk.Button(text='5',width=6, height=2, command=num_5_app)
b_6 = tk.Button(text='6',width=6, height=2, command=num_6_app)

b_7 = tk.Button(text='7',width=6, height=2, command=num_7_app)
b_8 = tk.Button(text='8',width=6, height=2, command=num_8_app)
b_9 = tk.Button(text='9',width=6, height=2, command=num_9_app)

b_0 = tk.Button(text='0',width=6, height=2, command=num_0_app)

cleaner_button = tk.Button(text='Clean', width=6, height=2, command=cleaner)

plus_button = tk.Button(text='+', width=12, height=2, command=plus_equal)
minus_button = tk.Button(text='-', width=12, height=2, command=minus_equal)
multiply_button = tk.Button(text='x', width=12, height=2, command=multiply_equal)
division_button = tk.Button(text='/', width=12, height=2, command=division_equal)

switch_num1 = tk.Button(text='Num 1', width=12, height=2, command=num_switch1)
switch_num2 = tk.Button(text='Num 2', width=12, height=2, command=num_switch2)

num1_lab.grid(row=0, column=2)
num2_lab.grid(row=1, column=2)

switch_num1.grid(row=0, column=5)
switch_num2.grid(row=1, column=5)

b_1.grid(row=2, column=1)
b_2.grid(row=2, column=2)
b_3.grid(row=2, column=3)

b_4.grid(row=3, column=1)
b_5.grid(row=3, column=2)
b_6.grid(row=3, column=3)

b_7.grid(row=4, column=1)
b_8.grid(row=4, column=2)
b_9.grid(row=4, column=3)

b_0.grid(row=5, column=2)

minus_button.grid(row=2, column=5)
plus_button.grid(row=3, column=5)
multiply_button.grid(row=4, column=5)
division_button.grid(row=5, column=5)

equal_lab.grid(row=6, column=4)
cleaner_button.grid(row=5, column=1)

root.mainloop()