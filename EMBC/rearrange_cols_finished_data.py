import pandas as pd 
from glob import glob

inputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Final Data\\Final data w bins\\"
inputFiles = glob(inputFolder + "*.xlsx")
outputFolder = inputFolder + "formatted w baseline\\"

new_cols = ["GUID", "Group", "Gender", "TSS Bin", "Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "Unrestricted Return to Play", "7 days Post-Unrestricted Return to Play", "6 months post-injury"]
context_list = ["Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "Unrestricted Return to Play", "7 days Post-Unrestricted Return to Play", "6 months post-injury"]


for f in inputFiles:
    df = pd.read_excel(f)
    new_file_names = [i for i in df.columns[5:-1]]
    guid_list = df["GUID"].values.tolist()
    for test in new_file_names:
        df1 = df[["GUID", "Date", "Group", "Context", "Gender", test]]
        test_rows = []
        for guid in guid_list:
            df2 = df1[df1["GUID"]==guid]
            if str(df2["TSS Bin"].values.tolist()[0]) != 'nan':
                tssbin = df2["TSS Bin"].values.tolist()[0]
            else:
                tssbin = ""
            df2 = df2.sort_values(by="Date")
            cc = df2["Group"].values.tolist()[0]
            gender = df2["Gender"].values.tolist()[0]
            while type(gender) == list:
                gender = gender[0]
            guid_row = [guid, cc, gender, tssbin]



            context_i = 0
            for t in df2.itertuples(index=False):
                if context_i <= context_list.index(t[3]):
                    while context_i < context_list.index(t[3]):
                        context_i += 1
                        guid_row.append("")
                    guid_row.append(t[6])
                    context_i +=1
                else:
                    test_rows.append(guid_row)
                    guid_row = [guid, cc, gender, tssbin]
                    context_i = context_list.index(t[3])
                    s = 0
                    while s < context_i:
                        guid_row.append("")
                        s += 1
                    guid_row.append(t[6])
                    context_i += 1

            test_rows.append(guid_row)
            # print(test_rows)

        test_df = pd.DataFrame(columns=new_cols, data=test_rows)
        print(test_df)
        test_df = test_df.drop_duplicates()
        test_df.to_excel(outputFolder + test + "_no_repeats_w_tss_bin.xlsx", index=False)
        