#!/bin/bash

# This script runs the testfiles

cd ./testfiles
python3 A_inputfile2
exit_status=$?
if [ "${exit_status}" -ne 0 ];
then
    echo "exit ${exit_status}"
fi
echo "EXIT 0"