# -*- coding: utf-8 -*-
'''
@author: Zack Roy

10/24/2019

Checking for multiple Case and Control Status's for any tests
'''

import pandas as pd
import numpy as np
from glob import glob
from sys import maxsize

# INPUT FILES
bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
bio_tests_folder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\"
raw_data = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\"
# # OUTPUT FILE
result_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CaseVsControl\\" 

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
    result_DF = pd.DataFrame()
    guid_list = set()
    test_list = set()

    for filename in bio_tests_files:
        print("Working file: {}".format(filename))
        btdf = pd.read_csv(filename, low_memory=False)
        true_file_name = filename.split(sep=r"\_")[-1].split(sep="_relevent")[0]
        file_name_col.append(true_file_name)
        guid_label = btdf.columns[2] # The name of the column that contains the guid
        visit_date_label = btdf.columns[3] # The name of the column that contains the visit date
        count = 0
        
        this_df = pd.DataFrame()
        for col in btdf.columns:
            if col.endswith("CaseContrlInd"):
                cc_id_label = col
                break
            count += 1
        
        if count == len(btdf.columns):
            print("******************* NO CASE CONTROL INDICATOR *********************")
            continue
        for guid in btdf[guid_label].values:
            df = btdf[btdf[guid_label] == guid]
            cc = df[cc_id_label].unique()
            if "Case" in cc and "Control" in cc:
                # df3 = df.iloc[:,2:11]
                # this_df = this_df.append(df3)
                guid_list.add(guid)
                test_list.add(true_file_name)
        # this_df.to_csv(result_file + true_file_name + "Both_Case_and_Control.csv", index=False)
    
    print(guid_list)
    print(test_list)

if __name__ == "__main__":
    main()
