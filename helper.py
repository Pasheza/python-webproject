import pandas as pd
from sqlalchemy import *


def connect_to_db(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = create_engine(url, client_encoding='utf8')
    meta = MetaData(bind=con, reflect=True)
    return con, meta


def read_excel_sheet(path, sheet):
    df = pd.read_excel(path, sheet_name=sheet)
    df = pd.DataFrame(df)
    return df


def dropdown_options(df):
    df = pd.DataFrame(df)
    options = []
    for index, item in enumerate(df.axes[0]):
        options.append({'label': item, 'value': index})
    return options


def graph_arguments(df):
    df = pd.DataFrame(df)
    return df.axes[1]


def graph_values(origin, row_index):
    df = pd.DataFrame(origin)
    return df.values[row_index]