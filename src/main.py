from numpy.random import randint

global distances
distances = {}

def getData(filePath: str):
    return 0

if __name__ == "__main__":
    list = [3,0,5,6,0,1,2,4]
    print(list[-len(list)])
    new = []
    current = list[randint(len(list))]
    print("Start: ", current)
    new.append(current)
    while len(list) > 1:
        dx = list[-len(list)+list.index(current)+1]
        print(dx)
        list.pop(list.index(current))
        current = dx
        new.append(current)
        print(new)
