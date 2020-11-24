import turtle as t
import random


def setTurtle(myTuple):
    t.up()
    t.setx(myTuple[0])
    t.sety(myTuple[1])
    t.setheading(myTuple[2])
    t.down()


def make_fractal(len, langle, rangle, iterations, axiom, t1, rep1, t2, rep2):
    state = axiom
    turtleStack = []

    # make the L system we want to process
    for i in range(iterations):
        nextState = ''
        for char in state:
            if char == t1:
                nextState += rep1
            elif char == t2:
                nextState += rep2
            else:
                nextState += char
        state = nextState

    t.down()
    t.color('green', 'black')
    t.begin_fill()

    for move in state:
        if move == '[':
            turtleStack.append((t.xcor(), t.ycor(), t.heading()))
        elif move == ']':
            setTurtle(turtleStack.pop())
        elif move == 'F':
            t.forward(len)
        elif move == '+':
            t.right(langle)
        elif move == '-':
            t.left(rangle)

    t.end_fill()

    t.mainloop()


if __name__ == "__main__":
    # type in the string
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))
    # myAlpha = int(input("Enter the angle: "))
    # JP curve drawing
    w = myLen * (2 ** iterations - 1)
    t.setup(width=w, height=w, startx=0, starty=0)
    setTurtle((-t.window_width()/2, t.window_height()/2, 0))
    t.setup(width=w*1.2, height=w*1.2, startx=0, starty=0)
    t.speed(0)

    axiom = 'L'
    target1 = 'L'
    replace1 = '+RF-LFL-FR+'
    target2 = 'R'
    replace2 = '-LF+RFR+FL-'

    # Hilbert curve
    make_fractal(myLen, 90, 90, iterations, axiom,
                 target1, replace1, target2, replace2)
