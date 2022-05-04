class Data:
    distMatrix = [
        [0, 4.1, 9.0, 6.0, 1.5, 4.7, 4.8, 7.3, 6.0, 3.3, 4.9, 3.6, 2.6, 5.1, 1.2, 2.5, 8.3, 10.5, 6.1, 7.1],
        [4.1, 0, 10.7, 5.4, 3.9, 5.8, 8.5, 4.0, 6.1, 3.8, 5.7, 3.7, 3.2, 2.8, 4.0, 5.6, 5.0, 9.5, 8.7, 8.8],
        [9.0, 10.7, 0, 13.6, 8.2, 3.3, 7.8, 9.9, 13.4, 5.4, 12.8, 11.0, 10.3, 7.7, 7.0, 8.7, 8.6, 2.8, 3.9, 2.9],
        [6.0, 5.4, 13.6, 0, 5.5, 9.5, 10.8, 9.8, 2.7, 10.1, 3.4, 3.1, 4.0, 8.1, 6.4, 7.1, 12.5, 15.4, 11.9, 12.0],
        [1.5, 3.9, 8.2, 5.5, 0, 5.4, 5.2, 7.4, 4.8, 4.1, 3.9, 2.7, 1.7, 4.8, 2.2, 3.2, 7.2, 11.0, 6.9, 7.9],
        [4.7, 5.8, 3.3, 9.5, 5.4, 0, 6.7, 6.7, 9.3, 2.3, 8.7, 7.0, 6.2, 3.9, 3.4, 5.2, 6.0, 5.0, 3.9, 4.0],
        [4.8, 8.5, 7.8, 10.8, 5.2, 6.7, 0, 10.9, 9.9, 7.4, 8.1, 7.5, 6.7, 8.6, 4.6, 2.7, 11.8, 10.6, 5.6, 6.5],
        [7.3, 4.0, 9.9, 9.8, 7.4, 6.7, 10.9, 0, 12.1, 5.2, 9.7, 7.3, 6.3, 2.8, 6.2, 8.3, 2.0, 8.8, 10.2, 10.3],
        [6.0, 6.1, 13.4, 2.7, 4.8, 9.3, 9.9, 12.1, 0, 9.4, 2.3, 3.4, 4.1, 9.5, 6.3, 7.0, 13.0, 15.3, 11.8, 11.9],
        [3.3, 3.8, 5.4, 10.1, 4.1, 2.3, 7.4, 5.2, 9.4, 0, 8.8, 6.4, 5.4, 2.1, 3.2, 5.6, 4.6, 6.5, 5.8, 5.9],
        [4.9, 5.7, 12.8, 3.4, 3.9, 8.7, 8.1, 9.7, 2.3, 8.8, 0, 2.2, 3.2, 7.8, 5.6, 6.4, 12.4, 14.6, 11.1, 11.2],
        [3.6, 3.7, 11.0, 3.1, 2.7, 7.0, 7.5, 6.3, 3.4, 6.4, 2.2, 0, 1.4, 6.1, 3.9, 4.6, 8.8, 12.9, 9.4, 9.5],
        [2.6, 3.2, 10.3, 4.0, 1.7, 6.2, 6.7, 6.3, 4.1, 5.4, 3.2, 1.4, 0, 4.1, 3.3, 4.0, 7.0, 11.7, 8.8, 8.9],
        [5.1, 2.8, 7.7, 8.1, 4.8, 3.9, 8.6, 2.8, 9.5, 2.1, 7.8, 6.1, 4.1, 0, 3.8, 5.6, 2.9, 7.7, 7.9, 8.0],
        [1.2, 4, 7, 6.4, 2.2, 3.4, 4.6, 6.2, 6.3, 3.2, 5.6, 3.9, 3.3, 3.8, 0, 2.2, 7.7, 10.0, 4.9, 5.7],
        [2.5, 5.6, 8.7, 7.1, 3.0, 5.2, 2.7, 8.3, 7.0, 5.6, 6.4, 4.6, 4.0, 5.6, 2.2, 0, 9.5, 10.6, 5.8, 6.6],
        [8.3, 5, 8.6, 12.5, 7.2, 6.0, 11.8, 2.0, 13.0, 4.6, 12.4, 8.8, 7.0, 2.9, 7.7, 9.5, 0, 6.8, 9.5, 11, 3],
        [10.5, 9.5, 2.8, 15.4, 11.0, 5.0, 10.6, 8.8, 15.3, 6.5, 14.6, 12.9, 11.7, 7.7, 10.0, 10.6, 6.8, 0, 6.5, 5.5],
        [6.1, 8.7, 3.9, 11.9, 6.9, 3.9, 5.6, 10.2, 11.8, 5.8, 11.1, 9.4, 8.8, 7.9, 4.9, 5.8, 9.5, 6.5, 0, 1.5],
        [7.1, 8.8, 2.9, 12.0, 7.9, 4.0, 6.5, 10.3, 11.9, 5.9, 11.2, 9.5, 8.9, 8.0, 5.7, 6.6, 11.3, 5.5, 1.5, 0],
    ]

    nbPeople = [117412, 33161, 24224, 178552, 47180, 39556, 55613, 24269, 85541, 51426, 21638, 96586, 50659, 27402,
                132.560, 81944, 24619, 54311, 41207]

    def getDistMatrix(self):
        return self.distMatrix

    def getNbPeople(self):
        return self.nbPeople

    def getDist(self, column: int, row: int):
        return self.distMatrix[column][row]


