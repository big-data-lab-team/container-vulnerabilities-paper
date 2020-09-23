# Commandlines for using Clair scanner

Clone Clair scanner repository. Then install and build it.

Scan using following commands

```
docker run -p 5433:5432 -d --name db arminc/clair-db:2019-09-18

docker run -p 6060:6060 --link db:postgres -d --name clair arminc/clair-local-scan:v2.0.6

./clair-scanner  --ip YOUR_LOCAL_IP IMAGENAME:TAG

```
