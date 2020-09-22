#!/usr/bin/env python
import sys
from typing import List


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
    """
    targets: List[str] = list()

    with open(rhsa2cve_file, "r") as fin:
        words = fin.readlines()

    with open(rhsa_file, "r") as fin:
        lines = fin.readlines()

        for word in words:
            word = word.strip()
            print(word)

            for line in lines:
                if word in line:
                    targets.append(line.split()[1])

        cves = [cve for target in targets for cve in target.split(",")]

    req_cves = list(set(cves))
    with open(output_file, "w") as fout:
        for cve in req_cves:
            fout.write(cve + "\n")
            print(cve)


if __name__ == "__main__":
    domapping(sys.argv[1], sys.argv[2], sys.argv[3])
