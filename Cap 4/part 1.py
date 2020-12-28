## desenho
import turtle
bob = turtle.Turtle()
print(bob)
c = k = 0
for i in range(0, 1000):
    c = c + 3
    k = k + 1
    bob.fd(c)
    bob.lt(k)


