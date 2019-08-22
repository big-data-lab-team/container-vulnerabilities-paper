#!/usr/bin/env bash

set -ue

function usage {
	echo "$0 <image_list>"
	exit 1
}

if [ $# -lt 1 ]
then
	usage
fi

for image in $*
do
	echo -n "Updating image ${image}... "
	docker run -e /bin/bash -v $PWD:$PWD -w $PWD ${image} ./update.sh &>${image}.log && echo "[ OK ]"
	echo -n "Commiting updated image... "
	ID=$(docker ps -a | head -2 | awk '$1!="CONTAINER" {print $1}')
	docker commit ${ID} updated_${image} && echo "[ OK ]"
done
