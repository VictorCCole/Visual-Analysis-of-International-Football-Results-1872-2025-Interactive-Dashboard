import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv("results.csv")
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

st.set_page_config(page_title="Dashboard Futebol", layout="wide")

st.title("⚽ Dashboard de Partidas Internacionais de Futebol")

# Filtros
anos = st.slider("Selecione o intervalo de anos", int(df['year'].min()), int(df['year'].max()), (1950, 2020))
tipo_torneio = st.selectbox("Selecione o tipo de torneio", ['Todos'] + sorted(df['tournament'].unique().tolist()))

# Aplicar filtros
df_filtrado = df[(df['year'] >= anos[0]) & (df['year'] <= anos[1])]
if tipo_torneio != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['tournament'] == tipo_torneio]

# Mapa de partidas por país
st.subheader("🗺️ Mapa de Partidas por País")
mapa_df = df_filtrado['country'].value_counts().reset_index()
mapa_df.columns = ['country', 'matches']
fig_mapa = px.choropleth(mapa_df, locations='country', locationmode='country names',
                         color='matches', color_continuous_scale='Viridis',
                         title='Número de Partidas por País')
st.plotly_chart(fig_mapa, use_container_width=True)

# Função para contar vitórias
def contar_vitorias(df):
    vitorias = {}
    for _, row in df.iterrows():
        if row['home_score'] > row['away_score']:
            vitorias[row['home_team']] = vitorias.get(row['home_team'], 0) + 1
        elif row['away_score'] > row['home_score']:
            vitorias[row['away_team']] = vitorias.get(row['away_team'], 0) + 1
    return pd.DataFrame(list(vitorias.items()), columns=['team', 'wins']).sort_values(by='wins', ascending=False)

# Gráfico de vitórias
st.subheader("🏆 Top 10 Seleções com Mais Vitórias")
vitorias_df = contar_vitorias(df_filtrado)
fig_barras = px.bar(vitorias_df.head(10), x='team', y='wins',
                    title="Vitórias por Seleção", text='wins')
fig_barras.update_traces(textposition='outside')
st.plotly_chart(fig_barras, use_container_width=True)
