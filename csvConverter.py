#!/usr/bin/env python3

import csv

def data2csv(data, titreFichier):
	with open(titreFichier,'w') as f:
		w = csv.writer(f)
		w.writerows(data.items())