# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
import csv
import sys
content = []
result = []
rhsa = {}
cves={}
def domapping(file1,file2):
    with open(file1,'r') as fp:
               rows = [line.split() for line in fp]
            #  rows=fp.readlines()
    del rows[0]
    for row in rows:
        vul = row[0]
        severity = row[2]
        package = row[1]
        print(vul)
        print(severity)
        print(package)
        rhsa[vul]= [package,severity]
        #rhsa[vul][1] = severity
        #row = row.strip()
    print(rhsa)
    print(len(rhsa))
    #Read the XML file
    with open("redhat.xml", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs(content, "lxml")
        for key, value in rhsa.items():
         vul = key
         severity = value[1]
         package = value[0]
         req_id = bs_content.find("reference", {"ref_id": vul})
         result = list(req_id.next_siblings)
         #print(result)
         for each in result:
           try:
               
               cves[each['ref_id']]=[package,severity]
               #cves[each['ref_id']][1]=severity
               print(each['ref_id'])
           except:
             continue
    print(cves)
    print(len(cves))
    #print(cves_req)
    #print(len(cves_req))
    with open(file2,'w') as out:
        out.write("Vulnerability_ID   Package   Severity\n")
        for key in cves.keys():
          st = key+"   "+cves[key][0]+"   "+cves[key][1]
          out.write("%s\n"%(st))
   #         for item in cves:
   #             out.write()
   #             out.write("\n")

def main():
    file1=sys.argv[1] ## csv file containing RHSA and needed to be mapped
    file2=sys.argv[2] ## csv file where mapped CVE needs to be written
    domapping(file1,file2)



if __name__== "__main__":
  main()
