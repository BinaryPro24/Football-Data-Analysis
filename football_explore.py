import pandas as pd

# Load dataset from GitHub — 208,028 matches, 21 columns
# Each row = one match, each column = one attribute (team, score, result etc)
url = "https://raw.githubusercontent.com/jfjelstul/englishfootball/master/data-csv/matches.csv"
df = pd.read_csv(url)


print(df.shape) # Dimensions of the dataset table
print(df.head()) # First 5 rows of the dataset

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- BASIC STATS ---")
print(df.describe())

# New columns for analysis of home and away scores together
# for every single row simultaneously
print("\n--- TOP 10 HIGHEST SCORING GAMES ---")
df['total_goals'] = df['home_team_score'] + df['away_team_score']

# Selects only those 5 columns
# Sorts by total goals highest to lowest
# Shows only the top 10 rows of the sorted table
print(df[['season', 'home_team_name', 'away_team_name', 'score', 'total_goals']]
    .sort_values('total_goals', ascending=False)
    .head(10))

# mean() on a binary column (1s and 0s) returns the proportion of 1s
# multiply by 100 to convert to percentage
print("\n--- WIN RATE BY HOME vs AWAY ---")
print(f"Home wins: {df['home_team_win'].mean()*100:.1f}%")
print(f"Away wins: {df['away_team_win'].mean()*100:.1f}%")
print(f"Draws: {df['draw'].mean()*100:.1f}%")