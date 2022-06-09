import matplotlib.pyplot as plt
import csv

# fileList = ["data/default_tourney1.csv", "data/default_tourney2.csv", "data/default_tourney3.csv"]
# fileList = ["data/default_ranked1.csv", "data/default_ranked2.csv", "data/default_ranked3.csv"]
fileList = ["data/Roulette1.csv", "data/Roulette2.csv", "data/Roulette3.csv"]
title = "Average Fitness of Tourney Selection"
xLabel = "Generation"
yLabel = "Average Fitness"


# keep the scatterplot readable
markers = ["." , "," , "o" , "v" , "^" , "<", ">"]
colors = ['r','g','b','c','m', 'y', 'k']

counter = 0
for file in fileList:
    data = []
    with open(file, "r") as f:
        csvOutput = csv.reader(f)
        
        for line in csvOutput:
            data.append(int(line[2])) # 3 for average, 2 for best

    plt.scatter(list(range(0, len(data))), data, s=2, marker=markers[counter], color=colors[counter], label=counter)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    counter += 1

    print(data[-1])
    print(len(data))


# plt.show()