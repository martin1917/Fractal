import turtle
import tkinter

length = 30

def modeling(count_repeat):
    state = "F"
    for _ in range(count_repeat):
        state = state.replace("F", "F-F+F+FF-F-F+F")
    return state

def draw_fractal(raw_turtle, state):
    for el in state:
        if el == "+":
            raw_turtle.right(90)
        if el == "-":
            raw_turtle.left(90)
        if el == "F":
            raw_turtle.forward(length)

root = tkinter.Tk()
root.geometry('1500x1000')
cv = turtle.ScrolledCanvas(root, width=1500, height=1000)
cv.pack()
screen = turtle.TurtleScreen(cv)
screen.screensize(9999,9999)
t = turtle.RawTurtle(screen)
t.speed(100)
t.hideturtle()
draw_fractal(t, modeling(3))
root.mainloop()