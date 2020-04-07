# -*- coding: utf-8 -*-
'''
@author: Zack Roy

9/17/2019

extracting and organizing assessment data from the CARE dataset
'''
# ****************************************************************************************************************
# ****************************************************************************************************************
# ****************************************************************************************************************
# * WARNING: Running this file without modifying filepath's WILL overwrite the summary file in the new_data_path *
# ****************************************************************************************************************
# ****************************************************************************************************************
# ****************************************************************************************************************
import pandas as pd
import numpy as np
from glob import glob
from sys import maxsize

bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
bio_tests_folder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_assessment_files\\"
new_data_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\"


def main():
    # take in orginal dataframe with blood biomarker results
    df = pd.read_csv(bio_assay_path)
    # drop all columns with empty values 
    df = df.dropna(axis=1, how='all')
    # match dataset and tests on GUID
    biomarker_guid_list = df['BiomarkerAssayDataForm.Main.GUID'].unique()
    bio_tests_files = glob(bio_tests_folder + "*.csv")
    guid_cc_dict = {}
    for guid in biomarker_guid_list:
        guid_cc_dict[guid] = df['BiomarkerAssayDataForm.Main.CaseContrlInd'].loc[df['BiomarkerAssayDataForm.Main.GUID'] == guid].iloc[0]
    guid_match_df = pd.DataFrame()
    file_name_col = []
    counter_list = []
    case_count = []
    control_count = []
    guid_list = []
    full_count_df = pd.DataFrame()
    rel_count_df = pd.DataFrame()
    guid_test_count_df = pd.Series(guid_cc_dict, index=biomarker_guid_list)

    for filename in bio_tests_files:
        print("Working on {}".format(filename.split(sep="result")[-1].split(sep="2019")[0]))
        # open and clean file
        file_name_col.append(filename.split(sep="result")[-1].split(sep="2019")[0])
        counter = 0
        with open(filename, 'r') as file_contents:
            btdf = pd.read_csv(file_contents)
        btdf = btdf.dropna(axis=1, how='all')
        # ******************************************************
        # ******* ASSUMES THE 3rd COLUMN IS THE GUID ***********
        # ******************************************************
        guid_label = btdf.columns[2]
        # ******************************************************
        # ******************************************************
        # ******************************************************
        
        # unique GUID matches
        btdf_unique = btdf.iloc[:,2].unique()
        btdf_isin = np.isin(btdf_unique, biomarker_guid_list)
        btdf_len = len(btdf_isin)
        btdf_isin_values = []
        for i in range(0,btdf_len):
            if btdf_isin[i] == True:
                btdf_isin_values.append(btdf_unique[i]) # creating list of unique GUIDs
                counter += 1
        guid_list.append(btdf_isin_values)
        counter_list.append(counter)

        # Case vs Control and Gathering All Biomarker Rows
        CvC = []
        relevent_rows = pd.DataFrame()
        for guid in btdf_isin_values:
            CvC.append(guid_cc_dict[guid])
            relevent_rows = relevent_rows.append(btdf.loc[btdf[guid_label] == guid])
        case_count.append(CvC.count('Case'))
        control_count.append(CvC.count('Control'))
        relevent_rows = relevent_rows.dropna(axis=1, how='all')

        if counter <= 1:
            continue
    
        # Columns to redo FULL count/unique count
        column=btdf.columns.values.tolist()
        dr=[]
        for i in column:
            ar=[i + " :" + str(btdf[i].nunique())+ ":"+ str(len(btdf[btdf[i].notnull()]))]
            dr=dr+ar
        Dr=pd.DataFrame(dr)
        Dr=Dr[0].str.split(":", n=3,expand = True)
        Dr=Dr.rename(columns={0:filename.split(sep="result")[-1].split(sep="2019")[0],1:"Count_unique",2:"Count"})
        full_count_df = pd.concat([full_count_df, Dr],axis=1)

        # Columns to do RELEVENT count/unique count
        column=relevent_rows.columns.values.tolist()
        dr=[]
        for i in column:
            ar=[i + " :" + str(relevent_rows[i].nunique())+ ":"+ str(len(relevent_rows[relevent_rows[i].notnull()]))]
            dr=dr+ar
        Dr=pd.DataFrame(dr)
        Dr=Dr[0].str.split(":", n=3,expand = True)
        Dr=Dr.rename(columns={0:filename.split(sep="result")[-1].split(sep="2019")[0],1:"Count_unique",2:"Count"})
        rel_count_df = pd.concat([rel_count_df, Dr],axis=1)

        # Row Count by GUID per test
        guid_this_test = relevent_rows[guid_label].value_counts()
        guid_test_count_df = pd.concat([guid_test_count_df, guid_this_test], axis=1, sort=True)
        

    writer = pd.ExcelWriter(new_data_path+'CARE_assessment_preprocessing.xlsx', engine='xlsxwriter')

    guid_match_df['CARE Assessment File Name'] = file_name_col
    guid_match_df['Unique GUID Matches'] = counter_list
    guid_match_df['Case Matches'] = case_count
    guid_match_df['Control Matches'] = control_count

    # *********************************************************************************
    # *********************************************************************************
    # * Moving Column names to get desired output! If more files are added, this will *
    # ********* need to be changed, otherwise you risk undesired formatting ***********
    # *********************************************************************************
    # *********************************************************************************
    guid_test_count_df = guid_test_count_df.rename(columns={0 : 'Case or Control'})
    col_list = guid_test_count_df.columns.tolist()
    col_list = [col_list[0]] + col_list[5:2:-1] + col_list[1:3] + col_list[6:]
    guid_test_count_df = guid_test_count_df.ix[:, col_list]
    # *********************************************************************************
    # *********************************************************************************
    # *********************************************************************************

    guid_match_df.to_excel(writer, sheet_name='GUID Matches',index=False)
    rel_count_df.to_excel(writer, sheet_name='CAREassesscounts matching GUIDs', index=False)
    guid_test_count_df.to_excel(writer, sheet_name='GUID count per test', index=True)
    full_count_df.to_excel(writer, sheet_name='Full counts wo blank attr', index=False)
    writer.save()

    return 0

if __name__ == "__main__":
    main()