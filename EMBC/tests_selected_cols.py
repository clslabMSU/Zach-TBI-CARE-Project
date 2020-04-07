import pandas as pd
from glob import glob

outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
raw_assessments = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Assessments\\"
raw_biomarkerFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Biomarker\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
biomarker_assessments = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\"
cadet_assessments = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Cadet Only Data\\Cadet Only Assessments\\"
civ_assessments = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Civilian Only Data\\Civilian Only Assessments\\"

bio_assessment_files = glob(biomarker_assessments + "*.csv")
cadet_assessment_files = glob(cadet_assessments + "*.csv")
civ_assessment_files = glob(civ_assessments + "*.csv")
baseline_date_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\baseline_dates\\baseline_dates.csv"

cadet_guid_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Military Cadets\\csv files\\cadet_biomarker_cc.csv"
civilian_guid_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Cadet Only Data\\civ_guid.csv"
# assessment_files = glob("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_assessment_files\\new_files\\" + "*.csv")

COLS_WANTED={
    # "_PostInjForm_" : ["PostInjForm.Main Group.GUID", "PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd", "PostInjForm.Form Administration.ContextTypeOTH",
    #                     "PostInjForm.Post Injury Description.ARCAthleteTyp", 
    #                     "PostInjForm.Post Injury Description.SportTeamParticipationTyp",
    #                     "PostInjForm.Post Injury Description.LOCDur", 
    #                     "PostInjForm.Post Injury Description.LOCInd", 
    #                     "PostInjForm.Post Injury Description.TBIHospitalizedInd",
    #                     "PostInjForm.Post Injury Description.PstTraumtcAmnsInd", 
    #                     "PostInjForm.Return to Play Description.ReturnToPlayActualDate"],

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

    # '_BESS_': ['BESS.Main.GUID', 'BESS.Main.VisitDate','BESS.Main.CaseContrlInd', 'BESS.Form Administration.ContextTypeOTH',
    #             'BESS.Balance Error Scoring Test.BESSTotalFirmErrorCt', 
    #             'BESS.Balance Error Scoring Test.BESSTotalFoamErrorCt', 
    #             'BESS.Balance Error Scoring Test.BESSTotalErrorCt'],
    # # '_BESS_': ['BESS.Main.GUID', 'BESS.Main.CaseContrlInd','BESS.Main.VisitDate', 'BESS.Form Administration.ContextTypeOTH'],
    
    # '_BSI18_': ['BSI18.Main.GUID',  'BSI18.Main.VisitDate','BSI18.Main.CaseContrlInd', 'BSI18.Main.GeneralNotesTxt',
    #             'BSI18.Form Completion.BSI18SomScoreRaw', 
    #             'BSI18.Form Completion.BSI18DeprScoreRaw', 
    #             'BSI18.Form Completion.BSI18AnxScoreRaw', 
    #             'BSI18.Form Completion.BSI18GSIScoreRaw'],

    # # '_BSI18_': ['BSI18.Main.GUID', 'BSI18.Main.CaseContrlInd', 'BSI18.Main.VisitDate', 'BSI18.Main.GeneralNotesTxt'],
    
    # '_ImPACT_': ['ImPACT.Main.GUID', 'ImPACT.Main.VisitDate','ImPACT.Main.CaseContrlInd',  'ImPACT.Form Administration Group.ContextTypeOTH',
    #                 'ImPACT.Post-Concussion Symptom Scale (PCSS).ImPACTTotalSymptomScore', 
    #                 'ImPACT.ImPACT Test.ImPACTVerbMemoryCompScore', 
    #                 'ImPACT.ImPACT Test.ImPACTVisMemoryCompScore', 
    #                 'ImPACT.ImPACT Test.ImPACTVisMotSpeedCompScore', 
    #                 'ImPACT.ImPACT Test.ImPACTReactTimeCompScore', 
    #                 'ImPACT.ImPACT Test.ImPACTImplseCntrlCompScore'],
    # # '_ImPACT_': ['ImPACT.Main.GUID', 'ImPACT.Main.CaseContrlInd', 'ImPACT.Main.VisitDate', 'ImPACT.Form Administration Group.ContextTypeOTH'],
    
    # '_SAC_': ['SAC.Main.GUID',  'SAC.Main.VisitDate','SAC.Main.CaseContrlInd', 'SAC.Form Administration Group.ContextTypeOTH',
    #             'SAC.Scoring Summary.SACOrientationSubsetScore',
    #             'SAC.Scoring Summary.SACImmdMemorySubsetScore',
    #             'SAC.Scoring Summary.SACConcentationSubsetScore',
    #             'SAC.Scoring Summary.SACDelayedRecallSubsetScore',
    #             'SAC.Scoring Summary.SACTotalScore'],
    # # '_SAC_': ['SAC.Main.GUID', 'SAC.Main.CaseContrlInd', 'SAC.Main.VisitDate', 'SAC.Form Administration Group.ContextTypeOTH'],
    # '_SCAT3_': ['SCAT3.Main.GUID', 'SCAT3.Main.VisitDate', 
    #             'SCAT3.Scoring Summary.Scat3TotalSymptoms', 
    #             'SCAT3.Scoring Summary.Scat3TotSympScore'],
    # '_Concussion_Hx_0000310_2_': ['Concussion_Hx_0000310_2.Main Group.GUID', 'Concussion_Hx_0000310_2.Main Group.VisitDate', 'Concussion_Hx_0000310_2.Form Administration.ContextTypeOTH',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.HistHeadInjOrConcussInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.ConcussionPriorNum',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.SportRelatedConcussionInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.DiagnosedInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.AgeAtTBIEvent',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.TBILocInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.LOCDurRang', 
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.LOCUnkDurInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.AmnesiaConcussInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.AmnesiaConcussDurRange',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.AmnsDurUnkInd',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.ConcussionSymptomDurDays',
    #                                 'Concussion_Hx_0000310_2.Previous Concussion.TBISxDurUnkInd'],
    # '_DemogrFITBIR_': ['DemogrFITBIR.Main Group.GUID', 'DemogrFITBIR.Main Group.VisitDate', 
    #                     'DemogrFITBIR.Subject Demographics.GenderTyp',
    #                     'DemogrFITBIR.Subject Demographics.EthnUSACat'],
    '_DemogrFITBIR_Appdx_0000310_': ['DemogrFITBIR_Appdx_0000310.Main.GUID', 'DemogrFITBIR_Appdx_0000310.Main.VisitDate', 'DemogrFITBIR_Appdx_0000310.Form Administration.ContextTypeOTH',
                                        'DemogrFITBIR_Appdx_0000310.Demographics.GenderTypExt',
                                        'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp',
                                        'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTypOTH',
                                        'DemogrFITBIR_Appdx_0000310.Military Club Sport Team Participation.SportTeamParticipationTyp'],
    # '_MedHx_FITBITR_': ['MedHx_FITBIR.Main.GUID', 'MedHx_FITBIR.Main.VisitDate', 'MedHx_FITBIR.Form Administration.ContextTypeOTH',
    #                         'MedHx_FITBIR.Headaches Migraines History.HeadachMigranDiagnsInd']
}

