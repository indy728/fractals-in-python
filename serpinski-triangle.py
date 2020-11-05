import turtle

t = turtle.Turtle()


def serpinski(sideLen, level):
    angle = 60

    if level == 0:
        for i in range(3):
            t.fd(sideLen)
            t.left(180 - angle)
    else:
        serpinski(sideLen / 2, level - 1)
        t.fd(sideLen/2)
        serpinski(sideLen/2, level - 1)
        t.bk(sideLen/2)
        t.left(angle)
        t.fd(sideLen/2)
        t.right(angle)
        serpinski(sideLen/2, level - 1)
        t.left(angle)
        t.bk(sideLen/2)
        t.right(angle)


if __name__ == "__main__":
    # type in the string
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the length of a side: "))
    # serpinski
    t.shape('turtle')

    t.up()
    t.speed(0)
    t.setpos(-myLen/2, -myLen/2)
    t.down()
    t.color("black", "black")
    t.begin_fill()
    serpinski(myLen, iterations)
    t.end_fill()
    turtle.mainloop()
