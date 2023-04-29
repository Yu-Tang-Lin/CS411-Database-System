#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State

#from neo4j_u import GraphDatabase
#from mongodb import publication_c

from mysql_utils import get_university, faculty_count, keyword_count, publication_count, publication_count_year

import pandas as pd
import plotly.express as px

# Import data For first graph

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#neo_db = db = GraphDatabase.driver('bolt://127.0.0.1:7687')

app = Dash(__name__)

import plotly.graph_objs as go


app.layout = html.Div([

    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Input(id='input'),
    html.Button('Search', id='search_button'),
    #faculty_count
    dash_table.DataTable(
        columns =[{'name': 'University Name', 'id': 'name'}, {'name': 'Publication_count', 'id': 'count1'}],
        id='faculty_count_table',
        ),

dcc.Graph(
    figure={
        'data': [
            {'x': ['f', 'a', 'c'], 'y': [1,2,3], 'type': 'bar', 'name': 'SF'},
            {'x': ['f', 'a', 'c'], 'y': [1,2,3], 'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
) ,
 dcc.Graph(
        id='plot',
        style={"max-width": "600px",
               "margin": "auto",
               "display": "inline-block"})
,

    #dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
    #dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),

    dcc.Textarea(id='tid'),

    dcc.Input(id='input2'),
    html.Button('Search', id='search_button2'),
    dash_table.DataTable(
        columns=[{'name': 'University Name', 'id': 'name'}, {'name': 'Publication_count', 'id': 'count3'}],
        id='publication_count_table',
    ),

    dcc.Textarea(id='tid2')

])

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
    #result = faculty_count(input_value)
    result=publication_c
    print(result)
    return result['pub_cnt'], 'search result for :' + input_value

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
@callback(
    Output('plot', 'figure'),
    Input('publication_count_table', 'columns')
)
def update_graph(cols):
    df = pd.DataFrame( columns=[c['University Name'] for c in cols])
    figure_2 = go.Figure(data=[
        go.Bar(x=df[''],
               y=df['Rate'],
               width=0.45,
               text=df['Rate'],
               textposition='inside',
               marker_color='indianred')])
    return figure_2

import json


# Close the driver

if __name__ == '__main__':
    app.run_server()





