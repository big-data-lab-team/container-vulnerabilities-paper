In experiment of minimizing images we are using a bunch of scripts.
So first of all we are taking original image and then installing
Reprozip tool inside that image. After that we are using a bash script
to run that image (which has Reprozip installed in it) and get
Reprozip trace inside the image. So now as we have a list of
packages that are necessary for the pipeline to function.
Now run instance of original image (without Reprozip) again
and place following scripts in mounted volume:
script.sh
check_virtuality.py
to_delete.py
Also place the necessary list of packages that you got from
packages in the mounted volume in required.csv
Python 2.7.3 or greater, or 3.3 or greater is required to run ReproZip
## Steps to install Reprozip
### 1.Get required dependencies
#### For Debian and Ubuntu
```
apt-get install python python-dev python-pip gcc libsqlite3-dev libssl-dev libffi-dev

```
### For Fedora and CentOS
```
yum install python python-devel gcc sqlite-devel openssl-devel libffi-devel
```
### 2. Install Reprozip
```
pip install -U reprozip
```
