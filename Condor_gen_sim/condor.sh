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

cmsRun Pion_gun_cfi_GEN_SIM.py $1

xrdcp step1.root root://cmseos.fnal.gov//${2}/Run3_RelVal_1TeV_pion_gun_GEN_SIM_${1}.root
