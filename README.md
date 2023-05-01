# Zhanchao-YuTang\
1.Title: Academic world dashboard.\
2.Purpose: The purpose of this app is to see more information about recent publications based on keywords, and the direction of school research. This is for any user including teachers and students who wish to find school research topics and papers based on their interests to better match their academic background.\
3.Demo: Give the link to your video demo. Read the video demo section below to understand what contents are expected in your demo.\
4.Installation: After download dashboard and dash_bootstrap, can run the application using the command py main.py.\
5.Usage: How to use it? \
6.Design: There is a main.py that uses the dashboard library and dash_bootstrap library for view_layout(R9) and other Python files mysql-utils, neo4j-utils and mongodb-utils(R3-R5),use to implement 6 widgets (R6-R8). The three databases files have helper functions for Neo4j, SQL and MongoDB and functions for connecting to local databases. Also some standard library files of pycharm.\
7.Implementation: We used many Python imports libraries such dash, panda, dataframe, html, dcc, plotly.expressas, use dash_bootstrap as the frameworks to generate cards, also import our functions and connections from database files.\
8.Database Techniques: We use techniques such as Indexing, View, Trigger, Stored procedure, and Prepared statements to meet the requirements of R10-R12. We create 6 SQL views that can be queried. We use boostrap to generate 6 widgets. Each widget will accept input, and then generate different types of views including pie-chart, bar, histogram, tree map, and use indexing to calculate the quantity. We created sql query statement and connect statement in database fies, first Prepared statements, so that it can be in main. py can be called directly without worrying about integration issues. The dataframe is used to store the data during the ouput procedure, and the callback equation is used to store the procedure. Finally, we created a submit trigger to better run the query process without problems.\
9.Extra-Credit Capabilities: N/A\
10.Contributions: 1) tasks done for each: Zhanchao: help to implement mysql, neo4j, mongodb functions, connect the datasets through utilties, generate cards and layout using bootstrap components, help to generate the some graphs(histogram, pie-chart,bar) for each widgets, write callback functions for each widgets.\ 2) time spent: each spend around 30-35 hours
