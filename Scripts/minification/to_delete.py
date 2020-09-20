#!/usr/bin/env python
with open("all-packages.csv", "r") as fin:
    packages = fin.readlines()

with open("uniq_keep_installed.csv", "r") as fin:
    keep = fin.readlines()

remove = [package.strip() for package in packages if package not in keep]
removed_packages: str = " ".join(str(e) for e in remove)

with open("to_remove.txt", "w") as f:
    f.write(removed_packages)

print(removed_packages)
print(len(remove))
