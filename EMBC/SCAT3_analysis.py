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

# for guid in guid_list:
#     tdf = bdf[bdf["GUID"]==guid]
#     if len(tdf["CC"].value_counts()) > 1:
#         print(guid)

# case_guid = bdf[bdf["CC"] == "Case"]
# case_guid = case_guid["GUID"].unique().tolist()
# control_guid = bdf[bdf["CC"] == "Control"]
# control_guid = control_guid["GUID"].unique().tolist()

# conchc = "Concussion_Hx_0000310_2.Previous Concussion.ConcussionPriorNum"

# fileFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\"
# filelist = glob(fileFolder + "*.xlsx")

# for f in filelist:
#     df = pd.read_excel(f)
#     real_file_name = f.split(sep="\\")[-1].split(sep=".xlsx")[0]
#     casedf = pd.DataFrame()
#     controldf = pd.DataFrame()
#     for guid in case_guid:
#         casedf = pd.concat([casedf, df[df["GUID"] == guid]], ignore_index=True)
#     for guid in control_guid:
#         controldf = pd.concat([controldf, df[df["GUID"] == guid]], ignore_index=True)
#     casedf.to_excel(fileFolder + real_file_name + "_case.xlsx", index=False)
#     controldf.to_excel(fileFolder + real_file_name + "_control.xlsx", index=False)


# fileFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\split case and control\\"
# casefilelist = glob(fileFolder + "*case.xlsx")
# confilelist = glob(fileFolder + "*control.xlsx")
# used_case_guids = set()
# used_control_guids = set()

# for f in casefilelist:
#     df = pd.read_excel(f)
#     guid_list = df["GUID"].unique().tolist()
#     for guid in guid_list:
#         used_case_guids.add(guid)

# for f in confilelist:
#     df = pd.read_excel(f)
#     guid_list = df["GUID"].unique().tolist()
#     for guid in guid_list:
#         used_control_guids.add(guid)

# print(len(used_case_guids))
# print(len(used_control_guids))

# finalcasedf = pd.DataFrame()
# finalcontroldf = pd.DataFrame()
# for f in demofiles:
#     i=0
#     df = pd.read_csv(f)
#     if "Concussion_Hx_0" in f:
#         real_file_name = "Concussion_Hx"
#         df = df[["Concussion_Hx_0000310_2.Main Group.GUID", "Concussion_Hx_0000310_2.Previous Concussion.ConcussionPriorNum"]]
#     elif "DemogrFITBIR_2019" in f:
#         real_file_name = "Demographics"
#         df = df[["DemogrFITBIR.Main Group.GUID", "DemogrFITBIR.Subject Demographics.GenderTyp", "DemogrFITBIR.Subject Demographics.EthnUSACat"]]
#     elif "DemogrFITBIR_Appdx" in f:
#         real_file_name = "Demographics Appendix"
#         df = df[["DemogrFITBIR_Appdx_0000310.Main.GUID", "DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp", "DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTypOTH"]]
#     else:
#         continue
#     # elif "MedHx_Appendix" in f:
#     #     df = [["MedHx_Appendix_CARE0000310.Main Group.GUID", "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesPastThreeMonthsInd", ""]]
#     df = df.rename(columns={df.columns[0]: "GUID"})
#     print(df.columns)
#     casedf = pd.DataFrame()
#     for guid in used_case_guids:
#         casedf = pd.concat([casedf, df[df["GUID"]==guid]], ignore_index=True)
#     condf = pd.DataFrame()
#     for guid in used_control_guids:
#         condf = pd.concat([condf, df[df["GUID"]==guid]], ignore_index=True)
#     casedf.to_excel(outputFolder + real_file_name +"_case.xlsx", index=False)
#     condf.to_excel(outputFolder + real_file_name +"_control.xlsx", index=False)







# for guid in guid_list:
#     resultdf = resultdf.append(rawdf[rawdf["SCAT3.Main.GUID"] == guid])
# print(len(resultdf["SCAT3.Main.GUID"].unique()))
# for guid in nocc_guid_list:
#     rdf = rdf.append(rawdf[rawdf["SCAT3.Main.GUID"] == guid])
# print(len(rdf["SCAT3.Main.GUID"].unique()))

# rdf = rdf[["SCAT3.Main.GUID", "SCAT3.Main.VisitDate", "SCAT3.Scoring Summary.Scat3TotalSymptoms", "SCAT3.Scoring Summary.Scat3TotSympScore"]]
# rdf["SCAT3.Main.VisitDate"] = rdf["SCAT3.Main.VisitDate"].apply(str)
# rdf["SCAT3.Main.VisitDate"] = rdf["SCAT3.Main.VisitDate"].apply(cleanDate)
# rdf.columns = ["GUID", "Visit Date", "Total Symptoms", "Total Symp Score"]

# xdf = rdf.merge(bdf, on="GUID")
# xdf = xdf.drop_duplicates()
# print(xdf.head())
# xdf.to_excel(outputFolder + "SCAT3 no cc doubles.xlsx", index=False)


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


# date_dict = {}

