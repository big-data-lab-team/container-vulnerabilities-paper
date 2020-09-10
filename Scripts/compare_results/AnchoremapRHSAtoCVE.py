# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
import csv
import sys
content = []
result = []
cves = []
def domapping(file1,file2):
    with open(file1,'r') as fp:
              rows=fp.readlines()
    for row in rows:
        row = row.strip()
    
    #Read the XML file
    with open("redhat.xml", "r") as file:
        # Read each line in the file, readlines() returns a list of lines
        content = file.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = bs(content, "lxml")
        for row in rows:
         row = row.strip()
         req_id = bs_content.find("reference", {"ref_id": row})
         result = list(req_id.next_siblings)
         for each in result:
           try:
               cves.append(each['ref_id'])
               print(each['ref_id'])
           except:
             continue
    cves_req = list(set(cves))
    #print(cves_req)
    #print(len(cves_req))
    with open(file2,'w') as out:
            for entry in cves_req:
                out.write(entry)
                out.write("\n")

def main():
    file1=sys.argv[1] ## csv file containing RHSA and needed to be mapped
    file2=sys.argv[2] ## csv file where mapped CVE needs to be written
    domapping(file1,file2)



if __name__== "__main__":
  main()
