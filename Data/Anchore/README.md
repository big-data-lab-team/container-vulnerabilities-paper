# Commandlines used for the Anchore scanner

Download docker-compose.yaml file.
Go to the path where you have docker-compose.yaml file. 

```
docker-compose up -d
docker-compose exec engine-api anchore-cli image add IMAGENAME:TAG
docker-compose exec engine-api anchore-cli image list
docker-compose exec engine-api anchore-cli image vuln IMAGENAME:TAG all

```
