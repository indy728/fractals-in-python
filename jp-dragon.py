import turtle

t = turtle


def make_fractal(len, langle, rangle, iterations, axiom, t1, rep1, t2, rep2):
    state = axiom

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
    t.color('red', 'black')
    t.speed(0)
    t.begin_fill()

    for move in state:
        if move == 'F':
            t.forward(len)
        if move == 'R':
            t.right(langle)
        if move == 'L':
            t.left(rangle)

    t.end_fill()

    t.mainloop()


if __name__ == "__main__":
    # type in the string
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))
    # JP curve drawing
    axiom = 'FX'
    target1 = 'X'
    replace1 = 'XRYFR'
    target2 = 'Y'
    replace2 = 'LFXLY'

    make_fractal(myLen, 90, 90, iterations, axiom,
                 target1, replace1, target2, replace2)
