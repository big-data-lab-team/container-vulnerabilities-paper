import csv
import sys
import os
import re

def getListOfFiles(dirName):
    listOfFiles=list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return listOfFiles




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

def get_end_of_life(listOfFiles,distro,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
        condition=None
        cves=list()
        for l in lines:
            l = l.strip()
            for elem in listOfFiles:
                if elem.endswith(l):
                   # flag=True
                   # print("found file")
                    with open(elem) as fp:
                         line =fp.readlines()
                    #package=find_package(clair_file,l)
                    #print(package)
                    for x in line:
                        if distro+"_" in x:
                            #print("found package")
                            if "reached end-of-life" in x:
                           # print("linux package")
                               condition=True
                               break
                    if condition:
                       # print("condition is met")
                        cves.append(l)
                       # with open('defaulter.csv','a') as out:
                       #      writer = csv.writer(out)
                       #      writer.write(l)
                       #      #out.write(l)
                        condition=False
                    break
    #with open('End_Of_Life.csv','w') as out:
    #        for entry in cves:
    #            out.write(entry)
    #            out.write("\n")
    return list(set(cves))


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

def not_affected(listOfFiles,distro,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
        condition=None
        cves=list()
        for l in lines:
            l = l.strip()
            for elem in listOfFiles:
                if elem.endswith(l):
                    with open(elem) as fp:
                         line =fp.readlines()
                    #package=find_package(clair_file,l)
                    for x in line:
                        if distro+"_" in x:
                            #print("found package")
                            if "not-affected" in x:
                           # print("linux package")
                               condition=True
                               break
                    if condition:
                       # print("condition is met")
                        cves.append(l)
                       # with open('defaulter.csv','a') as out:
                       #      writer = csv.writer(out)
                       #      writer.write(l)
                       #      #out.write(l)
                        condition=False
                    break
    required=list(set(cves))
    with open('Not_affected.csv','w') as out:
            for entry in required:
                out.write(entry)
                out.write("\n")

def get_ignored(listOfFiles,distro,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
        condition=None
        cves=list()
        for l in lines:
            l = l.strip()
            for elem in listOfFiles:
                if elem.endswith(l):
                    with open(elem) as fp:
                         line =fp.readlines()
                    #if distro+"/esm_" in line:
                    for x in line:
                            if distro+"_" in x:
                                if "ignored" in x:
                                   condition=True
                                   break
                    if condition:
                        cves.append(l)
                        condition=False
                    break
    required=list(set(cves))
    with open('End_Of_Life.csv','w') as out:
            for entry in required:
                out.write(entry)
                out.write("\n")

def clair_no_esm(listOfFiles,distro,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
        condition=None
        cves_remains=list()
        for l in lines:
            l = l.strip()
            for elem in listOfFiles:
                if elem.endswith(l):
                    with open(elem) as fp:
                         line =fp.readlines()
                    if distro+"/esm_" not in line:
                        condition=True
                    if condition:
                        cves_remains.append(l)
                        #with open('clair_remaining.csv','a') as out:
                        #     writer = csv.writer(out)
                        #     #writer.write(l)
                        #     out.write(l)
                        condition=False
                    break
    cves_required=list(set(cves_remains))
    with open('Esm_not_present.csv','w') as out:
        for entry in cves_required:
            out.write(entry)
            out.write("\n")

def extra_cliar(listOfFiles,distro,input_file,clair_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
        condition=None
        cves_remains=list()
        clair_status=['released','deferred','active','needed','released-esm','pending']
        for l in lines:
            l = l.strip()
            for elem in listOfFiles:
                if elem.endswith(l):
                    with open(elem) as fp:
                         line =fp.readlines()
                    package=find_package(clair_file,l)
                    if distro+"_"+package+":" not in line:
                        #print("only esm")
                        for x in line:
                            if distro+"/esm_"+package+":" in x:
                                if any(status in x for status in clair_status):  #check it
                                    condition=True
                                    break
                    elif distro+"_"+package+":" in line:
                        for x in line:
                            if distro+"_"+package+":" in x:
                                if "ignored" in x:
                                   condition=True
                                   break
                    if condition:
                        cves_remains.append(l)
                        #with open('clair_remaining.csv','a') as out:
                        #     writer = csv.writer(out)
                        #     #writer.write(l)
                        #     out.write(l)
                        condition=False
                    break
    cves_required=list(set(cves_remains))
    with open('Only_clair.csv','w') as out:
        for entry in cves_required:
            out.write(entry)
            out.write("\n")





def main():
    file1=sys.argv[1]
    file2=sys.argv[2]
    file3=sys.argv[3]
    distro=sys.argv[4]
    count =0
    listOfFiles=getListOfFiles("Downloads/Anchore_databases/ubuntu/ubuntu-cve-tracker")
    compare(file1,file2)
    with open('V-C.csv','r') as fp1:
        vuls=fp1.readlines()
    print('V-C ',len(vuls))
    with open('C-V.csv','r') as fp2:
        clair=fp2.readlines()
    print('C-V ',len(clair))
    #end_life=get_end_of_life(listOfFiles,distro,'V-C.csv')
    #with open('End-Of-Life.csv','w') as fp3:
    #     for cve in end_life:
    #         fp3.write(cve)
    #         fp3.write("\n")
    not_affected(listOfFiles,distro,'V-C.csv')
    with open('Not_affected.csv','r') as fp4:
        not_affect=fp4.readlines()
    print('Not affected ',len(not_affect))
    with open('After_effected.csv','w') as fp6:
        for cve in vuls:
            if cve not in not_affect:
                fp6.write(cve)
    get_ignored(listOfFiles,distro,'After_effected.csv')
    with open('After_effected.csv','r') as fp8:
        after_effect=fp8.readlines()
    #print('After effect ',len(after_effect))
    with open('End_Of_Life.csv','r') as fp5:
        end_life=fp5.readlines()
    print('End of Life ',len(end_life))
    with open('After_Life.csv','w') as fp7:
        for cve in after_effect:
            if cve not in end_life:
                   fp7.write(cve)
    with open('After_Life.csv','r') as fp9:
           after_life=fp9.readlines()
    #print('after life ',len(after_life))
    clair_no_esm(listOfFiles,distro,'After_Life.csv')
    with open('Esm_not_present.csv','r') as fp10:
        esm_not_present=fp10.readlines()
    print('Esm not present ',len(esm_not_present))
    extra_cliar(listOfFiles,distro,'C-V.csv',file3)
    with open('Only_clair.csv','r') as fp11:
         only_clair=fp11.readlines()
    print('Only clair ',len(only_clair))

if __name__== "__main__":
  main()
