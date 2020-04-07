#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from glob import glob


filepath = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\"
new_data_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Baseline split\\"
baseline_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Biomarker Assay Processing\\baseline_dates.xlsx"
from datetime import datetime, timedelta

COLS_WANTED = {
    # '_BESS_': ['BESS.Main.GUID', 'BESS.Main.CaseContrlInd','BESS.Main.VisitDate', 'BESS.Balance Error Scoring Test.BESSTotalFirmErrorCt', 'BESS.Balance Error Scoring Test.BESSTotalFoamErrorCt', 'BESS.Balance Error Scoring Test.BESSTotalErrorCt'],
    '_BESS_': ['BESS.Main.GUID', 'BESS.Main.CaseContrlInd', 'BESS.Main.VisitDate', 'BESS.Form Administration.ContextTypeOTH'],
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

bio_tests_files = glob(filepath + "*.csv")


def cleanDate(date):
    if type(date) != str:
        return date
    return date.split("T")[0]


def fixContext(context):
    context = context.strip()
    if context == "6 m onths post-injury":
        return "6 months post-injury"
    elif context.endswith("1") or context.endswith("2") or context.endswith("3"):
        return context[:-2]
    else:
        return context

full_writer = pd.ExcelWriter(new_data_path+'Full_summary.xlsx', engine='xlsxwriter')
full_summary = pd.DataFrame(columns=["Test", "Neg Count", "Pos Count"])

for filename in bio_tests_files:
    print("Working file: {}".format(filename))
    # ****************************************************
    #                open and clean file
    # ****************************************************
    true_file_name = filename.split(sep="\\")[-1].split(sep="relevent")[0]
    cols = COLS_WANTED.get(true_file_name, None)
    # skip file if we don't want any columns from it
    if not cols:
        print('no cols')
        continue
    
    df = pd.read_csv(filename, dtype=str, na_values="null")
    # Reduce the file to only the columns we want
    df1 = df[cols]
    cols.append("Days Since Baseline")
    # The name of the column that contains the guid
    guid_label = df1.columns[0]
    cc_label = df1.columns[1]
    # The name of the column that contains the visit date
    visit_date_label = df1.columns[2]
    context_label = df1.columns[3]

    df1.loc[:, visit_date_label] = df1[visit_date_label].apply(str)
    df1.loc[:, context_label] = df1[context_label].apply(str)
    df1.loc[:, visit_date_label] = df1[visit_date_label].apply(
        cleanDate)
    df1.loc[:, context_label] = df1[context_label].apply(
        fixContext)

    tot_baseline_neg = pd.DataFrame(columns=cols)
    tot_6hr_neg = pd.DataFrame(columns=cols)
    tot_2448_neg = pd.DataFrame(columns=cols)
    tot_asymp_neg = pd.DataFrame(columns=cols)
    tot_unres_neg = pd.DataFrame(columns=cols)
    tot_7d_neg = pd.DataFrame(columns=cols)
    tot_6mo_neg = pd.DataFrame(columns=cols)
    tot_baseline_pos = pd.DataFrame(columns=cols)
    tot_6hr_pos = pd.DataFrame(columns=cols)
    tot_2448_pos = pd.DataFrame(columns=cols)
    tot_asymp_pos = pd.DataFrame(columns=cols)
    tot_unres_pos = pd.DataFrame(columns=cols)
    tot_7d_pos = pd.DataFrame(columns=cols)
    tot_6mo_pos = pd.DataFrame(columns=cols)

    tot_full_neg = pd.DataFrame(columns=cols)
    tot_full_pos = pd.DataFrame(columns=cols)

    baseline_df = pd.read_excel(baseline_file, index_col=0)

    # writer = pd.ExcelWriter(new_data_path+true_file_name +
    #                         'summary.xlsx', engine='xlsxwriter')
    # workbook = writer.book
    # worksheet = workbook.add_worksheet(true_file_name + "pos")
    # writer.sheets[true_file_name + "pos"] = worksheet
    # worksheet = workbook.add_worksheet(true_file_name + "neg")
    # writer.sheets[true_file_name + "neg"] = worksheet

    # **********************************************************************************************************
    # **********************************************************************************************************
    # **********************************************************************************************************
    #                                         LOOP OVER GUID STARTS
    # **********************************************************************************************************
    # **********************************************************************************************************
    # **********************************************************************************************************

    for guid in df1[guid_label].unique():
        # print("Working GUID: {}".format(guid))
        df2 = df1[df1[guid_label] == guid]

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

        df_baseline_neg = pd.DataFrame(columns=cols)
        df_6hr_neg = pd.DataFrame(columns=cols)
        df_2448_neg = pd.DataFrame(columns=cols)
        df_asymp_neg = pd.DataFrame(columns=cols)
        df_unres_neg = pd.DataFrame(columns=cols)
        df_7d_neg = pd.DataFrame(columns=cols)
        df_6mo_neg = pd.DataFrame(columns=cols)
        df_baseline_pos = pd.DataFrame(columns=cols)
        df_6hr_pos = pd.DataFrame(columns=cols)
        df_2448_pos = pd.DataFrame(columns=cols)
        df_asymp_pos = pd.DataFrame(columns=cols)
        df_unres_pos = pd.DataFrame(columns=cols)
        df_7d_pos = pd.DataFrame(columns=cols)
        df_6mo_pos = pd.DataFrame(columns=cols)

        con_dict_neg = {"Baseline": df_baseline_neg,
                        "< 6 hours": df_6hr_neg,
                        "24-48 hours": df_2448_neg,
                        "Asymptomatic": df_asymp_neg,
                        "Unrestricted Return to Play": df_unres_neg,
                        "7 days Post-Unrestricted Return to Play": df_7d_neg,
                        "6 months post-injury": df_6mo_neg}
        con_dict_pos = {"Baseline": df_baseline_pos,
                        "< 6 hours": df_6hr_pos,
                        "24-48 hours": df_2448_pos,
                        "Asymptomatic": df_asymp_pos,
                        "Unrestricted Return to Play": df_unres_pos,
                        "7 days Post-Unrestricted Return to Play": df_7d_pos,
                        "6 months post-injury": df_6mo_pos}
        blank_row = pd.DataFrame({guid_label: [guid],
                                  cc_label: [np.nan],
                                  visit_date_label: [np.nan],
                                  context_label: [np.nan]})
        
        # ****************************************************
        #         Splitting Data into correct data sets
        # ****************************************************
        df_pos = df2[df2["Days Since Baseline"] >= 0].copy()
        df_neg = df2[df2["Days Since Baseline"] < 0].copy()
        tot_full_neg = tot_full_neg.append(df_neg)
        tot_full_pos = tot_full_pos.append(df_pos)
        max_bin_size_pos = df_pos[context_label].value_counts().max()
        max_bin_size_neg = df_neg[context_label].value_counts().max()

        # *****************************************************************************************************************************
        #               NEGATIVE LOOP THROUGH
        # *****************************************************************************************************************************
        for val in df_neg[context_label].unique():
            if val == 'nan':
                continue
            tdf = con_dict_neg[val]
            tdf = tdf.append(
                df_neg[df_neg[context_label] == val])
            while len(tdf[tdf[guid_label] == guid]) < max_bin_size_neg:
                tdf = tdf.append(blank_row, ignore_index=True)
            con_dict_neg[val] = tdf

        # If there are 0 of any bins, fill them with blanks
        col_counter = 0
        for k in con_dict_neg.keys():
            tdf = con_dict_neg[k]
            while len(tdf[tdf[guid_label] == guid]) < max_bin_size_neg:
                tdf = tdf.append(blank_row, ignore_index=True)
            con_dict_neg[k] = tdf
        
        tot_baseline_neg = tot_baseline_neg.append(con_dict_neg["Baseline"], ignore_index=True)
        tot_6hr_neg = tot_6hr_neg.append(con_dict_neg["< 6 hours"], ignore_index=True)
        tot_2448_neg = tot_2448_neg.append(con_dict_neg["24-48 hours"], ignore_index=True)
        tot_asymp_neg = tot_asymp_neg.append(con_dict_neg["Asymptomatic"], ignore_index=True)
        tot_unres_neg = tot_unres_neg.append(con_dict_neg["Unrestricted Return to Play"], ignore_index=True)
        tot_7d_neg = tot_7d_neg.append(con_dict_neg["7 days Post-Unrestricted Return to Play"], ignore_index=True)
        tot_6mo_neg = tot_6mo_neg.append(con_dict_neg["6 months post-injury"], ignore_index=True)

        # *****************************************************************************************************************************
        #               POSTIVE LOOP THROUGH
        # *****************************************************************************************************************************
        for val in df_pos[context_label].unique():
            if val == 'nan':
                continue
            tdf = con_dict_pos[val]
            tdf = tdf.append(
                df_pos[df_pos[context_label] == val])
            while len(tdf[tdf[guid_label] == guid]) < max_bin_size_pos:
                tdf = tdf.append(blank_row, ignore_index=True)
            con_dict_pos[val] = tdf

        # If there are 0 of any bins, fill them with blanks
        col_counter = 0
        for k in con_dict_pos.keys():
            tdf = con_dict_pos[k]
            while len(tdf[tdf[guid_label] == guid]) < max_bin_size_pos:
                tdf = tdf.append(blank_row, ignore_index=True)
            con_dict_pos[k] = tdf
        
        tot_baseline_pos = tot_baseline_pos.append(con_dict_pos["Baseline"], ignore_index=True)
        tot_6hr_pos = tot_6hr_pos.append(con_dict_pos["< 6 hours"], ignore_index=True)
        tot_2448_pos = tot_2448_pos.append(con_dict_pos["24-48 hours"], ignore_index=True)
        tot_asymp_pos = tot_asymp_pos.append(con_dict_pos["Asymptomatic"], ignore_index=True)
        tot_unres_pos = tot_unres_pos.append(con_dict_pos["Unrestricted Return to Play"], ignore_index=True)
        tot_7d_pos = tot_7d_pos.append(con_dict_pos["7 days Post-Unrestricted Return to Play"], ignore_index=True)
        tot_6mo_pos = tot_6mo_pos.append(con_dict_pos["6 months post-injury"], ignore_index=True)


    # *****************************************************************************************************************************
    #               SPLIT RESULTS WRITING
    # *****************************************************************************************************************************
    # result_df_neg = [tot_baseline_neg,
    #                 tot_6hr_neg,
    #                 tot_2448_neg,
    #                 tot_asymp_neg,
    #                 tot_unres_neg,
    #                 tot_7d_neg,
    #                 tot_6mo_neg]

    # result_df_pos = [tot_baseline_pos,
    #                 tot_6hr_pos,
    #                 tot_2448_pos,
    #                 tot_asymp_pos,
    #                 tot_unres_pos,
    #                 tot_7d_pos,
    #                 tot_6mo_pos]

    # col_counter=0
    # for d in result_df_neg:
    #     d = d.rename(columns={guid_label:"GUID", cc_label:"Case or Control", visit_date_label:"Visit Date", context_label:"Context", "Days Since Baseline": "Days Since Baseline"})
    #     d = d[["GUID","Case or Control", "Visit Date", "Days Since Baseline", "Context"]]
    #     d.to_excel(writer, sheet_name=true_file_name+"neg",index=False, startrow=1 , startcol=col_counter)
    #     col_counter += 6
    
    # col_counter=0
    # for d in result_df_pos:
    #     d = d.rename(columns={guid_label:"GUID", cc_label:"Case or Control", visit_date_label:"Visit Date", context_label:"Context", "Days Since Baseline": "Days Since Baseline"})
    #     d = d[["GUID","Case or Control", "Visit Date", "Days Since Baseline", "Context"]]
    #     d.to_excel(writer, sheet_name=true_file_name+"pos",index=False, startrow=1 , startcol=col_counter)
    #     col_counter += 6
    # writer.save()


    # *****************************************************************************************************************************
    #               SUMMARY RESULTS WRITING
    # *****************************************************************************************************************************
    neg_guid_count = len(tot_full_neg[guid_label].unique())
    pos_guid_count = len(tot_full_pos[guid_label].unique())
    test_name = true_file_name
    full_summary = full_summary.append({"Test":test_name, "Neg Count":neg_guid_count,"Pos Count":pos_guid_count},ignore_index=True)
    
full_summary.to_excel(full_writer,index=False)
full_writer.save()
