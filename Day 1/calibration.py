data = open("input.txt", "r")
lines = []

for line in data:
    lines.append(line.strip())

data.close()


tests = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
numericWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def generateVals(line):
    digits = []

    for i in range(len(line)):
        # check if the index contains a number
        if (line[i].isnumeric()):
            digits.append(int(line[i]))
        
        # check if the character leads to a numeric word
        else:
            for j in range(len(numericWords)):
                if ( line[i : len(numericWords[j]) + i ] == numericWords[j] ):
                    digits.append(j + 1)

    return int( str(digits[0]) + str(digits[-1]) )

def sumList(lst):
    sum = 0
    for line in lst:
        sum += generateVals(line)
    return sum

print(sumList(lines))