#!/bin/bash

# This script runs the testfiles

FILES="./testfiles/*.c"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
    python3 "main.py" $f
    exit_status=$?
    if [ "${exit_status}" -ne 0 ];
    then
      echo "exit ${exit_status}"
    else
      echo "EXIT 0"
    fi
  else
    echo "Error trying to open or run \"$f\""
  fi
done


