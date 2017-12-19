import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100') #设置大小

#define label on window
# l = tk.Label(window, text='OMG! this is TK', bg='green',
#         font=('Arial, 12'), width=15, height=2)
# l.pack() #放置 label
# l.place()

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green',
        font=('Arial, 12'), width=15, height=2)
l.pack()

#define button
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15, height=2,
        command=hit_me)
b.pack()


window.mainloop()
