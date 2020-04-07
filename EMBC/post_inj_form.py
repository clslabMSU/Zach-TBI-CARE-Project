import pandas as pd
from datetime import date, timedelta
from glob import glob

outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\repeated tests\\"

inputDataFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Assessments\\query_result_SCAT3_2019-08-22T11-36-453273569649714830957.csv"
guidFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\guids\\"
BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX", "TBIZU352RXE"]
bessCorrect = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\BESS_correct_data.xlsx"


demoFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_DemogrFITBIR_2019-08-22T11-33-593433479263719920494.csv"
demodf = pd.read_csv(demoFile)
biodf = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Biomarker\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv")
bessFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\_PostInjForm_correct_cols.csv"

# bessFile="\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_PostInjForm_2019-08-22T11-34-204240316875745846702.csv"
bessdf = pd.read_csv(bessFile)
# bessFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\CARE_blood_biomarkers\\CARE_original_assessment_files\\new_files\\"
# demofiles = glob(bessFile + "*.csv")

# PostInj
new_columns = ["GUID", "Date", "CC", "ARC Athlete", "Sport", "LOC Time", "LOC Ind", "PTA Time", "PTA Ind", "RTP Date"]
# BSI18
# new_columns = ["GUID", "Date", "Context", "CC", "Som Score", "Depr Score", "Anx Score", "GSI Score"]
# BESS
# new_columns = ["GUID", "Date", "Context", "CC", "Firm Error", "Foam Error", "Total Error"]
# ImPACT
# new_columns = ["GUID", "Date", "Context", "CC", "Total Symp", "Verb Mem", "Vis Mem", "Mot Speed", "React Time", "Impulse Control"]
# SAC
# new_columns = ["GUID", "Date", "Context", "CC", "Orientation", "Immd Mem", "Concentration", "Delayed Recall", "Total"]


def cleanDate(d):
    return d.split("T")[0]

rawdf = pd.read_csv(inputDataFile)
resultdf = pd.DataFrame()
rdf = pd.DataFrame()

df1 = pd.read_csv(guidFolder + "all_biomarker_guid.csv")
df2 = pd.read_csv(guidFolder + "no_casecontrol_doubles_biomarker_guid.csv")
bdf = biodf[["BiomarkerAssayDataForm.Main.GUID", "BiomarkerAssayDataForm.Main.CaseContrlInd", "BiomarkerAssayDataForm.Form Administration.ContextTypeOTH", "BiomarkerAssayDataForm.Main.VisitDate"]]
bdf.columns = ["GUID", "CC", "Context", "Date"]
bdf["Date"] = bdf["Date"].apply(str)
bdf["Date"] = bdf["Date"].apply(cleanDate)
bdf = bdf.drop_duplicates()
bdf = bdf.sort_values(by="Date")
demodf = demodf[["DemogrFITBIR.Main Group.GUID","DemogrFITBIR.Subject Demographics.GenderTyp"]]
demodf.columns = ["GUID", "Gender"]
# print(bdf)
guid_list = df1["GUID"]
# print(len(guid_list))
nocc_guid_list = df2["GUID"]
# print(len(nocc_guid_list))
newdemodf = pd.DataFrame()
for guid in nocc_guid_list:
    newdemodf = pd.concat([newdemodf, demodf[demodf["GUID"]==guid]], ignore_index=True)


# PostInj
bessdf = bessdf[["PostInjForm.Main Group.GUID","PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd","PostInjForm.Post Injury Description.ARCAthleteTyp","PostInjForm.Post Injury Description.SportTeamParticipationTyp","PostInjForm.Post Injury Description.LOCDur","PostInjForm.Post Injury Description.LOCInd","PostInjForm.Post Injury Description.PstTraumaticAmnsDur","PostInjForm.Post Injury Description.PstTraumtcAmnsInd","PostInjForm.Return to Play Description.ReturnToPlayActualDate"]]
# BSI18 
# bessdf = bessdf[["BSI18.Main.GUID","BSI18.Main.VisitDate","BSI18.Main.GeneralNotesTxt","BSI18.Main.CaseContrlInd","BSI18.Form Completion.BSI18SomScoreRaw","BSI18.Form Completion.BSI18DeprScoreRaw","BSI18.Form Completion.BSI18AnxScoreRaw","BSI18.Form Completion.BSI18GSIScoreRaw"]]
# BESS
# bessdf = bessdf[["BESS.Main.GUID","BESS.Main.VisitDate","BESS.Form Administration.ContextTypeOTH","BESS.Main.CaseContrlInd","BESS.Balance Error Scoring Test.BESSTotalFirmErrorCt","BESS.Balance Error Scoring Test.BESSTotalFoamErrorCt","BESS.Balance Error Scoring Test.BESSTotalErrorCt"]]
# ImPACT
# bessdf = bessdf[["ImPACT.Main.GUID","ImPACT.Main.VisitDate","ImPACT.Form Administration Group.ContextTypeOTH","ImPACT.Main.CaseContrlInd","ImPACT.Post-Concussion Symptom Scale (PCSS).ImPACTTotalSymptomScore","ImPACT.ImPACT Test.ImPACTVerbMemoryCompScore","ImPACT.ImPACT Test.ImPACTVisMemoryCompScore","ImPACT.ImPACT Test.ImPACTVisMotSpeedCompScore","ImPACT.ImPACT Test.ImPACTReactTimeCompScore","ImPACT.ImPACT Test.ImPACTImplseCntrlCompScore"]]
# # SAC
# bessdf = bessdf[["SAC.Main.GUID","SAC.Main.VisitDate","SAC.Form Administration Group.ContextTypeOTH","SAC.Main.CaseContrlInd","SAC.Scoring Summary.SACOrientationSubsetScore","SAC.Scoring Summary.SACImmdMemorySubsetScore","SAC.Scoring Summary.SACConcentationSubsetScore","SAC.Scoring Summary.SACDelayedRecallSubsetScore","SAC.Scoring Summary.SACTotalScore"]]


bessdf.columns = new_columns
# for guid in BANNED_GUID:
#     bessdf = bessdf[bessdf["GUID"] != guid]
# bessdf = bessdf.fillna({"Context":"Baseline"})
# print(len(bessdf["GUID"].unique()))

all_guids = set()
fileFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\split case and control\\with repeated\\output\\"
fileList = glob(fileFolder + "*.xlsx")

for f in fileList:
    print("Reading file", f.split(sep="\\")[-1])
    df = pd.read_excel(f)
    for guid in df["GUID"].unique():
        all_guids.add(guid)

print(len(all_guids))
finaldf= pd.DataFrame()
for guid in all_guids:
    finaldf = pd.concat([finaldf, bessdf[bessdf["GUID"]==guid]])

print(len(finaldf))
print(len(finaldf["GUID"].unique()))
finaldf.to_excel(outputFolder + "PostInj_AllGUID.xlsx", index=False)