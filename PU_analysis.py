from ROOT import *
from DataFormats.FWLite import Events, Handle

inputfiles=["/eos/uscms/store/user/lpcrutgers/huiwang/HCAL/6F18884E-08ED-1C44-9306-0402A98ACC32.root"]
#inputfiles=["/eos/uscms/store/user/lpcrutgers/huiwang/HCAL/UL_Single_Pion_gun_E_2to200_RAW_noPU-2022-01-20/UL_MC_RAW_noPU_60_2.root"]

# create handle outside of loop
handle2  = Handle ('vector<PileupSummaryInfo>')
label2 = ("addPileupInfo")

outputfile = "PU_analysis_plots.root"
out_file = TFile(outputfile, 'recreate')

hist_pileup   = TH1F('hist_pileup','pile up',100,0,100)

for inputfile in inputfiles:
    events = Events (inputfile, maxEvents=1000)
    print inputfile

    # loop over events
    for event in events:
        event.getByLabel(label2, handle2)
        PileupSummarys = handle2.product()

        for PileupSummary in PileupSummarys:
            if PileupSummary.getBunchCrossing() == 0: hist_pileup.Fill(PileupSummary.getPU_NumInteractions())

out_file.cd()
out_file.Write()
out_file.Close()
