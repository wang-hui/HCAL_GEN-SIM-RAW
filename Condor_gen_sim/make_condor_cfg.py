import os
from shutil import copyfile
from datetime import date

folder_name = "UL_p1TeV_pion_gun_GEN_SIM"
result_path = "/eos/uscms/store/user/lpcrutgers/huiwang/HCAL/"
condor_path = "/uscms_data/d3/huiwang/condor_temp/huiwang/HCAL/"
tot_jobs = 100

today = str(date.today())
folder_name_full = folder_name + "-" + today
result_path_full = result_path + folder_name_full
condor_path_full = condor_path + folder_name_full

os.system("mkdir -p " + result_path_full)
os.system("mkdir -p " + condor_path_full)

header = (""
+ "Output = " + condor_path_full + "/$(Process).out\n"
+ "Error = " + condor_path_full + "/$(Process).err\n"
+ "Log = " + condor_path_full + "/$(Process).log\n"
)

for j in range (tot_jobs):
	header = header + "\nArguments = " + str(j) + " " + result_path_full + "/ "
	header = header + "\nQueue"

copyfile("condor_submit.back", "condor_submit.txt")
f = open("condor_submit.txt", "a")
f.write(header)
f.close()
