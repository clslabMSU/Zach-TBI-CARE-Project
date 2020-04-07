import pandas as pd 
from glob import glob

inputFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
inputfiles = glob(inputFile + "*.xlsx")
demoFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_DemogrFITBIR_2019-08-22T11-33-593433479263719920494.csv"
demodf = pd.read_csv(demoFile)
demodf = demodf[["DemogrFITBIR.Main Group.GUID","DemogrFITBIR.Subject Demographics.GenderTyp"]]
demodf.columns = ["GUID", "Gender"]
outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Demographics\\"

all_guids = set()

#Added Gender
for f in inputfiles:
    df = pd.read_excel(f, index_col=0)
    # df["Gender"] = ""
    guids = df["GUID"].unique().tolist()
    for guid in guids:
        # gdf = df[df["GUID"]==guid]
        all_guids.add(guid)
        # tdf = demodf[demodf["GUID"]==guid]
        # gender = tdf["Gender"].values[0]
        # i=1
        # while not gender:
        #     gender = tdf["Gender"].values[i]
        #     i+=1
        # df.loc[df.GUID == guid, "Gender"] = gender
    # df.to_excel(inputFile + f.split(sep="\\")[-1].split(sep=".xlsx")[0] + "_with_gender.xlsx")
        
# guidf = pd.DataFrame({"GUID" : list(all_guids)})
# guidf.to_csv(inputFile + "master_guid_list.csv", index=False)
# Gather Demographics
# ddf = pd.from_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_PostInjForm_2019-08-22T11-34-204240316875745846702.csv")
# ddf = ddf[["PostInjForm.Main Group.GUID","PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd","PostInjForm.Post Injury Description.ARCAthleteTyp","PostInjForm.Post Injury Description.SportTeamParticipationTyp","PostInjForm.Post Injury Description.LOCDur","PostInjForm.Post Injury Description.LOCInd","PostInjForm.Post Injury Description.PstTraumaticAmnsDur","PostInjForm.Post Injury Description.PstTraumtcAmnsInd","PostInjForm.Return to Play Description.ReturnToPlayActualDate"]]
# new_columns = ["GUID", "Date", "CC", "ARC Athlete", "Sport", "LOC Time", "LOC Ind", "PTA Time", "PTA Ind", "RTP Date"]
# finaldf= pd.DataFrame()
# for guid in all_guids:
#     finaldf = pd.concat([finaldf, ddf[ddf["GUID"]==guid]])

# print(len(finaldf))
# print(len(finaldf["GUID"].unique()))
# finaldf.to_excel(outputFolder + "PostInj_AllGUID.xlsx", index=False)