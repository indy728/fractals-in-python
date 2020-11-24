import turtle as t
import random
t.colormode(255)


def setTurtle(myTuple):
    t.up()
    t.setx(myTuple[0])
    t.sety(myTuple[1])
    t.setheading(myTuple[2])
    t.down()


def make_fractal(len, langle, rangle, iterations, axiom, t1, rep1, t2, rep2):
    state = axiom
    turtleStack = []
    v = 0

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
    t.begin_fill()

    for move in state:
        v += 1
        t.color((v % 255, 2*v % 255, 3 * v % 255))
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
        elif move == 'L':
            t.right(rangle)
            t.forward(len)
            t.left(langle)
            t.forward(len)
            t.left(langle)
            t.forward(len)
            t.right(rangle)
        elif move == 'R':
            t.left(langle)
            t.forward(len)
            t.right(rangle)
            t.forward(len)
            t.right(rangle)
            t.forward(len)
            t.left(langle)

    t.end_fill()

    t.mainloop()


if __name__ == "__main__":
    # type in the string
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))
    # myAlpha = int(input("Enter the angle: "))
    # JP curve drawing
    w = myLen * (2 ** (iterations + 1))
    t.setup(width=w, height=w, startx=0, starty=0)
    setTurtle((-t.window_width()/2, -t.window_height()/2, 0))
    t.setup(width=w*1.2, height=w*1.2, startx=0, starty=0)
    t.speed(0)

    axiom = 'R'
    target1 = 'L'
    replace1 = '+R-L-R+'
    target2 = 'R'
    replace2 = '-L+R+L-'

    # Sierpinski curve
    make_fractal(myLen, 60, 60, iterations, axiom,
                 target1, replace1, target2, replace2)
