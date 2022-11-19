import turtle
t=turtle.Turtle()
t.shape(0)
t.speed(0)

def hexagon():
  for i in range(6):
    t.fd(100)
    t.lt(360/6)

for i in range(6):
  hexagon()
  t.fd(100)
  t.rt(60)