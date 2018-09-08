from model import get_base
import sqlhelper
import yaml

with open("dbdata.yaml", 'r') as stream:
    db_data = yaml.load(stream)
con = sqlhelper.connect_to_db(db_data.get('user'), db_data.get('password'), db_data.get('host'),
                                    db_data.get('port'), db_data.get('db'))
get_base().metadata.create_all(con)
