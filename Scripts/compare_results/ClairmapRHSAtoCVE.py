import sys
import csv

targets =[]
cves = {}
rhsa={}
severity=''
def domapping(file1,file2,file3):
  with open(file1,'r') as f1, open(file2,'r') as f2:
      words = [line.split() for line in f2]
      lines=f1.readlines()
      for word in words:
          if(len(word) >1):
              if (word[3] != "|" and word[4] != "|"):
                        rhsa[word[4]]=[word[3],word[6]]
  for key in rhsa.keys():
        severity = rhsa[key][0]
        package = rhsa[key][1]
        for line in lines:
            if key in line:
                data = line.split() 
                for cve in data[1].split(','):
                    cves[cve]=[severity,package]
  with open(file3,'w') as out:
        out.write("Vulnerability_ID     Package    Severity\n")
        for key in cves.keys():
            st = key+"   "+cves[key][1]+"   "+cves[key][0]
            out.write("%s\n"%(st))
def main():
    file1=sys.argv[1]   ## downloaded RHSA to CVE mapping file (rhsamapcpe.txt file in our case)
    file2=sys.argv[2]   ## csv file containing RHSA to convert
    file3=sys.argv[3]   ## csv file to write mapped CVE's 
    domapping(file1,file2,file3)



if __name__== "__main__":
  main()
