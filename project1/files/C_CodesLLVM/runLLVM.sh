#!/bin/bash

# This script runs the program and generates the llvm code

echo "*-----------------EXECUTING LLVMFILES-----------------*"

FILES="*.ll"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
    FILE=${f##*/}
    FILE=${FILE%.*}
    echo "*---- START EXECUTING FILE: ${f##*/}" 
    lli $f > "$FILE.txt"

    
  else
    echo "Error trying to open or run \"$f\""
  fi
done

echo "*-----------------------FINISHED----------------------*"
