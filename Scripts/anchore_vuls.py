import csv
import sys
import os
import re


'''
    For the given path, get the List of all files in the directory tree
'''
def getListOfFiles(dirName):
    listOfFiles=list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return listOfFiles

def default_package(listOfFiles,distro,input_file):
    with open(input_file,'r') as myfile:
        lines = myfile.readlines()
    condition=None
    cves_default = list()
    for l in lines:
            l = l.strip()
            for elem in listOfFiles:
                if elem.endswith(l):
                    with open(elem) as fp:
                         line =fp.readlines()
                    for x in line:
                        if "_linux" in x:
                            condition=True
                            break
                    if condition:
                        cves_default.append(l)
                        condition=False
                    break
    cves_required=list(set(cves_default))
    with open('defaulter.csv','w') as out:
            for entry in cves_required:
                out.write(entry)
                out.write("\n")

def find_epoch(listOfFiles,input_file,distro):
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
                    for x in line:
                        if distro+"_" in x:
                            splitted = x.split('(')
                            if len(splitted) > 1:
                                if ":" in splitted[1]:
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
    cves_required=list(set(cves))
    with open('epoch.csv','w') as out:
        for entry in cves_required:
            out.write(entry)
            out.write("\n")

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


def out_standard_support(listOfFiles,distro,input_file):
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
                    for x in line:
                        if distro+"_" in x:
                            if "out of standard support" in x:
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
    cves_required=list(set(cves))
    with open('Out_of_standard.csv','w') as out:
            for entry in cves_required:
                out.write(entry)
                out.write("\n")



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


def main():
    dir_name = "./"
    test = os.listdir(dir_name)
    for item in test:
       if item.endswith(".csv"):
            os.remove(os.path.join(dir_name, item))
    file1=sys.argv[1]
    file2=sys.argv[2]
    distro=sys.argv[3]
    count=0
    listOfFiles=getListOfFiles("../Database/Anchore_databases/ubuntu/ubuntu-cve-tracker")
    compare(file1,file2)
    default_package(listOfFiles,distro,'A-V.csv')
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
    #count=len(after_default)
    #print('After defaulter package ',count)
    anchore_cves = get_end_of_life(listOfFiles,distro,'After_default.csv')
    with open('End_Of_Life.csv','w') as out:
        for entry in anchore_cves:
            out.write(entry)
            out.write("\n")

    with open('End_Of_Life.csv','r') as fp5:
        end_of_life=fp5.readlines()
    count=len(end_of_life)
    print('End of Life ',count)
    with open('After_end_of_Life.csv','w') as fp6:
        for cve in after_default:
           if cve not in end_of_life:
              fp6.write(cve)
    with open('After_end_of_Life.csv','r') as inp:
        after_end_life=inp.readlines()
    count=len(after_end_life)
    print('After end of life ',count)
    print("\n")
    print('*********************************************************')
    print("\n")
    find_epoch(listOfFiles,'V-A.csv',distro)
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
    out_standard_support(listOfFiles,distro,'After_epoch.csv')
    with open('After_epoch.csv','r') as fp10:
          after_epoch=fp10.readlines()
    with open('Out_of_standard.csv','r') as fp11:
         out_of_standard=fp11.readlines()
    count=len(out_of_standard)
    print('out of standard ',count)
    with open('After_out_support.csv','w') as fp12:
         for cve in after_epoch:
             if cve not in out_of_standard:
                 fp12.write(cve)
    with open('After_out_support.csv','r') as fp13:
           after_out_standard=fp13.readlines()
    not_affected(listOfFiles,distro,'After_out_support.csv')
    with open('Not_affected.csv','r') as fp14:
        not_affect=fp14.readlines()
    print('Not-affected ',len(not_affect))
    with open('After_effect.csv','w') as fp15:
        for cve in after_out_standard:
            if cve not in not_affect:
                fp15.write(cve)
    with open('After_effect.csv','r') as fp16:
         after_effect=fp16.readlines()
    print('remaining ',len(after_effect))
        





if __name__== "__main__":
  main()
