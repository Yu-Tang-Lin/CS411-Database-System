import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State

#from neo4j_u import GraphDatabase
from mongodb import publication_c
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from mysql_utils import  insert_keyword,delete_keyword,faculty_count, keyword_count, publication_count, publication_count_year


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = html.Div([   html.H1(children='Title of Dash App', style={'textAlign':'center'}),
        dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 1"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id='input'),
                                        html.Button('Search', id='search_button'),
                                    ]
                                ),
                                dcc.Graph(
                                    id='pie-chart',
                                    figure={
                                    }
                                )
                            ],
                            className="mt-3",
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 2"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id='input2'),
                                        html.Button('Search', id='search_button2'),
                                    ]
                                ),
                                dcc.Graph(
                                    id='histogram',
                                    figure={
                                    }
                                )
                            ],
                            className="mt-3",
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 3"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id='input3', type='text', placeholder='Enter first string'),
                                        dcc.Input(id='input3-2', type='text', placeholder='Enter second string'),
                                        html.Div(id='output'),
                                        dbc.Button("Submit", id="widget-3-button", color="primary"),


                                        # faculty_count

                                        #keyword_id = 159691111,
                                       # keyword = 'meow',
                                        #html.H1(insert_keyword(159691111,'meow')),

                                        #xdcc.Textarea(id='tid3'),


                                    ]
                                ),
                            ],
                            className="mt-3",
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 4"),
                                dbc.CardBody(
                                    [

                                        dcc.Input(id='input4', type='text', placeholder='Enter second string'),
                                        html.Div(id='output2'),
                                        dbc.Button("Submit", id="widget-4-button", color="primary"),

                                    ]
                                ),
                            ],
                            className="mt-3",
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 5"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id="widget-5-input", type="text", value="Widget 5"),
                                        html.Br(),
                                        dbc.Button("Submit", id="widget-5-button", color="primary"),
                                    ]
                                ),
                            ],
                            className="mt-3",
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 6"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id="widget-6-input", type="text", value="Widget 6"),
                                        html.Br(),
                                        dbc.Button("Submit", id="widget-6-button", color="primary"),

                                    ]
                                ),
                            ],
                            className="mt-3",
                        ),
                    ],
                    width=4,
                ),
            ]
        )
    ],
    fluid=True,
) ])
## wignet1
@callback(
    Output('pie-chart', 'figure'),
    State('input', 'value'),
    Input('search_button', 'n_clicks'),

)

def update_table(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    result = faculty_count(input_value)
    count1_list = []
    name_list = []
    for d in result:
        count1_list.append(d['count1'])
        name_list.append(d['name'])

    return {
        'data': [{'labels': name_list,
                  'values': count1_list,
                  'type': 'pie'}],
        'layout': {'title': 'Pie Chart'}
    }



## wignet2
@callback(
    Output('histogram', 'figure'),
    State('input', 'value'),
    Input('search_button2', 'n_clicks'),

)
def update_table2(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    result = publication_count(input_value)
    print(result)
    df = pd.DataFrame(result)
    return {
        'data': [
            go.Bar(x=df['name'], y=df['count3'])
        ],
        'layout': go.Layout(
            title='Publication Count',
            xaxis={'title': 'University'},
            yaxis={'title': 'Publication Count'}
        )
    }


#widget3

@callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input3', 'value'),
     dash.dependencies.Input('input3-2', 'value')])
def update_output(str1, str2):
        result = insert_keyword(str1,str2)
        return f"insert keyword to database: {str2},{result}"


#widget4

@callback(
    dash.dependencies.Output('output2', 'children'),
    [dash.dependencies.Input('input4', 'value')])

def update_output(str3):
        result = delete_keyword(str3)
        return f"delete keyword to database: {str3},{result}"

if __name__ == "__main__":
    app.run_server(debug=True)
