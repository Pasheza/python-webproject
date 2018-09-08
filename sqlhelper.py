from sqlalchemy import *
from model import Output


def connect_to_db(user, password, host, port, db):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = create_engine(url, client_encoding='utf8')
    meta = MetaData(bind=con, reflect=True)
    return con, meta


def dropdown_options(session):
    options = []
    for row in session.query(Output.index).order_by(Output.index).distinct():
        options.append({'label': row[0], 'value': row[0]})
    return options


def graph_arguments(session):
    args = []
    for row in session.query(Output.year).order_by(Output.year).distinct():
        args.append(row[0])
    return args


def graph_values(session, row_index):
    values = []
    for row in session.query(Output.value).filter(Output.index == row_index).order_by(Output.year):
        values.append(row[0])
    return values


def first_dropdown_value(session):
    return session.query(Output.index).order_by(Output.index).distinct().first()[0]
