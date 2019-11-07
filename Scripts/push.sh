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

docker login -u kaurbhupinder
for image in $*
do
	
	name1="$(cut -d'/' -f1 <<<"$image")"
	name2="$(cut -d'/' -f2 <<<"$image")"
	#if [[ ${image} =~ ":" ]]
        #then 
        #     tag="$(cut -d':' -f2 <<<"$image")"
        #else
	#     tag="latest"
	#fi
        docker push kaurbhupinder/${name1}_${name2} 
        echo " pushed kaurbhupinder/${name1}_${name2}"
done
