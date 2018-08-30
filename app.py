import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import helper
import dbsetup

df = helper.read_excel_sheet('test.xlsx', 'Outputs')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Test project, load from xlsx'),

    html.Div(children='''
        A web application for displaying data from xlsx file.
    '''),

    dcc.Dropdown(
        id='dropdown',
        options=dbsetup.dropdown_options(),
        placeholder='Select index',
        value=dbsetup.first_dropdown_value()
    ),

    dcc.Graph(id='graph')
])


@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def update_graph(selected_dropdown_value):
    return go.Figure(
            data=[
                go.Scatter(
                    x=dbsetup.graph_arguments(),
                    y=dbsetup.graph_values(selected_dropdown_value),
                    mode='lines+markers',
                    name='Graph'
                )
            ]
        )


if __name__ == '__main__':
    app.run_server(debug=True)
