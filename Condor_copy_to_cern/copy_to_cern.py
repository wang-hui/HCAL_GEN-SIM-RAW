import sys, os

FNAL = "cmseos.fnal.gov"
LXPLUS = "eoscms.cern.ch"

folder = "Run3_RelVal_1TeV_pion_gun_RAW_PU65-2020-06-23/"
FNAL_path = "/eos/uscms/store/user/lpcrutgers/sve6/" + folder
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
