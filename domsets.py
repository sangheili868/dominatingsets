from subprocess import call
from sys import argv
import csv

if len(argv) != 2:
	print("Usage: python domsets.py inFile")
	exit(0)
script, inFile = argv
call(["./orca", "4", inFile, "counts.out"])
GDVs=[]
for line in open("counts.out"):
	GDVs.append(line[:-1].split(" "))
print GDVs[4][5]
print GDVs[5][4]
print len(GDVs)
print len(GDVs[5])

