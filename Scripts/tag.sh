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
	
	name1="$(cut -d'/' -f1 <<<"$image")"
	name2="$(cut -d'/' -f2 <<<"$image")"
        docker tag updated_${image} kaurbhupinder/${name1}_${name2}
        echo " tagged kaurbhupinder/${name1}_${name2}"
done