# ************************************************************************************************************************
# ************************************************************************************************************************
# ************************************************************************************************************************
#      Successful separation of correct dates in assessments. Requires file name changes, and col name changes
# ************************************************************************************************************************
# ************************************************************************************************************************
# ************************************************************************************************************************
finaldf = pd.DataFrame()
repeatdf = pd.DataFrame()
time_dict = {}
bio_context_list = ["Baseline", "6 Hours Post Injury", "24 hours Post Injury", "When Asymptomatic", "7 Days Post Return to Play"]
bess_context_list = ["Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "Unrestricted Return to Play", "7 days Post-Unrestricted Return to Play", "6 months post-injury"]
bessdf["Gender"] = ""
bessdf["Repeated"] = ""

# bessdf["Date"] = bessdf["Date"].apply(str)
# bessdf["Date"] = bessdf["Date"].apply(cleanDate)


for guid in nocc_guid_list:
    R = False
    bio_date_dict = {}
    tbdf = bdf[bdf["GUID"] == guid]
    timelines = []

    bio_dates = tbdf["Date"].unique().tolist()

    tbdf1 = tbdf[tbdf["Context"] == "Baseline"]
    bio_date_dict["Baseline"] = tbdf1["Date"].values.tolist()
    tbdf2 = tbdf[tbdf["Context"] == "6 Hours Post Injury"]
    bio_date_dict["< 6 hours"] = tbdf2["Date"].values.tolist()
    tbdf3 = tbdf[tbdf["Context"] == "24 hours Post Injury"]
    bio_date_dict["24-48 hours"] = tbdf3["Date"].values.tolist()
    tbdf4 = tbdf[tbdf["Context"] == "When Asymptomatic"]
    bio_date_dict["Asymptomatic"] = tbdf4["Date"].values.tolist()
    tbdf5 = tbdf[tbdf["Context"] == "7 Days Post Return to Play"]
    bio_date_dict["7 days Post-Unrestricted Return to Play"] = tbdf5["Date"].values.tolist()

    tempbessdf = bessdf[bessdf["GUID"] == guid]
    tempbessdf = tempbessdf.sort_values(by="Date")
    genderdf = newdemodf[newdemodf["GUID"]==guid]
    if len(genderdf["Gender"].unique().tolist()) > 1:
        print("MULTIPLE GENDER", guid)
    else:
        gender = genderdf["Gender"].values[0]
        tempbessdf["Gender"] = gender
    # #FOR POSTINJFORM ONLY
    for t in tempbessdf.itertuples(index=False):
        # print(t[1])
        if t[1] in bio_dates:
            timelines.append(t)
    
    # timeline = []
    # i = 0
    # write = False
    # for t in tempbessdf.itertuples(index=False):
    #     # FOR BSI, EMPTY IS BASELINE
    #     if type(t[2]) != str:
    #         print("BLANK CONTEXT FOR", guid)
    #         # timeline.append([guid,t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8]])
    #         # if t[1] in bio_date_dict["Baseline"]:
    #         #     if guid =="TBIBA122HW3":
    #         #         print("Is in base line", t[1])
    #         #     write = True
    #         # i = 1
    #         continue
    #     if t[2] not in bess_context_list[i:]:
    #         if write == True:
    #             timelines.append(timeline)
    #         # timeline = [[guid,t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8]]]
    #         timeline = [t]
    #         write = False
    #         i = bess_context_list.index(t[2]) + 1
    #     else:
    #         # timeline.append([guid,t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8]])
    #         timeline.append(t)
    #         i+=1
    #     if t[1] in bio_date_dict.get(t[2], []):
    #         write = True
    # if write:
    #     timelines.append(timeline)
    if len(timelines) > 1:
        R = True
        print("Repeated for", guid)
    j = 0
    for tl in timelines:
        if R == True:
            if j == 0:
                testdf = pd.DataFrame(tl)
                testdf[testdf.columns[-1]] = "R"
                finaldf = pd.concat([finaldf, testdf],  ignore_index=True)
                repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
                j+=1
            else:
                testdf = pd.DataFrame(tl)
                testdf[testdf.columns[-1]] = "R"
                repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
                j+=1
        else:
            testdf = pd.DataFrame(tl)
            finaldf = pd.concat([finaldf, testdf], ignore_index=True)
new_columns.extend(["Gender", "Repeated"])
print(finaldf)
finaldf.columns = new_columns
finaldf = finaldf.sort_values(by=["GUID", "Date"])
finaldf.to_excel(outputFolder + "PostInj_data.xlsx", index=False)
repeatdf.columns = new_columns
repeatdf.to_excel(outputFolder + "PostInj_repeated.xlsx", index=False)













# ************************************************************************************************************************
# ************************************************************************************************************************
# ************************************************************************************************************************

# ************************************************************************************************************************
# ************************************************************************************************************************
# # ************************************************************************************************************************
# scatdf = pd.read_excel(outputFolder + "SCAT3 no cc doubles.xlsx")
# finaldf = pd.DataFrame()
# bio_date_dict = {}
# time_dict = {}
# newbessdf = pd.read_excel(bessCorrect)
# newbsidf = pd.read_excel("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Assessments with no repeated Baselines\\BSI18_correct_data.xlsx")

# for guid in nocc_guid_list:
#     bio_date_dict[guid] = {}
#     tbdf = bdf[bdf["GUID"] == guid]
#     timelines = []

#     tbdf1 = tbdf[tbdf["Context"] == "Baseline"]
#     bio_dates = tbdf1["Date"].values.tolist()
#     tnewbessdf = newbessdf[newbessdf["GUID"] == guid]
#     tnewbessdf1 = newbessdf[newbessdf["Context"]== "Baseline"]
#     bess_dates = tnewbessdf1["Date"].unique().tolist()
#     tnewbsidf = newbsidf[newbsidf["GUID"] == guid]
#     tnewbsidf1 = newbsidf[newbsidf["Context"]== "Baseline"]
#     bsi_dates = tnewbsidf1["Date"].unique().tolist()

#     tempscatdf = scatdf[scatdf["GUID"] == guid]
#     tempscatdf = tempscatdf.sort_values(by="Visit Date")

#     for t in tempscatdf.itertuples(index=False):
#         if t[1] in bio_dates:
#             timelines.append([[guid,t[1],t[2],t[3],t[4]]])
#         elif t[1] in bess_dates:
#             timelines.append([[guid,t[1],t[2],t[3],t[4]]])
#         elif t[1] in bsi_dates:
#             timelines.append([[guid,t[1],t[2],t[3],t[4]]])

#     for tl in timelines:
#         testdf = pd.DataFrame(tl)
#         finaldf = pd.concat([finaldf, testdf], ignore_index=True)

# finaldf.columns = ["GUID", "Date", "Total Symptoms", "Total Symp Score", "CC"]
# finaldf = finaldf.sort_values(by=["GUID", "Date"])
# finaldf.to_excel(outputFolder + "SCAT3_correct_data.xlsx", index=False)
# ************************************************************************************************************************
# ************************************************************************************************************************
# ************************************************************************************************************************

# ************************************************************************************************************************
# ************************************************************************************************************************
# ************************************************************************************************************************



# xdf = pd.read_excel(outputFolder + "SCAT3_correct_data.xlsx")
# casedf = xdf[xdf["CC"] == "Case"]
# condf = xdf[xdf["CC"] == "Control"]

# # ***********************************CASE****************************************
# # ***********************************CASE****************************************
# b0df = casedf[casedf["Total Symp Score"] == 0]
# b1df = casedf[casedf["Total Symp Score"] > 0]
# b1df = b1df[b1df["Total Symp Score"] <= 5]
# b2df = casedf[casedf["Total Symp Score"] > 5]
# b2df = b2df[b2df["Total Symp Score"] <= 15]
# b3df = casedf[casedf["Total Symp Score"] > 15]
# b3df = b3df[b3df["Total Symp Score"] <= 50]
# b4df = casedf[casedf["Total Symp Score"] > 50]
# print([len(b0df),len(b1df),len(b2df),len(b3df),len(b4df)])
# print(len(b0df)+len(b1df)+len(b2df)+len(b3df)+len(b4df))
# print(len(casedf))

# dflist = [b0df,b1df,b2df,b3df,b4df]
# casedoubledf = pd.DataFrame()
# for guid in casedf["GUID"].unique():
#     count = 0
#     for d in dflist:
#         if guid in d["GUID"].values:
#             count += 1
#             if count > 1:
#                 casedoubledf = casedoubledf.append(casedf[casedf["GUID"] == guid])
# print(len(casedoubledf["GUID"].unique()), "PEOPLE FROM CASE IN 2 BINS")
# casedoubledf.to_excel(outputFolder + "case multiple bins.xlsx", index=False)



# # ***********************************CONTROL****************************************
# # ***********************************CONTROL****************************************
# b0df = condf[condf["Total Symp Score"] == 0]
# b1df = condf[condf["Total Symp Score"] > 0]
# b1df = b1df[b1df["Total Symp Score"] <= 5]
# b2df = condf[condf["Total Symp Score"] > 5]
# b2df = b2df[b2df["Total Symp Score"] <= 15]
# b3df = condf[condf["Total Symp Score"] > 15]
# b3df = b3df[b3df["Total Symp Score"] <= 50]
# b4df = condf[condf["Total Symp Score"] > 50]
# print([len(b0df),len(b1df),len(b2df),len(b3df),len(b4df)])
# print(len(b0df)+len(b1df)+len(b2df)+len(b3df)+len(b4df))
# print(len(condf))

# dflist = [b0df,b1df,b2df,b3df,b4df]
# condoubledf = pd.DataFrame()
# for guid in condf["GUID"].unique():
#     count = 0
#     for d in dflist:
#         if guid in d["GUID"].values:
#             count += 1
#             if count > 1:
#                 condoubledf = condoubledf.append(condf[condf["GUID"] == guid])
#                 break
# print(len(condoubledf["GUID"].unique()), "PEOPLE FROM CONTROL IN 2 BINS")                
# condoubledf.to_excel(outputFolder + "control multiple bins.xlsx", index=False)
