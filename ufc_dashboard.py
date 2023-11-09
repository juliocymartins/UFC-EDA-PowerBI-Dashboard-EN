import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
from ufc_functions import (create_ko_fighters_bar, create_submission_fighters_bar, create_longest_win_streak_bar, show_average_age, 
                           calculate_average_wins_per_stance, create_decision_fighters_bar, create_fighters_by_win_loss_differential_bar)
from ufc_functions2 import (plot_unique_events_per_year, plot_win_percentage_over_years, plot_age_diff_percentage, plot_reach_diff_percentage, 
                              plot_finish_counts_per_year, criar_grafico_lutas_por_ano_e_genero, plot_top_cities_events)

# Carregar os DataFrames
ufc_fighters_df = pd.read_excel('ufc_fighters.xlsx')
ufc_fighters_all_df = pd.read_excel('ufc_fighters_all.xlsx')
ufc_fights_df = pd.read_excel('ufc_fights.xlsx')

# Extrair categorias únicas de weight_class para criação do dropdown menu
unique_weight_classes = ufc_fighters_df['weight_class'].unique()
weight_class_options = [{'label': weight_class, 'value': weight_class} for weight_class in unique_weight_classes]
weight_class_options.append({'label': 'Overall', 'value': 'Overall'})
weight_class_options.append({'label': 'UFC-Events', 'value': 'UFC-Events'})

sorted_weight_classes = ['UFC-Events']+['Overall']+\
                        ['Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 
                         'Middleweight', 'Light Heavyweight', 'Heavyweight', 'Catch Weight'] + \
                        unique_weight_classes[~np.isin(unique_weight_classes, ['Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 
                                                                              'Middleweight', 'Light Heavyweight', 'Heavyweight', 'Catch Weight'])].tolist()

weight_class_options = [{'label': weight_class, 'value': weight_class} for weight_class in sorted_weight_classes]

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.H1("Dashboard UFC Fighters", style={'textAlign': 'center', 'fontFamily': 'Roboto, sans-serif', 'marginBottom': '5px'}),

    html.Div(id='selected-weight-class-subtitle', style={'textAlign': 'center', 'fontFamily': 'Roboto, sans-serif', 'color': 'grey', 'marginBottom': '5px'}),

    # Menu suspenso para selecionar a categoria
    dcc.Dropdown(
        id='category-dropdown',
        options=weight_class_options,
        value='UFC-Events',
        clearable=False,
        multi=False,
        style={
            'maxHeight': '28px',
            'width': '220px',
            'marginBottom': '20px'
        }
    ),
    
    # Container para o gráfico
    html.Div(id='graph-container')
])

# Callback para atualizar o gráfico com base na seleção do menu suspenso
@app.callback(
    Output('graph-container', 'children'),
    Output('selected-weight-class-subtitle', 'children'),    
    Input('category-dropdown', 'value')
)
def update_graph(selected_category):
    if selected_category == 'Overall':
        subtitle = "Overall"
        average_wins_per_stance = calculate_average_wins_per_stance(ufc_fighters_all_df)
        fig = px.pie(
            names=average_wins_per_stance.index,
            values=average_wins_per_stance.values,
            title='Média Proporcional de Vitórias por Stance'
        )
        fig.update_layout(
                title_x=0.5  # Esta linha centraliza o título
        )
        return [
            (dcc.Markdown(id='show-average-age', children=show_average_age(ufc_fighters_all_df)), # Usar dcc.Markdown para exibir o texto
            html.Div([
                html.Div(dcc.Graph(id='fighter-winloss-differential', figure=create_fighters_by_win_loss_differential_bar(ufc_fighters_all_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='ko-fighters-bar', figure=create_ko_fighters_bar(ufc_fighters_all_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='submission-fighters-bar', figure=create_submission_fighters_bar(ufc_fighters_all_df)), style={'display': 'inline-block', 'width': '32%'})
            ]),
            html.Div([
                html.Div(dcc.Graph(id='decision-fighters-bar', figure=create_decision_fighters_bar(ufc_fighters_all_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='longest-win-streak', figure=create_longest_win_streak_bar(ufc_fighters_all_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='average-wins-per-stance', figure=fig), style={'display': 'inline-block', 'width': '32%'})
            ])
            ),
            subtitle 
        ]
    elif selected_category == 'UFC-Events':
        subtitle = "UFC-Events"
        # Aqui você deve retornar os gráficos desejados para "UFC-Events"
        return [
            (html.Div([
                html.Div(dcc.Graph(id='unique-events-per-year', figure=plot_unique_events_per_year(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='win-percentage-over-years', figure=plot_win_percentage_over_years(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='age-diff-percentage', figure=plot_age_diff_percentage(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'})
            ]),
            html.Div([
                html.Div(dcc.Graph(id='reach-diff-percentage', figure=plot_reach_diff_percentage(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='finish_counts_per_year', figure=plot_finish_counts_per_year(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='lutas_por_ano_e_genero', figure=criar_grafico_lutas_por_ano_e_genero(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'})                
            ]),
            html.Div([
                html.Div(dcc.Graph(id='top_cities_events', figure=plot_top_cities_events(ufc_fights_df)), style={'display': 'inline-block', 'width': '32%'})
            ])
            ),
            subtitle
        ]
    else:
        subtitle = f"Categoria de peso: {selected_category}"
        # Aqui você deve retornar os gráficos para as categorias de peso
        data = ufc_fighters_df[ufc_fighters_df['weight_class'] == selected_category]
        average_wins_per_stance = calculate_average_wins_per_stance(data)
        fig = px.pie(
            names=average_wins_per_stance.index,
            values=average_wins_per_stance.values,
            title='Média Proporcional de Vitórias por Stance',
        )
        fig.update_layout(
            title_x=0.5  # Esta linha centraliza o título
        )
        return [
            (dcc.Markdown(id='show-average-age', children=show_average_age(data)), # Usar dcc.Markdown para exibir o texto
            html.Div([
                html.Div(dcc.Graph(id='fighter-winloss-differential', figure=create_fighters_by_win_loss_differential_bar(data)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='ko-fighters-bar', figure=create_ko_fighters_bar(data)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='submission-fighters-bar', figure=create_submission_fighters_bar(data)), style={'display': 'inline-block', 'width': '32%'})
            ]),
            html.Div([
                html.Div(dcc.Graph(id='decision-fighter-bar', figure=create_decision_fighters_bar(data)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='longest-win-streak', figure=create_longest_win_streak_bar(data)), style={'display': 'inline-block', 'width': '32%'}),
                html.Div(dcc.Graph(id='average-wins-per-stance', figure=fig), style={'display': 'inline-block', 'width': '32%'})
            ])
            ),
            subtitle 
        ]

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)

