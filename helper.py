import pandas as pd


def read_excel_sheet(path, sheet):
    df = pd.read_excel(path, sheet_name=sheet)
    df = pd.DataFrame(df)
    return df
