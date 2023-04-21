import sys

import turtle
import time

t = turtle.Turtle()

functions = {
    "F": t.forward,
    "B": t.backward,

    "R": t.right,
    "L": t.left,
    "H": t.seth,

    "C": t.circle,

    "U": t.penup,
    "D": t.pendown,

    "W": time.sleep,

    "T": t.shape,
    "V": t.speed,

    "P": t.pensize,
    "S": t.shapesize,

    "O": turtle.done
}


def prep_args(args):
    output = []
    for arg in args:
        try:
            output.append(int(arg))
        except:
            output.append(arg)

    return output


def parse_line(line):
    if line.strip() == "":
        return

    action = line.strip()[0]

    assert action in functions, f"Unknown Action: {action}"

    args = line.strip().split(" ")[1:]
    args = prep_args(args)

    functions[action](*args)


def parse_file(path):
    with open(path, "r") as f:
        for line in f.readlines():
            parse_line(line)


for argv in sys.argv[1:]:
    parse_file(argv)
