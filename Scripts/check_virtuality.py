#!/usr/bin/env python

import sys
import csv

packages = None
all = None
virts = None

f1 = sys.argv[1]
f2 = sys.argv[2]
f3 = sys.argv[3]
with open(f1, 'r') as f:
  packages = f.readlines()

with open('all-packages.csv', 'r') as f:
  all = f.readlines()

with open('virtual.csv', 'r') as f:
  virts = f.readlines()

installed = [ p.strip() for p in packages if p in all ]
virtual = [ p.strip() for p in packages if p in virts ]
out = open(f2,'w')
for line in installed:
    out.write(line)
    out.write("\n")
out.close()
out = open(f3,'w')
for line in virtual:
    out.write(line)
    out.write("\n")

