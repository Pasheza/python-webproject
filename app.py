# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from helpers import helper

df = helper.read_file('test.xlsx')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Test project, load from xlsx'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Dropdown(
        id='dropdown',
        options=helper.generate_dropdown_options(df),
        placeholder='Select index'
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'scatter', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'scatter', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)