# -*- coding: utf-8 -*-
'''
@author: Zack Roy

10/22/2019

Comparing Context Type names and counts for all biomarker tests
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
    bio_tests_files = glob(bio_tests_folder + "*.csv")
    file_name_col = []
    context_type = {}

    for filename in bio_tests_files:
        print("Working file: {}".format(filename))
        btdf = pd.read_csv(filename, low_memory=False)
        true_file_name = filename.split(sep=r"\_")[-1].split(sep="_relevent")[0]
        file_name_col.append(true_file_name)
        guid_label = btdf.columns[2] # The name of the column that contains the guid
        visit_date_label = btdf.columns[3] # The name of the column that contains the visit date

        for col in btdf.columns:
            # print(col)
            if col.endswith('ContextTypeOTH'):
                context_type[true_file_name] = np.unique(btdf[col].values, return_counts=True)
    result_df = pd.DataFrame()
    for key in context_type.keys():
        temp_df = pd.DataFrame({key: context_type[key][0], "Count": context_type[key][1]})
        result_df = pd.concat([result_df, temp_df], axis=1)
    result_df.to_csv(result_file + "Context_type_summary.csv", index=False)
    

main()