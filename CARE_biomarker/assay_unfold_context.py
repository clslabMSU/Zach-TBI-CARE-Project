'''
@author: Zack Roy

10/31/2019 SPOOKY

Unfolding Baseline Dates for BiomarkerAssay
'''

import pandas as pd

bio_assay_path = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
data_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_assessment_files_relevent_guids_only\\Dropped CaseControl Doubles\\"
result_file = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\Biomarker Assay Processing\\"
BANNED_GUID = ["TBICC177VED", "TBIDA795WGK", "TBIEB367ABR", "TBIGR129UEK", "TBIHK689VAG", "TBIJP385UKW", "TBIJY283VKB",
                "TBIKD367GBC", "TBIPD089DZ4", "TBIRH053MLX", "TBITC277FAU", "TBIUV221NTZ", "TBIYN163BNR", "TBIZK127XMX"]

df = pd.read_csv(bio_assay_path)
df= df[["BiomarkerAssayDataForm.Main.GUID", "BiomarkerAssayDataForm.Main.VisitDate", 
        # "BiomarkerAssayDataForm.Main.DaysSinceBaseline", "BiomarkerAssayDataForm.Main.CaseContrlInd", 
        # "BiomarkerAssayDataForm.Form Administration.ContextType", 
        "BiomarkerAssayDataForm.Form Administration.ContextTypeOTH"]]
df = df.rename(columns={"BiomarkerAssayDataForm.Main.GUID": "GUID",
                "BiomarkerAssayDataForm.Main.VisitDate": "VisitDate",
                # "BiomarkerAssayDataForm.Main.DaysSinceBaseline": "DaysSinceBaseline",
                # "BiomarkerAssayDataForm.Main.CaseContrlInd": "CCID",
                # "BiomarkerAssayDataForm.Form Administration.ContextType": "Context",
                "BiomarkerAssayDataForm.Form Administration.ContextTypeOTH": "ContextOTH"})


df1 = pd.DataFrame()
for guid in df["GUID"].unique():
    if guid not in BANNED_GUID:
        df1 = df1.append(df[df["GUID"]==guid])

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

df1["VisitDate"] = df1["VisitDate"].apply(str)
df1["VisitDate"] = df1["VisitDate"].apply(cleanDate)
df1["ContextOTH"] = df1["ContextOTH"].apply(fixContext)

context_list = ['Baseline','6 Hours Post Injury','24 Hours Post Injury','When Asymptomatic','7 Days Post Return to Play']
guid_list = df1["GUID"].unique()
# ********************************************************************
# Creating list of column names, which must be different for each run
# ********************************************************************
cols = ["GUID"]
for n in range(0, 5):
    for i in range(1, len(df1.columns)):
        cols.append(df1.columns[i]+'{}'.format(n+1))

result_df_list = []
for guid in guid_list:
    result_list = [guid]
    result_list_2 = [guid]
    result_list_3 = [guid]
    tdf = df1[df1["GUID"] == guid]
    write_2=False
    write_3=False
    
    for context in context_list:
        tdf1 = tdf[tdf["ContextOTH"]==context]

        if len(tdf1.index)==0:
            for i in range(1, 6):
                result_list.append(None)
                result_list_2.append(None)
                result_list_3.append(None)
            continue

        if len(tdf1["VisitDate"].unique()) > 1:
            counter = 0
            print("********" + guid + "**************")
            print(context)
            unique_dates = sorted(tdf1["VisitDate"].unique())
            for date in unique_dates:
                print(date)
                tdf2 = tdf1[tdf1["VisitDate"]==date]
                if counter == 1:
                    write_2 = True
                    for i in range(1, 6):
                        result_list_2.append(tdf2.iloc[0,i])
                elif counter == 2:
                    write_3 = True
                    for i in range(1, 6):
                        result_list_3.append(tdf2.iloc[0,i])
                else:
                    for i in range(1, 6):
                        result_list.append(tdf2.iloc[0,i])
                counter += 1
            max_len = max(len(result_list), len(result_list_2), len(result_list_3))
            while len(result_list) < max_len:
                result_list.append(None)
            while len(result_list_2) < max_len:
                result_list_2.append(None)
            while len(result_list_3) < max_len:
                result_list_3.append(None)
            continue

        for i in range(1, 6):
            result_list.append(tdf1.iloc[0,i])
            result_list_2.append(None)
            result_list_3.append(None)
    result_df_list.append(result_list)
    if write_2:
        result_df_list.append(result_list_2)
    if write_3:
        result_df_list.append(result_list_3)

result_df = pd.DataFrame(result_df_list,columns=cols)
result_df.to_csv(result_file + "UnfoldedByContext.csv", index=False)




