import pandas as pd

# Load the dataset into a DataFrame.
ufc_fighters_df = pd.read_excel(r'caminho\ufc_fighters.xlsx')

# List of columns for statistics to be summed
stat_columns = ['wins', 'draws', 'losses', 'age', 'win_by_Submission', 'win_by_KO/TKO', 'Stance',
                'total_title_bouts', 'total_rounds_fought', 'longest_win_streak', 'win_by_Decision_Majority',
                'win_by_Decision_Split', 'win_by_Decision_Unanimous', 'win_by_TKO_Doctor_Stoppage',
                'win_by_Decision', 'win-loss differential']

# Group by fighter, combine weight classes and most recent date
grouped = ufc_fighters_df.groupby('fighter', as_index=False).agg({
    'weight_class': '/'.join,
    'date': 'max',
    'age': 'max',  # Keep the highest age
    **{col: 'sum' for col in stat_columns if col not in ['fighter', 'date', 'age', 'Stance', ]}
})

# Rename the columns
# ufc_fighters_all_df = grouped.rename(columns={'win_by_KO/TKO': 'win_by_KO_TKO'})
# print(ufc_fighters_all_df)
