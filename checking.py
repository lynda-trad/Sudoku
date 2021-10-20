# Returns number possibilities of given cell depending of line
def checkLine(numberGrid, coordinates):
    i = coordinates[0]
    hypothesis = []
    for number in range(1, 9):
        boolean = False  # not on line
        for jx in range(len(numberGrid[i])):
            if number == numberGrid[i][jx]:  # found number on line
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Returns number possibilities of given cell depending of column
def checkColumn(numberGrid, coordinates):
    j = coordinates[1]
    hypothesis = []
    for number in range(1, 9):
        boolean = False  # not on column
        for ix in range(len(numberGrid[j])):
            if number == numberGrid[ix][j]:  # found number on column
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Functions to find neighbours coordinates in the box
def getIList(i):
    if i % 3 == 0:
        return [i + 1, i + 2]
    elif i % 3 == 1:
        return [i - 1, i + 1]
    elif i % 3 == 2:
        return [i - 1, i - 2]


def getJList(j):
    if j % 3 == 0:
        return [j + 1, j + 2]
    elif j % 3 == 1:
        return [j - 1, j + 1]
    elif j % 3 == 2:
        return [j - 1, j - 2]


def mergeLists(iList, jList):
    checkingList = []
    for i in iList:
        for j in jList:
            checkingList.append((i, j))
    return checkingList


# Returns number possibilities of given cell depending of box
def checkBox(numberGrid, coordinates):
    i = coordinates[0]
    j = coordinates[1]
    iList = getIList(i)
    jList = getJList(j)
    checkingList = mergeLists(iList, jList)
    hypothesis = []

    for cell in checkingList:
        ix = cell[0]
        jx = cell[1]
        for number in range(1, 9):
            boolean = False  # not in box
            if number == numberGrid[ix][jx]:  # found number in box
                boolean = True
            if not boolean:
                hypothesis.append(number)
            elif boolean and number in hypothesis:  # if number was placed after hypothesis init
                hypothesis.remove(number)
    return hypothesis

    ################

    # if i % 3 == 0 -> check i + 1 et i + 2     iList = [i + 1, i + 2]
    # if j % 3 == 0 -> check j + 1 et j + 2     jList = [j + 1, j + 2]

    # if i % 3 == 1 -> check i - 1 et i + 1     iList = [i - 1, i + 1]
    # if j % 3 == 1 -> check j - 1 et j + 1     jList = [j - 1, j + 1]

    # if i % 3 == 2 -> check i - 1 et i - 2     iList = [i - 1, i - 2]
    # if j % 3 == 2 -> check j - 1 et j - 2     jList = [j - 1, j - 2]

    # exemple : i % 3 == 1 et j % 3 == 2
    # needs to check :
    # checkingList = []
    # iList = [i - 1, i + 1]
    # jList = [j - 1, j - 2]
    # combinaison of the two :
    # for i in iList:
    #      for j in jList:
    #           checkingList.append((i,j))
    # then we check if number is in checkingList

    return hypothesis


# Returns numbers that are common to 3 checking lists
def getHypothesis(numberGrid, cursor):
    lineHypo = checkLine(numberGrid, cursor)
    columnHypo = checkColumn(numberGrid, cursor)
    boxHypo = checkBox(numberGrid, cursor)
    hypothesis = []
    for hypo in lineHypo:
        if hypo in columnHypo and hypo in boxHypo:
            hypothesis.append(hypo)
    print("coordinates", cursor, "hypothesis are: ", hypothesis)
    return hypothesis
