import pandas as pd
from glob import glob

def cleanDate(d):
    return d.split("T")[0]

# rawscatdf = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE dataset_2019-08-22T11-40-02\\query_result_SCAT3_2019-08-22T11-36-453273569649714830957.csv")
# print(rawscatdf.columns)
# rawscatdf = rawscatdf[['SCAT3.Main.GUID', 'SCAT3.Main.VisitDate', 'SCAT3.Scoring Summary.Scat3TotalSymptoms', 'SCAT3.Scoring Summary.Scat3TotSympScore']]
# rawscatdf.columns = ["GUID", "Date", "Total Symptoms", "Total Symptom Score"]
# guiddf = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\master_guid_list.csv")
# guid_list = guiddf["GUID"].tolist()
# scatdf = pd.DataFrame()
# inputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Final Data\\"
# inputFiles = glob(inputFolder + "*.xlsx")
# outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\"

# baseline = {}
# for guid in guid_list:
#     scatdf = pd.concat([scatdf, rawscatdf[rawscatdf["GUID"]==guid]], ignore_index=True)
#     baseline[guid] = set()

# scatdf["Date"] = scatdf["Date"].apply(str)
# scatdf["Date"] = scatdf["Date"].apply(cleanDate)
# print(scatdf)
# print(len(scatdf["GUID"].unique()))


# for f in inputFiles:
#     df = pd.read_excel(f, index_col=0)
#     for guid in guid_list:
#         gdf = df[df["GUID"]==guid]
#         bdf = gdf[gdf["Context"]=="Baseline"]
#         for d in bdf["Date"].unique().tolist():
#             baseline[guid].add(d)

# finalscatdflist = []
# for t in scatdf.itertuples(index=False):
#     if t[1] in baseline[t[0]]:
#         finalscatdflist.append(t)
# finalscatdf = pd.DataFrame(finalscatdflist)
# finalscatdf.columns = ["GUID", "Date", "Total Symptoms", "Total Symptom Score"]

# biodf = pd.read_csv("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Raw Data\\Raw Biomarker\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv")
# bdf = biodf[["BiomarkerAssayDataForm.Main.GUID", "BiomarkerAssayDataForm.Main.CaseContrlInd"]]
# bdf.columns = ["GUID", "Group"]
# finalscatdf = pd.merge(finalscatdf, bdf, how="left", on="GUID")
# finalscatdf = finalscatdf.drop_duplicates()
# print(finalscatdf)

finalscatdf = pd.read_excel("\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\SCAT3 Data\\SCAT3 FINAL ALL DATA.xlsx")

xdf = finalscatdf
casedf = xdf[xdf["Group"] == "Case"]
condf = xdf[xdf["Group"] == "Control"]

# ***********************************CASE****************************************
# ***********************************CASE****************************************
b0df = casedf[casedf["Total Symptom Score"] == 0]
b0df["Bin"] = 1
b1df = casedf[casedf["Total Symptom Score"] > 0]
b1df = b1df[b1df["Total Symptom Score"] <= 5]
b1df["Bin"] = 2
b2df = casedf[casedf["Total Symptom Score"] > 5]
b2df = b2df[b2df["Total Symptom Score"] <= 15]
b2df["Bin"] = 3
b3df = casedf[casedf["Total Symptom Score"] > 15]
b3df = b3df[b3df["Total Symptom Score"] <= 50]
b3df["Bin"] = 4
b4df = casedf[casedf["Total Symptom Score"] > 50]
b4df["Bin"] = 5
print([len(b0df),len(b1df),len(b2df),len(b3df),len(b4df)])
print(len(b0df)+len(b1df)+len(b2df)+len(b3df)+len(b4df))
print(len(casedf))
# newcasedf = pd.concat([b0df,b1df,b2df,b3df,b4df], ignore_index=True)
# newcasedf.to_excel(outputFolder + "SCAT3_case_concat_w_bins.xlsx", index=False)

# dflist = [b0df,b1df,b2df,b3df,b4df]
# casedoubledf = pd.DataFrame()
# for guid in casedf["GUID"].unique():
#     count = 0
#     for d in dflist:
#         if guid in d["GUID"].values:
#             count += 1
#             if count > 1:
#                 casedoubledf = casedoubledf.append(casedf[casedf["GUID"] == guid])
# print(len(casedoubledf["GUID"].unique()), "PEOPLE FROM CASE IN 2 BINS")
# casedoubledf.to_excel(outputFolder + "case multiple bins.xlsx", index=False)



# ***********************************CONTROL****************************************
# ***********************************CONTROL****************************************
b0df = condf[condf["Total Symptom Score"] == 0]
b0df["Bin"] = 1
b1df = condf[condf["Total Symptom Score"] > 0]
b1df = b1df[b1df["Total Symptom Score"] <= 5]
b1df["Bin"] = 2
b2df = condf[condf["Total Symptom Score"] > 5]
b2df = b2df[b2df["Total Symptom Score"] <= 15]
b2df["Bin"] = 3
b3df = condf[condf["Total Symptom Score"] > 15]
b3df = b3df[b3df["Total Symptom Score"] <= 50]
b3df["Bin"] = 4
b4df = condf[condf["Total Symptom Score"] > 50]
b4df["Bin"] = 5
print([len(b0df),len(b1df),len(b2df),len(b3df),len(b4df)])
print(len(b0df)+len(b1df)+len(b2df)+len(b3df)+len(b4df))
print(len(condf))
# newcondf = pd.concat([b0df,b1df,b2df,b3df,b4df], ignore_index=True)
# newcondf.to_excel(outputFolder + "SCAT3_control_concat_w_bins.xlsx", index=False)

# dflist = [b0df,b1df,b2df,b3df,b4df]
# condoubledf = pd.DataFrame()
# for guid in condf["GUID"].unique():
#     count = 0
#     for d in dflist:
#         if guid in d["GUID"].values:
#             count += 1
#             if count > 1:
#                 condoubledf = condoubledf.append(condf[condf["GUID"] == guid])
#                 break
# print(len(condoubledf["GUID"].unique()), "PEOPLE FROM CONTROL IN 2 BINS")                
# condoubledf.to_excel(outputFolder + "control multiple bins.xlsx", index=False)

# finalscatbindf = pd.concat([newcasedf, newcondf], ignore_index=True)
# finalscatbindf.to_excel(outputFolder + "SCAT3_final_w_bins.xlsx", index=False)