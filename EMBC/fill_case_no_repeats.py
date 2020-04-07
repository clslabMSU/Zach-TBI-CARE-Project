import pandas as pd
import numpy as np 
from glob import glob
finalAssessFolder = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Final Data\\"
finalAssessFiles = glob(finalAssessFolder + "*.xlsx")
outputFolder = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"

df_list = []
for f in finalAssessFiles:
    df1 = pd.read_excel(f, index_col=0)
    df1["Repeated"] = ""
    real_file_name = f.split(sep="\\")[-1].split(sep="final")[0]

    assess_context_list = ["Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "Unrestricted Return to Play", "7 days Post-Unrestricted Return to Play", "6 months post-injury"]

    assess_guids = df1["GUID"].unique().tolist()
    finaldf = pd.DataFrame()
    repeatdf = pd.DataFrame()
    n = 0
    for guid in assess_guids:
        R= False
        temp_assess_df = df1[df1["GUID"]==guid]
        temp_assess_df["Group"] = temp_assess_df["Group"].values[1]
        temp_assess_df = temp_assess_df.sort_values(by="Date")

        timeline = []
        timelines = []
        i = 0
        write = True
        for t in temp_assess_df.itertuples(index=False):

            if t[3] not in assess_context_list[i:]:
                timelines.append(timeline)
                timeline = [t]
                i = assess_context_list.index(t[3]) + 1
            else:
                timeline.append(t)
                i = assess_context_list.index(t[3]) + 1

        if write == True:
            timelines.append(timeline)
        if len(timelines) > 1:
            print(len(timelines))
            R = True
            print("Repeated for", guid)
            # print(timelines)
            n+=1
            print(n)
        j = 0
        for tl in timelines:
            if R == True:
                if j == 0:
                    testdf = pd.DataFrame(tl)
                    testdf["Repeated"] = "R"
                    finaldf = pd.concat([finaldf, testdf],  ignore_index=True)
                    repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
                    j+=1
                else:
                    testdf = pd.DataFrame(tl)
                    testdf["Repeated"] = "R"
                    repeatdf = pd.concat([repeatdf, testdf], ignore_index=True)
                    j+=1
            else:
                testdf = pd.DataFrame(tl)
                testdf["Repeated"] = ""
                finaldf = pd.concat([finaldf, testdf], ignore_index=True)

    
    repeatdf.to_excel(outputFolder + real_file_name + "repeated_timelines.xlsx")
    finaldf.to_excel(outputFolder + real_file_name + "final_timelines.xlsx")