import pandas as pd
import numpy as np 
from glob import glob

rawAssessment = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Assessments\\"
rawDemographics = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Assessments\\Demographs\\"
rawAssessFiles = glob(rawAssessment + "*.csv")
rawDemoFiles = glob(rawDemographics + "*.csv")
rawBioFile = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Biomarker\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
outputFolder = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
rawScat = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Biomarker\\query_result_SCAT3_2019-08-22T11-36-453273569649714830957.csv"
finalAssessFolder = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Final Data\\"
finalAssessFiles = glob(finalAssessFolder + "*.xlsx")


COLS_WANTED={
    "_PostInjForm_" : ["PostInjForm.Main Group.GUID", "PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd", "PostInjForm.Form Administration.ContextTypeOTH",
                        "PostInjForm.Post Injury Description.ARCAthleteTyp", 
                        "PostInjForm.Post Injury Description.SportTeamParticipationTyp",
                        "PostInjForm.Post Injury Description.LOCDur", 
                        "PostInjForm.Post Injury Description.LOCInd", 
                        "PostInjForm.Post Injury Description.PstTraumaticAmnsDur",
                        "PostInjForm.Post Injury Description.PstTraumtcAmnsInd", 
                        "PostInjForm.Return to Play Description.ReturnToPlayActualDate"],

    # "_MedHx_Appendix_CARE0000310_" : ["MedHx_Appendix_CARE0000310.Main Group.GUID", "MedHx_Appendix_CARE0000310.Main Group.VisitDate", "MedHx_Appendix_CARE0000310.Main Group.CaseContrlInd", 
    #                                     "MedHx_Appendix_CARE0000310.Form Adminstration.ContextTypeOTH",
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesPastThreeMonthsInd", 
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).HeadachWorkLimitAbilityInd",
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).HeadacheLightBotherInd", 
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).HeadacheNasuseaInd",
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).LearningDisordrDiagnosInd", 
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).ModerateSevereTBIDiagnosInd",
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesDisordrDiagnosInd", 
    #                                     "MedHx_Appendix_CARE0000310.Medical History (You).MemoryDisorderDxInd"],

    '_BESS_': ['BESS.Main.GUID', 'BESS.Main.VisitDate','BESS.Main.CaseContrlInd', 'BESS.Form Administration.ContextTypeOTH',
                'BESS.Balance Error Scoring Test.BESSTotalFirmErrorCt', 
                'BESS.Balance Error Scoring Test.BESSTotalFoamErrorCt', 
                'BESS.Balance Error Scoring Test.BESSTotalErrorCt'],
    # # '_BESS_': ['BESS.Main.GUID', 'BESS.Main.CaseContrlInd','BESS.Main.VisitDate', 'BESS.Form Administration.ContextTypeOTH'],
    
    '_BSI18_': ['BSI18.Main.GUID',  'BSI18.Main.VisitDate','BSI18.Main.CaseContrlInd', 'BSI18.Main.GeneralNotesTxt',
                'BSI18.Form Completion.BSI18SomScoreRaw', 
                'BSI18.Form Completion.BSI18DeprScoreRaw', 
                'BSI18.Form Completion.BSI18AnxScoreRaw', 
                'BSI18.Form Completion.BSI18GSIScoreRaw'],

    # # '_BSI18_': ['BSI18.Main.GUID', 'BSI18.Main.CaseContrlInd', 'BSI18.Main.VisitDate', 'BSI18.Main.GeneralNotesTxt'],
    
    '_ImPACT_': ['ImPACT.Main.GUID', 'ImPACT.Main.VisitDate','ImPACT.Main.CaseContrlInd',  'ImPACT.Form Administration Group.ContextTypeOTH',
                    'ImPACT.Post-Concussion Symptom Scale (PCSS).ImPACTTotalSymptomScore', 
                    'ImPACT.ImPACT Test.ImPACTVerbMemoryCompScore', 
                    'ImPACT.ImPACT Test.ImPACTVisMemoryCompScore', 
                    'ImPACT.ImPACT Test.ImPACTVisMotSpeedCompScore', 
                    'ImPACT.ImPACT Test.ImPACTReactTimeCompScore', 
                    'ImPACT.ImPACT Test.ImPACTImplseCntrlCompScore'],
    # # '_ImPACT_': ['ImPACT.Main.GUID', 'ImPACT.Main.CaseContrlInd', 'ImPACT.Main.VisitDate', 'ImPACT.Form Administration Group.ContextTypeOTH'],
    
    '_SAC_': ['SAC.Main.GUID',  'SAC.Main.VisitDate','SAC.Main.CaseContrlInd', 'SAC.Form Administration Group.ContextTypeOTH',
                'SAC.Scoring Summary.SACOrientationSubsetScore',
                'SAC.Scoring Summary.SACImmdMemorySubsetScore',
                'SAC.Scoring Summary.SACConcentationSubsetScore',
                'SAC.Scoring Summary.SACDelayedRecallSubsetScore',
                'SAC.Scoring Summary.SACTotalScore'],
    # # '_SAC_': ['SAC.Main.GUID', 'SAC.Main.CaseContrlInd', 'SAC.Main.VisitDate', 'SAC.Form Administration Group.ContextTypeOTH'],

    '_SCAT3_': ['SCAT3.Main.GUID', 'SCAT3.Main.VisitDate', 
                'SCAT3.Scoring Summary.Scat3TotalSymptoms', 
                'SCAT3.Scoring Summary.Scat3TotSympScore'],

    '_Concussion_Hx_0000310_2_': ['Concussion_Hx_0000310_2.Main Group.GUID', 'Concussion_Hx_0000310_2.Main Group.VisitDate', 'Concussion_Hx_0000310_2.Form Administration.ContextTypeOTH',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.HistHeadInjOrConcussInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.ConcussionPriorNum'],
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.SportRelatedConcussionInd',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.DiagnosedInd',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.AgeAtTBIEvent',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.TBILocInd',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.LOCDurRang', 
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.LOCUnkDurInd',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.AmnesiaConcussInd',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.AmnesiaConcussDurRange',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.AmnsDurUnkInd',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.ConcussionSymptomDurDays',
                                    # 'Concussion_Hx_0000310_2.Previous Concussion.TBISxDurUnkInd'],

    '_DemogrFITBIR_': ['DemogrFITBIR.Main Group.GUID', 'DemogrFITBIR.Main Group.VisitDate', 
                        'DemogrFITBIR.Subject Demographics.GenderTyp'],

    '_DemogrFITBIR_Appdx_0000310_': ['DemogrFITBIR_Appdx_0000310.Main.GUID', 'DemogrFITBIR_Appdx_0000310.Main.VisitDat', 'DemogrFITBIR_Appdx_0000310.Form Administration.ContextTypeOTH',
                                        # 'DemogrFITBIR_Appdx_0000310.Demographics.GenderTypExt',
                                        'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp'],
                                        # 'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTypOTH',
                                        # 'DemogrFITBIR_Appdx_0000310.Military Club Sport Team Participation.SportTeamParticipationTyp'],

    # '_MedHx_FITBITR_': ['MedHx_FITBIR.Main.GUID', 'MedHx_FITBIR.Main.VisitDate', 'MedHx_FITBIR.Form Administration.ContextTypeOTH',
    #                         'MedHx_FITBIR.Headaches Migraines History.HeadachMigranDiagnsInd']
}

