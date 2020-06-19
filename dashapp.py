import datetime
import pandas_datareader.data as web

import dash
import dash_core_components as dcc
import dash_html_components as html

stock = 'TSLA'

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("TSLA", 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

app = dash.Dash()

market = web.DataReader("^GSPC", 'yahoo', start, end)
market.reset_index(inplace=True)
market.set_index('Date', inplace=True)

app.layout = html.Div(children=[
    html.H1(children='Tesla vs Market!'),

    html.Div(children='''
    	Time Series Plot
    '''),


    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
				{'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
				{'x': market.index, 'y':market.Close, 'type':'line', 'name':'Market Index'}
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
	app.run_server(debug=True)
