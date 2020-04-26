import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import n_colors
import numpy as np


server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/'
)

df = pd.read_csv('dummy_data.csv')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

data_canada = px.data.gapminder().query("country == 'Canada'")
fig1 = px.bar(data_canada, x='year', y='pop')



np.random.seed(1)

colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
a = np.random.randint(low=0, high=9, size=10)
b = np.random.randint(low=0, high=9, size=10)
c = np.random.randint(low=0, high=9, size=10)

fig2 = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
    line_color='white', fill_color='white',
    align='center',font=dict(color='black', size=12)
  ),
  cells=dict(
    values=[a, b, c],
    line_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
    fill_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
    align='center', font=dict(color='white', size=11)
    ))
])

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig4 = px.line(df, x='Date', y='AAPL.High')

app.layout = html.Div([
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig4)
])
if __name__ == '__main__':
    app.run_server(debug=True)