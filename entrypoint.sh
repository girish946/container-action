#!/bin/sh

echo "Hello $1"
file_exists=0

if test -f "$2"; then
    echo "$2 exists."
    file_exists=1
else
    exit 1
fi

file_contents=`cat $2`

echo "::set-output name=file_exists::$file_exists"
echo "::set-output name=file_contents::$file_contents"


dir_hash=`. /opt/venv/bin/activate && python get-hash.py .`
echo "::set-output name=dir_hash::$dir_hash"

export SERVICE_FILE=$2
export dir_hash
echo_log=`. /opt/venv/bin/activate && python echo-message.py $1`
echo "::set-output name=echo_log::$echo_log"
