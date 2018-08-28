import pandas as pd


def read_file(path):
    df = pd.read_excel(path,sheet_name='Outputs')
    df = pd.DataFrame(df)
    return df


def generate_dropdown_options(df):
    df = pd.DataFrame(df)
    options = []
    for index in df.axes[0]:
        options.append({'label': index, 'value': index})
    return options
