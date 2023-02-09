#!/usr/bin/env python3

from matplotlib import pyplot

def plotDataBW(y, x, legende, yRange):
	pyplot.plot(x, y, color='blue')
	pyplot.title(legende)
	pyplot.ylim(yRange)
	pyplot.xlabel('Temps (sec)')
	pyplot.ylabel('Kbits/sec')
	pyplot.show()

def plotDataJit(y, x, legende, yRange):
	pyplot.plot(x, y, color='red')
	pyplot.xlabel('Temps (sec)')
	pyplot.ylim(yRange)
	pyplot.ylabel('ms')
	pyplot.title(legende)
	pyplot.show()