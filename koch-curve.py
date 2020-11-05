import turtle

t = turtle

iterations = input("Enter the number of generations: ")  # type in the string
iterations = int(iterations)
startingLen = 500  # length of gen0 line

# pick up the pen and move the turtle to the left
t.up()
t.setpos(-startingLen*1/2, startingLen*1/4)

t.speed(0)

# koch = 'F'
koch = 'FRFRF'  # koch snowflake axiom

# make the final L system based on number of iterations

for i in range(iterations):
    # replace any line in the system with a line that has a triangle
    koch = koch.replace('F', 'FLFRFLF')

t.down()
# draw the line in red, fill in enclosed spaces in black
t.color('red', 'black')
t.begin_fill()

for move in koch:
    if move == 'F':
        t.forward(startingLen / (3 ** iterations - 1))
    if move == 'R':
        t.right(120)
    if move == 'L':
        t.left(60)

t.end_fill()

t.mainloop()
