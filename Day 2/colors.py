data = open("input.txt", "r")
lines = []

for line in data:
    lines.append(line.strip())

data.close()

maxRed = 12
maxGreen = 13
maxBlue = 14

tests = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

games = []
cubes = []
for line in lines: 
    gameIndex = line.find(":")
    gameNum = int(line.split(":")[0].split(" ")[1])
    cleanLine = line[gameIndex + 1 :].strip().split(";")
    flag = False
    highRed = 0
    highGreen = 0
    highBlue = 0


    for data in cleanLine:
        for val in data.split(","):
            number = int(val.strip().split(" ")[0])
            color = val.strip().split(" ")[1]
            if ( (color[0] == "g" and number > maxGreen) or (color[0] == "b" and number > maxBlue) or (color[0] == "r" and number > maxRed)):
                flag = True
            
            if ( (color[0] == "g") ):
                highGreen = max(number, highGreen)
            if ( (color[0] == "b") ):
                highBlue = max(number, highBlue)
            if ( (color[0] == "r")):
                highRed = max(number, highRed)
    
    if (not flag):
        games.append(gameNum)
    cubes.append(highGreen * highRed * highBlue)


print(sum(games))
print(sum(cubes))