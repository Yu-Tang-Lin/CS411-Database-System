# Zhanchao-YuTang

## Title 
Academic world dashboard.

## Purpose 
The purpose of this app is to provide more information about recent publications based on keywords, and the direction of school research. This is for any user, including teachers and students, who wish to find school research topics and papers based on their interests to better match their academic background.

## Demo
Please refer to the video demo to get a better understanding of the features. [Link to video demo]

## Installation 
After downloading the dashboard and dash_bootstrap, run the application using the command "py main.py".

## Usage 
To use the application, follow these steps:

1. Launch the application 
2. Enter relevant keywords to search for academic papers and publication trends 
3. View different types of views including pie chart, bar, histogram, and tree map 
4. Navigate through the application using the bootstrap components

## Design 
The main.py file uses the Dashboard and Dash Bootstrap libraries for view_layout (R9), and other Python files such as mysql-utils, neo4j-utils, and mongodb-utils (R3-R5) to implement 6 widgets (R6) with updating widgets (R7) and querying widgets (R8). The three databases files have helper functions for Neo4j, SQL, and MongoDB and functions for connecting to local databases. Also, the standard library files of python are used, including Dash, pandas, pymongo, pymysql and neo4j.

## Implementation 
We used various Python imported libraries such as dash, panda, dataframe, html, dcc, and plotly.expressas. We use dash_bootstrap as the framework to generate cards and we import our functions and connections from database files. 

## Database Techniques
Database Techniques: We use techniques such as Indexing, View, Trigger, Stored procedure, and Prepared statements to meet the requirements of (R10-R12). We create 6 SQL views that can be queried. We used boostrap to generate 6 widgets. Each widget will accept input, and then generate different types of views including pie-chart, bar, histogram, tree map, and used indexing to calculate the quantity. We created SQL query statement and connect statement in database files with Prepared statements, so that it can be in main.py can be called directly without worrying about integration issues. The dataframe is used to store the data during the output procedure, and the callback equation is used to store the procedure. Finally, we created a submit trigger to better run the query process without problems.

## Extra-Credit Capabilities 
N/A.

## Contributions 
Zhanchao: helped to implement mysql, neo4j, mongodb functions, connect the datasets through utilties, generate cards and layout using bootstrap components, helped to generate some graphs (histogram, pie-chart, bar) for each widget, write callback functions for each widget.
Yu-Tang: Wrote the query for wignet1, wignet2, wignet5 wignet6, including mysql, neo4j, mongodb database. Design the return and callback function by dataframe to the main.py in order to plot  histogram, pie-chart, bar and tree map. 

Each team member spent around 30-35 hours on the project.
