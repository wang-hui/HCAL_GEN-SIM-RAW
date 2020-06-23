#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
#export SCRAM_ARCH=slc6_amd64_gcc630
echo $SCRAM_ARCH
eval `scramv1 project CMSSW CMSSW_11_1_0_pre8`
cd CMSSW_11_1_0_pre8/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
tar -xvf FileList.tar
pwd

cmsRun step2_DIGI_L1_DIGI2RAW.py $1
cmsRun step2_DIGI_L1_DIGI2RAW_PU.py $1

xrdcp step2.root root://cmseos.fnal.gov//${2}/Run3_RelVal_1TeV_pion_gun_RAW_${3}.root
xrdcp step2_PU.root root://cmseos.fnal.gov//${2}/Run3_RelVal_1TeV_pion_gun_RAW_PU65_${3}.root
