# Joseph Kelley
# Implements benchmark functions, fitness evaluation and tournament selection

import numpy as np
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import sin
from numpy import abs
import random

## Benchmark Functions
def ackley(x, y):
	z = -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * pi * y)+cos(2 * pi * y))) + e + 20
	return z

def threeHumpCamel(x, y):
	z = (2 * (x ** 2)) - (1.05 * (x ** 4)) + ((x ** 6) / 6) + (x * y) + (y ** 2)
	return z

def crossInTray(x, y):
	z = -0.0001 * ((abs(sin(x) * sin(y) * exp(abs(100 - sqrt(x ** 2 + y ** 2) / pi)))) + 1) ** 0.1
	return z


#Fitness Score
#evaluates fitness of population, population, which is done by scoring
#each chromosone based off of the testing function.
#returns a sorted list of scores and their corresponding population (sorted: min(best) to max)

def evalFitnessAckley(population):
	scores = []
	for chromosone in population:
		score = ackley(chromosone[0], chromosone[1])
		scores.append(score)
	scores, pop = np.array(scores), np.array(population)
	indices = np.argsort(scores)
	sortedScores = list(scores[indices][:])
	sortedPop = list(pop[indices, :][:])
	return sortedScores, sortedPop

def evalFitnessThreeHumpCamel(population):
	scores = []
	for chromosone in population:
		score = threeHumpCamel(chromosone[0], chromosone[1])
		scores.append(score)
	scores, pop = np.array(scores), np.array(population)
	indices = np.argsort(scores)
	sortedScores = list(scores[indices][:])
	sortedPop = list(pop[indices, :][:])
	return sortedScores, sortedPop

def evalFitnessCrossInTray(population):
	scores = []
	for chromosone in population:
		score = crossInTray(chromosone[0], chromosone[1])
		scores.append(score)
	scores, pop = np.array(scores), np.array(population)
	indices = np.argsort(scores)
	sortedScores = list(scores[indices][:])
	sortedPop = list(pop[indices, :][:])
	return sortedScores, sortedPop

## Selection

#Tournament Selection With Elitism
#creates rounds of numInRound and selects the top 1 from each.
#returns a population of size popByFit * numOfParents

def tournamentSelect(scores, popByFit, numInRound, numOfParents):
	popOfParents = []
	for i in range(numOfParents):
		popOfParents.append(popByFit[0])
	for i in range(numOfParents):
		popOfParents.append(popByFit[len(popByFit) - 1])

	for i in range(numOfParents):
		for j in range(1, len(scores) - 1):
			indices = []
			for k in range(numInRound):
				indices.append(random.randint(1, (len(scores) - 1)))
			temp, scores = np.array(indices), np.array(scores)
			round = list(scores[temp][:])
		
			top = round.index(min(round))
			popOfParents.append(popByFit[indices[top]])

	return popOfParents