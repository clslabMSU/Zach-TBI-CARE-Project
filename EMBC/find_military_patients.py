import pandas as pd
# import numpy as np
from glob import glob

outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
raw_assessments = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Assessments\\"
biomarkerFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Biomarker\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
assessment_files = glob(raw_assessments + "*.csv")
cadet_guid_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Military Cadets\\csv files\\cadet_biomarker_cc.csv"
# assessment_files = glob("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_assessment_files\\new_files\\" + "*.csv")

COLS_WANTED={
    "_PostInjForm_" : ["PostInjForm.Main Group.GUID", "PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd", "PostInjForm.Form Administration.ContextTypeOTH",
                        "PostInjForm.Post Injury Description.ARCAthleteTyp", 
                        "PostInjForm.Post Injury Description.SportTeamParticipationTyp",
                        "PostInjForm.Post Injury Description.LOCDur", 
                        "PostInjForm.Post Injury Description.LOCInd", 
                        "PostInjForm.Post Injury Description.TBIHospitalizedInd",
                        "PostInjForm.Post Injury Description.PstTraumtcAmnsInd", 
                        "PostInjForm.Return to Play Description.ReturnToPlayActualDate"],

    "_MedHx_Appendix_CARE0000310_" : ["MedHx_Appendix_CARE0000310.Main Group.GUID", "MedHx_Appendix_CARE0000310.Main Group.VisitDate", "MedHx_Appendix_CARE0000310.Main Group.CaseContrlInd", 
                                        "MedHx_Appendix_CARE0000310.Form Adminstration.ContextTypeOTH",
                                        "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesPastThreeMonthsInd", 
                                        "MedHx_Appendix_CARE0000310.Medical History (You).HeadachWorkLimitAbilityInd",
                                        "MedHx_Appendix_CARE0000310.Medical History (You).HeadacheLightBotherInd", 
                                        "MedHx_Appendix_CARE0000310.Medical History (You).HeadacheNasuseaInd",
                                        "MedHx_Appendix_CARE0000310.Medical History (You).LearningDisordrDiagnosInd", 
                                        "MedHx_Appendix_CARE0000310.Medical History (You).ModerateSevereTBIDiagnosInd",
                                        "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesDisordrDiagnosInd", 
                                        "MedHx_Appendix_CARE0000310.Medical History (You).MemoryDisorderDxInd"],

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
                                    'Concussion_Hx_0000310_2.Previous Concussion.HistHeadInjOrConcussInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.ConcussionPriorNum',
                                    'Concussion_Hx_0000310_2.Previous Concussion.SportRelatedConcussionInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.DiagnosedInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.AgeAtTBIEvent',
                                    'Concussion_Hx_0000310_2.Previous Concussion.TBILocInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.LOCDurRang', 
                                    'Concussion_Hx_0000310_2.Previous Concussion.LOCUnkDurInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.AmnesiaConcussInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.AmnesiaConcussDurRange',
                                    'Concussion_Hx_0000310_2.Previous Concussion.AmnsDurUnkInd',
                                    'Concussion_Hx_0000310_2.Previous Concussion.ConcussionSymptomDurDays',
                                    'Concussion_Hx_0000310_2.Previous Concussion.TBISxDurUnkInd'],
    '_DemogrFITBIR_': ['DemogrFITBIR.Main Group.GUID', 'DemogrFITBIR.Main Group.VisitDate', 
                        'DemogrFITBIR.Subject Demographics.GenderTyp',
                        'DemogrFITBIR.Subject Demographics.EthnUSACat'],
    '_DemogrFITBIR_Appdx_0000310_': ['DemogrFITBIR_Appdx_0000310.Main.GUID', 'DemogrFITBIR_Appdx_0000310.Main.VisitDat', 'DemogrFITBIR_Appdx_0000310.Form Administration.ContextTypeOTH',
                                        'DemogrFITBIR_Appdx_0000310.Demographics.GenderTypExt',
                                        'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp',
                                        'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTypOTH',
                                        'DemogrFITBIR_Appdx_0000310.Military Club Sport Team Participation.SportTeamParticipationTyp'],
    '_MedHx_FITBITR_': ['MedHx_FITBIR.Main.GUID', 'MedHx_FITBIR.Main.VisitDate', 'MedHx_FITBIR.Form Administration.ContextTypeOTH',
                            'MedHx_FITBIR.Headaches Migraines History.HeadachMigranDiagnsInd']
}

