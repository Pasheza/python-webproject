from sqlalchemy import *


def connect_to_db(user, password, host, port, db):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = create_engine(url, client_encoding='utf8')
    meta = MetaData(bind=con, reflect=True)
    return con, meta


def dropdown_options(con, meta):
    outputs = Table('outputs', meta)
    s = select([outputs.c.index])
    result = con.execute(s)
    options = []
    for row in result:
        options.append({'label': row[0], 'value': row[0]})
    return options


def graph_arguments(meta):
    outputs = Table('outputs', meta)
    args = outputs.columns.keys()
    args.remove('index')
    return args


def graph_values(con, meta, row_index):
    outputs = Table('outputs', meta)
    s = select([outputs]).where(outputs.c.index == row_index)
    result = con.execute(s).fetchone()
    values = list(result)
    values.remove(row_index)
    return values


def first_dropdown_value(con, meta):
    outputs = Table('outputs', meta)
    s = select([outputs.c.index])
    result = con.execute(s).fetchone()
    return result[0]
