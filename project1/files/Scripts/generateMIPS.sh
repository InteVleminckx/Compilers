#!/bin/bash

# This script runs the program and generates the llvm code
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
TOP="*------------------------GENERATING MIPSFILES-------------------------*"
echo $TOP

FILES="./files/C_CodesMIPS/*.c"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
	    FILE=${f##*/}
    	    FILE=${FILE%.*}
       	    LINE="*---- $FILE"
	    LENL=$((${#TOP} - ${#LINE} - 14))
	    LINE="$LINE "
	    for i in $(seq 1 $LENL);
	    do
	    	CHECK=$(( $LENL - $i))
	        if (( $CHECK == 4))
	    	then
	    	    LINE="$LINE ${GREEN}[GENERATED]${NC} ";
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
    python3 "/home/inte/PycharmProjects/Compilers/project1/main.py" $f " False" "True" > "./files/outputMIPS/$FILE.txt"

     


  else
   	    LINE="*---- $FILE"
	    LENL=$((${#TOP} - ${#LINE} - 10))
	    LINE="$LINE "
	    for i in $(seq 1 $LENL);
	    do
	    	CHECK=$(( $LENL - $i))
	        if (( $CHECK == 4))
	    	then
	    	    LINE="$LINE ${RED}[FAILED]${NC} ";
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
done

echo "*-------------------------------FINISHED------------------------------*"
echo ""
