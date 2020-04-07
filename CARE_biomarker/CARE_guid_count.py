# -*- coding: utf-8 -*-
"""
Created on Tue Oct 8 11:05 PM

@author: zjr0213

Counting Relevent GUID's from biomarker analysis in all other CARE files.
"""

import pandas as pd
import numpy as np
from os import listdir

biomarkerFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
originalDataFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\"
resultFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\"
file_list = ['_DemogrFITBIR_',
            '_MedHx_FITBIR_',
            '_Concussion_Hx_0000310_2_',
            '_BSSS_',
            '_PostInjForm_',
            '_WTAR_FITBIR_'
            ]

def main():
    df = pd.read_csv(biomarkerFile)
    biomarker_guid_list = set(df['BiomarkerAssayDataForm.Main.GUID'].tolist())
    result_df = pd.DataFrame(columns=["Filename", "Number of GUID matches"])
    DF = pd.DataFrame()
    for filename in listdir(originalDataFolder):
        if filename.endswith(".csv"):
            df1 = pd.read_csv(originalDataFolder + filename)
            guid_label = df1.columns[2]
            file_guid_list = set(df1[guid_label].tolist())
            short_file = filename.split("result")[-1].split("2019")[0]
            guid_matches = len(biomarker_guid_list.intersection(file_guid_list))
            result_df = result_df.append({"Filename" : short_file, "Number of GUID matches" : guid_matches}, ignore_index = True)
        for f in file_list:
            if short_file in f:
                guid_list = []
                df_unique = df1.iloc[:,0].unique()
                btdf_isin = np.isin(df_unique, biomarker_guid_list)
                btdf_len = len(btdf_isin)
                btdf_isin_values = []
                for i in range(0,btdf_len):
                    if btdf_isin[i] == True:
                        btdf_isin_values.append(df_unique[i]) # creating list of unique GUIDs
                        counter += 1
                guid_list.append(btdf_isin_values)

                # Gathering All Biomarker Rows
                relevent_rows = pd.DataFrame()
                for guid in btdf_isin_values:
                    relevent_rows = relevent_rows.append(df1.loc[df1[guid_label] == guid])
                df2 = relevent_rows
                dr=[]
                column=df2.columns.values.tolist()
                for i in column:
                    ar=[i + ":" + str(df2[i].nunique())+ ":"+ str(len(df2[df2[i].notnull()]))]
                    dr=dr+ar
                Dr=pd.DataFrame(dr)
                Dr=Dr[0].str.split(":", n=3,expand = True)
                Dr=Dr.rename(columns={0:short_file, 1:"Count_unique",2:"Count"})
                DF = pd.concat([DF, Dr], axis=1)

    print(DF)
    # writer = pd.ExcelWriter(resultFolder+'GUID Count per test.xlsx', engine='xlsxwriter')
    # result_df.to_excel(writer, sheet_name='GUID Counts per test', index=False)
    # writer.save()


    return 0

if __name__ == "__main__":
    main()