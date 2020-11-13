#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node

#cd ${_CONDOR_SCRATCH_DIR}
tar -xvf FileList.tar
pwd

python copy_to_cern.py $1
