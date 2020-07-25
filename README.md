# HCAL GEN-SIM-RAW ntuple production  

This is the branch for 2018 GEN-SIM-RAW production. For Run3 production, please go to the CMSSW_11_1_x branch  

1. setup CMSSW.  
```
cmsrel CMSSW_10_2_12_patch1
cd CMSSW_10_2_12_patch1/src
cmsenv
```

2. checkout this repo
```
git clone https://github.com/wang-hui/HCAL_GEN-SIM-RAW.git
cd HCAL_GEN-SIM-RAW
```

3. local test
```
cmsRun Pion_gun_cfi_GEN_SIM.py #produce GEN-SIM
cmsRun step2_DIGI_L1_DIGI2RAW.py #produce RAW with 0 PU
cmsRun step2_DIGI_L1_DIGI2RAW_PU.py #produce RAW with 65 PU
```
and use the corresponding xx_analysis.py to check the output of each step  

4. submit condor
```
cd Condor
python make_condor_cfg.py
condor_submit condor_submit.txt
```
