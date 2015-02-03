#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Ch 4 Exercises
# Multiple exons from genomic DNA

# open and read the input file
genomicDNA = open("genomic_dna.txt").read()

# open the output file and allow appending (i.e., concatenate exons)
codingDNA = open("coding_dna.txt", "a")

# open the file of exon positions
exon_positions = open("exons.txt")

# get the start/stop postions from each line
for startstop in exon_positions:
    positions = startstop.split(",")
    start = int(positions[0])
    stop = int(positions[1])
    
    # cut the exons from the genomic DNA sequence
    exon = genomicDNA[start:stop]
    
    # print the trimmed sequences to 'output.txt'
    codingDNA.write(exon)

    
    
    
