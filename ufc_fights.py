import pandas as pd

# Carregar o DataFrame
ufc_fights_df = pd.read_excel(r'caminho\ufc_master(excel).xlsx')

for index in range(0, 58):  # Intervalo de linhas 0 a 57 (lembrando que o índice começa em 0)
    old_date = ufc_fights_df.at[index, 'date']
    parts = old_date.split('-')
    year = parts[0]
    month = parts[1]
    day = parts[2]
    new_date = f"{int(month)}/{int(day)}/{year}"  # Convertendo para formato 'm/d/Y'
    ufc_fights_df.at[index, 'date'] = new_date

# Converter a coluna 'date' para o tipo datetime.
ufc_fights_df['date'] = pd.to_datetime(ufc_fights_df['date'])   
ufc_fights_df.to_excel(r'C:\Users\yamas\OneDrive\Área de Trabalho\PROJETO_UFC_DS\ufc_fights.xlsx')
