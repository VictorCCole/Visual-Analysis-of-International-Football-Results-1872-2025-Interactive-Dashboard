
# 📊 Dashboard de Partidas Internacionais de Futebol

Este projeto apresenta um **dashboard interativo** desenvolvido em **Python com Streamlit** para visualização e análise de partidas internacionais de futebol ao longo da história.

## 🔍 Funcionalidades

- Filtros interativos por:
  - Intervalo de anos
  - Tipo de torneio (ex: Copa do Mundo, amistosos, etc.)
- Mapa interativo com número de partidas por país
- Gráfico de barras com as seleções com mais vitórias
- Atualização dinâmica de acordo com os filtros

## 📁 Dataset Utilizado

O dataset contém registros de todas as partidas internacionais entre seleções nacionais desde 1872. As colunas principais incluem:

- `date`: Data da partida
- `home_team` e `away_team`: Seleções mandante e visitante
- `home_score` e `away_score`: Placar final
- `tournament`: Tipo do torneio
- `country`: País onde a partida ocorreu

Fonte: [International Football Results - Kaggle](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)

## 📌 Tecnologias e Bibliotecas

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – para criar o dashboard web
- [Plotly](https://plotly.com/python/) – para gráficos interativos
- [Pandas](https://pandas.pydata.org/) – para manipulação dos dados

## ▶️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/dashboard-futebol.git
cd dashboard-futebol
```

2. Instale as dependências:
```bash
pip install streamlit pandas plotly
```

3. Coloque o arquivo `results.csv` na mesma pasta do script.

4. Execute o dashboard:
```bash
streamlit run dashboard_futebol.py
```

> Caso `streamlit` não seja reconhecido, use:
```bash
python -m streamlit run dashboard_futebol.py
```


## 📚 Estrutura do Projeto

```
dashboard_futebol/
├── results.csv              # Dataset principal
├── dashboard_futebol.py     # Código do dashboard
└── README.md                # Documentação
```