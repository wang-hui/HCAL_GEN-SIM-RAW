#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
export SCRAM_ARCH=slc7_amd64_gcc700
echo $SCRAM_ARCH
eval `scramv1 project CMSSW CMSSW_10_6_12`
cd CMSSW_10_6_12/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
tar -xvf FileList.tar
pwd

#cmsRun step2_DIGI_L1_DIGI2RAW.py $1
#xrdcp step2.root root://cmseos.fnal.gov//${2}/UL_MC_RAW_noPU_${3}.root
#rm step2.root

cmsRun step2_DIGI_L1_DIGI2RAW_PU.py $1
xrdcp step2_PU.root root://cmseos.fnal.gov//${2}/UL_MC_RAW_PU_${3}.root
