import csv
import sys
import os
import re


def find_package(inFile,cve):
    with open(inFile, 'r') as file:
      file.readline() # skip the first line
      rows = [[str(x) for x in line.split('|')[:-1]] for line in file]
      cols = [list(col) for col in zip(*rows)]
    package = ""
    for row in rows:
        if len(row) > 1:
           split_cve = row[2].split()
           if len(split_cve) > 1:
                 only_cve=split_cve[1]
                 if only_cve == cve.strip():
                    package = row[3].strip()
                    break
    file.close()
    return package

def Linux_package(input_file,info_file):
    with open(input_file,'r') as inp:
        lines=inp.readlines()
    cves=list()
    for l in lines:
        l=l.strip()
        package=find_package(info_file,l)
        if package == "linux":
           cves.append(l)
    with open('default.csv','w') as out:
         for entry in cves:
                out.write(entry)
                out.write("\n")


def compare(file1,file2):
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


def main():
    dir_name = "./"
    test = os.listdir(dir_name)
    for item in test:
       if item.endswith(".csv"):
            os.remove(os.path.join(dir_name, item))
    file1=sys.argv[1]
    file2=sys.argv[2]
    file3=sys.argv[3]
    file4=sys.argv[4]
    compare(file1,file2)
    with open('V-C.csv','r') as fp1:
        vuls=fp1.readlines()
    print('V-C ',len(vuls))
    print('***************************************')
    with open('C-V.csv','r') as fp2:
        clair=fp2.readlines()
    print('C-V ',len(clair))
    Linux_package('C-V.csv',file3)
    with open('default.csv','r') as fp3:
        defaulter=fp3.readlines()
    print('Default package ',len(defaulter))
    with open('after_default.csv','w') as fp4:
        for cve in clair:
            if cve not in defaulter:
                fp4.write(cve)
    with open('after_default.csv','r') as fp5:
        after_default=fp5.readlines()
    print('After default ',len(after_default))

if __name__== "__main__":
  main()