def fixContext(context):
    context = str(context)
    context = context.strip()
    if context == "6 m onths post-injury":
        return "6 months post-injury"
    elif context.endswith("1") or context.endswith("2") or context.endswith("3"):
        return context[:-2]
    elif context == 'nan':
        return "Baseline"
    else:
        return context


# biodf = pd.read_csv(rawBioFile)
# biodf = biodf[["BiomarkerAssayDataForm.Main.GUID", "BiomarkerAssayDataForm.Main.VisitDate", "BiomarkerAssayDataForm.Main.CaseContrlInd", "BiomarkerAssayDataForm.Form Administration.ContextTypeOTH"]]
# biodf.columns = ["GUID", "Date", "CC", "Context"]
# raw_bio_guids = biodf["GUID"].unique().tolist()
# final_bio_guid = []
# BANNED_GUID = set()
# for guid in raw_bio_guids:
#     tempdf = biodf[biodf["GUID"]==guid]
#     if len(tempdf["CC"].unique()) != 1:
#         BANNED_GUID.add(guid)
#         continue
#     elif len(tempdf["Context"].unique()) <= 1:
#         BANNED_GUID.add(guid)
#         continue
#     else:
#         final_bio_guid.append(guid)
# print(len(final_bio_guid))
# biodf["Context"] = biodf["Context"].apply(fixContext)

