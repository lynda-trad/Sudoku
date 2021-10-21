class Line:
    def __init__(self, index):
        self.index = index
        self.occupied = []

    def initOccupied(self, number):
        self.occupied.append(number)


    # pour chaque ligne i de grid
    # on recup grid i j et on lappend a occupied de la ligne concernée soit index == i

    # pour chaque collone i de grid
    # on recup grid i j et on lappend a occupied de la coloone concernée soit index == j


    # donc il nous faut la liste les lignes
    # et la liste des colonnes