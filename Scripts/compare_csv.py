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


def out_standard_support(listOfFiles,distro,input_file,clair_file):
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
                    package=find_package(clair_file,l)
                    for x in line:
                        if distro+"_"+package+":" in x:
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

def get_end_of_life(listOfFiles,distro,input_file,clair_file):
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

def clair_esm(listOfFiles,distro,input_file,clair_file):
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
                                if "reached end-of-life" in x:
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
    with open('clair_remaining.csv','w') as out:
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
    default_package(listOfFiles,distro,'A-C.csv')
    with open('A-C.csv','r') as fp1:
        anchore = fp1.readlines()
    count=len(anchore)
    print('A-C = ' , count)
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
    anchore_cves = get_end_of_life(listOfFiles,distro,'After_default.csv',file3)
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
    find_epoch(file3,'C-A.csv')
    with open('C-A.csv','r') as fp8:
        clair=fp8.readlines()
    count=len(clair)
    print('C-A ',count)
    with open('epoch.csv','r') as fp7:
        epoch=fp7.readlines()
    count=len(epoch)
    print('Epoch ',count)
    with open('After_epoch.csv','w') as fp9:
        for cve in clair:
            if cve not in epoch:
                fp9.write(cve)
    out_standard_support(listOfFiles,distro,'After_epoch.csv',file3)
    with open('After_epoch.csv','r') as fp10:
          after_epoch=fp10.readlines()
    #count=len(after_epoch)
    #print('after epoch ',count)
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
    #count=len(after_out_standard)
    #print('After out of standard ',count)
    #with open('C-A','r') as fp3:
    #    clair=fp3.readlines()
    #with open('Out_of_standard.csv','r') as fp1, open('','r') as fp2:
    #    standard_out=fp1.readlines()
    #    epoch=fp2.readlines()
    #    for cve in clair:
    #        if cve not in standard_out:
    #            if cve not in 
    clair_esm(listOfFiles,distro,'After_out_support.csv',file3)
    with open('clair_remaining.csv','r') as fp14:
        after_standard=fp14.readlines()
    count=len(after_standard)
    print('ignored or not in LTS ',count)


if __name__== "__main__":
  main()
