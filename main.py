import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State
from neo4j_utils import keyword_count
from mongodb_utils import publication_count_by_year
import plotly.graph_objs as go
from mysql_utils import faculty_count, publication_count,insert_keyword,delete_keyword
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = html.Div([   html.H1(children='University of California dashboard', style={'textAlign':'center'}),
        dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 1: MYSQL"),
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
                                dbc.CardHeader("Widget 2: MYSQL"),
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
                                dbc.CardHeader("Widget 3: MYSQL"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id='input3', type='text', placeholder='Enter keyword id'),
                                        dcc.Input(id='input3-2', type='text', placeholder='Enter keyword name'),
                                        html.Button('Submit', id='widget3-submit-button', n_clicks=0),

                                        html.Div(id='output'),


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
                                dbc.CardHeader("Widget 4: MYSQL"),
                                dbc.CardBody(
                                    [

                                        dcc.Input(id='input4', type='text', placeholder='Enter keyword name'),
                                        html.Button('Submit', id='widget4-submit-button', n_clicks=0),
                                        html.Div(id='output2'),

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
                                dbc.CardHeader("Widget 5: MongoDB"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id='input5'),
                                        html.Button('Search', id='search_button5'),
                                    ]
                                ),
                                dcc.Graph(
                                    id='histogram5',
                                    figure={
                                    }
                                )
                            ],
                            className="mt-3",
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Widget 6: Neo4j"),
                                dbc.CardBody(
                                    [
                                        dcc.Input(id='input6'),
                                        html.Button('Search', id='search_button6'),
                                    ]
                                ),
                                dcc.Graph(
                                    id='histogram6',
                                    figure={
                                    }
                                )
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
        'layout': {'title': 'How many faculty in University of California for each campus?'}
    }



## wignet2
@callback(
    Output('histogram', 'figure'),
    State('input2', 'value'),
    Input('search_button2', 'n_clicks'),
)
def update_table(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    result = publication_count(input_value)
    df = pd.DataFrame(result)
    return {
        'data': [
            go.Bar(x=df['name'], y=df['count3'])
        ],
        'layout': go.Layout(
            title='How many publications in University of California for each campus?',
            xaxis={'title': 'University'},
            yaxis={'title': 'Publication Count'}
        )
    }


#widget3

@callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('widget3-submit-button', 'n_clicks')],
    [dash.dependencies.Input('input3', 'value'),
     dash.dependencies.Input('input3-2', 'value')])
def update_output(n_clicks,str1, str2):
    if n_clicks > 0 and str1 is not None and str2 is not None:
        result = insert_keyword(str1,str2)
        return html.Div([
            html.P(f"insert keyword to database: {str2}"),
            html.P(f"keyword amount: {result[0]['keyword_inserted_amount']}")
        ])
        return f"insert keyword to database: {str2},{result}"


#widget4

@callback(
    dash.dependencies.Output('output2', 'children'),
    [dash.dependencies.Input('widget4-submit-button', 'n_clicks')],
    [dash.dependencies.Input('input4', 'value')])

def update_output4(n_clicks,str3):
    if n_clicks > 0 and str3 is not None:
        result = delete_keyword(str3)
        return html.Div([
            html.P(f"delete keyword to database: {str3}"),
            html.P(f"keyword amount: {result[0]['keyword_deleted_amount']}")
        ])
        return f"delete keyword to database: {str3},{result}"




## wignet5
@callback(
    Output('histogram5', 'figure'),
    State('input5', 'value'),
    Input('search_button5', 'n_clicks'),
)

def update_table5(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    result = publication_count_by_year(input_value)
    df = result
    num_rows = len(df)
    return {
        'data': [
            go.Treemap(
                labels=df["_id"],
                parents=[""] * num_rows,  # since there are no subcategories for this treemap, all parents will be blank
                values=df["pub_cnt"],
            )
        ],
        'layout': go.Layout(
            title='How many publications in University of California for each campus in recent three years?',
            xaxis={'title': 'University'},
            yaxis={'title': 'Publication Count'}
        )
    }






## wignet6
@callback(
    Output('histogram6', 'figure'),
    State('input6', 'value'),
    Input('search_button6', 'n_clicks'),

)


def update_table6(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    result = keyword_count(input_value)
    df = pd.DataFrame(result)
    return {
        'data': [
            go.Bar(x=df['name'], y=df['keyword_count'])
        ],
        'layout': go.Layout(
            title="How much research diversity is there in the University of California schools?",
            xaxis={'title': 'University'},
            yaxis={'title': 'Keyword Count'}
        )
    }









if __name__ == "__main__":
    app.run_server(debug=True)
