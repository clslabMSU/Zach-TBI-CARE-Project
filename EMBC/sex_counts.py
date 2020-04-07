import pandas as pd
# import numpy as np
from glob import glob

outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
assessments = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\Biomarker Only Data\\"
biomarkerFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\CARE_blood_biomarkers\\CARE_original_biomarkerassay_file\\query_result_BiomarkerAssayDataForm_2019-08-22T11-35-543865203855005414924.csv"
assessment_files = glob(assessments + "*.csv")

def main():
    # for f in assessment_files:
    #     df = pd.read_csv(f)
    # bdf = pd.read_csv(biomarkerFile)
    # bioguid = bdf["BiomarkerAssayDataForm.Main.GUID"].unique()
    df = pd.read_csv(assessments + "_DemogrFITBIR_.csv")
    guid_label = df.columns[2]
    print(guid_label)
    df = df.drop_duplicates(subset=guid_label)
    male_count = len(df[df["DemogrFITBIR.Subject Demographics.GenderTyp"]=="Male"])
    female_count = len(df[df["DemogrFITBIR.Subject Demographics.GenderTyp"]=="Female"])
    df = df[[guid_label, "DemogrFITBIR.Subject Demographics.GenderTyp"]]
    df.columns = ["GUID", "Sex"]
    df.to_csv(outputFolder + "biomarker_guid_sex.csv", index=False)

        

if __name__ == "__main__":
    main()