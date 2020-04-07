import pandas as pd 
from glob import glob 

inputFolders = "\\\EGR-1L11QD2\\CLS_lab\\TBI data\\CARE data\\EMBC Paper\\working files\\"
inputFiles = glob(inputFolders + "*.xlsx")

BANNED_GUID = ['TBITC277FAU', 'TBIEB367ABR', 'TBIZU352RXE', 'TBIJP385UKW', 'TBIHK689VAG', 'TBICC177VED', 
                'TBIDA795WGK', 'TBICY850PF3', 'TBIYN163BNR', 'TBIGR129UEK', 'TBIUV221NTZ', 'TBIKD367GBC', 
                'TBIRH053MLX', 'TBIPD089DZ4', 'TBIZK127XMX', 'TBIJY283VKB']

def cleanDate(d):
    return d.split("T")[0]

for f in inputFiles:
    df = pd.read_excel(f)
    for guid in BANNED_GUID:
        df = df[df[df.columns[0]] != guid]
    df["_1"] = df["_1"].apply(str)
    df["_1"] = df["_1"].apply(cleanDate)
    df.to_excel(inputFolders + f.split(sep="\\")[-1].split(sep="final")[0] + "final_data.xlsx")