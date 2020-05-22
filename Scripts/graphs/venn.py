#!/usr/bin/env python3
import csv
import sys
import os
import re


def compare(file1,file2,file3):
    with open(file1, 'r') as a, open(file2, 'r') as c, open(file3,'r') as v:
        anchore = a.readlines()
        clair = c.readlines()
        vuls= v.readlines()
    with open('A+C+V.csv', 'w') as f1:
        for line in anchore:
            if line in clair:
                if line in vuls:
                     f1.write(line)
    with open('A+C+V.csv','r') as f2:
        common=f2.readlines()
    with open('A+C.csv', 'w') as f3:
        for line in anchore:
               if line in clair:
                   if line not in vuls:
                       f3.write(line)
    with open('A+C.csv','r') as f4:
        ac=f4.readlines()
    with open('A.csv','w') as f5:
        for line in anchore:
            if line not in clair:
                if line not in vuls:
                    f5.write(line)
    with open('A.csv','r') as f6:
        a=f6.readlines()
    
    with open('C.csv','w') as f7:
        for line in clair:
            if line not in anchore:
                if line not in vuls:
                    f7.write(line)
    with open('C.csv','r') as f8:
        c=f8.readlines()


    with open('V.csv','w') as f9:
        for line in vuls:
            if line not in clair:
                if line not in anchore:
                    f9.write(line)
    with open('V.csv','r') as f:
        v=f.readlines()



    with open('A+V.csv', 'w') as f10:
        for line in anchore:
               if line in vuls:
                   if line not in clair:
                       f10.write(line)
    with open('A+V.csv','r') as f11:
        av=f11.readlines()

    with open('C+V.csv', 'w') as f12:
        for line in clair:
               if line in vuls:
                   if line not in anchore:
                       f12.write(line)
    with open('C+V.csv','r') as f13:
        cv=f13.readlines()

    print("A+C+V ",len(common))
    print("Anchore",len(a))
    print("Clair",len(c))
    print("Vuls",len(v))

    print("A+C",len(ac))
    print("A+V",len(av))
    print("C+V",len(cv))
    

def main():
    dir_name = "./"
    test = os.listdir(dir_name)
    for item in test:
       if item.endswith(".csv"):
            os.remove(os.path.join(dir_name, item))

    file1=sys.argv[1]
    file2=sys.argv[2]
    file3=sys.argv[3]
    compare(file1,file2,file3)

if __name__== "__main__":
  main()