df_list = []
for f in finalAssessFiles:
    df1 = pd.read_excel(f, index_col=0)
    df1["Repeated"] = ""
    real_file_name = f.split(sep="\\")[-1].split(sep="final")[0]
    # cols = COLS_WANTED.get(real_file_name, None)
    # df = df[cols]
    # guid_col = df.columns[0]
    # date_col = df.columns[1]
    # cc_col = df.columns[2]
    # context_col = df.columns[3]
    
    # df1 = pd.DataFrame()
    # for guid in final_bio_guid:
    #     tempdf = df[df[guid_col]==guid]
    #     cc_list = [x for x in tempdf[cc_col].unique() if str(x) != 'nan']
    #     if len(cc_list) > 1:
    #         print(cc_list)
    #         print(guid)
    #         BANNED_GUID.add(guid)
    #     else:
    #         df1 = pd.concat([df1, tempdf], ignore_index=True)
    # df1[context_col] = df1[context_col].apply(fixContext)

    bio_context_list = ["Baseline", "6 Hours Post Injury", "24 hours Post Injury", "When Asymptomatic", "7 Days Post Return to Play"]
    assess_context_list = ["Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "Unrestricted Return to Play", "7 days Post-Unrestricted Return to Play", "6 months post-injury"]

    assess_guids = df1["GUID"].unique().tolist()
    finaldf = pd.DataFrame()
    repeatdf = pd.DataFrame()
    for guid in assess_guids:
        bio_date_dict = {}
        temp_assess_df = df1[df1["GUID"]==guid]
        temp_assess_df["Group"] = temp_assess_df["Group"].values[1]
        temp_assess_df = temp_assess_df.sort_values(by="Date")

        # tbdf = biodf[biodf["GUID"]==guid]
        # tbdf1 = tbdf[tbdf["Context"] == "Baseline"]
        # bio_date_dict["Baseline"] = tbdf1["Date"].values.tolist()
        # tbdf2 = tbdf[tbdf["Context"] == "6 Hours Post Injury"]
        # bio_date_dict["< 6 hours"] = tbdf2["Date"].values.tolist()
        # tbdf3 = tbdf[tbdf["Context"] == "24 hours Post Injury"]
        # bio_date_dict["24-48 hours"] = tbdf3["Date"].values.tolist()
        # tbdf4 = tbdf[tbdf["Context"] == "When Asymptomatic"]
        # bio_date_dict["Asymptomatic"] = tbdf4["Date"].values.tolist()
        # tbdf5 = tbdf[tbdf["Context"] == "7 Days Post Return to Play"]
        # bio_date_dict["7 days Post-Unrestricted Return to Play"] = tbdf5["Date"].values.tolist()

        timeline = []
        timelines = []
        i = 0
        write = True
        for t in temp_assess_df.itertuples(index=False):
            if type(t[3]) != str: # If Context blank, consider it baseline
                if i != 0:
                    if write == True:
                        timelines.append(timeline)
                        timeline = [t]
                        # write = False
                    else:
                        timeline = [t]
                timeline = [t]
                # if t[1] in bio_date_dict["Baseline"]:
                #     write = True
                i = 1
                continue
                
            if t[3] not in assess_context_list[i:]:
                if assess_context_list.index(t[3]) == i-1:
                    timeline[-1] = t
                    # if t[1] in bio_date_dict.get(t[3], []):
                    #     write = True
                    continue
                if write == True:
                    timelines.append(timeline)
                timeline = [t]
                # write = False
                i = assess_context_list.index(t[3]) + 1
            else:
                timeline.append(t)
                i = assess_context_list.index(t[3]) + 1
            # if t[1] in bio_date_dict.get(t[3], []):
            #     write = True
        if write == True:
            timelines.append(timeline)
        if len(timelines) > 1:
            R = True
            print("Repeated for", guid)
        j = 0
        for tl in timelines:
            if len(tl) == 1:
                print("dropping", tl)
                continue
            if R == True:
                if j == 0:
                    testdf = pd.DataFrame(tl)
                    testdf["Repeated"] = "R"
                    finaldf = pd.concat([finaldf, testdf],  ignore_index=True)
                    repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
                    j+=1
                else:
                    testdf = pd.DataFrame(tl)
                    testdf["Repeated"] = "R"
                    repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
                    j+=1
            else:
                testdf = pd.DataFrame(tl)
                finaldf = pd.concat([finaldf, testdf], ignore_index=True)
    
    repeatdf.to_excel(outputFolder + real_file_name + "repeated_timelines.xlsx")
    finaldf.to_excel(outputFolder + real_file_name + "final_timelines.xlsx")

# SCAT3 ONLY
# df = pd.read_csv(rawScat)
# real_file_name = "SCAT3"
# cols = COLS_WANTED.get(real_file_name, None)
# df = df[cols]
# guid_col = df.columns[0]
# date_col = df.columns[1]
# # cc_col = df.columns[2]
# # context_col = df.columns[3]

# df1 = pd.DataFrame()
# for guid in final_bio_guid:
#     tempdf = df[df[guid_col]==guid]
#     cc_list = [x for x in tempdf[cc_col].unique() if str(x) != 'nan']
#     if len(cc_list) > 1:
#         print(cc_list)
#         print(guid)
#         BANNED_GUID.add(guid)
#     else:
#         df1 = pd.concat([df1, tempdf], ignore_index=True)
# df1[context_col] = df1[context_col].apply(fixContext)

# bio_context_list = ["Baseline", "6 Hours Post Injury", "24 hours Post Injury", "When Asymptomatic", "7 Days Post Return to Play"]
# assess_context_list = ["Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "Unrestricted Return to Play", "7 days Post-Unrestricted Return to Play", "6 months post-injury"]

# assess_guids = df1[guid_col].unique().tolist()
# finaldf = pd.DataFrame()
# for guid in assess_guids:
#     bio_date_dict = {}
#     temp_assess_df = df1[df1[guid_col]==guid]
#     temp_assess_df = temp_assess_df.sort_values(by=date_col)

#     tbdf = biodf[biodf["GUID"]==guid]
#     tbdf1 = tbdf[tbdf["Context"] == "Baseline"]
#     bio_date_dict["Baseline"] = tbdf1["Date"].values.tolist()
#     tbdf2 = tbdf[tbdf["Context"] == "6 Hours Post Injury"]
#     bio_date_dict["< 6 hours"] = tbdf2["Date"].values.tolist()
#     tbdf3 = tbdf[tbdf["Context"] == "24 hours Post Injury"]
#     bio_date_dict["24-48 hours"] = tbdf3["Date"].values.tolist()
#     tbdf4 = tbdf[tbdf["Context"] == "When Asymptomatic"]
#     bio_date_dict["Asymptomatic"] = tbdf4["Date"].values.tolist()
#     tbdf5 = tbdf[tbdf["Context"] == "7 Days Post Return to Play"]
#     bio_date_dict["7 days Post-Unrestricted Return to Play"] = tbdf5["Date"].values.tolist()

#     timeline = []
#     timelines = []
#     i = 0
#     write = False
#     for t in temp_assess_df.itertuples(index=False):
#         if type(t[3]) != str: # If Context blank, consider it baseline
#             if i != 0:
#                 if write == True:
#                     timelines.append(timeline)
#                     timeline = [t]
#                     write = False
#                 else:
#                     timeline = [t]
#             timeline = [t]
#             if t[1] in bio_date_dict["Baseline"]:
#                 write = True
#             i = 1
#             continue
            
#         if t[3] not in assess_context_list[i:]:
#             if assess_context_list.index(t[3]) == i-1:
#                 timeline[-1] = t
#                 if t[1] in bio_date_dict.get(t[3], []):
#                     write = True
#                 continue
#             if write == True:
#                 timelines.append(timeline)
#             timeline = [t]
#             write = False
#             i = assess_context_list.index(t[3]) + 1
#         else:
#             timeline.append(t)
#             i = assess_context_list.index(t[3]) + 1
#         if t[1] in bio_date_dict.get(t[3], []):
#             write = True
#     if write == True:
#         timelines.append(timeline)
#     if len(timelines) > 1:
#         R = True
#         print("Repeated for", guid)
#     j = 0
#     for tl in timelines:
#         if len(tl) == 1:
#             print("dropping", tl)
#             continue
#         if R == True:
#             if j == 0:
#                 testdf = pd.DataFrame(tl)
#                 testdf[testdf.columns[-1]] = "R"
#                 finaldf = pd.concat([finaldf, testdf],  ignore_index=True)
#                 repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
#                 j+=1
#             else:
#                 testdf = pd.DataFrame(tl)
#                 testdf[testdf.columns[-1]] = "R"
#                 repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
#                 j+=1
#         else:
#         testdf = pd.DataFrame(tl)
#         finaldf = pd.concat([finaldf, testdf], ignore_index=True)