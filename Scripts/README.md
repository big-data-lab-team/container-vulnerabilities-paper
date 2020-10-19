
The script in `update` was used to update container images:
```
./update-images.sh bids/example:latest bids/freesurfer:latest
```

The script in `minification` was used for minification:
```
./run_script.sh FULL_PATH_TO_DATASET IMAGENAME:TAG

```

The FULL_PATH_TO_DATASET represents the full path to the dataset which
is required to be processed by the container.
This dataset should contains ```scripts``` folder where following
scripts should be kept (these scripts are present in minification folder ):
check_virtuality.py
run_repro_script.sh 
script.sh 
to_delete.py

