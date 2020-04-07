'''
@author: Zack Roy

11/05/2019

All Chosen Col's matched with biomarker assay data

*************************
Yo this is bonkers, many things were hardcoded and must be changed based on which file is printed
*************************
'''
import pandas as pd
from glob import glob

COLS_WANTED={
    # "PostInjForm" : ["PostInjForm.Main Group.GUID", "PostInjForm.Main Group.VisitDate","PostInjForm.Main Group.CaseContrlInd", "PostInjForm.Form Administration.ContextTypeOTH","PostInjForm.Post Injury Description.ARCAthleteTyp", 
    #             "PostInjForm.Post Injury Description.SportTeamParticipationTyp","PostInjForm.Post Injury Description.LOCDur", 
    #             "PostInjForm.Post Injury Description.LOCInd", "PostInjForm.Post Injury Description.TBIHospitalizedInd",
    #             "PostInjForm.Post Injury Description.PstTraumtcAmnsInd", "PostInjForm.Return to Play Description.ReturnToPlayActualDate"],

    "MedHx_Appendix_CARE0000310" : ["MedHx_Appendix_CARE0000310.Main Group.GUID", "MedHx_Appendix_CARE0000310.Main Group.VisitDate", "MedHx_Appendix_CARE0000310.Main Group.CaseContrlInd", 
                "MedHx_Appendix_CARE0000310.Form Adminstration.ContextTypeOTH",
                "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesPastThreeMonthsInd", "MedHx_Appendix_CARE0000310.Medical History (You).HeadachWorkLimitAbilityInd",
                "MedHx_Appendix_CARE0000310.Medical History (You).HeadacheLightBotherInd", "MedHx_Appendix_CARE0000310.Medical History (You).HeadacheNasuseaInd",
                "MedHx_Appendix_CARE0000310.Medical History (You).LearningDisordrDiagnosInd", "MedHx_Appendix_CARE0000310.Medical History (You).ModerateSevereTBIDiagnosInd",
                "MedHx_Appendix_CARE0000310.Medical History (You).HeadachesDisordrDiagnosInd", "MedHx_Appendix_CARE0000310.Medical History (You).MemoryDisorderDxInd"],

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
    # # Still Deciding '_CNSVitalSignsDomainScores_': ['CNSVitalSignsDomainScores.Main.GUID', 'CNSVitalSignsDomainScores.Main.VisitDate', 'CNSVitalSignsDomainScores.Global Domain NCI.CNSVtlSnsNCIStdScore', 'CNSVitalSignsDomainScores.Composite Memory.CNSVtlSnsCompMemStdScore', 'CNSVitalSignsDomainScores.Verbal Memory.CNSVtlSnsVBMStdScore', 'CNSVitalSignsDomainScores.Visual Memory.CNSVtlSnsVIMStdScore', 'CNSVitalSignsDomainScores.Psychomotor Speed.CNSVtlSnsPMSpeedStdScore', 'CNSVitalSignsDomainScores.Reaction Time.CNSVtlSnsReactTimeStdScore', 'CNSVitalSignsDomainScores.Complex Attention.CNSVtlSnsCAStdScore', 'CNSVitalSignsDomainScores.Cognitive Flexibility.CNSVtlSnsCFStdScore', 'CNSVitalSignsDomainScores.Processing Speed.CNSVtlSnsProcSpeedStdScore', 'CNSVitalSignsDomainScores.Executive Function.CNSVtlSnsExecFunctStdScore', 'CNSVitalSignsDomainScores.Simple Attention.CNSVtlSnsSVAStdScore', 'CNSVitalSignsDomainScores.Motor Speed.CNSVtlSnsMotorSpeedStdScore' ,'CNSVitalSignsDomainScores.Form Administration.ContextTypeOTH'],
    
    # # Image Data  '_ImagingFunctionalMR_': ['ImagingFunctionalMR.Main.GUID', 'ImagingFunctionalMR.Main.VisitDate', 'ImagingFunctionalMR.Image Information.ImgFile' ,'ImagingFunctionalMR.Form Administration.ContextTypeOTH'],
    
    # # Image Data  '_ImagingMR_': ['ImagingMR.Main.GUID', 'ImagingMR.Main.VisitDate', 'ImagingMR.Main.AgeYrs', 'ImagingMR.Image Information.ImgFile', 'ImagingMR.Main.GeneralNotesTxt'],
    
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
    # # '_SCAT3_': ['SCAT3.Main.GUID', 'SCAT3.Main.VisitDate', 'SCAT3.Scoring Summary.Scat3TotalSymptoms', 'SCAT3.Scoring Summary.Scat3TotSympScore'],
    
    # # NOT USEFUL, DISCONTINUTED FROM USE '_SF12_': ['SF12.Main.GUID', 'SF12.Main.VisitDate', 'SF12.SF-12.SF36GenHlthScore', 'SF12.Form Administration.ContextTypeOTH'],
    
    # '_SWLS_CDISC_FITBIR_': ['SWLS_CDISC_FITBIR.Main.GUID','SWLS_CDISC_FITBIR.Main.VisitDate',
    #                         'SWLS_CDISC_FITBIR.Main.CaseContrlInd', 'SWLS_CDISC_FITBIR.Form Administration.ContextTypeOTH',
    #                         'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifClosIdlScore', 
    #                         'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifCondExcllncScore', 
    #                         'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifSatfctnScore', 
    #                         'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifAchvmntScore', 
    #                         'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifChngScore', 
    #                         'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSTotalScore'],
    # # '_SWLS_CDISC_FITBIR_': ['SWLS_CDISC_FITBIR.Main.GUID', 'SWLS_CDISC_FITBIR.Main.CaseContrlInd', 'SWLS_CDISC_FITBIR.Main.VisitDate', 'SWLS_CDISC_FITBIR.Form Administration.ContextTypeOTH'],
    # '_VOMS_': [ "VOMS.Main.GUID", "VOMS.Main.VisitDate" , "VOMS.Main.CaseContrlInd", "VOMS.Form Administration.ContextTypeOTH",
    #             "VOMS.Baseline  Symptoms.VOMSHeadacheSymptomScl",
    #             "VOMS.Baseline  Symptoms.VOMSDizzinesSymptomScl",
    #             "VOMS.Baseline  Symptoms.VOMSNauseaSymptomScl",
    #             "VOMS.Baseline  Symptoms.VOMSFogginesSymptomScl",
    #             "VOMS.Smooth Pursuits.VOMSHeadacheSymptomScl",
    #             "VOMS.Smooth Pursuits.VOMSDizzinesSymptomScl",
    #             "VOMS.Smooth Pursuits.VOMSNauseaSymptomScl",
    #             "VOMS.Smooth Pursuits.VOMSFogginesSymptomScl",
    #             "VOMS.Smooth Pursuits.CommentTXT",
    #             "VOMS.Saccades - Horizontal.VOMSHeadacheSymptomScl",
    #             "VOMS.Saccades - Horizontal.VOMSDizzinesSymptomScl",
    #             "VOMS.Saccades - Horizontal.VOMSNauseaSymptomScl",
    #             "VOMS.Saccades - Horizontal.VOMSFogginesSymptomScl",
    #             "VOMS.Saccades - Vertical.VOMSHeadacheSymptomScl",
    #             "VOMS.Saccades - Vertical.VOMSDizzinesSymptomScl",
    #             "VOMS.Saccades - Vertical.VOMSNauseaSymptomScl",
    #             "VOMS.Saccades - Vertical.VOMSFogginesSymptomScl",
    #             "VOMS.Saccades - Vertical.CommentTXT",
    #             "VOMS.Convergence.VOMSHeadacheSymptomScl",
    #             "VOMS.Convergence.VOMSDizzinesSymptomScl",
    #             "VOMS.Convergence.VOMSNauseaSymptomScl",
    #             "VOMS.Convergence.VOMSFogginesSymptomScl",
    #             "VOMS.Convergence.VOMSNearPointConvergence1Measr",
    #             "VOMS.Convergence.VOMSNearPointConvergence2Measr",
    #             "VOMS.Convergence.VOMSNearPointConvergence3Measr",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSHeadacheSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSDizzinesSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSNauseaSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSFogginesSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSHeadacheSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSDizzinesSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSNauseaSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSFogginesSymptomScl",
    #             "VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.CommentTXT",
    #             "VOMS.Visual Motion Sensitivity (VMS) Test.VOMSHeadacheSymptomScl",
    #             "VOMS.Visual Motion Sensitivity (VMS) Test.VOMSDizzinesSymptomScl",
    #             "VOMS.Visual Motion Sensitivity (VMS) Test.VOMSNauseaSymptomScl",
    #             "VOMS.Visual Motion Sensitivity (VMS) Test.VOMSFogginesSymptomScl"]
}


bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
data_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\"
result_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Biomarker Assay Processing\\"
BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX"]

df = pd.read_csv(bio_assay_path)
df= df[["BiomarkerAssayDataForm.Main.GUID", "BiomarkerAssayDataForm.Main.VisitDate", 
        "BiomarkerAssayDataForm.Main.DaysSinceBaseline", "BiomarkerAssayDataForm.Main.CaseContrlInd", 
        "BiomarkerAssayDataForm.Form Administration.ContextType", "BiomarkerAssayDataForm.Form Administration.ContextTypeOTH"]]
df = df.rename(columns={"BiomarkerAssayDataForm.Main.GUID": "GUID",
                "BiomarkerAssayDataForm.Main.VisitDate": "VisitDate",
                "BiomarkerAssayDataForm.Main.DaysSinceBaseline": "DaysSinceBaseline",
                "BiomarkerAssayDataForm.Main.CaseContrlInd": "CCID",
                "BiomarkerAssayDataForm.Form Administration.ContextType": "Context",
                "BiomarkerAssayDataForm.Form Administration.ContextTypeOTH": "ContextOTH"})
df1 = pd.DataFrame()
for guid in df["GUID"].unique():
    if guid not in BANNED_GUID:
        df1 = df1.append(df[df["GUID"]==guid])

