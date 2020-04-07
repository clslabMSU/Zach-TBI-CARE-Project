import pandas as pd 
from glob import glob

inputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Biomarker Data\\"
f = inputFolder + "Biomarker wo TSS bins.xlsx"
outputFolder = inputFolder

new_cols = ["GUID", "Group", "Gender", "Baseline", "< 6 hours", "24-48 hours", "Asymptomatic", "7 days Post-Unrestricted Return to Play"]
context_list = ["Baseline", "< 6 Hours", "24-48 hours", "Asymptomatic", "7 days post"]


xlsx = pd.ExcelFile(f)
sheets = xlsx.sheet_names
for sheet in sheets:
    if "repeat" in sheet:
        continue
    df = pd.read_excel(f, sheet_name=sheet)
    guid_list = df["GUID"].values.tolist()
    df1 = df[["GUID", "Date", "CC", "Context", "Gender", "Test Result"]]
    test_rows = []

    for guid in guid_list:
        df2 = df1[df1["GUID"]==guid]
        df2 = df2.sort_values(by="Date")
        cc = df2["CC"].values.tolist()[0]
        gender = df2["Gender"].values.tolist()[0]
        while type(gender) == list:
            gender = gender[0]
        guid_row = [guid, cc, gender]

        context_i = 0
        for t in df2.itertuples(index=False):
            if context_i <= context_list.index(t[3]):
                while context_i < context_list.index(t[3]):
                    context_i += 1
                    guid_row.append("")
                guid_row.append(t[5])
                context_i +=1
            else:
                test_rows.append(guid_row)
                guid_row = [guid, cc, gender]
                context_i = context_list.index(t[3])
                s = 0
                while s < context_i:
                    guid_row.append("")
                    s += 1
                guid_row.append(t[5])
                context_i += 1

        test_rows.append(guid_row)
        # print(test_rows)

    test_df = pd.DataFrame(columns=new_cols, data=test_rows)
    print(test_df)
    test_df = test_df.drop_duplicates()
    test_df.to_excel(outputFolder + sheet + " biomarker formatted wo bins.xlsx", index=False)
            