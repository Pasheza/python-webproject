import helper
from sqlalchemy import *

# TODO Add parameters from arg line
# TODO How to save db info and make sqlhelper?
con, meta = helper.connect_to_db('testuser', 'testuser', 'test_db')
df_inputs = helper.read_excel_sheet('test.xlsx', 'Inputs')
df_outputs = helper.read_excel_sheet('test.xlsx', 'Outputs')
df_inputs.to_sql('inputs', con=con, if_exists='replace')
df_outputs.to_sql('outputs', con=con, if_exists='replace')


def dropdown_options():
    outputs = Table('outputs', meta)
    s = select([outputs.c.index])
    result = con.execute(s)
    options = []
    for row in result:
        options.append({'label': row[0], 'value': row[0]})
    return options


def graph_arguments():
    outputs = Table('outputs', meta)
    args = outputs.columns.keys()
    args.remove('index')
    return args


def graph_values(row_index):
    outputs = Table('outputs', meta)
    s = select([outputs]).where(outputs.c.index == row_index)
    result = con.execute(s).fetchone()
    values = list(result)
    values.remove(row_index)
    return values


def first_dropdown_value():
    outputs = Table('outputs', meta)
    s = select([outputs.c.index])
    result = con.execute(s).fetchone()
    return result[0]