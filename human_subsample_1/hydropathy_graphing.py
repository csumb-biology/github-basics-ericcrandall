#!/usr/bin/env python

import sys
from matplotlib import pyplot
#Working template of hydropathy score calculation script
#You need to put in comments for every line

InFileName = "amino_acid_hydropathy_values.txt"
InFile = open(InFileName, 'r')
Data=[]
Hydropathy={}
LineNumber = 0

for Line in InFile:
    if(LineNumber>0):
        Line = Line.strip("\n")
        Data = Line.split(",")
        Hydropathy[Data[1]]=float(Data[2])
    LineNumber = LineNumber + 1
InFile.close()


for i in range(len(sys.argv)):
    if sys.argv[i] == "-i":
        InSeqFileName = sys.argv[i+1]
    if sys.argv[i] == "-w":
        window = int(sys.argv[i+1])




Value=0
window_counter=0

InSeqFile = open(InSeqFileName, 'r')
LineNumber = 0

for Line in InSeqFile:
    if(LineNumber>0):
        ProtSeq=Line.strip('\n')
    LineNumber = LineNumber + 1
InSeqFile.close()

OutFileName = InSeqFileName.strip('.fasta') + "_" + window + ".png"
OutFile = open(OutFileName,"w")

for i in range(len(ProtSeq)):
    Value+=Hydropathy[ProtSeq[i]]
    if(i>(window-1) and i<=(len(ProtSeq)-window)):
        Value=Value-Hydropathy[ProtSeq[i-window]]
        OutString = "%d,%.2f" % (window_counter, Value)
        OutFile.write(OutString + "\n")

    window_counter+=1

OutFile.close()
