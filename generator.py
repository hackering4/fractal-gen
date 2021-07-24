# first import turtle
from turtle import *
# set the speed of the shape *optional*
speed(0)

# this is the function to create the l system


def lsystem(ax, rule, its):
    if its == 0:
        return ax
    for _ in range(its):
        new = ''
        for axiom in ax:
            if axiom in rule:
                new += rule[axiom]
            else:
                new += axiom
        # set the axiom to the new variable
        ax = new
    # return
    return ax


def draw(cmds, di, an):
    for cmd in cmds:
        # instructions
        if cmd == "A":
            forward(di)
        elif cmd == '-':
            left(an)
        elif cmd == "+":
            right(an)


rule = {"A": "A+A-AA"}


def main(rule, y_off, x_off):
    ins = lsystem('A', rule, 9)

    backward(-x_off)
    left(90)
    backward(-y_off)
    draw(ins, 0.7, 120)
    pensize(1)
    hideturtle()


# call the function
main(rule, 0, 0)
# initialize mainloop
mainloop()


# sources for parts of the code that i changed
# https://elc.github.io/posts/plotting-fractals-step-by-step-with-python/
# https://stackoverflow.com/questions/48113662/simple-l-system-in-python
# https://stackoverflow.com/questions/19159963/how-to-make-fractal-plants-with-l-system-in-turtle-graphics
