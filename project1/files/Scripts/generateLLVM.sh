#!/bin/bash

# This script runs the program and generates the llvm code

TOP="*------------------------GENERATING INPUTFILES------------------------*"
echo $TOP

FILES="./files/C_CodesLLVM/*.c"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
	
    LINE="*---- START GENERATING FILE: ${f##*/}.ll" 
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
    python3 "/home/inte/PycharmProjects/Compilers/project1/main.py" $f
    
     


  else
    echo "Error trying to open or run \"$f\""
  fi
done

echo "*-------------------------------FINISHED------------------------------*"
echo ""
