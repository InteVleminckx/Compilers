#!/bin/bash

# This script runs the program and generates the llvm code
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
TOP="*---------------------------COMPARE MIPSCODE--------------------------*"
echo $TOP
cd "files/"
FILES="correctRunOutputMIPS/*.asm"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
    FILE=${f##*/}
    FILE=${FILE%.*}
    if cmp --silent -- "correctRunOutputMIPS/$FILE.asm" "GeneratedMIPS/$FILE.asm"; then
       	    LINE="*---- $FILE"
	    LENL=$((${#TOP} - ${#LINE} - 10))
	    LINE="$LINE "
	    for i in $(seq 1 $LENL);
	    do
	    	CHECK=$(( $LENL - $i))
	        if (( $CHECK == 4))
	    	then
	    	    LINE="$LINE ${GREEN}[EQUAL]${NC} ";
	    	else
    		    if (( $CHECK < 4))
    		    then
	    	    	LINE="$LINE-";
    		    else
	    	    	LINE="$LINE ";
    		    fi
	    	fi

	    done 
	    LINE="$LINE*"
	    echo -e "$LINE"
    else
       	    LINE="*---- $FILE"
	    LENL=$((${#TOP} - ${#LINE} - 10))
	    LINE="$LINE "
	    for i in $(seq 1 $LENL);
	    do
	    	CHECK=$(( $LENL - $i))
	        if (( $CHECK == 4))
	    	then
	    	    LINE="$LINE ${RED}[FAULT]${NC} ";
	    	else
    		    if (( $CHECK < 4))
    		    then
	    	    	LINE="$LINE-";
    		    else
	    	    	LINE="$LINE ";
    		    fi
	    	fi

	    done 
	    LINE="$LINE*"
	    echo -e "$LINE"
    fi
  else
    echo "Error trying to open or run \"$f\""
  fi
done
cd ../
echo "*-------------------------------FINISHED------------------------------*"
echo ""
