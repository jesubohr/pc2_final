import psycopg2
import pandas.io.sql as sqlio
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

cnx = psycopg2.connect("postgresql://postgres:postgres@db")  
cursor = cnx.cursor()
query1 = sqlio.read_sql_query('SELECT SUM(watchtime) AS watch_time, language FROM twitch GROUP BY language ORDER BY watch_time DESC LIMIT 10',cnx)
query2 = sqlio.read_sql_query('SELECT channel as Channel,averageviewers FROM twitch ORDER BY averageviewers DESC LIMIT 20',cnx)
query3 = sqlio.read_sql_query('SELECT peakviewers as peak,averageviewers as avg,channel FROM twitch LIMIT 5',cnx)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

page = dash.Dash(__name__, external_stylesheets=external_stylesheets)

graph1 = px.pie(query1, values='watch_time', names='language', title='Most common Languages ordered by Watch Time')
graph2 = px.bar(query2, x='channel', y='averageviewers', title='Average Viewers by Channel')

graph3 = go.Figure(data=[
    go.Bar(name='Peak Viewers', x=query3.channel, y=query3.peak),
    go.Bar(name='Average Viewers', x=query3.channel, y=query3.avg)
])
graph3.update_layout(barmode='group', title='Peak vs Average Viewers by Channel')

page.layout = html.Div(children=[
    html.H1(children='PC2 FINAL'),

    dcc.Graph(
        id='Graph1',
        figure=graph1
    ),

    dcc.Graph(
        id='Graph2',
        figure=graph2
    ),

    dcc.Graph(
        id='Graph3',
        figure=graph3
    )
])

if __name__ == '__main__':
    page.run_server(host='0.0.0.0', debug=True, port=8050)