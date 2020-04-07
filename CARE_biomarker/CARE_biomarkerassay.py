# -*- coding: utf-8 -*-
'''
@author: Zack Roy

9/26/2019

Organizing relevent columns from BiomarkerAssayForm
'''
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

biomarkerAssayFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\CARE_blood_biomarkers\\Biomarker Assay Processing\\BiomarkerAssayForm_cols_preselected.csv"
resultFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
cols = ["GUID", 
        "Age in Years", 
        "Visit Date", 
        "Days Since Baseline", 
        "Case or Control", 
        "Before or After Injury", 
        "Time of test with respect to injury", 
        "HGNC Gene Abbrev", 
        "Lab Result Value (pg/mL)",
        "Lab Result Normality"]

BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX"]

def main():
    data = pd.read_csv(biomarkerAssayFile)
    column=data.columns.values.tolist()
    # rename columns
    i = 0
    for col in column:
        data = data.rename(columns={col:cols[i]})
        i+=1
    
    # Gather Baseline Dates to calculate DaysSinceBaseline for assessments
    df = data[["GUID", "Visit Date", "Days Since Baseline"]]
    df = df.drop_duplicates(subset="GUID")
    baseline_date = []
    for _idx, row in df.iterrows():
        date_str = row[1].split("T")[0]
        date_ints = date_str.split("-")
        visit_date = datetime(year=int(date_ints[0]), month=int(date_ints[1]),day=int(date_ints[2]))
        bl = visit_date - timedelta(days=row[2])
        baseline_date.append(bl)
    df["Baseline Date"] = baseline_date
    baseline_df = df.set_index(df["GUID"])
    for guid in BANNED_GUID:
        df = df[df["GUID"] != guid]
    print(len(df))


    # PRINTS COUNT DATA FOR BIOMARKERASSAY
    # dr=[]
    # column=data.columns.values.tolist()
    # for i in column:
    #     ar=[i + " :" + str(data[i].nunique())+ ":"+ str(len(data[data[i].notnull()]))]
    #     dr=dr+ar
    # Dr=pd.DataFrame(dr)
    # Dr=Dr[0].str.split(":", n=3,expand = True)
    # Dr=Dr.rename(columns={0:"FULL_BiomarkerAssayForm", 1:"Count_unique",2:"Count"})

    # # COUNT DATA FOR ABNORMAL DATA
    # dr=[]
    # column=data.columns.values.tolist()
    # abnormal_data = data.loc[data["Lab Result Normality"] == "Abnormal"]
    # for i in column:
    #     ar=[i + " :" + str(abnormal_data[i].nunique())+ ":"+ str(len(abnormal_data[abnormal_data[i].notnull()]))]
    #     dr=dr+ar
    # ab_Dr=pd.DataFrame(dr)
    # ab_Dr=ab_Dr[0].str.split(":", n=3,expand = True)
    # ab_Dr=ab_Dr.rename(columns={0:"ABNORMAL_BiomarkerAssayForm", 1:"Count_unique",2:"Count"})

    # # COUNT DATA FOR NORMAL DATA
    # dr=[]
    # column=data.columns.values.tolist()
    # normal_data = data.loc[data["Lab Result Normality"] == "Normal"]
    # for i in column:
    #     ar=[i + " :" + str(normal_data[i].nunique())+ ":"+ str(len(normal_data[normal_data[i].notnull()]))]
    #     dr=dr+ar
    # n_Dr=pd.DataFrame(dr)
    # n_Dr=n_Dr[0].str.split(":", n=3,expand = True)
    # n_Dr=n_Dr.rename(columns={0:"NORMAL_BiomarkerAssayForm", 1:"Count_unique",2:"Count"})

    # # COMBINING THE THREE COUNT DATAS
    # full_Dr = pd.concat([Dr, ab_Dr, n_Dr], axis=1)

    # ABNORMAL TEST RESULT STATISTICS
    
    # value_series = abnormal_data["HGNC Gene Abbrev"].value_counts()
    # ab_sum = pd.DataFrame(value_series).rename(columns={"HGNC Gene Abbrev" : "Count of Abnormal Findings for each HGNC test"})

    # ab_high_s = abnormal_data.loc[abnormal_data["Lab Result Value (pg/mL)"] > 6]["HGNC Gene Abbrev"].value_counts()
    # ab_high_df = pd.DataFrame(ab_high_s).rename(columns={"HGNC Gene Abbrev" : "Count of Abnormal ABOVE the High Range"})

    # ab_low_s = abnormal_data.loc[abnormal_data["Lab Result Value (pg/mL)"] < 6]["HGNC Gene Abbrev"].value_counts()
    # ab_low_df = pd.DataFrame(ab_low_s).rename(columns={"HGNC Gene Abbrev" : "Count of Abnormal BELOW the Low Range"})

    # ab_cc = abnormal_data.loc[abnormal_data["Case or Control"] == "Case"]["HGNC Gene Abbrev"].value_counts()
    # ab_cc_case = pd.DataFrame(ab_cc).rename(columns={"HGNC Gene Abbrev" : "Count of Abnormal 'Case'"})

    # ab_cc = abnormal_data.loc[abnormal_data["Case or Control"] == "Control"]["HGNC Gene Abbrev"].value_counts()
    # ab_cc_control = pd.DataFrame(ab_cc).rename(columns={"HGNC Gene Abbrev" : "Count of Abnormal 'Control'"})

    # ab_time_full = pd.DataFrame()
    # time_list = ["Baseline", "When Asymptomatic", "6 Hours Post Injury", "24 Hours Post Injury", "7 Days Post Return to Play"]
    # for val in time_list:
    #     ab_time = abnormal_data.loc[abnormal_data["Time of test with respect to injury"] == val]["HGNC Gene Abbrev"].value_counts()
    #     ab_time_df = pd.DataFrame(ab_time).rename(columns={"HGNC Gene Abbrev" : "Count of Abnormal - {}".format(val)})
    #     ab_time_full = pd.concat([ab_time_full, ab_time_df], axis=1, sort=True)

    # ab_sum = pd.concat([ab_sum, ab_high_df, ab_low_df, ab_cc_case, ab_cc_control, ab_time_full], axis=1, sort=True).fillna(0)

    writer = pd.ExcelWriter(resultFolder+'baseline_dates.xlsx', engine='xlsxwriter')
    baseline_df.to_excel(writer, sheet_name="Days since baseline")
    writer.save()

    # WRITING ALL OUTPUTS TO EXCEL SUMMARY
    # writer = pd.ExcelWriter(resultFolder+'biomarker_preprocessing_no_summary.xlsx', engine='xlsxwriter')
    # full_Dr.to_excel(writer, sheet_name='Normal vs Abnormal Counts', index=False)
    # ab_sum.to_excel(writer, sheet_name="Abnormal Stats")
    # writer.save()


    return 0

if __name__ == "__main__":
    main()