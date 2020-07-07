import pandas as pd
import csv

with open('mindboggle_vendorfalse_info.csv', "r") as f:
        reader = csv.reader(f, delimiter=" ")
        filtered = filter(lambda x: x[1] in ("linux-libc-dev-3.16.43-2"), list(reader))
uni=list()
for row in filtered:
    uni.append(row[0])
req=list(set(uni))
print(len(req))
