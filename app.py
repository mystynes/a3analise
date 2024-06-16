import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output

df_dxy = pd.read_csv('dxy_daily_2023_marketwatch.csv')
df_xau = pd.read_csv('xauusd_daily_2023_metaquotesdemo.csv')
df_eur = pd.read_csv('eurusd_daily_2023_metaquotesdemo.csv')
df_gbp = pd.read_csv('gbpusd_daily_2023_metaquotesdemo.csv')
df_aud = pd.read_csv('audusd_daily_2023_metaquotesdemo.csv')

# armazenar 'data e fechamento diário' num dataframe independente
df_dxy_close = df_dxy[['date', 'open', 'close']].copy()
df_xau_close = df_xau[['date', 'open', 'close']].copy()
df_eur_close = df_eur[['date', 'open', 'close']].copy()
df_gbp_close = df_gbp[['date', 'open', 'close']].copy()
df_aud_close = df_aud[['date', 'open', 'close']].copy()

# converter valores na coluna data em tipo datetime de ambos dataframes
df_xau_close['date'] = pd.to_datetime(df_xau_close['date'])
df_dxy_close['date'] = pd.to_datetime(df_dxy_close['date'])
df_eur_close['date'] = pd.to_datetime(df_eur_close['date'])
df_gbp_close['date'] = pd.to_datetime(df_gbp_close['date'])
df_aud_close['date'] = pd.to_datetime(df_aud_close['date'])

# ordenar valores no dataframe do índice do dólar
df_dxy_close = df_dxy_close.sort_values(by='date')

# DEFININDO ALTA VOLATILIDADE -----------------------------------------------------------------
df_xau_close['diferenca'] = df_xau_close['close'].diff()
df_xau_close = df_xau_close.dropna()
media_df_xau = df_xau_close['diferenca'].mean()
desvio_padrao_xau = df_xau_close['diferenca'].std()
limite_volatilidade = media_df_xau + desvio_padrao_xau
alta_volatilidade_xau = df_xau_close[df_xau_close['diferenca'] > limite_volatilidade]


# figura DXY x XAUUSD
fig_xau = go.Figure()
fig_xau.add_trace(go.Scatter(x=df_dxy_close['date'], y=df_dxy_close['close'], mode='lines', name='Índice do Dólar', yaxis='y1'))
fig_xau.add_trace(go.Scatter(x=df_xau_close['date'], y=df_xau_close['close'], mode='lines', name='Histórico XAUUSD', yaxis='y2'))
fig_xau.update_layout(
    xaxis_title='DATA',
    yaxis=dict(
        title='ÍNDICE DO DÓLAR',
        titlefont=dict(color='#1f77b4'),
        tickfont=dict(color='#1f77b4')),
    yaxis2=dict(
        title='HISTÓRICO XAUUSD',
        titlefont=dict(color='#ff7f0e'),
        tickfont=dict(color='#ff7f0e'),
                overlaying='y',
                side='right'
                ),
    legend=dict(x=0.01, y=0.99)
)

# figura DXY x EURUSD
fig_eur = go.Figure()
fig_eur.add_trace(go.Scatter(x=df_dxy_close['date'], y=df_dxy_close['close'], mode='lines', name='Índice do Dólar', yaxis='y1'))
fig_eur.add_trace(go.Scatter(x=df_eur_close['date'], y=df_eur_close['close'], mode='lines', name='Histórico EURUSD', yaxis='y2'))
fig_eur.update_layout(
    xaxis_title='DATA',
    yaxis=dict(
        title='ÍNDICE DO DÓLAR',
        titlefont=dict(color='#1f77b4'),
        tickfont=dict(color='#1f77b4')),
    yaxis2=dict(
        title='HISTÓRICO EURUSD',
        titlefont=dict(color='#ff7f0e'),
        tickfont=dict(color='#ff7f0e'),
                overlaying='y',
                side='right'
                ),
    legend=dict(x=0.01, y=0.99)
)

