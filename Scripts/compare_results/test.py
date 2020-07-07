#!/usr/bin/env python3

import csv
import sys
import os
import re

def find_epoch(inFile,input_file):
    with open(input_file,'r') as f:
        lines=f.readlines()
    new_list=list()
    for line in lines:
        new_list.append(line.strip())
    with open(inFile, 'r') as file:
      file.readline() # skip the first line
      rows = [[str(x) for x in line.split('|')[:-1]] for line in file]
      cols = [list(col) for col in zip(*rows)]
    epoch_cves=list()
    for row in rows:
        if len(row) > 1:
           if ":" in row[4].strip():
               cve=row[2].split()[1]
               if cve in new_list:
                   epoch_cves.append(cve)
    required_cves=list(set(epoch_cves))
    with open('epoch.csv','w') as out:
        for entry in required_cves:
            out.write(entry)
            out.write("\n")
    file.close()

def compare2(file1,file2):
    with open(file1, 'r') as t1, open(file2, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    
    with open('V-C.csv', 'w') as f1:
        for line in filetwo:
            if line not in fileone:
                f1.write(line)
    with open('C-V.csv', 'w') as f2:
        for line in fileone:
            if line not in filetwo:
                f2.write(line)
    with open('Common.csv', 'w') as f3:
        for line in fileone:
            if line in filetwo:
                f3.write(line)
def compare1(file1,file2):
    with open(file1, 'r') as t1, open(file2, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    with open('V-A.csv', 'w') as f1:
        for line in filetwo:
            if line not in fileone:
                f1.write(line)
    with open('A-V.csv', 'w') as f2:
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
    #compare(file1,file2)
    #with open('C-V.csv','r') as fp1:
    #    anchore = fp1.readlines()
    #count=len(anchore)
    #print('C-V = ' , count)
    #with open('V-C.csv','r') as fp8:
    #    clair=fp8.readlines()
    #count=len(clair)
    #print('V-C ',count)
    #with open('Common.csv','r') as fp1:
    #    common = fp1.readlines()
    #count=len(common)
    #print('Common = ' , count)
    ##################################################
    compare1(file1,file2)
    with open('V-A.csv','r') as fp1:
        anchore = fp1.readlines()
    count=len(anchore)
    print('V-A = ' , count)
    with open('A-V.csv','r') as fp8:
        clair=fp8.readlines()
    count=len(clair)
    print('A-V ',count)
    with open('Common.csv','r') as fp1:
        common = fp1.readlines()
    count=len(common)
    print('Common = ' , count)
    #################################################
    #find_epoch(file2,'C-A.csv')
    #with open('epoch.csv','r') as fp7:
    #    epoch=fp7.readlines()
    #count=len(epoch)
    #print('Epoch ',count)
if __name__== "__main__":
  main()
