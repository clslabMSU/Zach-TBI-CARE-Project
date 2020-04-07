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

cadet_guid_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Military Cadets\\csv files\\cadet_biomarker_cc.csv"
civilian_guid_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Cadet Only Data\\civ_guid.csv"
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
    # '_DemogrFITBIR_Appdx_0000310_': ['DemogrFITBIR_Appdx_0000310.Main.GUID', 'DemogrFITBIR_Appdx_0000310.Main.VisitDate', 'DemogrFITBIR_Appdx_0000310.Form Administration.ContextTypeOTH',
    #                                     'DemogrFITBIR_Appdx_0000310.Demographics.GenderTypExt',
    #                                     'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTyp',
    #                                     'DemogrFITBIR_Appdx_0000310.Sport History.SportTeamParticipationTypOTH',
    #                                     'DemogrFITBIR_Appdx_0000310.Military Club Sport Team Participation.SportTeamParticipationTyp'],
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

def main():
    # Generate Cadet Files
    for f in cadet_assessment_files:
        filename = f.split(sep="\\")[-1].split(sep='.csv')[0]
        if filename not in COLS_WANTED.keys():
            continue
        print(filename)
        df1 = pd.read_csv(f)
        df1 = df1[COLS_WANTED[filename]]
        
        df1.iloc[:,2] = df1.iloc[:,2].apply(str)
        df1.iloc[:,2] = df1.iloc[:,2].apply(cleanDate)
        df1.iloc[:,3] = df1.iloc[:,3].apply(fixContext)

        context_list = df1.iloc[:,3].unique()
        print(context_list)
        guid_list = df1.iloc[:,0].unique()
        # print(guid_list)
        guid_label = df1.columns[0]
        visit_label = df1.columns[1]
        context_label = df1.columns[3]

        # ********************************************************************
        # Creating list of column names, which must be different for each run
        # ********************************************************************
        # cols = ["GUID"]
        # for n in range(0, len(context_list)):
        #     for i in range(1, len(df1.columns)):
        #         cols.append(df1.columns[i]+'{}'.format(n+1))
        # print(cols)

        result_df_list = []
        for guid in guid_list:
            result_list = [guid]
            result_list_2 = [guid]
            result_list_3 = [guid]
            tdf = df1[df1[guid_label] == guid]
            print(tdf[context_label].value_counts())
            exit()
            continue
            write_2=False
            write_3=False
            
            for context in context_list:
                tdf1 = tdf[tdf[context_label]==context]

                if len(tdf1.index)==0:
                    for i in range(1, 6):
                        result_list.append(None)
                        result_list_2.append(None)
                        result_list_3.append(None)
                    continue

                if len(tdf1[visit_label].unique()) > 1:
                    counter = 0
                    print("********" + guid + "**************")
                    print(context)
                    unique_dates = sorted(tdf1[visit_label].unique())
                    for date in unique_dates:
                        print(date)
                        tdf2 = tdf1[tdf1[visit_label]==date]
                        if counter == 1:
                            write_2 = True
                            for i in range(1, 6):
                                result_list_2.append(tdf2.iloc[0,i])
                        elif counter == 2:
                            write_3 = True
                            for i in range(1, 6):
                                result_list_3.append(tdf2.iloc[0,i])
                        else:
                            for i in range(1, 6):
                                result_list.append(tdf2.iloc[0,i])
                        counter += 1
                    max_len = max(len(result_list), len(result_list_2), len(result_list_3))
                    while len(result_list) < max_len:
                        result_list.append(None)
                    while len(result_list_2) < max_len:
                        result_list_2.append(None)
                    while len(result_list_3) < max_len:
                        result_list_3.append(None)
                    continue

                for i in range(1, 6):
                    result_list.append(tdf1.iloc[0,i])
                    result_list_2.append(None)
                    result_list_3.append(None)
            result_df_list.append(result_list)
            if write_2:
                result_df_list.append(result_list_2)
            if write_3:
                result_df_list.append(result_list_3)

        result_df = pd.DataFrame(result_df_list,columns=cols)
        result_df.to_csv(outputFolder + "\\UnfoldedByContext_Military.csv", index=False)


    # Generate Civilian Files
    


if __name__ == "__main__":
    main()