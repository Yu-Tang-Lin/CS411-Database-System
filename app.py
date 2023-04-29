import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State

#from neo4j_u import GraphDatabase
#from mongodb import publication_c

from mysql_utils import get_university, faculty_count, keyword_count, publication_count, publication_count_year


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
                                        # faculty_count
                                        dash_table.DataTable(
                                            columns=[{'name': 'University Name', 'id': 'name'},
                                                     {'name': 'faculty_count', 'id': 'count1'}],
                                            id='faculty_count_table',
                                        ),
                                        dcc.Textarea(id='tid'),
                                    ]
                                ),
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
                                        dash_table.DataTable(
                                            columns=[{'name': 'University Name', 'id': 'name'},
                                                     {'name': 'Publication_count', 'id': 'count3'}],
                                            id='publication_count_table',
                                        ),

                                        dcc.Textarea(id='tid2'),
                                        dcc.Input(id="widget-2-input", type="text", value="Widget 2"),
                                        html.Br(),
                                        dbc.Button("Submit", id="widget-2-button", color="primary"),
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
                                dbc.CardHeader("Widget 3"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id="widget-3-input", type="text", value="Widget 3"),
                                        html.Br(),
                                        dbc.Button("Submit", id="widget-3-button", color="primary"),
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
                                        dcc.Input(id="widget-4-input", type="text", value="Widget 4"),
                                        html.Br(),
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
@callback(
    Output('faculty_count_table', 'data'),
    Output('tid', 'value'),

    State('input', 'value'),
    Input('search_button', 'n_clicks'),

)


def update_table(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    #result = get_university(input_value)
    result = faculty_count(input_value)
    print(result)
    return result, 'search result for :' + input_value

@callback(
    Output('publication_count_table', 'data'),
    Output('tid2', 'value'),

    State('input2', 'value'),
    Input('search_button2', 'n_clicks'),

)
def update_table2(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    #result = get_university(input_value)
    result = publication_count(input_value)
    print(result)
    return result, 'search2 result for :' + input_value

if __name__ == "__main__":
    app.run_server(debug=True)
