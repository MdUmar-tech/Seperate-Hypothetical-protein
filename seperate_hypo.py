#!/usr/bin/env python3

from Bio import SeqIO
import os
import shutil
import re
import sys
import subprocess
from subprocess import Popen, PIPE, STDOUT

x = input('enter your fasta sequence:')
sequences = SeqIO.parse(x, 'fasta')
filtered = [seq for seq in sequences if 'hypothetical protein' not in seq.description]
sequences2 = SeqIO.parse(x, 'fasta')
filtered1 = [seq for seq in sequences2 if 'hypothetical protein' in seq.description]

y = input('enter main output file name without hypothetical proteine : ')
with open(y, 'wt') as output:
    SeqIO.write(filtered, output, 'fasta')
    
z = input('enter output file name with hypothetical proteine :')
with open(z, 'wt') as hypothetical:
    SeqIO.write(filtered1, hypothetical, 'fasta')

a = input('give the destination folder or pathe to copy file :')

subprocess.call("mv %s %s" % (y, a), shell=True)

#os.rename(y, a)
