import helper
import sqlhelper
import yaml
import sys


# Default value of path
excel_path = 'excel_data.xlsx'
try:
    excel_path = sys.argv[1]
except IndexError:
    print('You need to enter path to excel file as parameter')
with open("dbdata.yaml", 'r') as stream:
    db_data = yaml.load(stream)
con, meta = sqlhelper.connect_to_db(db_data.get('user'), db_data.get('password'), db_data.get('host'),
                                    db_data.get('port'), db_data.get('db'))
df_inputs = helper.read_excel_sheet(excel_path, 'Inputs')
df_outputs = helper.read_excel_sheet(excel_path, 'Outputs')
df_inputs.to_sql('inputs', con=con, if_exists='replace')
df_outputs.to_sql('outputs', con=con, if_exists='replace')
