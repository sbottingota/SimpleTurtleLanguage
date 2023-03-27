import sys

import turtle as t
import time

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

    "O": t.done
}

#variable = {}
#constants = {}

def prepArgs(args):
    output = []
    for arg in args:
        try:
            output.append(int(arg))
        except:
            output.append(arg)

    return output

def parseLine(line):
    if line.strip() == "":
        return

    action = line.strip()[0]

    assert action in functions, f"Unknown Action: {action}"

    args = line.strip().split(" ")[1:]
    args = prepArgs(args)

    functions[action](*args)

def parseFile(path):
    with open(path, "r") as f:
        for line in f.readlines():
            parseLine(line)

for argv in sys.argv[1:]:
    parseFile(argv)
