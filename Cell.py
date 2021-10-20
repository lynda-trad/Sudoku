class Cell:
    def __init__(self, i, j, number, original):
        self.coordinates = (i, j)
        self.number = number
        self.hypothesis = []
        self.original = original

    def getNumber(self):
        return self.number

    def getHypothesis(self):
        return self.hypothesis

    def getCoordinates(self):
        return self.coordinates

    def getOriginal(self):
        return self.original

    def setNumber(self, number):
        self.number = number

    def setHypothesis(self, hypo):
        self.hypothesis = hypo

    # Printing method
    def printCell(self):
        print("Position:", self.getCoordinates())
        print("Number:", self.getNumber())
        print("Hypothesis:", self.getHypothesis())
        print("Original:", self.getOriginal())

    # Adds number to hypothesis
    def addHypothesis(self, number):
        self.hypothesis.append(number)

    # Removes a number from hypothesis
    def delHypothesis(self, number):
        self.hypothesis.remove(number)

    # Returns True if a number is in hypothesis, False if not
    def inHypothesis(self, number):
        if number in self.hypothesis:
            return True
        else:
            return False

    # Returns number if a number can be placed and places it, 0 if not
    def placeNumber(self):
        if not self.getOriginal():
            if len(self.getHypothesis()) == 1:
                self.setNumber(self.hypothesis[0])
                return self.hypothesis[0]
            else:
                return 0
        else:
            return self.getNumber()
