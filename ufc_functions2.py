import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# # # Carregar o DataFrame ufc_fights
# ufc_fights_df = pd.read_excel(r'C:\Users\yamas\OneDrive\Área de Trabalho\PROJETO_UFC_DS\ufc_fights.xlsx')
def plot_unique_events_per_year(dataframe):
    dataframe['year'] = dataframe['date'].dt.year
    dataframe['day'] = dataframe['date'].dt.date
    unique_events_per_year = dataframe.groupby('year')['day'].nunique()
    
    # Criar o gráfico de linha usando Plotly Express
    fig = px.line(
        x=unique_events_per_year.index,
        y=unique_events_per_year.values,
        title='Eventos do UFC por Ano',
        labels={'x': 'Ano', 'y': 'Número de Dias com Eventos'},
        markers=True
    )
    # Centralizar o título
    fig.update_layout(title_x=0.5)
    fig.update_xaxes(tickangle=45)

    return fig


def plot_win_percentage_over_years(df):
    # Contar o número de vitórias para Red e Blue
    win_counts = df['Winner'].value_counts()

    # Definir as cores personalizadas
    colors = ['FF6347', '4169E1']  # Red: 'tomato', Blue: 'slateblue'
    # FF6347 e #6A5ACD
    # Criar o gráfico de rosca (donut chart) usando Plotly Graph Objects
    fig = go.Figure(data=[go.Pie(
        labels=win_counts.index,
        values=win_counts.values,
        hole=0.3,  # Define a largura do anel
        marker=dict(colors=colors)  # Especificar as cores aqui
    )])

    # Adicionar o título fora do gráfico
    fig.update_layout(
        title='Quantidade de Vitórias para Red e Blue',
        title_x=0.5  # Centralizar o título
    )

    return fig


# Criar a função de plot de age_diff
def plot_age_diff_percentage(df, interval_start=-17, interval_end=19, interval_step=4):
    df['age_diff_category'] = pd.cut(df['age_dif'], bins=range(interval_start, interval_end + interval_step, interval_step)).astype(str)

    age_diff_percentages = (df.groupby('age_diff_category')['Winner']
                            .value_counts(normalize=True)
                            .unstack()
                            .fillna(0) * 100)

    # Criar o gráfico de barras empilhadas usando Plotly Express
    fig = px.bar(
        age_diff_percentages,
        x=age_diff_percentages.index,
        y=['Red','Blue'],  # Troquei a ordem aqui
        title='Porcentagem de Lutas Ganhas por Diferença de Idade (Blue - Red)',
        labels={'x': 'Diferença de Idade', 'value': 'Porcentagem'},
        color_discrete_map={'Red': '#FF6347', 'Blue': '#4169E1'}  # Troquei a ordem aqui também
    )
    fig.update_layout(title_x=0.5)
    fig.update_layout(barmode='stack')

    return fig


def plot_reach_diff_percentage(df, interval_start=-35, interval_end=35, interval_step=10):
    relevant_reach_dif = df['reach_dif'].nsmallest(4).iloc[-1]
    filtered_df = df[df['reach_dif'] >= relevant_reach_dif]
    # Converta o objeto Interval em uma string
    filtered_df.loc[:, 'reach_diff_category'] = pd.cut(filtered_df['reach_dif'], bins=range(interval_start, interval_end + interval_step, interval_step)).astype(str)

    reach_diff_percentages = (filtered_df.groupby('reach_diff_category')['Winner']
                              .value_counts(normalize=True)
                              .unstack()
                              .fillna(0) * 100)

    fig = px.bar(
        reach_diff_percentages,
        x=reach_diff_percentages.index,
        y=['Red', 'Blue'],
        title='Porcentagem de Lutas Ganhas por Diferença de Alcance (Blue - Red)',
        labels={'x': 'Diferença de Alcance', 'value': 'Porcentagem'},
        color_discrete_map={'Red': '#FF6347', 'Blue': '#4169E1'}
        # color_discrete_map={'Blue': 'blue', 'Red': 'red'}
    )
    fig.update_layout(title_x=0.5)
    fig.update_layout(barmode='stack')
    return fig


def plot_finish_counts_per_year(dataframe):
    # Agrupa os dados por ano e contagem de cada tipo de finalização
    finish_counts = dataframe.groupby([dataframe['date'].dt.year, 'finish']).size().unstack(fill_value=0)

    # Ordena as colunas pelo total de finalizações em ordem decrescente
    finish_counts = finish_counts[finish_counts.sum().sort_values(ascending=False).index]

    # Criar o gráfico de linha usando Plotly Express
    fig = px.line(
        finish_counts,
        x=finish_counts.index,
        y=finish_counts.columns,
        title='Quantidade de Finalizações por Ano',
        labels={'x': 'Ano', 'y': 'Quantidade'}
    )
    fig.update_layout(title_x=0.5)
    fig.update_xaxes(tickangle=45)
    return fig


def criar_grafico_lutas_por_ano_e_genero(ufc_fights_df):
    # Extrair o ano da coluna 'date'
    ufc_fights_df['year'] = ufc_fights_df['date'].dt.year
    # Filtrar por gênero e contar o número de lutas
    gender_counts = ufc_fights_df.groupby(['year', 'gender']).size().reset_index(name='count')
    # Criar o gráfico de barras agrupadas
    fig = px.bar(gender_counts, x='year', y='count', color='gender', barmode='group',
                 labels={'count': 'Número de Lutas', 'year': 'Ano'}, title='Número de Lutas por Ano e Gênero')    
    fig.update_layout(title_x=0.5)
    # Reordenar os rótulos do eixo y
    fig.update_yaxes(categoryorder='total ascending')
    return fig


def plot_top_cities_events(ufc_fights_df):
    # Agrupar por localização (cidade) e contar o número de eventos
    top_cidades = ufc_fights_df['location'].value_counts().nlargest(10)
    # Resetar o índice para transformar em DataFrame
    top_cidades = top_cidades.reset_index()
    # Renomear as colunas
    top_cidades.columns = ['Cidade', 'Número de Eventos']
    # Inverter a ordem do DataFrame para mostrar a cidade com mais eventos no topo
    top_cidades = top_cidades[::-1]

    # Criar o gráfico de barras horizontais
    fig = px.bar(top_cidades, x='Número de Eventos', y='Cidade', orientation='h', labels={'index':'Cidade', 'value':'Número de Eventos'})

    # Adicionar título
    fig.update_layout(title='Top 10 Cidades com Maior Número de Eventos no UFC')
    fig.update_layout(title_x=0.5)

    return fig
