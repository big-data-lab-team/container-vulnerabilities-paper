#!/usr/bin/env python3

import csv
import sys
import os
import re

def compare(file1,file2):
    with open(file1, 'r') as t1, open(file2, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    
    with open('C-A.csv', 'w') as f1:
        for line in filetwo:
            if line not in fileone:
                f1.write(line)
    with open('A-C.csv', 'w') as f2:
        for line in fileone:
            if line not in filetwo:
                f2.write(line)
    with open('Common.csv', 'w') as f3:
        for line in fileone:
            if line in filetwo:
                f3.write(line)

def main():
    file1=sys.argv[1]
    file2=sys.argv[2]
    count=0
    compare(file1,file2)
    with open('A-C.csv','r') as fp1:
        anchore = fp1.readlines()
    count=len(anchore)
    print('A-C = ' , count)
    with open('C-A.csv','r') as fp8:
        clair=fp8.readlines()
    count=len(clair)
    print('C-A ',count)
    with open('Common.csv','r') as fp1:
        common = fp1.readlines()
    count=len(common)
    print('Common = ' , count)

if __name__== "__main__":
  main()
