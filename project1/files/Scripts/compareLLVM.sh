#!/bin/bash

# This script runs the program and generates the llvm code

TOP="*---------------------------COMPARE LLVMCODE--------------------------*"
echo $TOP
cd "files/"
FILES="outputLLVM/*.txt"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
    FILE=${f##*/}
    FILE=${FILE%.*}
    if cmp --silent -- "correctRunOutput/$FILE.txt" "outputLLVM/$FILE.txt"; then
       	    LINE="*---- $FILE IS CORRECT"
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
    else
            LINE="*---- $FILE IS NOT CORRECT"
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
    fi
  else
    echo "Error trying to open or run \"$f\""
  fi
done
cd ../
echo "*-------------------------------FINISHED------------------------------*"
echo ""
