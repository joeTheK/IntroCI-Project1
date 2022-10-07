# Joseph Kelley
# Main code to implement Project 1 algorithm

from ast import If
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from selection import evalFitnessAckley, evalFitnessThreeHumpCamel, evalFitnessCrossInTray
from selection import tournamentSelect
from selection import ackley, threeHumpCamel, crossInTray
from exploreExploit import avgCrossover, simplexSpaceCross
from exploreExploit import crossover
from exploreExploit import mutate


#Chromosone Structure [x, y] ex. [3,2] = coordinate point. (3,2)

#Initial Population
#Creates a population of size, size. Returns the population, which is a set
#of chromosones with random (between -10 and 10) x and y values

def initPop(size, bounds):
	population = []
	for i in range(size):
		chromosone = ((np.random.rand(2) - 0.5) * 2) * bounds
		population.append(chromosone)
	return population

#Quick fucntion that creates and saves contour plots (used for analysis)

def contourPlot(pop, gen, function):
	a = np.linspace(-10, 10, 100)
	b = np.linspace(-10, 10, 100)
	x, y = np.meshgrid(a, b)

	if function == 0:
		z = ackley(x, y)
	if function == 1:
		z = threeHumpCamel(x, y)
	if function == 2:
		z = crossInTray(x, y)

	fig,ax=plt.subplots(1,1)
	cp = ax.contour(x, y, z, alpha=0.7)

	if function == 0:
		name = "Ackley, gen: {}"
		ax.set_title(name.format(gen))
	if function == 1:
		name = "Three Hump Camel, gen: {}"
		ax.set_title(name.format(gen))
	if function == 2:
		name = "Cross in Tray, gen: {}"
		ax.set_title(name.format(gen))

	plt.scatter([x[0] for x in pop], [y[1] for y in pop], edgecolor='b', alpha=0.3)
	name = "contourGen{}_{}"
	#plt.savefig(name.format(gen, function))
	#plt.show()
	
	return

#Main Function
#function = {ackley = 0, threeHumpCamel = 1, crossInTray = 2}
#selection = {1-pointCrossover = 0, averageCrossover = 1, simplexSpaceCross = 2}
 
def runEA(nGen, size, mutationRate, function, selection):
	if function == 0 or function == 1:
		nextGenPop = initPop(size, 5)
	elif function == 2:
		nextGenPop = initPop(size, 10)
	
	initialPop = nextGenPop
	statsMin = np.zeros(nGen)
	statsAvg = np.zeros(nGen)
	statsMax = np.zeros(nGen)

	for i in range(nGen):
		if(i % 10 == 0 or i == 1 or i == 5):
			contourPlot(nextGenPop, i, function)

		if function == 0:
			scores, sortedPop = evalFitnessAckley(nextGenPop)
		if function == 1:
			scores, sortedPop = evalFitnessThreeHumpCamel(nextGenPop)
		if function == 2:
			scores, sortedPop = evalFitnessCrossInTray(nextGenPop)
		
		if selection == 0:
			selectedPop = tournamentSelect(scores, sortedPop, 10, 2)
			crossPop = crossover(selectedPop, size)
		if selection == 1:
			selectedPop = tournamentSelect(scores, sortedPop, 10, 2)
			crossPop = avgCrossover(selectedPop)
		if selection == 2:
			selectedPop = tournamentSelect(scores, sortedPop, 10, 3)
			crossPop = simplexSpaceCross(selectedPop)
		
		nextGenPop = mutate(crossPop, mutationRate)

		statsMin[i] = np.amin(scores)
		statsAvg[i] = np.mean(scores)  
		statsMax[i] = np.amax(scores)
	
	contourPlot(nextGenPop, i, function)
	return initialPop, nextGenPop, statsMin, statsAvg, statsMax

#TEST AREA
#This code was changed on a per run basis to adjust the result that was recieved

initialPop, lastPop, statsMin, statsAvg, statsMax = runEA(nGen=50, size=100, mutationRate=.1, function=0, selection=0)

preXAvg = [chromosone[0] for chromosone in initialPop[0:100]]
preXAvg = mean(preXAvg)
preYAvg = [chromosone[1] for chromosone in initialPop[0:100]]
preYAvg = mean(preYAvg)

postXAvg = [chromosone[0] for chromosone in lastPop[0:100]]
postXAvg = mean(postXAvg)
postYAvg = [chromosone[1] for chromosone in lastPop[0:100]]
postYAvg = mean(postYAvg)

#pyplot code taken from VCS GA2.py (used with permission)
plt.plot(statsMin,'r')
plt.plot(statsAvg,'b')
plt.plot(statsMax,'g')
plt.title("Cross in Tray SPX")
plt.ylabel('score')
plt.xlabel('generations')
#plt.savefig('linePlot_CIT_SPX3')
#plt.show()
