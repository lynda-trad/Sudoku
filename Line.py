class Line:
    def __init__(self, index):
        self.index = index
        self.occupied = []

    def initOccupied(self, number):
        self.occupied.append(number)

    # for every line i in grid
    # append number in grid i j to occupied list of line.index = i
