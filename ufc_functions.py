import plotly.express as px
import numpy as np

# Função para criar o gráfico de barra horizontal dos top 10 lutadores com mais nocautes
def create_ko_fighters_bar(data):
    top_10_ko_fig = px.bar(data.sort_values(by='win_by_KO/TKO', ascending=False).head(10)[::-1],
                           x='win_by_KO/TKO', y='fighter', orientation='h',
                           title='Lutadores da Categoria com Mais Vitórias por KO/TKO')
    
    x_max = int(np.ceil(top_10_ko_fig.data[0].x.max()))  # Arredondar para cima
    x_ticks = np.arange(0, x_max + 1)  # Criar array de números inteiros de 0 até x_max

    top_10_ko_fig.update_layout(title_x=0.5)
    top_10_ko_fig.update_xaxes(title_text='Vitórias por KO/TKO', tickvals=x_ticks)
    top_10_ko_fig.update_yaxes(title_text='Lutador')   
    
    return top_10_ko_fig

# Função para criar o gráfico de barra horizontal dos top 10 lutadores com mais finalizações por submissão
def create_submission_fighters_bar(data):
    top_10_sub_fig = px.bar(data.sort_values(by='win_by_Submission', ascending=False).head(10)[::-1],
                            x='win_by_Submission', y='fighter', orientation='h',
                            title='Lutadores da Categoria com Mais Vitórias por Submissão')
    
    x_max = int(np.ceil(top_10_sub_fig.data[0].x.max()))  # Arredondar para cima
    x_ticks = np.arange(0, x_max + 1)  # Criar array de números inteiros de 0 até x_max
    
    top_10_sub_fig.update_layout(title_x=0.5)
    top_10_sub_fig.update_xaxes(title_text='Vitórias por Submissão', tickvals=x_ticks)
    top_10_sub_fig.update_yaxes(title_text='Lutador')
    
    return top_10_sub_fig

# Função para criar o gráfico de barra horizontal dos top 10 lutadores com a maior sequência de vitórias
def create_longest_win_streak_bar(data):
    top_10_streak_fig = px.bar(data.sort_values(by='longest_win_streak', ascending=False).head(10)[::-1],
                               x='longest_win_streak', y='fighter', orientation='h',
                               title='Lutadores da Categoria com Maior Sequência de Vitórias')
    
    x_max = int(np.ceil(top_10_streak_fig.data[0].x.max()))  # Arredondar para cima
    x_ticks = np.arange(0, x_max + 1)  # Criar array de números inteiros de 0 até x_max
    
    top_10_streak_fig.update_layout(title_x=0.5)
    top_10_streak_fig.update_xaxes(title_text='Maior Sequência de Vitórias', tickvals=x_ticks)
    top_10_streak_fig.update_yaxes(title_text='Lutador')
    
    return top_10_streak_fig

# Função para mostrar a média de idade
def show_average_age(data):
    average_age = data['age'].mean()
    return f"Média de Idade da Categoria: {average_age:.2f}"

# Função para calcular as médias de vitórias por Stance
def calculate_average_wins_per_stance(data):
    # Filtrar o DataFrame para remover stances 'Open Stance' e com média de vitórias zero
    filtered_df = data[(data['Stance'] != 'Open Stance') & (data['wins'] > 0)]

    # Calcular as médias de vitórias por Stance
    stance_counts = filtered_df['Stance'].value_counts()
    stance_wins_total = filtered_df.groupby('Stance')['wins'].sum()
    average_wins_per_stance = stance_wins_total / stance_counts
    
    return average_wins_per_stance

def create_decision_fighters_bar(data):
    top_10_decision_fig = px.bar(
        data.sort_values(by='win_by_Decision', ascending=False).head(10)[::-1],
        x='win_by_Decision', y='fighter', orientation='h',
        title='Lutadores com Mais Vitórias por Decisão'
    )
    
    x_max = int(np.ceil(top_10_decision_fig.data[0].x.max()))  # Arredondar para cima
    x_ticks = np.arange(0, x_max + 1)  # Criar array de números inteiros de 0 até x_max
    
    top_10_decision_fig.update_layout(title_x=0.5)
    top_10_decision_fig.update_xaxes(title_text='Vitórias por Decisão', tickvals=x_ticks)
    top_10_decision_fig.update_yaxes(title_text='Lutador')
    
    return top_10_decision_fig

def create_fighters_by_win_loss_differential_bar(data):
    top_10_win_loss_differential_fig = px.bar(
        data.sort_values(by='win-loss differential', ascending=False).head(10)[::-1],
        x='win-loss differential', y='fighter', orientation='h',
        title='Lutadores Destaques da Categoria'
    )
    
    x_max = int(np.ceil(top_10_win_loss_differential_fig.data[0].x.max()))  # Arredondar para cima
    x_ticks = np.arange(0, x_max + 1)  # Criar array de números inteiros de 0 até x_max
    
    top_10_win_loss_differential_fig.update_layout(title_x=0.5)
    top_10_win_loss_differential_fig.update_xaxes(title_text='Vitórias por Diferencial de Vitórias e Derrotas', tickvals=x_ticks)
    top_10_win_loss_differential_fig.update_yaxes(title_text='Lutador')
    
    return top_10_win_loss_differential_fig
