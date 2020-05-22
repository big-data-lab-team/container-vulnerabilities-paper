#!/bin/bash

set -e


if [ $(dpkg-query -W -f='${Status}' reprozip 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  apt-get update -y;
  apt-get install python python-dev python-pip gcc libsqlite3-dev libssl-dev libffi-dev -y;
  pip install -U reprozip;
  if [ $(dpkg-query -W -f='${Status}' reprozip 2>/dev/null | grep -c "ok installed") -eq 0 ];
  then
    echo "Some problem occured: Cannot install Reprozip";
    command || exit 1;
  else
    echo "Reprozip installed successfully";
  fi
else
  echo "Reprozip was already installed"
fi

