#!/usr/bin/env python
import sys
from typing import Dict
from typing import Tuple

from bs4 import BeautifulSoup as bs


def domapping(input_file: str, output_file: str) -> None:
    """Convert the Anchore RHSA to CVE.
    Parameters
    ----------
    input_file : str
        Path to csv file containing RHSA and needed to be mapped.
    output_file : str
        Path to csv file where mapped CVE needs to be written.
    Returns
    -------
    None
    """
    cves: Dict[str, Tuple[str, str]] = {}
    rhsa: Dict[str, Tuple[str, str]] = {}

    with open(input_file, "r") as fin:
        rows = list(map(str.split, fin.readlines()))

        for row in rows[1:]:
            vul, severity, package = row
            rhsa[vul] = (package, severity)

    with open("redhat.xml", "r") as fin:
        content = "".join(fin.readlines())
        bs_content = bs(content, "lxml")

        for k, v in rhsa.items():
            req_id = bs_content.find("reference", {"ref_id": k})
            results = list(req_id.next_siblings)

            for result in results:
                if "ref_id" in result:
                    cves[result["ref_id"]] = (v[0], v[1])

    with open(output_file, "w") as fout:
        fout.write("Vulnerability_ID   Package   Severity\n")
        for k, v in cves.items():
            fout.write(f"{k} {v[0]} {v[1]}\n")


if __name__ == "__main__":
    domapping(sys.argv[1], sys.argv[2])