import pandas as pd
from glob import glob

outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\New Demographics with guid from formatted tests\\"

def cleanDate(d):
    return d.split("T")[0]

df = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_PostInjForm_2019-08-22T11-34-204240316875745846702.csv")
df = df[["PostInjForm.Main Group.GUID","PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd","PostInjForm.Post Injury Description.ARCAthleteTyp","PostInjForm.Post Injury Description.SportTeamParticipationTyp","PostInjForm.Post Injury Description.LOCDur","PostInjForm.Post Injury Description.LOCInd","PostInjForm.Post Injury Description.PstTraumaticAmnsDur","PostInjForm.Post Injury Description.PstTraumtcAmnsInd","PostInjForm.Return to Play Description.ReturnToPlayActualDate"]]
new_columns = ["GUID", "Date", "CC", "ARC Athlete", "Sport", "LOC Time", "LOC Ind", "PTA Time", "PTA Ind", "RTP Date"]
# df.columns = new_columns
df["PostInjForm.Main Group.VisitDate"] = df["PostInjForm.Main Group.VisitDate"].apply(str)
df["PostInjForm.Main Group.VisitDate"] = df["PostInjForm.Main Group.VisitDate"].apply(cleanDate)

# df.to_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\_PostInjForm_correct_cols.csv", index=False)

#DEMOAPPX
# df = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_DemogrFITBIR_Appdx_0000310_2019-08-22T11-38-428884192043024417668.csv")
# df = df[["DemogrFITBIR_Appdx_0000310.Main.GUID","DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp"]]
# new_columns = ["GUID", "Sport"]

#DEMO
# df = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_DemogrFITBIR_2019-08-22T11-33-593433479263719920494.csv")
# df = df[["DemogrFITBIR.Main Group.GUID","DemogrFITBIR.Subject Demographics.GenderTyp"]]
# new_columns = ["GUID", "Gender"]

# Concussion HX 
# df = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_Concussion_Hx_0000310_2_2019-08-22T11-36-002178571715763674339.csv")
# df = df[["Concussion_Hx_0000310_2.Main Group.GUID","Concussion_Hx_0000310_2.Previous Concussion.ConcussionPriorNum"]]
# new_columns = ["GUID", "Num of Prior Concussions"]

df.columns = new_columns
# df["Date"] = df["Date"].apply(str)
# df["Date"] = df["Date"].apply(cleanDate)

all_guids = set()
case_guids = set()
control_guids = set()
fileFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\old results\\split case and control\\with repeated\\output\\"
fileList = glob(fileFolder + "*.xlsx")

for f in fileList:
    print("Reading file", f.split(sep="\\")[-1])
    df1 = pd.read_excel(f)
    for guid in df1["GUID"].unique():
        all_guids.add(guid)
    dfcase = df1[df1["Group"]=="Case"]
    for guid in dfcase["GUID"].unique():
        case_guids.add(guid)
    dfControl = df1[df1["Group"]=="Control"]
    for guid in dfControl["GUID"].unique():
        control_guids.add(guid)

print(len(all_guids))
print(len(case_guids))
print(len(control_guids))
finaldf = pd.DataFrame()
for guid in all_guids:
    finaldf = pd.concat([finaldf, df[df["GUID"]==guid]])

casedf = pd.DataFrame()
for guid in case_guids:
    casedf = pd.concat([casedf, df[df["GUID"]==guid]])

controldf = pd.DataFrame()
for guid in control_guids:
    controldf = pd.concat([controldf, df[df["GUID"]==guid]])   

print(len(finaldf))
# print(len(finaldf["GUID"].unique()))
# finaldf.to_excel(outputFolder + "Gender_All.xlsx", index=False)
casedf.to_excel(outputFolder + "PostInjForm_case.xlsx", index=False)
controldf.to_excel(outputFolder + "PostInjForm_control.xlsx", index=False)