# figura DXY x GBPUSD
fig_gbp = go.Figure()
fig_gbp.add_trace(go.Scatter(x=df_dxy_close['date'], y=df_dxy_close['close'], mode='lines', name='Índice do Dólar', yaxis='y1'))
fig_gbp.add_trace(go.Scatter(x=df_gbp_close['date'], y=df_gbp_close['close'], mode='lines', name='Histórico GBPUSD', yaxis='y2'))
fig_gbp.update_layout(
    xaxis_title='DATA',
    yaxis=dict(
        title='ÍNDICE DO DÓLAR',
        titlefont=dict(color='#1f77b4'),
        tickfont=dict(color='#1f77b4')),
    yaxis2=dict(
        title='HISTÓRICO GBPUSD',
        titlefont=dict(color='#ff7f0e'),
        tickfont=dict(color='#ff7f0e'),
                overlaying='y',
                side='right'
                ),
    legend=dict(x=0.01, y=0.99)
)

# figura DXY x AUDUSD
fig_aud = go.Figure()
fig_aud.add_trace(go.Scatter(x=df_dxy_close['date'], y=df_dxy_close['close'], mode='lines', name='Índice do Dólar', yaxis='y1'))
fig_aud.add_trace(go.Scatter(x=df_aud_close['date'], y=df_aud_close['close'], mode='lines', name='Histórico AUDUSD', yaxis='y2'))
fig_aud.update_layout(
    xaxis_title='DATA',
    yaxis=dict(
        title='ÍNDICE DO DÓLAR',
        titlefont=dict(color='#1f77b4'),
        tickfont=dict(color='#1f77b4')),
    yaxis2=dict(
        title='HISTÓRICO AUDUSD',
        titlefont=dict(color='#ff7f0e'),
        tickfont=dict(color='#ff7f0e'),
                overlaying='y',
                side='right'
                ),
    legend=dict(x=0.01, y=0.99)
)

# figura ALTA VOLATILIDADE XAUUSD
fig_alta_volat = go.Figure()
fig_alta_volat.add_trace(go.Scatter(x=df_xau_close['date'], y=df_xau_close['close'], mode='lines', name='Histórico de Preços', yaxis='y1'))
fig_alta_volat.add_trace(go.Scatter(x=alta_volatilidade_xau['date'], y=alta_volatilidade_xau['close'], mode='markers', name='Dias Alta Volatilidade', yaxis='y2'))
fig_alta_volat.update_layout(
    xaxis_title='DATA',
    yaxis=dict(
        title='HISTÓRICO DE PREÇOS XAU',
        titlefont=dict(color='#1f77b4'),
        tickfont=dict(color='#1f77b4')),
    yaxis2=dict(
        title='DIAS COM ALTA VOLATILIDADE',
        titlefont=dict(color='#ff7f0e'),
        tickfont=dict(color='#ff7f0e'),
                overlaying='y',
                side='right'
                ),
    legend=dict(x=0.01, y=0.99)
)

app = Dash(__name__)
# layout da aplicação
app.layout = html.Div([
    html.H2(children='RELAÇÃO INVERSA', style={'text-align': 'center'}),
    # gráfico inferência
    html.Div([
        # botão de selecionar relação   
        dcc.Dropdown(['XAU', 'EUR', 'GBP', 'AUD'], value='XAU', id='relacao_dxy',
                     style={'width':'100%','text-align': 'left', 'display': 'inline-block'}),
        dcc.Graph(id='inferencia', figure=fig_xau)],
        style={'display': '100%', 'justify-content': 'center', 'align-items': 'center'}),

    html.H2(children='ALTA VOLATILIDADE XAUUSD', style={'text-align': 'center'}),
    # gráfico inferência
    html.Div([
        dcc.Graph(id='alta volatilidade', figure=fig_alta_volat)],
        style={'display': '100%', 'justify-content': 'center', 'align-items': 'center'})
])

# callbacks da aplicação
@app.callback(
    Output('inferencia', 'figure'),
    Input('relacao_dxy', 'value')
)
def update_output(value):
    if value == 'XAU':
        # figura do xau
        return fig_xau
    elif value == 'EUR':
        # figura do eur
        return fig_eur
    elif value == 'GBP':
        # figura do GBP
        return fig_gbp
    elif value == 'AUD':
        # figura do AUD
        return fig_aud

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)
