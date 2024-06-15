import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc

df_dxy = pd.read_csv('dxy_daily_2023_marketwatch.csv')
df_gold = pd.read_csv('gold_daily_2023_metaquotesdemo.csv')
df_eur = pd.read_csv('eurusd_daily_2023_metaquotesdemo.csv')

# armazenar 'data e fechamento diário' num dataframe independente
df_dxy_close = df_dxy[['date', 'close']].copy()
df_gold_close = df_gold[['date', 'close']].copy()
df_eur_close = df_eur[['date', 'close']].copy()

# converter valores na coluna data em tipo datetime de ambos dataframes
df_gold_close['date'] = pd.to_datetime(df_gold_close['date'])
df_dxy_close['date'] = pd.to_datetime(df_dxy_close['date'])
df_eur_close['date'] = pd.to_datetime(df_eur_close['date'])

# ordenar valores no dataframe do índice do dólar
df_dxy_close = df_dxy_close.sort_values(by='date')

# juntar dataframes em um só
dxy_gold = df_dxy_close.merge(df_gold_close, on='date')
dxy_gold_eur = dxy_gold.merge(df_eur_close, on='date')

# cria e personaliza os gráficos
fig_dxy = px.line(df_dxy_close, x="date", y="close")
fig_gold = px.line(df_gold_close, x="date", y="close")
fig_junto = go.Figure()
fig_junto.add_trace(go.Scatter(x=df_dxy_close['date'], y=df_dxy_close['close'], mode='lines', name='Índice do Dólar', yaxis='y1'))
fig_junto.add_trace(go.Scatter(x=df_gold_close['date'], y=df_gold_close['close'], mode='lines', name='Histórico XAUUSD', yaxis='y2'))
fig_junto.update_layout(
    xaxis_title='Data',
    yaxis=dict(title='ÍNDICE DO DÓLAR', titlefont=dict(color='#1f77b4'), tickfont=dict(color='#1f77b4')),
    yaxis2=dict(title='HISTÓRICO XAUUSD', titlefont=dict(color='#ff7f0e'), tickfont=dict(color='#ff7f0e')),
    legend=dict(x=0.5, y=0.5)
)
# configura app dash
app = Dash(__name__)
app.layout = html.Div([ # componente principal
    html.H1(children='INSIGHT DE TENDÊNCIA', style={'text-align': 'center'}),
    
    html.Div([ # componente dxy
        html.H1(children='ÍNDICE DO DÓLAR', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_dxy)],
        style={'width':'50%', 'display':'inline-block'}),

    html.Div([ # componente gold
        html.H1(children='HISTÓRICO XAUUSD', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_gold)],
        style={'width':'50%','display':'inline-block'}),
    
    html.Div([ # componente gold
        html.H1(children='INFERÊNCIA', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_junto)],
        style={'width':'100%','display':'block'})
])
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)