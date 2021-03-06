import helper
import sqlhelper
import yaml
import sys
from model import Input, Output, get_base
from sqlalchemy.orm import sessionmaker


# Default value of path
excel_path = 'excel_data.xlsx'
try:
    excel_path = sys.argv[1]
except IndexError:
    print('You need to enter path to excel file as parameter')
with open("dbdata.yaml", 'r') as stream:
    db_data = yaml.load(stream)
con = sqlhelper.connect_to_db(db_data.get('user'), db_data.get('password'), db_data.get('host'),
                                    db_data.get('port'), db_data.get('db'))
df_inputs = helper.read_excel_sheet(excel_path, 'Inputs')
df_outputs = helper.read_excel_sheet(excel_path, 'Outputs')

inputs = []
for index, row in df_inputs.iterrows():
    for year in df_inputs.columns:
        input = Input(value=row[year], index=index, year=year)
        inputs.append(input)

outputs = []
for index, row in df_outputs.iterrows():
    for year in df_outputs.columns:
        output = Output(value=row[year], index=index, year=year)
        outputs.append(output)

Session = sessionmaker(bind=con)
session = Session()
try:
    session.query(Input).delete()
    session.query(Output).delete()
    session.commit()
    session.add_all(inputs + outputs)
    session.commit()
except:
    session.rollback()
finally:
    session.close()
