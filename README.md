# Vulnerability-Analysis of container images

Here we conducted four experiments to analyze vulnerability inside
BIDS and Boutiques images that are used in neuroimaging field.

## Experiment 1: Scanning Original images as is:
Here simply we added all these images to scanners like Anchore,
Vuls and Clair Scanner and got the results.

## Experiment 2: Updating images and then rescanning
Here we used a bash script to update all images. This script is
available in scripts/update folder. 
#### Usage 
1. Get both scripts in scripts/update folder
2. Run bash script update-images.sh in bash followed by a list
of image names that you want to update. This script will
call another bash script (update.sh) inside itself.
```
./update-images.sh bids/example:latest bids/freesurfer:latest
```
## Experiment 3: Minimizing images and then rescanning
In this third experiment to minimize images also we used a bash script.
This script is available in scripts/minimification folder

In experiment of minimizing images we are using a bunch of scripts.
So first of all we are taking origin{list of images that you want to update}al image and then installing
Reprozip tool inside that image. After that we are using a bash script
to run that image (which has Reprozip installed in it) and get
Reprozip trace inside the image. So after that we get a list of
packages that are necessary for the pipeline to function.

## Steps to install Reprozip
Python 2.7.3 or greater, or 3.3 or greater is required to run ReproZip.
### 1.Get required dependencies
#### For Debian and Ubuntu
```
apt-get install python python-dev python-pip gcc libsqlite3-dev libssl-dev libffi-dev

```
#### For Fedora and CentOS
```
yum install python python-devel gcc sqlite-devel openssl-devel libffi-devel
```
### 2. Install Reprozip
```
pip install -U reprozip
```
## Example of getting Reprozip trace from image
Below is the example of running bids/freesurfer image (that has Reprozip installed inside it) to get Reprozip trace. Similarly all other images can be run accordingly by changing data and commands that need to be run inside them
```
#!/bin/bash
export DOCKER_FLAG='-v /home/bhupinder_kaur/BMB_1:/data:ro -v /home/bhupinder_kaur/freesurfer_out:/outputs -v /home/bhupinder_kaur/license.txt:/license.txt'
export cmd1='python3 /run.py /data /outputs participant --participant_label 0003001 0003002 --license_file /license.txt'
export cmd2='python3 /run.py /data /outputs group1 --participant_label 0003001 0003002 --license_file /license.txt'
export cmd3='python3 /run.py /data /outputs group2 --participant_label 0003001 0003002 --license_file /license.txt'
docker run -itd --entrypoint="bash" --name surfer --security-opt seccomp=unconfined $DOCKER_FLAG freesurfer:reprozip
docker exec -i surfer bash -c "reprozip trace --overwrite $cmd1"
docker exec -i surfer bash -c "reprozip trace --continue $cmd2"
docker exec -i surfer bash -c "reprozip trace --continue $cmd3"
echo "its done"

```
Now the reprozip trace is generated and it can be found inside image in ./reprozip-trace/config.yaml
