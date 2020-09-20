#!/usr/bin/env python
import sys


# Read list of packages from file.
with open(sys.argv[1], "r") as fin:
    packages = fin.readlines()

with open("all-packages.csv", "r") as fin:
    installed = [package.strip() for package in packages if package in fin.readlines()]

with open("virtual.csv", "r") as fin:
    virtual = [package.strip() for package in packages if package in fin.readlines()]

# Write the installed packages to file.
with open(sys.argv[2], "w") as fout:
    for package in installed:
        fout.write(package +'\n')

# TODO add comment about what is written to the file here.
with open(sys.argv[3], "w") as fout:
    for package in virtual:
        fout.write(package +'\n')
