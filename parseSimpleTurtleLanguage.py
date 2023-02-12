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

    "W": time.sleep
}

#variable = {}
#constants = {}

def parseLine(line):
    if line.strip() == "":
        return

    action = line.strip()[0]

    assert action in functions, "Unknown Action: " + action

    args = [int(value) for value in line.split(" ")[1:]]

    functions[action](*args)

def parseFile(path):
    with open(path, "r") as f:
        for line in f.readlines():
            parseLine(line)

parseFile("demoTurtleFile")