def cleanDate(date):
    return date.split("T")[0]

def fixContext(context):
    context = context.strip()
    if context == "6 m onths post-injury":
        return "6 months post-injury"
    elif context.endswith("1") or context.endswith("2") or context.endswith("3"):
        return context[:-2]
    else:
        return context

BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX"]

bdf = pd.read_csv(baseline_date_file)
for guid in BANNED_GUID:
    bdf = bdf[bdf["GUID"] != guid]

for f in bio_assessment_files:
    filename = f.split(sep="\\")[-1].split(sep='selected')[0]
    # if filename not in COLS_WANTED.keys():
    #     continue
    print(filename)
    df1 = pd.read_csv(f)
    guid_label = df1.columns[0]
    context_label = df1.columns[3]
    date_label = df1.columns[1]

    # ************ SELECTING COLS (ARE ALREADY SELECTED IN FILE NOW) *************
    # df1 = df1[COLS_WANTED[filename]]
    
    # print(df1.iloc[:,1])
    # df1.iloc[:,1] = df1.iloc[:,1].apply(str)
    # df1.iloc[:,1] = df1.iloc[:,1].apply(cleanDate)
    # df1.iloc[:,2] = df1.iloc[:,2].apply(str)
    # df1.iloc[:,2] = df1.iloc[:,2].apply(fixContext)
    # # print(df1.head)
    # df1.to_csv(outputFolder+filename+"selected_cols.csv", index=False)

    for guid in bdf["GUID"].unique():
        df2 = df1[df1[guid_label] == guid]
        df3 = df2[df2[context_label] == "Baseline"]
        byr = bdf[bdf["GUID"] == guid]["Biomarker Baseline Date"].values[0].split(sep='/')[-1]
        for date in df3[date_label].values:
            if len(df3[date_label].values) > 1:
                print(len(df3[date_label].values))
            try:
                dfyr = date.split(sep="-")[0]
                # print(dfyr)
                if dfyr == byr:
                    print(guid, dfyr, byr)
            except:
                print("Error on", guid, date)
    