def main():
    # print("hello")
    # ================= Finding ALL Military Cadets from study =================
    # df1 = pd.read_csv(files[35], low_memory=False)
    # df1= df1[["DemogrFITBIR_Appdx_0000310.Main.GUID","DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp","DemogrFITBIR_Appdx_0000310.Sport History.MilitarySportActivityInd"]]
    # df1.columns = ["GUID", "Sport", "Milsport"]
    # df1 = df1.fillna(0)
    # df2 = df1[df1["Milsport"] != 0]
    # # print(df1)
    # # df2 = df1[df1["Milsport"] != "Skip this Question"]
    # # print(df2["Milsport"].value_counts())
    # mil_guid = df2["GUID"].unique()
    # pdf = pd.DataFrame({"GUID" : mil_guid})
    # pdf.to_csv(outputFolder + "cadet_guids.csv", index=False)
    
    # ================= Finding ALL Military Cadets Case/Control Status =================
    # df = pd.read_csv(outputFolder + "cadet_guids.csv")
    # result_df = pd.DataFrame()
    # for f in files:
    #     try:
    #         tdf = pd.read_csv(f, low_memory=False)
    #     except:
    #         print("Broke reading", f)
    #         continue
    #     guid_label = tdf.columns[2]
    #     cc_label = None
    #     for col in tdf.columns:
    #         if col.endswith("CaseContrlInd"):
    #             cc_label = col
    #     if not cc_label:
    #         print("No Case/Control in", f)
    #         continue
    #     else:
    #         print("Success with", f)
    #         tdf = tdf[[guid_label, cc_label]]
    #         tdf.columns = ["GUID", "CC"]
    #         tdf = tdf.fillna(0)
    #         tdf = tdf[tdf["CC"] != 0]
    #         rdf = tdf.merge(df, left_on="GUID", right_on="GUID")
    #         result_df = result_df.append(rdf)
    # result_df = result_df.fillna(0)
    # result_df = result_df[result_df["CC"] != 0]
    # result_df = result_df.drop_duplicates()
    # result_df = result_df[["GUID", "CC"]]
    # result_df.to_csv(outputFolder + "cadet_cc.csv", index=False)

    # ================= ALL Cadets Case/Control and Sport =================
    # result_df = pd.read_csv(outputFolder + "cadet_cc.csv")
    # rdf = result_df.merge(df2, left_on="GUID", right_on="GUID", how="right")
    # rdf = rdf.drop_duplicates()
    # rdf.to_csv(outputFolder + "cadet_ccandsport.csv", index=False)

    # ================= Finding ALL Cadets value counts (with duplicates) =================
    # sumdf = pd.read_csv(outputFolder + "cadet_ccandsport.csv")
    # rdf = pd.DataFrame()
    # rdf = pd.concat([rdf, sumdf["CC"].value_counts()], axis=1)
    # rdf = pd.concat([rdf, sumdf["Sport"].value_counts()], axis=1)
    # rdf = pd.concat([rdf, sumdf["Milsport"].value_counts()], axis=1)
    # rdf.to_csv(outputFolder + "cadet_ccandsport_counts.csv")

    # ================= Finding biomarker Military Cadets from study =================
    # cdf = pd.read_csv(outputFolder + "cadet_guids.csv")
    # bdf = pd.read_csv(biomarkerFile)
    # bdf = bdf[["BiomarkerAssayDataForm.Main.GUID", "BiomarkerAssayDataForm.Main.CaseContrlInd"]]
    # bdf.columns = ["GUID", "CC"]
    # bdf = bdf.fillna(0)
    # bdf = bdf[bdf["CC"] != 0]
    # bio_guid = bdf["GUID"].unique()
    # both_guid = []
    # rdf = pd.DataFrame()
    # for guid in cdf["GUID"]:
    #     if guid in bio_guid:
    #         both_guid.append(guid)
    #         rdf = rdf.append(bdf[bdf["GUID"] == guid])
    # rdf = rdf.merge(df2, left_on="GUID", right_on="GUID", how="left")
    # rdf = rdf.drop_duplicates()
    # rdf.to_csv(outputFolder + "cadet_biomarker_ccandsports.csv", index=False)

    # ================= Finding ALL Military Cadets from study =================
    # newdf = pd.read_csv(outputFolder + "cadet_biomarker_ccandsports.csv")
    # rdf = pd.DataFrame()
    # rdf = pd.concat([rdf, newdf["CC"].value_counts()], axis=1)
    # rdf = pd.concat([rdf, newdf["Sport"].value_counts()], axis=1)
    # rdf = pd.concat([rdf, newdf["Milsport"].value_counts()], axis=1)
    # rdf.to_csv(outputFolder + "biomarker_cadet_ccandsport_counts.csv")

    # df = pd.read_csv(cadet_guid_file)
    count = {}
    # mguid = df["GUID"].unique()
    bdf = pd.read_csv(biomarkerFile)
    mguid = bdf["BiomarkerAssayDataForm.Main.GUID"].unique()
    for f in assessment_files:
        try:
            tdf = pd.read_csv(f, low_memory=False)
        except:
            print("Broke reading", f)
            continue
        filename = f.split("result")[-1].split("2019")[0]
        guid_label = tdf.columns[2]
        # fguid = tdf[guid_label].unique()
        rdf = pd.DataFrame()
        for guid in mguid:
            rdf = rdf.append(tdf[tdf[guid_label] == guid])
        count[filename] = len(rdf[guid_label].unique())
        rdf.to_csv(outputFolder + "Biomarker Only Data\\{}.csv".format(filename), index=False)
    # countdf = pd.DataFrame(count)
    # countdf.to_csv(outputFolder + "assessments_biomarker_cadets_counts.csv", index=False)

                
    

if __name__ == "__main__":
    main()