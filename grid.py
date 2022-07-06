from asyncio import constants
from tile import Tile
from random import randint
from constantes import *
from decorators import decorateurCheckIndex

class Grid :
    
    def __init__(self, dim) -> None:
        self.dim = dim
        self.origin = (0,0)
        self.__grid = [ [Tile() for _ in range(self.dim)] for _ in range(self.dim) ] # Create the __grid at moment 0

    def __repr__(self) -> str:
        s = "[\n"
        for i in range(self.dim) :
            s += "\t" + str(self.__grid[i]).replace("],", "]\t") + "\n"
        return s + "]"
    
    def getGridOrientation (self) :
        g = [ [ None for _ in range(self.dim)] for _ in range (self.dim) ]
        for i in range(self.dim) :
            for j in range(self.dim) :
                tile = self.__getTile(i,j)
                if not tile.collapsed : continue
                    # if len(tile.getOptions()) == 1 : tile.collapse(tile.getOptions()[0])
                    # else : continue
                g[i][j] = orientationToConst(outputsToOrientation([tile.getType()])[0])
        return g


    def runStep(self) -> int:
        """
        collapse one tile by one :
        Find the min entropy in all tiles not collapsed then
        Collapse it
        """
        listeEntropy = self.__getAllEntropies()

        if len(listeEntropy) == 0 : return 0
        if len(listeEntropy) == 1 : randIndex = 0
        elif len(listeEntropy) == 2 : randIndex = randint(0,1)
        else : randIndex = randint(0,2)

        # randIndex = randint(0,len(listeEntropy)-1)

        if len(listeEntropy) == self.dim * self.dim : i,j = self.origin
        else : i,j = (listeEntropy[randIndex][0], listeEntropy[randIndex][1])

        tile = self.__getTile(i,j) # Tile get randomly from tiles with max entropy
        self.collapseTile(i, j, tile.getOptions()[randint(0, len(tile.getOptions()) - 1)]) # Collapse the tile with random option

        # Recalculate all options
        collapsed = [(i,j)]
        k = 0
        while k < len(collapsed) and k < self.dim:
            i,j = collapsed[k][0], collapsed[k][1]
            tile = self.__getTile(i,j)

            # for tile up
            if i > 0 :
                if self.__getTile(i-1, j).setOptionsWith(tile.getType(),Constantes.UP.value) : collapsed.append((i-1,j))
            
            # for tile down
            if i+1 < self.dim :
                if self.__getTile(i+1, j).setOptionsWith(tile.getType(),Constantes.DOWN.value) : collapsed.append((i+1,j))

            # for tile left
            if j > 0 :
                if self.__getTile(i, j-1).setOptionsWith(tile.getType(),Constantes.LEFT.value) : collapsed.append((i,j-1))
            
            # for tile right
            if j+1 < self.dim :
                if self.__getTile(i, j+1).setOptionsWith(tile.getType(),Constantes.RIGHT.value) : collapsed.append((i,j+1))
            k+=1

        return 1


    def __getAllEntropies(self) -> list[int]:
        """
        Return indexes of all tiles not collapsed with max entropy
        """
        # Get all Entropy if not collasped and sort it in reverse
        ret = []
        for i in range(self.dim):
            for j in range(self.dim) :
                if self.__grid[i][j].collapsed :
                    continue
                ret.append((i,j, self.__grid[i][j].getEntropy()))
        ret.sort(key=lambda x : x[2])

        if len(ret) == 0 : return [] # If all tiles are collapsed

        maxEntropy = ret[0][2] # Get minimum of entropy and return all entropy == to this min

        return list(filter(lambda x: x[2] >= maxEntropy, ret))

    @decorateurCheckIndex
    def __getTile(self, i, j) -> Tile:
        """
        return the tile from this indexes
        """
        return self.__grid[i][j]

    @decorateurCheckIndex
    def collapseTile(self, i, j, type) -> None :
        """
        Set the type for a specific tile
        """
        self.__grid[i][j].collapse(type)
    
    @decorateurCheckIndex
    def setTileOption(self, i, j, options) -> None :
        """
        Set the options for a specific tile
        """
        self.__grid[i][j].options = options

# A chaque tour on regarde quelle case à le moins d'entropy
# Parmi les cases avec le moins d'entropy, on en choisit une au hasard
# On collapse cette case avec les différentes options quelle a 
# On recommence