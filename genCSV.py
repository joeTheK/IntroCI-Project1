# Joseph Kelley
# Runs the genetic algorithm 900 times creating a CSV of results
## WARNING
# will save csv files to your computer
# will take a long time

from genAlgorithm import runEA
import csv

headers = ['CrossAckley', 'CrossTHC', 'CrossCIT', 'ACrossAckley', 'ACrossTHC', 'ACrossCIT', 'SPXAckley', 'SPXTHC', 'SPXCIT']

file1 = open('best.csv', 'w', newline='')
file2 = open('avg.csv', 'w', newline='')

writer1 = csv.writer(file1)
writer2 = csv.writer(file2)

writer1.writerow(headers)
writer2.writerow(headers)

print("headers in place")
for i in range(0, 100):
    best = []
    avg = []

    print(i)
    for selection in range(0, 3):
        for function in range(0, 3):
            initialPop, lastPop, statsMin, statsAvg, statsMax = runEA(nGen=50, size=100, mutationRate=.1, function=function, selection=selection)

            if function < 2:
                avgDiff = 0 - statsAvg[49]
                bestDiff = 0 - statsMin[49]
            else:
                bestDiff = -2.06261 - statsMin[49]
                avgDiff = -2.06261 - statsAvg[49]
            
            best.append(bestDiff)
            avg.append(avgDiff)

    writer1.writerow(best)
    writer2.writerow(avg)

file1.close()
file2.close()
            
