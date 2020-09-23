import sys
import csv

targets =[]
cves = []
def domapping(file1,file2,file3):
  with open(file1,'r') as f1, open(file2,'r') as f2:
      words = f2.readlines()
      lines=f1.readlines()
      for word in words:
        word=word.strip()
        print(word)
        #targets.append([line for line in lines if word in line])
        for line in lines:
            if word in line:
                data = line.split() 
                targets.append(data[1])
      for target in targets:
        #print(target)
        target = target.split(',')
        for t in target:
            cves.append(t)
  req_cves = list(set(cves))
  with open(file3,'w') as f:
      for cve in req_cves:
          f.write(cve)
          f.write("\n")
          print(cve)

def main():
    file1=sys.argv[1]   ## downloaded RHSA to CVE mapping file (rhsamapcpe.txt file in our case)
    file2=sys.argv[2]   ## csv file containing RHSA to convert
    file3=sys.argv[3]   ## csv file to write mapped CVE's 
    domapping(file1,file2,file3)



if __name__== "__main__":
  main()
