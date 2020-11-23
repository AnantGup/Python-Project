import turtle

wn = turtle.Screen()
wn.title("Pong by Anant")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shape("while")
paddle_a.penup()
paddle_a.goto(-350, 0)
# Paddle 2

# Game Loops
while True:
    wn.update()