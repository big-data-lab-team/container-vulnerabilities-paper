### These are the commandlines for the images that we minified:

#### bids/example

```
cmd1='python3 /run.py /data /data/outputs participant --participant_label 01 02'
cmd2='python3 /run.py /data /data/outputs group'
```

#### bids/freesurfer
```
cmd1='python3 /run.py /data /data/outputs participant --participant_label 0003001 0003002 --license_file /data/license.txt'
cmd2='python3 /run.py /data /data/outputs group1 --participant_label 0003001 0003002 --license_file /data/license.txt'
cmd3='python3 /run.py /data /data/outputs group2 --participant_label 0003001 0003002 --license_file /data/license.txt'
```

#### bids/ndmg
```
cmd1='ndmg_bids /data data/outputs participant --participant_label 123'
```

#### bids/mindboggle:0.0.4-1
```
cmd1='python /opt/bids-mindboggle/run.py /home/jovyan/work/data /home/jovyan/work/data/derivatives/ participant --participant_label 01'
```

#### poldracklab/fmriprep:1.2.3
```
cmd1='/usr/local/miniconda/bin/fmriprep /data /data/outputs participant --participant_label 01 --fs-license-file /data/license.txt'
```
