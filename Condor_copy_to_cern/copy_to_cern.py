import sys, os

FNAL = "cmseos.fnal.gov"
LXPLUS = "eoscms.cern.ch"

folder = "UL_Single_Pion_gun_E_2to200_noPU_RECO_simHits_fix_HB-2022-02-28/"
FNAL_path = "/eos/uscms/store/user/lpcrutgers/huiwang/HCAL/" + folder

LXPLUS_path = "/eos/cms/store/group/dpg_hcal/comm_hcal/Rutgers/" + folder

f=open(sys.argv[1], "r")
my_list = f.readlines()
f.close()

for line in my_list:
    line = line.strip()
    newloc = line.replace(FNAL, LXPLUS)
    newloc = newloc.replace(FNAL_path, LXPLUS_path)
    cmd = "xrdcp " + line + " " + newloc
    print cmd
    os.system(cmd)
