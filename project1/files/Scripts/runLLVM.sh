#!/bin/bash

# This script runs the program and generates the llvm code

TOP="*-------------------------EXECUTING LLVMFILES-------------------------*"
echo $TOP

FILES="./files/GeneratedLLVM/*.ll"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
    FILE=${f##*/}
    FILE=${FILE%.*}
    LINE="*---- START EXECUTING FILE: ${f##*/}"
    LENL=$((${#TOP} - ${#LINE} - 2))
    LINE="$LINE "
    for i in $(seq 1 $LENL);
    do
    	CHECK=$(( $LENL - $i))
    	if (( $CHECK < 4))
    	then
    	    LINE="$LINE-";
    	else
    	    LINE="$LINE ";
    	fi
    done 
    LINE="$LINE*"
    echo "$LINE"
    lli $f > "files/outputLLVM/$FILE.txt"

    
  else
    echo "Error trying to open or run \"$f\""
  fi
done

echo "*-------------------------------FINISHED----------------------------*"
echo ""
