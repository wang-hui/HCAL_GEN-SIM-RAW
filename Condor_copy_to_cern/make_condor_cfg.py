import os
from shutil import copyfile
from datetime import date

folder_name = "UL_Single_Pion_gun_E_2to200_noPU_RECO_simHits_fix_HB_copy_to_CERN"
file_list = "../FileList/UL_Single_Pion_gun_E_2to200_noPU_RECO_simHits_fix_HB.list"

condor_path = "/uscms_data/d3/huiwang/condor_temp/huiwang/HCAL/"
tot_jobs = 10

condor_path_full = condor_path + folder_name
os.system("mkdir -p " + condor_path_full)

f = open(file_list, "r")
my_list = f.readlines()
f.close()

header = (""
+ "Output = " + condor_path_full + "/$(Process).out\n"
+ "Error = " + condor_path_full + "/$(Process).err\n"
+ "Log = " + condor_path_full + "/$(Process).log\n"
)

my_list.sort()
tot_lines = len(my_list)
my_step = max(int(tot_lines / tot_jobs),1) #int returns floor
list_of_sublist = []
for i in xrange (0, tot_lines, my_step):
	list_of_sublist.append(my_list[i : i + my_step])

for j in range (len(list_of_sublist)):
	f = open("FileList_" + str(j) + ".list", "w")
	for line in list_of_sublist[j]:
		f.write(line)
	f.close()
	header = header + "\nArguments = FileList_" + str(j) + ".list "
	header = header + "\nQueue"

os.system("tar -cf FileList.tar FileList_*.list")
os.system("mkdir -p FileList_test")
os.system("rm FileList_test/*.list")
os.system("mv FileList_*.list FileList_test")

copyfile("condor_submit.back", "condor_submit.txt")
f = open("condor_submit.txt", "a")
f.write(header)
f.close()
