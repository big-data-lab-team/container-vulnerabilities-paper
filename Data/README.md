# Commandlines used for the Anchore scanner

Download docker-compose.yaml file.
Go to the path where you have docker-compose.yaml file.

```
docker-compose up -d
docker-compose exec engine-api anchore-cli image add IMAGENAME:TAG
docker-compose exec engine-api anchore-cli image list
docker-compose exec engine-api anchore-cli image vuln IMAGENAME:TAG all

```
# Commandlines for using Clair scanner

Clone Clair scanner repository. Then install and build it.

Scan using following commands

```
docker run -p 5433:5432 -d --name db arminc/clair-db:2019-09-18

docker run -p 6060:6060 --link db:postgres -d --name clair arminc/clair-local-scan:v2.0.6

./clair-scanner  --ip YOUR_LOCAL_IP IMAGENAME:TAG

```
# Commandlines used for Vuls scanner

#### Step 1: Get required Docker images


```
docker pull vuls/go-cve-dictionary

docker pull vuls/goval-dictionary

docker pull vuls/gost

docker pull princechrismc/go-exploitdb

docker pull vuls/vuls
```

#### Step 2: Fetch Data feed

```
cd /path/to/working/dir
mkdir go-cve-dictionary-log goval-dictionary-log gost-log go-exploitdb-log

for i in `seq 2002 $(date +"%Y")`; do     docker run --rm -it     -v $PWD:/vuls     -v $PWD/go-cve-dictionary-log:/var/log/vuls     vuls/go-cve-dictionary fetchnvd -years $i;   done

docker run --rm -it     -v $PWD:/vuls     -v $PWD/goval-dictionary-log:/var/log/vuls     vuls/goval-dictionary fetch-redhat 5 6 7 
docker run --rm -it     -v $PWD:/vuls     -v $PWD/goval-dictionary-log:/var/log/vuls     vuls/goval-dictionary fetch-debian 7 8 9 10 
docker run --rm -it     -v $PWD:/vuls     -v $PWD/goval-dictionary-log:/var/log/vuls     vuls/goval-dictionary fetch-ubuntu 12 14 16 18
docker run --rm -it     -v $PWD:/vuls     -v $PWD/goval-dictionary-log:/var/log/vuls     vuls/goval-dictionary fetch-alpine 3.3 3.4 3.5 3.6 3.7 3.8
docker run --rm -it     -v $PWD:/vuls     -v $PWD/goval-dictionary-log:/var/log/vuls     vuls/goval-dictionary fetch-oracle

docker run --rm -i      -v $PWD:/vuls     -v $PWD/gost-log:/var/log/gost                vuls/gost fetch redhat --after=2010-01-01
docker run --rm -i      -v $PWD:/vuls     -v $PWD/gost-log:/var/log/gost                vuls/gost fetch debian


docker run --rm -i      -v $PWD:/vuls     -v $PWD/go-exploitdb-log:/var/log/go-exploitdb                princechrismc/go-exploitdb fetch 
docker run --rm -i      -v $PWD:/vuls     -v $PWD/go-exploitdb-log:/var/log/go-exploitdb                princechrismc/go-exploitdb fetch -deep 

```

#### Step 3: Scan


```

docker run -dt \ --name go-cve-dictionary \ -v $PWD:/vuls \ -v $PWD/go-cve-dictionary-log:/var/log/vuls \ --expose 1323 \ -p 1323:1323 \ vuls/go-cve-dictionary server --bind=0.0.0.0

docker run -dt \ --name goval-dictionary \ -v $PWD:/vuls \ -v $PWD/goval-dictionary-log:/var/log/vuls \ --expose 1324 \ -p 1324:1324 \ vuls/goval-dictionary server --bind=0.0.0.0

docker run -dt \ --name gost \ -v $PWD:/vuls \ -v $PWD/gost-log:/var/log/gost \ --expose 1325 \ -p 1325:1325 \ vuls/gost server --bind=0.0.0.0

docker run -dt     --name go-exploitdb     -v $PWD:/vuls     -v $PWD/go-exploitdb-log:/var/log/vuls     --expose 1326     -p 1326:1326     princechrismc/go-exploitdb server –bind=0.0.0.0

docker run -dt --name image1 --entrypoint /bin/bash IMAGE_TO_SCAN:TAG

docker run --rm -it \
    -v ~/.ssh:/root/.ssh:ro \
    -v $PWD:/vuls \
    -v $PWD/vuls-log:/var/log/vuls \
    -v /etc/localtime:/etc/localtime:ro \
    -v /etc/timezone:/etc/timezone:ro \
    vuls/vuls scan \
    -config=./config.toml # path to config.toml in docker
```

#### Step 4: Generate report

```
docker run --rm -it -v ~/.ssh:/root/.ssh:ro -v $PWD:/vuls -v $PWD/vuls-log:/var/log/vuls -v /etc/localtime:/etc/localtime:ro vuls/vuls report  --format-one-line-text -config=./config.toml


```

