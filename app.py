import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import sqlhelper
import yaml

with open("dbdata.yaml", 'r') as stream:
    db_data = yaml.load(stream)

con, meta = sqlhelper.connect_to_db(db_data.get('user'), db_data.get('password'), db_data.get('host'),
                                    db_data.get('port'), db_data.get('db'))

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.layout = html.Div(children=[
    html.H1(children='Test project'),

    html.H3(children='''
        A web application for displaying data from DB table Outputs.
    '''),
    html.Label('Choose index to display'),
    dcc.Dropdown(
        id='dropdown',
        options=sqlhelper.dropdown_options(con, meta),
        placeholder='Select index',
        value=sqlhelper.first_dropdown_value(con, meta)
    ),

    dcc.Graph(id='graph')
])


@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def update_graph(selected_dropdown_value):
    return go.Figure(
            data=[
                go.Scatter(
                    x=sqlhelper.graph_arguments(meta),
                    y=sqlhelper.graph_values(con, meta, selected_dropdown_value),
                    mode='lines+markers',
                    name='Graph'
                )
            ],
            layout={
                'title': 'Values of chosen index - {}'.format(selected_dropdown_value),
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Value'}
            }
        )


if __name__ == '__main__':
    app.run_server(debug=True)
