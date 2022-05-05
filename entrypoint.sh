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