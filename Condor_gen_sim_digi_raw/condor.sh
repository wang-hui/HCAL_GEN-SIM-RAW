#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
export SCRAM_ARCH=slc7_amd64_gcc700
echo $SCRAM_ARCH
eval `scramv1 project CMSSW_10_6_12`
cd CMSSW_10_6_12/src
eval `scramv1 runtime -sh`
#curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HCA-RunIISpring18GS-00011 --retry 3 --create-dirs -o Configuration/GenProduction/python/HCA-RunIISpring18GS-00011-fragment.py
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/PPD-RunIISummer19ULPrePremix-00004 --retry 3 --create-dirs -o ../Configuration/GenProduction/python/PPD-RunIISummer19ULPrePremix-00004-fragment.py
cd ${_CONDOR_SCRATCH_DIR}

#cmsRun QCD_GENToHLT_2018_cfg.py $1
cmsRun NuGun_GENToHLT_2018_cfg.py $1

xrdcp RAW_PU.root root://cmseos.fnal.gov//${2}/RAW_PU${1}.root
