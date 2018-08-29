import pandas as pd


def read_file(path):
    df = pd.read_excel(path,sheet_name='Outputs')
    df = pd.DataFrame(df)
    return df


def dropdown_options(df):
    df = pd.DataFrame(df)
    options = []
    for index, item in enumerate(df.axes[0]):
        options.append({'label': item, 'value': index})
    return options


def graph_argument(df):
    df = pd.DataFrame(df)
    return df.axes[1]


def graph_values(origin, row_index):
    df = pd.DataFrame(origin)
    return df.values[row_index]
