#!/usr/bin/env python3

"""Main."""

import sys
from sys import argv
from cpu import *


cpu = CPU()

# Obtain the program path from args
fh = argv[1]
# Parse the program string
program = open(fh, 'r').read().split('\n')
# Load it into memory
cpu.load(program)
# Run the program
cpu.run()
