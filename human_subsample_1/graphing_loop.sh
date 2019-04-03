#!/bin/bash

for w in 10 20 30
  do
  for f in *.fasta
    do
    ./hydropathy_graphing.py -i $f -w $w
    done
done
