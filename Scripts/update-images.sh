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
	name1="$(cut -d'/' -f1 <<<"$image")"
	name2="$(cut -d'/' -f2 <<<"$image")"
	name="$(cut -d':' -f1 <<<"$name2")"
	#docker run -e /bin/bash -v $PWD:$PWD -w $PWD ${image} ./update.sh &>${image}.log && echo "[ OK ]"
        docker run -v $PWD:$PWD -w $PWD --entrypoint /bin/bash ${image} ./update.sh &>${name1}_${name}.log && echo "[ OK ]"
        #docker run -it --entrypoint /bin/bash ${image} ./update.sh &>${image}.log && echo "[ OK ]"
	echo -n "Commiting updated image... "
	ID=$(docker ps -a | head -2 | awk '$1!="CONTAINER" {print $1}')
	docker commit ${ID} updated_${image} && echo "[ OK ]"
done
