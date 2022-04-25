#!/bin/bash

# This script runs the testfiles

FILES="*.ll"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then
	
    filename="$f"
#    echo "#include <stdio.h>" > filename.c
 #   echo "int main() {" >> filename.c
#	
    echo ""
    echo "---------------------------------------------------"
    echo "Running: " $f
    echo ""
#    input="$f"
#    while read -r line
#      do
#        echo "$line" >> filename.c
#      done < "$input"
#
#    echo "return 0;}" >> filename.c

#    clang -S -emit-llvm filename.c
    # clang -cc1 foo.c -emit-llvm
    # -ast-print

    lli $f
    echo ""
    echo "Finished: " $f
    echo "---------------------------------------------------"
    echo ""

#    exit_status=$?
#    if [ "${exit_status}" -ne 0 ];
#    then
#      echo "$f : EXIT CODE ${exit_status}"
#    else
#      echo "$f : EXIT CODE 0"
#    fi
  else
    echo "Error trying to open or run \"$f\""
  fi
done



