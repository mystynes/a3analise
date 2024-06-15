import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# Dados de exemplo
data = {
    'Date': pd.date_range(start='2022-01-01', periods=10, freq='D'),
    'Dollar_Index': [95, 96, 97, 96, 95, 94, 93, 92, 91, 90],
    'XAUUSD': [1800, 1790, 1780, 1795, 1805, 1810, 1820, 1830, 1840, 1850]
}

df = pd.DataFrame(data)

app = dash.Dash(__name__)
server = app.server  # Expondo o servidor Flask subjacente para o Gunicorn

app.layout = html.Div(children=[
    html.H1(children='Comparação do Índice do Dólar e XAUUSD'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Dollar_Index'],
                    mode='lines',
                    name='Dollar Index',
                    yaxis='y1'
                ),
                go.Scatter(
                    x=df['Date'],
                    y=df['XAUUSD'],
                    mode='lines',
                    name='XAUUSD',
                    yaxis='y2'
                )
            ],
            'layout': go.Layout(
                title='Comparação do Índice do Dólar e XAUUSD',
                xaxis={'title': 'Data'},
                yaxis={'title': 'Dollar Index', 'titlefont': {'color': '#1f77b4'}, 'tickfont': {'color': '#1f77b4'}},
                yaxis2={'title': 'XAUUSD', 'titlefont': {'color': '#ff7f0e'}, 'tickfont': {'color': '#ff7f0e'}, 'overlaying': 'y', 'side': 'right'},
                legend={'x': 0.1, 'y': 0.9}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
