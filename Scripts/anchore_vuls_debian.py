import csv
import sys
import os
import re
import numpy
import math
import pandas as pd


def default_package(info_file,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
    condition=None
    cves_default = list()
    df = pd.read_csv(info_file,delimiter=r"\s+")
    packages = df.Package
    cves = df.Vulnerability_ID
    for package in packages:
         if "linux-libc-dev" in package:
             defaulter=package
             break
    is_defaulter = df['Package']==defaulter
    defaulter_info = df[is_defaulter]
    cves = defaulter_info['Vulnerability_ID'] 
    unique_cves=set(cves)
    with open('defaulter.csv','w') as out:
            for entry in unique_cves:
                out.write(entry)
                out.write("\n")

def find_epoch(info_file,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
    condition=None
    cves=list()  
    df = pd.read_csv(info_file,delimiter=",",header=None)
    for l in lines:
        l = l.strip()
        for index, row in df.iterrows():
            if not pd.isnull(row[0]):
                if row[0].strip().endswith(l):
                    if not row[0].strip().startswith('TEMP'):
              #if l in row[0].strip():
                        if ":" in row[2].strip():
                          condition=True
                          break
        if condition:
            cves.append(l)
            condition=False
    unique_cves=set(cves)
    with open('epoch.csv','w') as out:
            for entry in unique_cves:
                out.write(entry)
                out.write("\n")

        #print(row['Vulnerability'], row['Package'])
    #package_version = df.Version
    #cves = df.Vulnerability
    #for l in lines:
    #    l=l.strip()
    #    if l in cves:

    #for version in package_version:
    #    if ":" in version:
    #         defaulter=package
    #         break
    #is_defaulter = df['Package']==defaulter
    #defaulter_info = df[is_defaulter]
    #cves = defaulter_info['Vulnerability_ID']
    #unique_cves=set(cves)
    #with open('defaulter.csv','w') as out:
    #        for entry in unique_cves:
    #            out.write(entry)
    #            out.write("\n")



def compare(file1,file2):
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
    dir_name = "./"
    test = os.listdir(dir_name)
    for item in test:
       if item.endswith(".csv"):
            os.remove(os.path.join(dir_name, item))
    file1=sys.argv[1]
    file2=sys.argv[2]
    file3=sys.argv[3]
    file4=sys.argv[4]
    count=0
    compare(file1,file2)
    default_package(file3,'A-V.csv')
    with open('A-V.csv','r') as fp1:
        anchore = fp1.readlines()
    count=len(anchore)
    print('A-V = ' , count)
    with open('defaulter.csv','r') as fp2:
        defaulter = fp2.readlines()
    count=len(defaulter)
    print('defaulter = ',count)
    with open('After_default.csv','w') as fp3:
        for cve in anchore:
            if cve not in defaulter:
                fp3.write(cve)
    with open('After_default.csv','r') as fp4:
        after_default=fp4.readlines()
    print('remaining ',len(after_default))
    print("\n")
    print('*********************************************************')
    print("\n")
    find_epoch(file4,'V-A.csv')
    with open('V-A.csv','r') as fp8:
        vuls=fp8.readlines()
    count=len(vuls)
    print('V-A ',count)
    with open('epoch.csv','r') as fp7:
        epoch=fp7.readlines()
    count=len(epoch)
    print('Epoch ',count)
    with open('After_epoch.csv','w') as fp9:
        for cve in vuls:
            if cve not in epoch:
                fp9.write(cve)
    with open('After_epoch.csv','r') as fp10:
          after_epoch=fp10.readlines()
    print('remaining ',len(after_epoch))
        
if __name__== "__main__":
  main()
