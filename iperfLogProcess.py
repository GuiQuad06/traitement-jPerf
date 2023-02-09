#!/usr/bin/env python3

from plotData import *
from csvConverter import *
from statistics import *
import sys

fichier_in = sys.argv[1] + '.log'
fichier_out = sys.argv[1] + '.csv'

#Ouverture d'un fichier log jPerf serveur de flux UDP en read-only et lecture ligne à ligne
fichier = open(fichier_in, "r")
text = fichier.readlines()
data = []
lost = []
T =  []
jitter = []
debit = []
bw =  []
dataReport = { 'Max Jitter':0, 'Min Bandwidth':0, 'Bandwidth moyenne':0, 'Paquets perdus':0, 'Ecart type jitter':0, 'Ecart type bandwidth':0}

#Je parcours chaque ligne du texte
for line in text[1:len(text)-1]:
	if 'KBytes' not in line: 
		#Si la ligne ne contient pas les données exploitables, je passe à l'itération suivante
		continue
	else:
		#Push des valeurs dans les différentes listes
		data.append(line[:len(line)-1].split(" "))
		lost.append(float(line[line.find('(')+1:line.find('%')]))
		jitter.append(float(line[line.find('/sec')+5:line.find('ms')])/(2*coeff_debit))
		bw.append(float(line[line.find('KBytes')+7:line.find('Kbits/sec')])*coeff_debit)
		debit.append(float(line[line.find(' sec')+5:line.find('KBytes')])*coeff_debit)
		T.append(float(line[line.find(']')+2:line.find('-')]))

#MAJ du dictionnaire de data report	
dataReport['Max Jitter'] = max(jitter)
dataReport['Min Bandwidth'] = min(bw)
dataReport['Bandwidth moyenne'] = mean(bw)
dataReport['Paquets perdus'] = lost[len(lost)-1]
dataReport['Ecart type jitter'] = pstdev(jitter)
dataReport['Ecart type bandwidth'] = pstdev(bw)

#J'envoie le dictionnaire report dans un fichier CSV dont le titre est passé dans la console
data2csv(dataReport, fichier_out)

#Affichage des courbes
plotDataJit(jitter[1:len(jitter)-1], T[1:len(T)-1], 'Jitter (ms)', (0,10))
plotDataBW(bw[1:len(bw)-1], T[1:len(T)-1], 'Bande Passante d\'un flux UDP(Kbits/sec)', (0, 10000))

