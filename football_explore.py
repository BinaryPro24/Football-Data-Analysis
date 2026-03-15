import pandas as pd

url = "https://raw.githubusercontent.com/jfjelstul/englishfootball/master/data-csv/matches.csv"

df = pd.read_csv(url)

print(df.shape)
print(df.head())

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- BASIC STATS ---")
print(df.describe())

print("\n--- TOP 10 HIGHEST SCORING GAMES ---")
df['total_goals'] = df['home_team_score'] + df['away_team_score']
print(df[['season', 'home_team_name', 'away_team_name', 'score', 'total_goals']]
    .sort_values('total_goals', ascending=False)
    .head(10))

print("\n--- WIN RATE BY HOME vs AWAY ---")
print(f"Home wins: {df['home_team_win'].mean()*100:.1f}%")
print(f"Away wins: {df['away_team_win'].mean()*100:.1f}%")
print(f"Draws: {df['draw'].mean()*100:.1f}%")