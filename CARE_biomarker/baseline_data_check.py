# -*- coding: utf-8 -*-
'''
@author: Zack Roy

10/22/2019

Checking baseline data stats for inconsistencies
'''

import pandas as pd
import numpy as np
from glob import glob
from sys import maxsize

# INPUT FILES
bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
bio_tests_folder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\"
baseline_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Biomarker Assay Processing\\baseline_dates.xlsx"
# # OUTPUT FILE
result_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\" 

def main():
    # take in orginal dataframe with blood biomarker results
    df1 = pd.read_csv(bio_assay_path)
    # drop all columns with empty values 
    df1 = df1.dropna(axis=1, how='all')
    # Case only
    # df1 = df1[df1["BiomarkerAssayDataForm.Main.CaseContrlInd"] == "Case"]
    # match dataset and tests on GUID
    df2 = df1[df1['BiomarkerAssayDataForm.Form Administration.ContextTypeOTH'] == "Baseline"]
    total_diff = len(df2['BiomarkerAssayDataForm.Main.DaysSinceBaseline'])
    zeros = len(df2[df2['BiomarkerAssayDataForm.Main.DaysSinceBaseline'] == 0])
    print(df2)

main()