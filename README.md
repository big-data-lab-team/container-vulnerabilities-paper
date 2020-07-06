# Vulnerability-Analysis of container images

Here, we conducted different image scanning experiments to analyze vulnerability inside
BIDS and Boutiques images that are used in neuroimaging field.

## Experiment 1: Scanning Original images as is:
Here, simply we added Docker images to scanners like Anchore,
Vuls, and Clair and Singularity images to Stools. 

## Experiment 2: Updating images and then rescanning
Here, we used a bash script to update all images. This script is
available in scripts/update folder. 
#### Usage 
1. Get both scripts from scripts/update folder
2. Run bash script update-images.sh in bash followed by a list
of image names that you want to update. This script will
call another bash script (update.sh) inside itself.
```
./update-images.sh bids/example:latest bids/freesurfer:latest
```
## Experiment 3: Minimizing images and then rescanning
To minimize images also we used bash scripts.
These scripts are available in scripts/minimification folder names.
The main script is run\_script.sh and other scripts are called by it automatically. 
Here, in this script you need to change commands cmd1, cmd2, and cmd3 to your image specific
commands.
This script takes two parameters. First one is the full path of
the dataset that is needed to run pipeline and second one is full image name along with the tag
that you want to run.
Others scripts in scripts/minification folder should be placed in ``scripts`` folder
in dataset that you mounted in image. Nohup can be used to run this script because
pipeline can take sveral hours to finish. Command line to run minimization is as follows:

```
nohup ./run_script.sh FULL_PATH_TO_DATASET IMAGENAME:TAG > nohup.out &

```
For example:

```
nohup ./run_script.sh /home/bhupinder_kaur/BMB_1/ bids/freesurfer:latest > nohup.out &

```
