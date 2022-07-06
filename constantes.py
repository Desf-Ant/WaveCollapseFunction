from enum import Enum
from turtle import right

class Constantes(Enum):
    BLANCK  = 0
    UP      = 1
    LEFT    = 2
    RIGHT   = 3
    DOWN    = 4

    OUTPUTS = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 0],
        [0, 1, 1, 1]
    ]

    CONST_ORIENTATIONS = {
        0: BLANCK,
        1: UP,
        2: LEFT,
        3: RIGHT,
        4: DOWN
    }

    ORIENTATIONS = {
        0: "BLANCK",
        1: "UP",
        2: "LEFT",
        3: "RIGHT",
        4: "DOWN"
    }

    O = {
        0: "B",
        1: "U",
        2: "L",
        3: "R",
        4: "D"
    }

def outputsToO (output):
    ret = []
    for el in output :
        ret.append(Constantes.O.value[Constantes.OUTPUTS.value.index(el)])
    return str(ret).replace("'","")

def outputsToOrientation (output):
    ret = []
    for el in output :
        ret.append(Constantes.ORIENTATIONS.value[Constantes.OUTPUTS.value.index(el)])
    return ret

def orientationToConst(orientation) :
    num = ["BLANCK","UP","LEFT","RIGHT","DOWN"].index(orientation)
    return Constantes.CONST_ORIENTATIONS.value.get(num) 