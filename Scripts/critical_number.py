#!/usr/bin/env python
import csv
import sys
import os
import re
import pandas as pd

def main():
    inp=sys.argv[1]
    #csv.writer(open(r"abx.csv",'w'),delimiter=' ').writerows(filtered)
    df = pd.read_csv(inp,delimiter=r"\s+")
    isHigh=df['Severity'] == 'High'
    filtered=df[isHigh]
    unique_cves=filtered['Vulnerability_ID'].unique()
    #filtered = filter(lambda p: 'High' == p[1], df)
    print(len(unique_cves))
    #id=df.Vulnerability_ID
    #print(id)


if __name__== "__main__":
  main()
