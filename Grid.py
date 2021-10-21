import numpy


class Grid:
    def __init__(self):
        self.numberGrid = []
        self.cellList = []
        self.lineList = []
        self.columnList = []

    def getNumberGrid(self):
        return self.numberGrid

    def getCellList(self):
        return self.cellList

    def getLineList(self):
        return self.lineList

    def getColumnList(self):
        return self.columnList

    def initNumberGrid(self):
        self.numberGrid = numpy.zeros((9, 9), dtype=int)

    def initCellList(self, cellList):
        self.cellList = cellList

