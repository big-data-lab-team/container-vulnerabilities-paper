#!/usr/bin/env python


all = None
keep = None

with open('all-packages.csv', 'r') as f:
  all = f.readlines()

with open('uniq_keep_installed.csv', 'r') as f:
  keep = f.readlines()

hold = [ p.strip() for p in keep ]
str1 = ' '.join(str(e) for e in hold)
print("***********************************following packages should be held****************************")
print(str1)
remove = [ p.strip() for p in all if not p in keep ]
str3 = ' '.join(str(e) for e in remove)
print(str3)
print(len(remove))
for p in remove:
    print(p)

