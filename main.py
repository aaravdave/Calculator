def update(value):
    if value == '=':
        try:
            expr = list(text.get())
            for i in range(len(expr)):
                special_char = '× ÷ ² ³ ^ √ π EE e '.split()
                special_repl = '* / **2 ** ** sprt 3.14159 *10** 2.71828'.split()
                if expr[i] in special_char:
                    expr[i] = special_repl[special_char.index(expr[i])]
            text.set(eval(''.join(expr)))
        except Exception:
            text.set('Error')
    elif value == '\u232B':
        text.set(text.get()[:-1])
    elif value == 'C':
        text.set('')
    elif value == 'x²':
        text.set(text.get() + '²')
    elif value == 'x³':
        text.set(text.get() + '³')
    elif value == 'eˣ':
        text.set(text.get() + 'e^')
    else:
        text.set(text.get() + str(value))


def preferences(event):
    options = Tk()
    options.geometry('450x300')
    options.title('Preferences')

    apply = Button(options, command=options.destroy, text='Apply', bg='#1fdd48', fg='white')
    apply.place(x=125, y=250, width=225, height=50)

    options.mainloop()


from tkinter import *
import themes
# import math

window = Tk()
window.geometry('450x300')
window.title('Calculator')

window.bind('<Command-o>', preferences)

calculator_color_theme = themes.default

x, y = 0, 50
limit, original_x = x + 75 * 6, x
double = '0C'

text = StringVar()
label = Label(window, textvariable=text)
label.place(x=x, y=y - 50, width=limit - x, height=50)

buttons = ['(', ')', 'C', '%', '÷',
           'tan', 'π', 7, 8, 9, '×',
           'x³', 'xʸ', 4, 5, 6, '-',
           '#', 'EE', 1, 2, 3, '+',
           'eˣ', 'e', '0', '.', '=']

for item in buttons:
    if str(item) in '1234567890.C':
        background, foreground = calculator_color_theme[0]
    elif str(item) in '+-×÷=':
        background, foreground = calculator_color_theme[1]
    else:
        background, foreground = calculator_color_theme[2]

    button = Button(window, text=item, highlightbackground=background, fg=foreground, command=lambda i=item: update(i))
    button.config(highlightthickness=0)
    button.place(x=x, y=y, width=150 if str(item) in double else 75, height=50)

    x += 150 if str(item) in double else 75
    if x == limit:
        x = original_x
        y += 50

window.mainloop()
