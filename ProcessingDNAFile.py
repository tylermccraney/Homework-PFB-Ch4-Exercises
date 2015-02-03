#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Ch 4 Exercises
# Processing DNA in a file

# open the input file
input = open("input.txt")

# open the output file
output = open("output.txt", "w")

# trim the sequences one line at a time
for sequence in input:
    trimmed = sequence[14:100]
    
    # print the trimmed sequences to 'output.txt'
    output.write(trimmed)
    
    # print the length of each trimmed sequence to the screen
    print("Trimmed sequence length: " + str(len(trimmed)) + " bp")
    