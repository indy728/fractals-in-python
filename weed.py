import turtle
import random

t = turtle


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
        elif move == 'R':
            t.right(random.randint(langle - 5, langle + 5))
        elif move == 'L':
            t.left(random.randint(rangle - 5, rangle + 5))

    t.end_fill()

    t.mainloop()


if __name__ == "__main__":
    # type in the string
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))
    myAlpha = int(input("Enter the angle: "))
    plantType = input("Enter type of plant: ")
    # JP curve drawing
    plantTypes = {'weed': 'F[RF]F[LF]F',
                  'tree': 'F[RF]F[LF]', 'pitchfork': 'FFR[RFLFLF]L[LFRFRF]'}
    axiom = 'F'
    target1 = 'F'
    # replace1 =
    target2 = ''
    replace2 = ''
    t.speed(0)
    turtle.bgcolor('black')
    setTurtle((0, -250, 90))

# simple plant
    make_fractal(myLen, myAlpha, myAlpha, iterations, axiom,
                 target1, plantTypes[plantType], target2, replace2)
