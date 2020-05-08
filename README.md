# Vulnerability-Analysis of container images
In experiment of minimizing images we are using a bunch of scripts.
So first of all we are taking original image and then installing
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

