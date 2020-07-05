#!/usr/bin/env python3
import csv
import sys
import os
import re


def compare(file1,file2):
    with open(file1, 'r') as a, open(file2, 'r') as c:
        anchore = a.readlines()
        clair = c.readlines()
    with open('A+C.csv', 'w') as f3:
        for line in anchore:
               if line in clair:
                       f3.write(line)
    with open('A+C.csv','r') as f4:
        ac=f4.readlines()
    with open('A.csv','w') as f5:
        for line in anchore:
            if line not in clair:
                    f5.write(line)
    with open('A.csv','r') as f6:
        a=f6.readlines()
    
    with open('C.csv','w') as f7:
        for line in clair:
            if line not in anchore:
                    f7.write(line)
    with open('C.csv','r') as f8:
        c=f8.readlines()


    print("Anchore",len(a))
    print("Clair",len(c))
    print("A+C",len(ac))
    

def main():
#    dir_name = "./"
#    test = os.listdir(dir_name)
#    for item in test:
#       if item.endswith(".csv"):
#            os.remove(os.path.join(dir_name, item))
#
    file1=sys.argv[1]
    file2=sys.argv[2]
    compare(file1,file2)

if __name__== "__main__":
  main()
