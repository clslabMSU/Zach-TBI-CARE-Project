'''
@author: Zack Roy

11/5/2019

Gathering all possible Baseline dates from all assessment files
'''

import pandas as pd
import numpy as np
from glob import glob

bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
data_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\Dropped CaseControl Doubles\\"
result_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Baseline Dates\\"
data_files = glob(data_file + "*.csv")

BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX"]

bdf = pd.read_csv(bio_assay_path)
guid_list = bdf["BiomarkerAssayDataForm.Main.GUID"].unique()
GUID_DATES = {}
for guid in guid_list:
    if guid in BANNED_GUID:
        continue
    tdf = bdf[bdf["BiomarkerAssayDataForm.Main.GUID"]==guid]
    tdf1 = tdf[tdf["BiomarkerAssayDataForm.Form Administration.ContextTypeOTH"]=="Baseline"]
    if len(tdf1.index) == 0:
        GUID_DATES[guid] = set()
        continue
    GUID_DATES[guid] = set([("BiomarkerAssay", tdf1.iloc[0,6])])
    for row in tdf1.itertuples():
        GUID_DATES[guid].update([("BiomarkerAssay", row[7])])


for filename in data_files:
    df = pd.read_csv(filename)
    true_file_name = filename.split(sep="\_")[-1].split(sep="_relevent_no")[0]
    for col in df.columns:
        if true_file_name == "BSI18":
            if col.endswith("GeneralNotesTxt"):
                context_label = col
        if col.endswith("ContextTypeOTH"):
            context_label = col
        if col.endswith("VisitDate"):
            visit_label = col
        if col.endswith("GUID"):
            guid_label = col
        # if col.endswith("CaseContrlInd"):
        #     cc_label = col
    df1 = df[df[context_label]=="Baseline"]
    df1 = df1[[guid_label, visit_label, context_label]]
    for guid in df1[guid_label].unique():
        tdf = df1[df1[guid_label]==guid]
        if len(tdf.index) == 0:
            continue
        for row in tdf.itertuples():
            GUID_DATES[guid].update([(true_file_name, row[2])])

result_dict = {}
for k in GUID_DATES.keys():
    print(k)
    result_list = []
    for t in GUID_DATES[k]:
        for i in t:
            result_list.append(i)
    while len(result_list) < 37:
        result_list.append(None)
    result_dict[k] = result_list
result_df = pd.DataFrame(result_dict)
result_df.to_csv(result_file + "countbyguid.csv")
