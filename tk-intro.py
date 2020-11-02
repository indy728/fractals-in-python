import tkinter

top = tkinter.Tk()
win = tkinter.Canvas(top, width=1000, height=1000)
win.pack()
win.master.title('cantor set')
# win.create_line(0, 0, 100, 100, fill='blue')
# win.create_polygon(100, 100, 100, 200, 200, 100, 200, 200, fill='red')
# win.create_oval(100, 100, 200, 200, fill='green')


def cantor_set(x, y, l):
    if l > 1:  # keep doing this while line is > 1px long
        win.create_line(x, y, x+l, y)  # draw horizontal line
        y = y + 50
        cantor_set(x, y, l/3)
        cantor_set(x + 2/3 * l, y, l/3)


cantor_set(50, 50, 900)

top.mainloop()
