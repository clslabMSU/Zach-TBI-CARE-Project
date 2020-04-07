# -*- coding: utf-8 -*-
'''
@author: Zack Roy

10/31/2019 SPOOKY

Creates a dataset with only the GUID's wanted
DROPS ALL EMPTY COLUMNS
'''
import pandas as pd
import numpy as np
from glob import glob

bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
bio_tests_folder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_assessment_files\\"
new_data_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\Dropped CaseControl Doubles\\"

BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX"]

def main():
    # take in orginal dataframe with blood biomarker results
    df = pd.read_csv(bio_assay_path)
    # drop all columns with empty values 
    df = df.dropna(axis=1, how='all')
    # match dataset and tests on GUID
    biomarker_guid_list = df['BiomarkerAssayDataForm.Main.GUID'].unique()
    bio_tests_files = glob(bio_tests_folder + "*.csv")

    for filename in bio_tests_files:
        print("Working on {}".format(filename.split(sep="result")[-1].split(sep="2019")[0]))
        true_file_name = filename.split(sep="result")[-1].split(sep="2019")[0]
        # open and clean file  
        btdf = pd.read_csv(filename)
        result_df = pd.DataFrame(columns = btdf.columns)
        guid_label = btdf.columns[2]
        
        btdf = btdf.dropna(axis=1, how='all')

        for guid in biomarker_guid_list:
            if guid in BANNED_GUID:
                continue
            result_df = result_df.append(btdf.loc[btdf[guid_label] == guid])

        result_df.to_csv(new_data_path+true_file_name+'relevent_no_caseandcontrol.csv')

main()