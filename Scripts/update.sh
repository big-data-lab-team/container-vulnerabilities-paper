#!/usr/bin/env bash

function die {
	echo $1
	exit 1
}

function find-pm {
		(type $1 &> /dev/null && echo "> Found $1") || \
		(echo "> $1 not found" && return 1)
}

\rm -f .updated
find-pm yum && (yum update -y && touch .updated)
find-pm apt && (apt update -y && apt upgrade -y && apt-get autoremove -y && apt-get autoclean -y && touch .updated)
test -f .updated || die "Cannot find package manager or update failed"
