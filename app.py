# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from helpers import helper
from dash.dependencies import Input, Output

df = helper.read_file('test.xlsx')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Test project, load from xlsx'),

    html.Div(children='''
        A web application for displaying data from xlsx file.
    '''),

    dcc.Dropdown(
        id='dropdown',
        options=helper.dropdown_options(df),
        placeholder='Select index',
        value=0
    ),

    dcc.Graph(id='graph')
])


@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def update_graph(selected_dropdown_value):
    return go.Figure(
            data=[
                go.Scatter(
                    x=helper.graph_argument(df),
                    y=helper.graph_values(df, selected_dropdown_value),
                    mode='lines+markers',
                    name='Graph'
                )
            ]
        )


if __name__ == '__main__':
    app.run_server(debug=True)
