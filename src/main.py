import sys


def extract(inputFile, outputFile, word):
    output = open(outputFile, 'w')

    with open(inputFile, 'r') as f:
        lines = f.readlines()

        for i in range(len(lines) - 1):
            if lines[i].find(word) != -1:
                output.write(lines[i])


def intervalFinder(outputFile):

    with open(outputFile, 'r') as f:
        lines = f.readlines()

        for i in range(len(lines) - 1):

            if i == 0:
                print(lines[i].split())

            currentline = lines[i].split()
            nextline = lines[i + 1].split()
            if (len(currentline) > 0) & (len(nextline) > 0):
                if int(nextline[-1]) - int(currentline[-1]) > 30000:
                    print(currentline)
                    print(nextline)

            if i == len(lines) - 2:
                print(lines[len(lines) - 1].split())


if __name__ == '__main__':
    extract(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
    intervalFinder(str(sys.argv[2]))
