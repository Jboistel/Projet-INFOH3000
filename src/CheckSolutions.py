from Solution import *

def lineToInfoConverter(line):
    ret = line.strip("\n").split(",", 2)
    ret[0] = float(ret[0])
    ret[1] = float(ret[1])
    ret[2] = ret[2].strip('"[]"').split(", ")
    ret[2] = [int(i) for i in ret[2]]
    return ret


if __name__ == "__main__":
    with open("solutions.csv") as file:
        print(file.readline())
        for line in file:
            info = lineToInfoConverter(line)
            sol = Solution(info[2])
            if sol.totalDist != info[0] or sol.totalRisk != info[1]:
                print("Solution mal calculée: " + str(info[2]))
                print(str(info[0]) + " != " + str(sol.totalDist))
                print(str(info[1]) + " != " + str(sol.totalRisk))

