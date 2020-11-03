import turtle

t = turtle

t.screensize(1000, 1000)
t.pensize(6)
j = 1

# for i in range(10):
#     j = i + j
#     t.speed(j)
#     t.color(1, i/10, 0)
#     t.circle(100)
#     t.right(360/10)

color = ['red', 'blue', 'green', 'yellow', 'pink']
t.bgcolor('black')
t.speed(0)

for x in range(100):
    t.pencolor(color[x % 5])
    t.forward(x)
    # t.left(60)  # 1/6 of 360 for hexagon
    t.left(58)  # > 1/6 of 360 for hexagon for spiral offset

t.mainloop()
