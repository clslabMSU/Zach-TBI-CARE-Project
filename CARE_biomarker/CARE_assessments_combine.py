# -*- coding: utf-8 -*-
'''
@author: Zack Roy

9/17/2019

extracting and organizing blood biomarker data from the CARE dataset
'''

import pandas as pd
import numpy as np
from glob import glob
from sys import maxsize
from datetime import datetime, timedelta

# INPUT FILES
bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
bio_tests_folder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\"
baseline_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Biomarker Assay Processing\\baseline_dates.xlsx"
# # OUTPUT FILE
new_data_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\context_type\\" 


# **************************************************************************************************************
# * Column names for each file must be listed here.
# * GUID MUST COME FIRST
# * VISIT DATE MUST COME SECOND
# * List all other columns AFTER those 2.
# **************************************************************************************************************
COLS_WANTED = { 
                # '_BESS_': ['BESS.Main.GUID', 'BESS.Main.CaseContrlInd','BESS.Main.VisitDate', 'BESS.Balance Error Scoring Test.BESSTotalFirmErrorCt', 'BESS.Balance Error Scoring Test.BESSTotalFoamErrorCt', 'BESS.Balance Error Scoring Test.BESSTotalErrorCt'],
                '_BESS_': ['BESS.Main.GUID', 'BESS.Main.CaseContrlInd','BESS.Main.VisitDate', 'BESS.Form Administration.ContextTypeOTH'],
                # '_BSI18_': ['BSI18.Main.GUID', 'BSI18.Main.CaseContrlInd', 'BSI18.Main.VisitDate', 'BSI18.Form Completion.BSI18SomScoreRaw', 'BSI18.Form Completion.BSI18DeprScoreRaw', 'BSI18.Form Completion.BSI18AnxScoreRaw', 'BSI18.Form Completion.BSI18GSIScoreRaw'],
                '_BSI18_': ['BSI18.Main.GUID', 'BSI18.Main.CaseContrlInd', 'BSI18.Main.VisitDate', 'BSI18.Main.GeneralNotesTxt'],
                # Still Deciding '_CNSVitalSignsDomainScores_': ['CNSVitalSignsDomainScores.Main.GUID', 'CNSVitalSignsDomainScores.Main.VisitDate', 'CNSVitalSignsDomainScores.Global Domain NCI.CNSVtlSnsNCIStdScore', 'CNSVitalSignsDomainScores.Composite Memory.CNSVtlSnsCompMemStdScore', 'CNSVitalSignsDomainScores.Verbal Memory.CNSVtlSnsVBMStdScore', 'CNSVitalSignsDomainScores.Visual Memory.CNSVtlSnsVIMStdScore', 'CNSVitalSignsDomainScores.Psychomotor Speed.CNSVtlSnsPMSpeedStdScore', 'CNSVitalSignsDomainScores.Reaction Time.CNSVtlSnsReactTimeStdScore', 'CNSVitalSignsDomainScores.Complex Attention.CNSVtlSnsCAStdScore', 'CNSVitalSignsDomainScores.Cognitive Flexibility.CNSVtlSnsCFStdScore', 'CNSVitalSignsDomainScores.Processing Speed.CNSVtlSnsProcSpeedStdScore', 'CNSVitalSignsDomainScores.Executive Function.CNSVtlSnsExecFunctStdScore', 'CNSVitalSignsDomainScores.Simple Attention.CNSVtlSnsSVAStdScore', 'CNSVitalSignsDomainScores.Motor Speed.CNSVtlSnsMotorSpeedStdScore' ,'CNSVitalSignsDomainScores.Form Administration.ContextTypeOTH'],
                
                # Image Data  '_ImagingFunctionalMR_': ['ImagingFunctionalMR.Main.GUID', 'ImagingFunctionalMR.Main.VisitDate', 'ImagingFunctionalMR.Image Information.ImgFile' ,'ImagingFunctionalMR.Form Administration.ContextTypeOTH'],
                
                # Image Data  '_ImagingMR_': ['ImagingMR.Main.GUID', 'ImagingMR.Main.VisitDate', 'ImagingMR.Main.AgeYrs', 'ImagingMR.Image Information.ImgFile', 'ImagingMR.Main.GeneralNotesTxt'],
                
                # '_ImPACT_': ['ImPACT.Main.GUID', 'ImPACT.Main.CaseContrlInd', 'ImPACT.Main.VisitDate', 'ImPACT.Post-Concussion Symptom Scale (PCSS).ImPACTTotalSymptomScore', 'ImPACT.ImPACT Test.ImPACTVerbMemoryCompScore', 'ImPACT.ImPACT Test.ImPACTVisMemoryCompScore', 'ImPACT.ImPACT Test.ImPACTVisMotSpeedCompScore', 'ImPACT.ImPACT Test.ImPACTReactTimeCompScore', 'ImPACT.ImPACT Test.ImPACTImplseCntrlCompScore'],
                '_ImPACT_': ['ImPACT.Main.GUID', 'ImPACT.Main.CaseContrlInd', 'ImPACT.Main.VisitDate', 'ImPACT.Form Administration Group.ContextTypeOTH'],
                # '_SAC_': ['SAC.Main.GUID', 'SAC.Main.CaseContrlInd', 'SAC.Main.VisitDate', 'SAC.Scoring Summary.SACOrientationSubsetScore','SAC.Scoring Summary.SACImmdMemorySubsetScore','SAC.Scoring Summary.SACConcentationSubsetScore','SAC.Scoring Summary.SACDelayedRecallSubsetScore','SAC.Scoring Summary.SACTotalScore'],
                '_SAC_': ['SAC.Main.GUID', 'SAC.Main.CaseContrlInd', 'SAC.Main.VisitDate', 'SAC.Form Administration Group.ContextTypeOTH'],
                # '_SCAT3_': ['SCAT3.Main.GUID', 'SCAT3.Main.VisitDate', 'SCAT3.Scoring Summary.Scat3TotalSymptoms', 'SCAT3.Scoring Summary.Scat3TotSympScore'],
                
                # NOT USEFUL, DISCONTINUTED FROM USE '_SF12_': ['SF12.Main.GUID', 'SF12.Main.VisitDate', 'SF12.SF-12.SF36GenHlthScore', 'SF12.Form Administration.ContextTypeOTH'],
                
                # '_SWLS_CDISC_FITBIR_': ['SWLS_CDISC_FITBIR.Main.GUID', 'SWLS_CDISC_FITBIR.Main.CaseContrlInd','SWLS_CDISC_FITBIR.Main.VisitDate', 'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifClosIdlScore', 'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifCondExcllncScore', 'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifSatfctnScore', 'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifAchvmntScore', 'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSLifChngScore', 'SWLS_CDISC_FITBIR.Satisfaction with Life Scale.SWLSTotalScore'],
                '_SWLS_CDISC_FITBIR_': ['SWLS_CDISC_FITBIR.Main.GUID', 'SWLS_CDISC_FITBIR.Main.CaseContrlInd', 'SWLS_CDISC_FITBIR.Main.VisitDate', 'SWLS_CDISC_FITBIR.Form Administration.ContextTypeOTH'],
                # '_VOMS_': ['VOMS.Main.GUID', 'VOMS.Main.VisitDate', 'VOMS.Smooth Pursuits.VOMSHeadacheSymptomScl','VOMS.Smooth Pursuits.VOMSDizzinesSymptomScl','VOMS.Smooth Pursuits.VOMSNauseaSymptomScl','VOMS.Smooth Pursuits.VOMSFogginesSymptomScl','VOMS.Saccades - Horizontal.VOMSHeadacheSymptomScl','VOMS.Saccades - Horizontal.VOMSDizzinesSymptomScl','VOMS.Saccades - Horizontal.VOMSNauseaSymptomScl','VOMS.Saccades - Horizontal.VOMSFogginesSymptomScl','VOMS.Saccades - Vertical.VOMSHeadacheSymptomScl','VOMS.Saccades - Vertical.VOMSDizzinesSymptomScl', 'VOMS.Saccades - Vertical.VOMSNauseaSymptomScl', 'VOMS.Saccades - Vertical.VOMSFogginesSymptomScl', 'VOMS.Convergence.VOMSHeadacheSymptomScl', 'VOMS.Convergence.VOMSDizzinesSymptomScl', 'VOMS.Convergence.VOMSNauseaSymptomScl', 'VOMS.Convergence.VOMSFogginesSymptomScl', 'VOMS.Convergence.VOMSNearPointConvergence1Measr', 'VOMS.Convergence.VOMSNearPointConvergence2Measr', 'VOMS.Convergence.VOMSNearPointConvergence3Measr','VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSHeadacheSymptomScl', 'VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSDizzinesSymptomScl', 'VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSNauseaSymptomScl', 'VOMS.Vestibular Ocular Reflex (VOR) - Horizontal Test.VOMSFogginesSymptomScl', 'VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSHeadacheSymptomScl', 'VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSDizzinesSymptomScl', 'VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSNauseaSymptomScl','VOMS.Vestibular Ocular Reflex (VOR) - Vertical Test.VOMSFogginesSymptomScl' ,'VOMS.Visual Motion Sensitivity (VMS) Test.VOMSHeadacheSymptomScl','VOMS.Visual Motion Sensitivity (VMS) Test.VOMSDizzinesSymptomScl', 'VOMS.Visual Motion Sensitivity (VMS) Test.VOMSNauseaSymptomScl','VOMS.Visual Motion Sensitivity (VMS) Test.VOMSFogginesSymptomScl','VOMS.Form Administration.ContextTypeOTH'],
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
    # take in orginal dataframe with blood biomarker results
    df1 = pd.read_csv(bio_assay_path)
    # drop all columns with empty values 
    df1 = df1.dropna(axis=1, how='all')
    # Case only
    # df1 = df1[df1["BiomarkerAssayDataForm.Main.CaseContrlInd"] == "Case"]
    # match dataset and tests on GUID
    # biomarker_guid_list = set(df1['BiomarkerAssayDataForm.Main.GUID'].unique().tolist())
    bio_tests_files = glob(bio_tests_folder + "*.csv")
    file_name_col = []


    for filename in bio_tests_files:
        print("Working file: {}".format(filename))
        # ****************************************************
        #                open and clean file
        # ****************************************************
        true_file_name = filename.split(sep="\\")[-1].split(sep="relevent")[0]
        file_name_col.append(true_file_name)
        columns = COLS_WANTED.get(true_file_name, None)
        # skip file if we don't want any columns from it
        if not columns:
            print('no cols')
            continue
        btdf = pd.read_csv(filename, low_memory=False)
        # Reduce the file to only the columns we want
        btdf = btdf[columns]
        relevent_rows = btdf.dropna(axis=1, how='all')
        guid_label = relevent_rows.columns[0] # The name of the column that contains the guid
        cc_label = relevent_rows.columns[1]
        visit_date_label = relevent_rows.columns[2] # The name of the column that contains the visit date
        context_label = relevent_rows.columns[3]
        
        relevent_rows[visit_date_label] = relevent_rows[visit_date_label].apply(str)
        relevent_rows[visit_date_label] = relevent_rows[visit_date_label].apply(cleanDate)
        relevent_rows[context_label] = relevent_rows[context_label].apply(fixContext)

        # ***********************************************************************
        #  Iterating over each test for each patient and separating into columns
        # ***********************************************************************
        relevent_unique = relevent_rows[guid_label].unique()
        # result_df = pd.DataFrame()
        
        # need to know how many tests were done so we can create the correct number of columns
        # max_tests_done = relevent_rows[guid_label].value_counts().max()
        

        baseline_df = pd.read_excel(baseline_file, index_col=0)
        # ********************************************************************
        # Creating list of column names, which must be different for each run
        # ********************************************************************
        # cols = []
        # SCAT3 has no CASE CONTROL data
        # if true_file_name == "_SCAT3_":
        #     for n in range(0, max_tests_done):
        #         cols.append('Test{}_VisitDate'.format(n+1))
        #         cols.append('Test{}_DaysSinceBaseline'.format(n+1))
        #         for i in range(3, len(columns)):
        #             cols.append(columns[i]+'{}'.format(n+1))
        # else:
        #     for n in range(0, max_tests_done):
        #         cols.append('Test{}_CaseControl'.format(n+1))
        #         cols.append('Test{}_VisitDate'.format(n+1))
        #         cols.append('Test{}_DaysSinceBaseline'.format(n+1))
        #         for i in range(3, len(columns)):
        #             cols.append(columns[i]+'{}'.format(n+1))

        # result_df_pos = result_df.reindex(columns=cols).copy()
        # result_df_neg = result_df.reindex(columns=cols).copy()

        df_baseline_neg = pd.DataFrame()
        df_6hr_neg = pd.DataFrame()
        df_2448_neg = pd.DataFrame()
        df_asymp_neg = pd.DataFrame()
        df_unres_neg = pd.DataFrame()
        df_7d_neg = pd.DataFrame()
        df_6mo_neg = pd.DataFrame()
        df_baseline_pos = pd.DataFrame()
        df_6hr_pos = pd.DataFrame()
        df_2448_pos = pd.DataFrame()
        df_asymp_pos = pd.DataFrame()
        df_unres_pos = pd.DataFrame()
        df_7d_pos = pd.DataFrame()
        df_6mo_pos = pd.DataFrame()

        df_result_list = [df_baseline_neg,df_6hr_neg,df_2448_neg,df_asymp_neg,df_unres_neg,df_7d_neg,df_6mo_neg,df_baseline_pos,df_6hr_pos,df_2448_pos,df_asymp_pos,df_unres_pos,df_7d_pos,df_6mo_pos]

        writer = pd.ExcelWriter(new_data_path+true_file_name+'summary.xlsx', engine='xlsxwriter')
        workbook = writer.book
        worksheet = workbook.add_worksheet(true_file_name + "pos")
        writer.sheets[true_file_name + "pos"] = worksheet
        worksheet = workbook.add_worksheet(true_file_name + "neg")
        writer.sheets[true_file_name + "neg"] = worksheet

        for guid in relevent_unique:
            df2 = relevent_rows.loc[relevent_rows[guid_label] == guid]
            pd.to_datetime(relevent_rows[visit_date_label], yearfirst=True)
            df2 = df2.sort_values(relevent_rows.columns[2])
            df2 = df2.reset_index()
            visits = len(df2.index)
            max_bin_size = df2[context_label].value_counts().max()

            # ****************************************************
            #          Finding days Since Baseline data
            # ****************************************************
            baseline_date = baseline_df.loc[guid]["Baseline Date"]
            days_since_baseline = []
            for idx, row in df2.iterrows():
                # Handling missing visit dates
                if row[visit_date_label] == 'nan':
                    days_since_baseline.append(np.nan)
                    continue
                date_str = row[visit_date_label]
                date_ints = date_str.split("-")
                visit_date = datetime(year=int(date_ints[0]), month=int(date_ints[1]),day=int(date_ints[2]))
                bl = visit_date - baseline_date
                days_since_baseline.append(bl.days)
            df2["Days Since Baseline"] = days_since_baseline
            df2 = df2.drop(columns="index")

            # ****************************************************
            #         Splitting Data into correct data sets
            # ****************************************************
            df_pos = df2[df2["Days Since Baseline"] >= 0].copy()
            df_neg = df2[df2["Days Since Baseline"] < 0].copy()
            max_bin_size_pos = df_pos[context_label].value_counts().max()
            max_bin_size_neg = df_neg[context_label].value_counts().max()
            
            temp_df_baseline_neg = df_neg[df_neg[context_label] == "Baseline"]
            temp_df_6hr_neg = df_neg[df_neg[context_label] == "< 6 hours"]
            temp_df_2448_neg = df_neg[df_neg[context_label] == "24-48 hours"]
            temp_df_asymp_neg = df_neg[df_neg[context_label] == "Asymptomatic"]
            temp_df_unres_neg = df_neg[df_neg[context_label] == "Unrestricted Return to Play"]
            temp_df_7d_neg = df_neg[df_neg[context_label] == "7 days Post-Unrestricted Return to Play"]
            temp_df_6mo_neg = df_neg[df_neg[context_label] == "6 months post-injury"]
            temp_df_baseline_pos = df_pos[df_pos[context_label] == "Baseline"]
            temp_df_6hr_pos = df_pos[df_pos[context_label] == "< 6 hours"]
            temp_df_2448_pos = df_pos[df_pos[context_label] == "24-48 hours"]
            temp_df_asymp_pos = df_pos[df_pos[context_label] == "Asymptomatic"]
            temp_df_unres_pos = df_pos[df_pos[context_label] == "Unrestricted Return to Play"]
            temp_df_7d_pos = df_pos[df_pos[context_label] == "7 days Post-Unrestricted Return to Play"]
            temp_df_6mo_pos = df_pos[df_pos[context_label] == "6 months post-injury"]

            df_temp_list = [temp_df_baseline_neg, temp_df_6hr_neg, temp_df_2448_neg, temp_df_asymp_neg, temp_df_unres_neg, temp_df_7d_neg, temp_df_6mo_neg, temp_df_baseline_pos, temp_df_6hr_pos, temp_df_2448_pos, temp_df_asymp_pos, temp_df_unres_pos, temp_df_7d_pos, temp_df_6mo_pos]
            i = 0
            for d in df_temp_list:
                if i < 6:
                    while len(d) < max_bin_size_neg:
                        d = d.append(pd.Series([guid, np.nan,np.nan,np.nan,np.nan]), ignore_index=True)
                if i >= 6:
                    while len(d) < max_bin_size_pos:
                        d = d.append(pd.Series([guid, np.nan,np.nan,np.nan,np.nan]), ignore_index=True)
                df_result_list[i] = pd.concat([df_result_list[i], d], axis=0, ignore_index=True, sort=False)
                i += 1
        
        #df_result_list = [df_baseline_neg,df_6hr_neg,df_2448_neg,df_asymp_neg,df_unres_neg,df_7d_neg,df_6mo_neg,df_baseline_pos,df_6hr_pos,df_2448_pos,df_asymp_pos,df_unres_pos,df_7d_pos,df_6mo_pos]

        col_counter = 0
        i = 0
        for d in df_result_list:
            if i < 6:
                d.to_excel(writer, sheet_name=true_file_name+"neg",index=False, startrow=1 , startcol=col_counter)
                i+=1
                col_counter += 5
            if i == 6:
                col_counter = 0
            if i >= 6:
                d.to_excel(writer, sheet_name=true_file_name+"pos",index=False, startrow=1 , startcol=col_counter)
                i+=1
                col_counter += 5


            # ****************************************************
            #                 UNFOLDING THE DATA
            # ****************************************************
            # negative_visit_list = []
            # positive_visit_list = []
            # for i in range(0, visits):
            #     if days_since_baseline[0] < 0:
            #         for j in range(2, len(df2.columns)):
            #             negative_visit_list.append(df2.iloc[i,j])
            #             if j == 3:
            #                     negative_visit_list.append(days_since_baseline.pop(0))
            #     elif days_since_baseline[0] >= 0:
            #         for j in range(2, len(df2.columns)):
            #             positive_visit_list.append(df2.iloc[i,j])
            #             if j == 3:
            #                 positive_visit_list.append(days_since_baseline.pop(0))
            # Add empty values so the list has a constant length
            # while len(negative_visit_list) < len(cols):
            #     negative_visit_list.append(np.nan)
            # while len(positive_visit_list) < len(cols):
            #     positive_visit_list.append(np.nan)
            # result_df_neg.loc[guid] = negative_visit_list
            # result_df_pos.loc[guid] = positive_visit_list
            
        # result_df_neg.to_excel(new_data_path + true_file_name + 'neg.xlsx', index=True)
        # result_df_pos.to_excel(new_data_path + true_file_name + 'pos.xlsx', index=True)
        # writer.sheets[filename[:-4]].write_string(0, col_counter, alg)
        # result_df1.to_excel(writer, sheet_name=filename[:-4],index=True, startrow=1 , startcol=col_counter)
        # result_df2.to_excel(writer, sheet_name=filename[:-4],index=True, startrow=12 , startcol=col_counter)
        # result_df3.to_excel(writer, sheet_name=filename[:-4],index=True, startrow=23 , startcol=col_counter)

        writer.save()
    return 0

if __name__ == "__main__":
    main()