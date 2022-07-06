from ast import Pass
from constantes import *

class Tile :

    def __init__(self) -> None:
        self.collapsed = False
        self.type = None
        self.options = list(Constantes.OUTPUTS.value)

    def getEntropy(self) -> int:
        return len(self.options)

    def getType(self) -> list[int] :
        if self.type is not None :
            return self.type
    
    def  getOptions(self) -> list[list[int]]:
        return self.options
    
    def collapse(self, type) -> None :
        if not self.collapsed :
            self.type = type
            self.collapsed = True

    def setOptionsWith(self, t, direction) -> None:
        """
        return all options possible for a tile in the direction of the tile type in param\n
        (BLANCK, UP)      -> UP\n
        (UP, UP)          -> LEFT, RIGHT, DOWN\n
        (UP, DOWN)        -> BLANCK, DOWN
        """
        if type(t) == list : 
            t = orientationToConst(outputsToOrientation([t])[0])
        if type(direction) == list : 
            direction = outputsToOrientation([direction])[0]

        opt = []
        if (t == Constantes.BLANCK.value) :
            if (direction == Constantes.UP.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                ]
            if (direction == Constantes.LEFT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                ]
            if (direction == Constantes.RIGHT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                ]
            if (direction == Constantes.DOWN.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]

        if (t == Constantes.UP.value) :
            if (direction == Constantes.UP.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.LEFT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.RIGHT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.DOWN.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]

        if (t == Constantes.LEFT.value) :
            if (direction == Constantes.UP.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.LEFT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.RIGHT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                ]
            if (direction == Constantes.DOWN.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                ]

        if (t == Constantes.RIGHT.value) :
            if (direction == Constantes.UP.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.LEFT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                ]
            if (direction == Constantes.RIGHT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.DOWN.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                ]
 
        if (t == Constantes.DOWN.value) :
            if (direction == Constantes.UP.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.BLANCK.value],
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                ]
            if (direction == Constantes.LEFT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.RIGHT.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.DOWN.value],
                ]
            if (direction == Constantes.DOWN.value) :
                opt = [
                    Constantes.OUTPUTS.value[Constantes.UP.value],
                    Constantes.OUTPUTS.value[Constantes.LEFT.value],
                    Constantes.OUTPUTS.value[Constantes.RIGHT.value],
                ]

        # delete all options not in opt
        o = []
        for element in self.options :
            if element in opt :
                o.append(element)
        self.options = o
        
        # If only one option remains, collaps and refresh all options
        if self.getEntropy() == 1 :
            self.collapse(self.options[0])
            return 1

        return 0


    def __repr__(self) -> str:
        if self.type is None :
            return str(outputsToO(self.options))
        return str(outputsToO([self.type]))+"c"