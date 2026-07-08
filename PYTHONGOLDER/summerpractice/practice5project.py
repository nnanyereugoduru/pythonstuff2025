import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\Users\\Durun\\OneDrive\\Documents\\term 1 freshman\\c++ projects\\PYTHONGOLDER\\summerpractice\\fifa_world_cup_2026_player_performance.csv')
#print(df.head())        # first 5 rows
#print(df.shape)         # how many rows and columns
#print(df.columns)       # all column names
#print(df.describe())    # basic stats on every numeric column

players = df.groupby('player_name').agg({
    'total_goals_tournament': 'max',
    'nationality': 'first',
    'position': 'first',
    'club_name' : 'last',
    'market_value_eur' : 'last',
}).reset_index()

# top 20 scorers
top_scorers = players.nlargest(100, 'total_goals_tournament')
top_scorers['label'] = top_scorers['player_name'].str.split().str[-1] + '(' + top_scorers['nationality'].str[:3].str.upper() + ')'
fig, ax1 = plt.subplots(figsize=(25, 10))

ax1.bar(top_scorers['label'], top_scorers['total_goals_tournament'], color='gold', edgecolor='black', label='Goals')
ax1.set_ylabel('Goals', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)
ax1.set_axisbelow(True)

ax2 = ax1.twinx()
ax2.scatter(top_scorers['label'], top_scorers['market_value_eur']/1_000_000, color='blue', marker='o', s=100, label='Market Value', zorder=5)
ax2.set_ylabel('Market Value (Millions EUR)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.title('Top 20 Scorers - Goals vs Market Value', fontsize=16)
ax1.set_xticks(range(len(top_scorers['label'])))
ax1.set_xticklabels(top_scorers['label'], rotation=90, ha='center', fontsize=7)
fig.tight_layout()
plt.subplots_adjust(bottom=0.35)
plt.show()

#trying to find the average valuation relative to the amount of goals scores
count10 = 0
count10val = 0
count5 = 0
count5val = 0
for i, row in top_scorers.iterrows() :

    if row['total_goals_tournament'] >= 10:
        count10 += 1
        count10val += row['market_value_eur']

    if row['total_goals_tournament'] >= 5:
        count5 += 1
        count5val += row['market_value_eur']
if count10 > 0:
    average_val = count10val / count10
    print(f'the players with 10+ goals {count10}')
    print(f'Average market valuation{average_val / 1_000_000: .2f} M')

if count5 > 0:
    average_val5 = count5val / count5
    print(f'the players with 10+ goals {count5}')
    print(f'Average market valuation{average_val5 / 1_000_000: .2f} M')




