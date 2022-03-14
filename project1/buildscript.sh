#!/bin/bash

# This script runs the testfiles

FILES="./testfiles/A*.c"
for f in $FILES
do
# Check if "$f" FILE exists and is a regular file and then only copy it #
  if [ -f "$f" ]
  then

    filename = "complete_$f"
    echo "#include <stdio.h>\n" >> filename
    echo "int main() {\n" >> filename

    input="$f"
    while read -r line
      do
        echo "$line" >> filename
      done < "$input"

    echo "return 0;}" >> filename

    clang -S -emit-llvm filename
    # clang -cc1 foo.c -emit-llvm
    # -ast-print

    python3 "main.py" $f
    exit_status=$?
    if [ "${exit_status}" -ne 0 ];
    then
      echo "$f : EXIT CODE ${exit_status}"
    else
      echo "$f : EXIT CODE 0"
    fi
  else
    echo "Error trying to open or run \"$f\""
  fi
done


