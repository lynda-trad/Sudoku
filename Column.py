class Column:
    def __init__(self, index):
        self.index = index
        self.occupied = []

    def initOccupied(self, number):
        self.occupied.append(number)

    # for every column j in grid
    # append number in grid i j to occupied list of column.index= j
