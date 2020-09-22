#!/usr/bin/env python
import sys
from typing import List

from bs4 import BeautifulSoup as bs


def domapping(input_file: str, output_file: str) -> None:
    """Convert the Anchore RHSA to CVE.

    Parameters
    ----------
    input_file : str
        Path to csv file containing RHSA and needed to be mapped.
    output_file : str
        Path to csv file where mapped CVE needs to be written.
    """
    cves: List[str] = []

    with open(input_file, "r") as fin:
        rows = map(str.strip, fin.readlines())

    with open("redhat.xml", "r") as fin:
        content = "".join(fin.readlines())

        bs_content = bs(content, "lxml")

        for row in rows:
            req_id = bs_content.find("reference", {"ref_id": row.strip()})
            results = list(req_id.next_siblings)

            for result in results:
                if "ref_id" in result:
                    cves.append(result["ref_id"])
                    print(result["ref_id"])

    cves_req = list(set(cves))

    with open(output_file, "w") as fout:
        for entry in cves_req:
            fout.write(entry + "\n")


if __name__ == "__main__":
    domapping(sys.argv[1], sys.argv[2])
