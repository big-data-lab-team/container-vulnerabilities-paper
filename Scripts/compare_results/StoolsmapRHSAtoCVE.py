import sys
import csv

def domapping(rhsa2cve_file: str, rhsa_file: str, output_file: str) -> None:
  """Convert the Stools RHSA to CVE.
    Parameters
    ----------
    rhsa2cve_file : str
        Path to downloaded RHSA to CVE mapping file (rhsamapcpe.txt file in our case).
    rhsa_file : str
        Path to csv file containing RHSA to convert.
    output_file : str
        Path to csv file to write mapped CVEs.
    -------
    None
  """
  rhsa: Dict[str, str] = {}
  cves: Dict[str, str] = {}

  with open(rhsa2cve_file,'r') as fin:
      lines=fin.readlines()

  with open(rhsa_file,'r') as fin:
      words = list(map(str.split,fin.readlines()))

      for word in words:
          if (len(word) == 2):
                vul, severity = [word[r] for r in (0,1)]
                rhsa[vul] = severity 
  
  for k,v in rhsa.items():
        for line in lines:
            if k in line:
                data = line.split()
                for cve in data[1].split(','):
                    cves[cve]=v
  with open(output_file,'w') as fout:
        fout.write("Vulnerability_ID   Severity\n")
        for k,v in cves.items():
            val = v.split("(")[1].split(")")[0]
            fout.write(f"{k} {val}\n")
def main():
    domapping(sys.argv[1],sys.argv[2],sys.argv[3])



if __name__== "__main__":
  main()
