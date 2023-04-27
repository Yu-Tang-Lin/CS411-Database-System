#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State

#from neo4j import GraphDatabase

from mysql_utils import get_university, faculty_count, keyword_count, publication_count, publication_count_year


#neo_db = db = GraphDatabase.driver('bolt://127.0.0.1:7687')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Input(id='input'),
    html.Button('Search', id='search_button'),
    #faculty_count
    dash_table.DataTable(
        columns = [{'name': 'University Name', 'id': 'namde'}, {'name': 'Publication_count', 'id': 'count1'},{'name': 'University Name', 'id': 'name'}, {'name': 'faculty_count', 'id': 'count3'}],
        id='faculty_count_table',
        ),
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
@callback(
    Output('publication_count_table', 'data'),
    Output('tid2', 'value'),

    State('input2', 'value'),
    Input('search_button2', 'n_clicks'),

)

def update_table(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    #result = get_university(input_value)
    result = publication_count(input_value)
    result1 = faculty_count(input_value)
    print(result)
    return result, 'search result for :' + input_value

def update_table2(input_value, n_clicks):
    if not input_value:
        return dash.no_update
    #result = get_university(input_value)
    result = faculty_count(input_value)
    print(result)
    return result, 'search2 result for :' + input_value
if __name__ == '__main__':
    app.run_server()





