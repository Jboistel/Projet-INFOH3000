import csv

global distances
distances = []

towns = ['Anderlecht', 'Auderghem', 'Berchem-Sainte-Agathe', 'Bruxelles-Ville', 'Etterbeek', 'Evere', 'Forest',
         'Ganshoren', 'Ixelles', 'Jette', 'Koekelberg', 'Molenbeek-Saint-Jean', 'Saint-Gilles', 'Saint-Josse-ten-Noode',
         'Schaerbeek', 'Uccle', 'Watermael-Boitsfort', 'Woluwe-Saint-Lambert', 'Woluwe-Saint-Pierre']


def getData(filePath: str):
    file = open(filePath, mode='r', encoding='utf-8-sig')
    csvreader = csv.reader(file)
    count = -1
    for row in csvreader:
        distances.append([])
        count += 1
        for col in row:
            distances[count].append(float(col))
    return 0


if __name__ == "__main__":
    getData("matrix.csv")
    print(distances)
