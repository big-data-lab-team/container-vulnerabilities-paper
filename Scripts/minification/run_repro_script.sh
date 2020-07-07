#!/bin/bash

set -e


if [ $(dpkg-query -W -f='${Status}' reprozip 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt-get update -y;
  apt-get install python python-dev python-pip gcc libsqlite3-dev libssl-dev libffi-dev -y;
  pip install -U reprozip;
fi