def cleanDate(date):
    return date.split("T")[0]

def fixContext(context):
    if not context:
        return None
    context = str(context)
    context = context.strip()
    if context == "6 m onths post-injury":
        return "6 months post-injury"
    elif context.endswith("1") or context.endswith("2") or context.endswith("3"):
        return context[:-1].strip()
    else:
        return context

df1["VisitDate"] = df1["VisitDate"].apply(str)
df1["VisitDate"] = df1["VisitDate"].apply(cleanDate)
df1["ContextOTH"] = df1["ContextOTH"].apply(fixContext)

context_list = ["Baseline","< 6 hours","24-48 hours","Asymptomatic",
                "Unrestricted Return to Play","7 days Post-Unrestricted Return to Play","6 months post-injury"]

guid_list = df1["GUID"].unique()

filelist = glob(data_file + "*.csv")
for f in filelist:

    true_file_name = f.split(sep="result_")[-1].split(sep="_2019")[0]
    print(true_file_name)
    if not COLS_WANTED.get(true_file_name, None):
        continue
    
    df_fail = pd.DataFrame()
    tdf = pd.read_csv(f)
    cols_wanted = COLS_WANTED[true_file_name]
    col_count = len(cols_wanted)
    guid_label = cols_wanted[0]
    visit_label = cols_wanted[1]
    cc_label = cols_wanted[2]
    context_label = cols_wanted[3]
    tdf[visit_label] = tdf[visit_label].apply(str)
    tdf[visit_label] = tdf[visit_label].apply(cleanDate)
    tdf[context_label] = tdf[context_label].apply(fixContext)
    true_context_list = tdf[context_label].unique()
    print(true_context_list)
    for context in true_context_list:
        if context not in context_list:
            print("FOUND {} ANOMOLY".format(context))
            df_fail = df_fail.append(tdf[tdf[context_label] == context])
            tdf = tdf[tdf[context_label] != context]
    tdf = tdf[cols_wanted]

    # ********************************************************************
    # Creating list of column names, which must be different for each run
    # ********************************************************************
    cols = [guid_label]
    for n in range(0, len(context_list)):
        for i in range(1, len(cols_wanted)):
            cols.append(cols_wanted[i]+'{}'.format(n+1))

    result_df_list = []
    banned_df_list = []
    for guid in guid_list:
        result_list = [guid]
        result_list_2 = [guid]
        result_list_3 = [guid]
        result_list_4 = [guid]
        xdf = tdf[tdf[guid_label] == guid]
        if guid == "TBIPN535ZAR":
            print(xdf)
        write_2=False
        write_3=False
        write_4=False
        for context in context_list:
            if guid == "TBIPN535ZAR":
                print(context)
            tdf1 = xdf[xdf[context_label]==context]
            if guid == "TBIPN535ZAR":
                print(tdf1)
            if len(tdf1.index)==0:
                for i in range(1, col_count):
                    result_list.append(None)
                    result_list_2.append(None)
                    result_list_3.append(None)
                    result_list_4.append(None)
                continue

            elif len(tdf1.index) > 1:
                counter = 0
                unique_dates = sorted(tdf1[visit_label].unique())
                for date in unique_dates:
                    tdf2 = tdf1[tdf1[visit_label]==date]
                    if counter == 1:
                        if guid == "TBIPN535ZAR":
                            print("****************************************Writing to 2")
                        write_2 = True
                        for i in range(1, col_count):
                            result_list_2.append(tdf2.iloc[0,i])
                    elif counter == 2:
                        if guid == "TBIPN535ZAR":
                            print("***********************************Writing to 3")
                        write_3 = True
                        for i in range(1, col_count):
                            result_list_3.append(tdf2.iloc[0,i])
                    elif counter == 3:
                        if guid == "TBIPN535ZAR":
                            print("******************************************Writing to 4")
                        write_4 = True
                        for i in range(1, col_count):
                            result_list_4.append(tdf2.iloc[0,i])
                    else:
                        for i in range(1, col_count):
                            result_list.append(tdf2.iloc[0,i])
                    counter += 1
                max_len = max(len(result_list), len(result_list_2), len(result_list_3), len(result_list_4))
                while len(result_list) < max_len:
                    result_list.append(None)
                while len(result_list_2) < max_len:
                    result_list_2.append(None)
                while len(result_list_3) < max_len:
                    result_list_3.append(None)
                while len(result_list_4) < max_len:
                    result_list_4.append(None)
                continue

            else:
                for i in range(1, col_count):
                    result_list.append(tdf1.iloc[0,i])
                    result_list_2.append(None)
                    result_list_3.append(None)
                    result_list_4.append(None)
        if guid not in BANNED_GUID:
            result_df_list.append(result_list)
            if write_2:
                result_df_list.append(result_list_2)
            if write_3:
                result_df_list.append(result_list_3)
            if write_4:
                result_df_list.append(result_list_4)
        else:
            banned_df_list.append(result_list)
            if write_2:
                banned_df_list.append(result_list_2)
            if write_3:
                banned_df_list.append(result_list_3)
            if write_4:
                banned_df_list.append(result_list_4)

    print(cols)
    print(result_df_list[0])
    banned_df = pd.DataFrame(banned_df_list,columns=cols)
    result_df = pd.DataFrame(result_df_list,columns=cols)
    result_df.to_csv(result_file + true_file_name +"_UnfoldedByContext.csv", index=False)
    banned_df.to_csv(result_file + true_file_name +"_Unfolded_BANNED.csv", index=False)
    df_fail.to_csv(result_file + true_file_name + "_ContextType_Mistakes.csv", index=False)


# df1 = pd.DataFrame()
# dfban = pd.DataFrame()

# for guid in df["GUID"].unique():
#     if guid not in BANNED_GUID:
#         df1 = df1.append(df[df["GUID"]==guid])
#     else:
#         dfban = dfban.append(df[df["GUID"]==guid])

# guid_list = df1["GUID"].unique()
# df2 = pd.read_csv(wanted_file)
# guid_label = df2.columns[2]
# visit_label = df2.columns[5]
# df3 = pd.DataFrame()
# df4 = pd.DataFrame()

# for guid in guid_list:
#     df3 = df3.append(df2[df2[guid_label]==guid])
# for guid in BANNED_GUID:
#     df4 = df4.append(df2[df2[guid_label]==guid])

# df3 = df3[COLS_WANTED]
# df4 = df4[COLS_WANTED]
# df3[visit_label] = df3[visit_label].apply(str)
# df3[visit_label] = df3[visit_label].apply(cleanDate)
# df3.to_csv(result_file + "PostInj.csv", index=False)

# df4[visit_label] = df4[visit_label].apply(str)
# df4[visit_label] = df4[visit_label].apply(cleanDate)
# df4.to_csv(result_file + "PostInj_banned.csv", index=False)