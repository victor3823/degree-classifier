#!/usr/bin/python
import sys


def getWeightedAvg(y3mods, y2mods):
    weight3 = y3mods[:5]
    weight2 = y3mods[6:] + y2mods[:2]
    weight1 = y2mods[3:]

    weightedTotal = sum([x*3 for x in weight3]) \
                    + y3mods[5] * (2 + 1/3) \
                    + sum([y*2 for y in weight2]) \
                    + y2mods[2] * (1 + 2/3) \
                    + sum(weight1)
    weightedAvg = weightedTotal / 32

    return weightedAvg


def classify(avg):
    if avg >= 70:
        return "1st"
    elif avg >= 60:
        return "2:1"
    elif avg >= 50:
        return "2:2"
    elif avg >= 40:
        return "3rd"
    elif avg >= 35:
        return "Pass"
    else:
        return "Fail"


def main():
    if len(sys.argv) != 17:
        sys.exit("Incorrect number of arguments.")

    y3mods = sorted([int(x) for x in sys.argv[1:9]], reverse=True)
    y2mods = sorted([int(x) for x in sys.argv[9:]], reverse=True)

    avg = getWeightedAvg(y3mods, y2mods)
    print(f"Weighted average = {avg}")
    print(f"Classification: {classify(avg)}")


if __name__ == "__main__":
    main()