bank = [0, 4.1, 9.0, 6.0, 1.5, 4.7, 4.8, 7.3, 6.0, 3.3, 4.9, 3.6, 2.6, 5.1, 1.2, 2.5, 8.3, 10.5, 6.1, 7.1]
anderlecht = [4.1, 0, 10.7, 5.4, 3.9, 5.8, 8.5, 4.0, 6.1, 3.8, 5.7, 3.7, 3.2, 2.8, 4.0, 5.6, 5.0, 9.5, 8.7, 8.8]
auderghem = [9.0, 10.7, 0, 13.6, 8.2, 3.3, 7.8, 9.9, 13.4, 5.4, 12.8, 11.0, 10.3, 7.7, 7.0, 8.7, 8.6, 2.8, 3.9, 2.9]
berchem_Sainte_Agathe = [6.0, 5.4, 13.6, 0, 5.5, 9.5, 10.8, 9.8, 2.7, 10.1, 3.4, 3.1, 4.0, 8.1, 6.4, 7.1, 12.5, 15.4,
                         11.9, 12.0]
bruxelles_ville = [1.5, 3.9, 8.2, 5.5, 0, 5.4, 5.2, 7.4, 4.8, 4.1, 3.9, 2.7, 1.7, 4.8, 2.2, 3.2, 7.2, 11.0, 6.9, 7.9]
etterbeek = [4.7, 5.8, 3.3, 9.5, 5.4, 0, 6.7, 6.7, 9.3, 2.3, 8.7, 7.0, 6.2, 3.9, 3.4, 5.2, 6.0, 5.0, 3.9, 4.0]
evere = [4.8, 8.5, 7.8, 10.8, 5.2, 6.7, 0, 10.9, 9.9, 7.4, 8.1, 7.5, 6.7, 8.6, 4.6, 2.7, 11.8, 10.6, 5.6, 6.5]
forest = [7.3, 4.0, 9.9, 9.8, 7.4, 6.7, 10.9, 0, 12.1, 5.2, 9.7, 7.3, 6.3, 2.8, 6.2, 8.3, 2.0, 8.8, 10.2, 10.3]
ganshoren = [6.0, 6.1, 13.4, 2.7, 4.8, 9.3, 9.9, 12.1, 0, 9.4, 2.3, 3.4, 4.1, 9.5, 6.3, 7.0, 13.0, 15.3, 11.8, 11.9]
ixelles = [3.3, 3.8, 5.4, 10.1, 4.1, 2.3, 7.4, 5.2, 9.4, 0, 8.8, 6.4, 5.4, 2.1, 3.2, 5.6, 4.6, 6.5, 5.8, 5.9]
jette = [4.9, 5.7, 12.8, 3.4, 3.9, 8.7, 8.1, 9.7, 2.3, 8.8, 0, 2.2, 3.2, 7.8, 5.6, 6.4, 12.4, 14.6, 11.1, 11.2]
koekelberg = [3.6, 3.7, 11.0, 3.1, 2.7, 7.0, 7.5, 6.3, 3.4, 6.4, 2.2, 0, 1.4, 6.1, 3.9, 4.6, 8.8, 12.9, 9.4, 9.5]
molenbeek_Saint_Jean = [2.6, 3.2, 10.3, 4.0, 1.7, 6.2, 6.7, 6.3, 4.1, 5.4, 3.2, 1.4, 0, 4.1, 3.3, 4.0, 7.0, 11.7, 8.8,
                        8.9]
saint_Gilles = [5.1, 2.8, 7.7, 8.1, 4.8, 3.9, 8.6, 2.8, 9.5, 2.1, 7.8, 6.1, 4.1, 0, 3.8, 5.6, 2.9, 7.7, 7.9, 8.0]
saint_Josse_ten_Noode = [1.2, 4, 7, 6.4, 2.2, 3.4, 4.6, 6.2, 6.3, 3.2, 5.6, 3.9, 3.3, 3.8, 0, 2.2, 7.7, 10.0, 4.9, 5.7]
schaerbeek = [2.5, 5.6, 8.7, 7.1, 3.0, 5.2, 2.7, 8.3, 7.0, 5.6, 6.4, 4.6, 4.0, 5.6, 2.2, 0, 9.5, 10.6, 5.8, 6.6]
uccle = [8.3, 5, 8.6, 12.5, 7.2, 6.0, 11.8, 2.0, 13.0, 4.6, 12.4, 8.8, 7.0, 2.9, 7.7, 9.5, 0, 6.8, 9.5, 11, 3]
watermael_Boitsfort = [10.5, 9.5, 2.8, 15.4, 11.0, 5.0, 10.6, 8.8, 15.3, 6.5, 14.6, 12.9, 11.7, 7.7, 10.0, 10.6, 6.8, 0,
                       6.5, 5.5]
woluwe_Saint_Lambert = [6.1, 8.7, 3.9, 11.9, 6.9, 3.9, 5.6, 10.2, 11.8, 5.8, 11.1, 9.4, 8.8, 7.9, 4.9, 5.8, 9.5, 6.5, 0,
                        1.5]
woluwe_Saint_Pierre = [7.1, 8.8, 2.9, 12.0, 7.9, 4.0, 6.5, 10.3, 11.9, 5.9, 11.2, 9.5, 8.9, 8.0, 5.7, 6.6, 11.3, 5.5,
                       1.5, 0]
