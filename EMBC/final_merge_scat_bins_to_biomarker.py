import pandas as pd
from glob import glob

inputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Final Data\\"
inputFiles = glob(inputFolder + "*.xlsx")
print(inputFiles)
outputFolder = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\Final Data\\Final data w bins\\"
scatFile = "\\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\SCAT3 Data\\SCAT3 FINAL ALL DATA.xlsx"

def main(): 
    scatdf = pd.read_excel(scatFile)
    scatbins = scatdf[["GUID", "TSS Bin"]]
    scatbins = scatbins.drop_duplicates()
    # writer = pd.ExcelWriter(outputFolder + 'Biomarker w TSS bins.xlsx', engine='xlsxwriter')
    for f in inputFiles:
        xlsx = pd.ExcelFile(f)
        sheets = xlsx.sheet_names
        test_name = f.split(sep="\\")[-1].split(sep="final")[0]
        writer = pd.ExcelWriter(outputFolder + test_name + 'w TSS bins.xlsx', engine='xlsxwriter')
        for sheetname in sheets:
            df = pd.read_excel(f, sheet_name=sheetname, index_col=0)
            newdf = pd.merge(scatbins, df, how="right", on="GUID")
            newdf.to_excel(writer, sheet_name=sheetname, index=False)
        writer.save()


if __name__ == "__main__":
    main()