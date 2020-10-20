#!/usr/bin/env python
import sys
from typing import Dict
from typing import Tuple


def domapping(rhsa2cve_file: str, rhsa_file: str, output_file: str) -> None:
    """Map Clair RHSA to CVE.
    Parameters
    ----------
    rhsa2cve_file : str
        Path to downloaded RHSA to CVE mapping file (rhsamapcpe.txt file in our case).
    rhsa_file : str
        Path to csv file containing RHSA to convert.
    output_file : str
        Path to csv file to write mapped CVEs.
    Returns
    -------
    None
    """
    cves: Dict[str, Tuple[str, str]] = {}

    with open(rhsa2cve_file, "r") as fin:
        words = map(str.split, fin.readlines())
        rhsa: Dict[str, Tuple[str, str]] = {
            word[4]: (word[3], word[6])
            for word in words
            if (len(word) > 1 and "|" not in [word[3], word[4]])
        }

    with open(rhsa_file, "r") as fin:
        lines = fin.readlines()

    for k, v in rhsa.items():
        for line in lines:
            if k in line:
                data = line.split()
                for cve in data[1].split(","):
                    cves[cve] = (v[0], v[1])

    with open(output_file, "w") as fout:
        fout.write("Vulnerability_ID     Package    Severity\n")
        for k, v in cves.items():
            fout.write(f"{k} {v[0]} {v[1]}\n")


if __name__ == "__main__":
    domapping(sys.argv[1], sys.argv[2], sys.argv[3])