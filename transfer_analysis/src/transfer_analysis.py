import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.ticker import FuncFormatter

# Set up directory structure
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the directory of the current script
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')  # Create assets directory path
os.makedirs(ASSETS_DIR, exist_ok=True)  # Create assets directory if it doesn't exist

# Create comprehensive dataset
transfer_data = [
    # Galatasaray
    {"Player": "Mauro Icardi", "Team": "Galatasaray", "Position": "Forward", "Fee (M€)": 10.0, "Goals": 22, "Assists": 8, "Rating": 7.8},
    {"Player": "Dries Mertens", "Team": "Galatasaray", "Position": "Forward", "Fee (M€)": 0, "Goals": 8, "Assists": 9, "Rating": 7.6},
    {"Player": "Lucas Torreira", "Team": "Galatasaray", "Position": "Midfielder", "Fee (M€)": 6.0, "Goals": 0, "Assists": 4, "Rating": 7.3},
    {"Player": "Nicolò Zaniolo", "Team": "Galatasaray", "Position": "Midfielder", "Fee (M€)": 16.4, "Goals": 5, "Assists": 5, "Rating": 7.0},
    {"Player": "Sacha Boey", "Team": "Galatasaray", "Position": "Defender", "Fee (M€)": 1.1, "Goals": 1, "Assists": 4, "Rating": 7.2},
    {"Player": "Victor Nelsson", "Team": "Galatasaray", "Position": "Defender", "Fee (M€)": 7.0, "Goals": 2, "Assists": 1, "Rating": 7.1},
    
    # Fenerbahçe
    {"Player": "Michy Batshuayi", "Team": "Fenerbahçe", "Position": "Forward", "Fee (M€)": 3.5, "Goals": 12, "Assists": 4, "Rating": 7.1},
    {"Player": "João Pedro", "Team": "Fenerbahçe", "Position": "Forward", "Fee (M€)": 3.0, "Goals": 5, "Assists": 3, "Rating": 6.8},
    {"Player": "Joshua King", "Team": "Fenerbahçe", "Position": "Forward", "Fee (M€)": 0.5, "Goals": 8, "Assists": 2, "Rating": 6.9},
    {"Player": "Lincoln Henrique", "Team": "Fenerbahçe", "Position": "Midfielder", "Fee (M€)": 2.2, "Goals": 3, "Assists": 7, "Rating": 7.0},
    {"Player": "Ferdi Kadıoğlu", "Team": "Fenerbahçe", "Position": "Defender", "Fee (M€)": 0, "Goals": 2, "Assists": 6, "Rating": 7.3},
    {"Player": "Attila Szalai", "Team": "Fenerbahçe", "Position": "Defender", "Fee (M€)": 2.0, "Goals": 1, "Assists": 2, "Rating": 7.0},
    
    # Beşiktaş
    {"Player": "Cenk Tosun", "Team": "Beşiktaş", "Position": "Forward", "Fee (M€)": 0, "Goals": 15, "Assists": 3, "Rating": 7.4},
    {"Player": "Nathan Redmond", "Team": "Beşiktaş", "Position": "Midfielder", "Fee (M€)": 0, "Goals": 3, "Assists": 6, "Rating": 6.9},
    {"Player": "Gedson Fernandes", "Team": "Beşiktaş", "Position": "Midfielder", "Fee (M€)": 6.0, "Goals": 2, "Assists": 9, "Rating": 7.2},
    {"Player": "Romain Saïss", "Team": "Beşiktaş", "Position": "Defender", "Fee (M€)": 2.5, "Goals": 4, "Assists": 1, "Rating": 7.1},
    {"Player": "Arthur Masuaku", "Team": "Beşiktaş", "Position": "Defender", "Fee (M€)": 2.0, "Goals": 1, "Assists": 7, "Rating": 7.0},
    {"Player": "Vincent Aboubakar", "Team": "Beşiktaş", "Position": "Forward", "Fee (M€)": 0, "Goals": 12, "Assists": 4, "Rating": 7.3},
    {"Player": "Valentin Rosier", "Team": "Beşiktaş", "Position": "Defender", "Fee (M€)": 0, "Goals": 1, "Assists": 3, "Rating": 7.0},
    
    # Other clubs
    {"Player": "Cherif Ndiaye", "Team": "Karagümrük", "Position": "Forward", "Fee (M€)": 0.8, "Goals": 14, "Assists": 4, "Rating": 7.2},
    {"Player": "M'Baye Niang", "Team": "Adana Demirspor", "Position": "Forward", "Fee (M€)": 3.5, "Goals": 18, "Assists": 5, "Rating": 7.5},
    {"Player": "Younès Belhanda", "Team": "Karagümrük", "Position": "Midfielder", "Fee (M€)": 1.2, "Goals": 6, "Assists": 11, "Rating": 7.4},
    {"Player": "Emre Tezgel", "Team": "Adana Demirspor", "Position": "Forward", "Fee (M€)": 0.2, "Goals": 1, "Assists": 0, "Rating": 6.2},
    {"Player": "Yusuf Sari", "Team": "İstanbul Başakşehir", "Position": "Midfielder", "Fee (M€)": 1.5, "Goals": 7, "Assists": 8, "Rating": 7.1},
    {"Player": "Stefano Okaka", "Team": "İstanbul Başakşehir", "Position": "Forward", "Fee (M€)": 0, "Goals": 10, "Assists": 3, "Rating": 7.0},
    {"Player": "Olimpiu Moruţan", "Team": "Ankaragücü", "Position": "Midfielder", "Fee (M€)": 0.5, "Goals": 9, "Assists": 6, "Rating": 7.3},
    {"Player": "Pedro Henrique", "Team": "Trabzonspor", "Position": "Forward", "Fee (M€)": 4.0, "Goals": 11, "Assists": 4, "Rating": 7.0},
    {"Player": "Maxi Gómez", "Team": "Trabzonspor", "Position": "Forward", "Fee (M€)": 3.0, "Goals": 13, "Assists": 3, "Rating": 7.1},
    {"Player": "Trezeguet", "Team": "Trabzonspor", "Position": "Midfielder", "Fee (M€)": 4.0, "Goals": 9, "Assists": 8, "Rating": 7.4},
    {"Player": "Dimitrios Goutas", "Team": "Sivasspor", "Position": "Defender", "Fee (M€)": 0.5, "Goals": 5, "Assists": 1, "Rating": 7.0},
]

df = pd.DataFrame(transfer_data)

# Calculate additional metrics
df['Contribution'] = df['Goals'] + df['Assists']
df['Value'] = (df['Contribution'] / df['Fee (M€)']).replace(np.inf, 50)
df['Fee Category'] = pd.cut(df['Fee (M€)'], 
                            bins=[-1, 0, 2, 5, 10, 20],
                            labels=['Free', 'Low (≤€2M)', 'Medium (€2-5M)', 'High (€5-10M)', 'Premium (>€10M)'])

# Save raw data to CSV in assets directory
csv_path = os.path.join(ASSETS_DIR, 'super_lig_transfers_2022_2023.csv')
df.to_csv(csv_path, index=False)
print(f"Data saved to: {csv_path}")

# Style settings
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlepad'] = 15
plt.rcParams['figure.figsize'] = (12, 7)
club_colors = {'Galatasaray': '#e82229', 'Fenerbahçe': '#0a5494', 'Beşiktaş': '#000000'}

# Function to save and show figures in assets directory
def save_and_show(name):
    file_path = os.path.join(ASSETS_DIR, name)
    plt.savefig(f'{file_path}.png', dpi=120, bbox_inches='tight')
    print(f"Figure saved: {file_path}.png")
    plt.show()

# 1. Club Expenditure and Performance
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Expenditure
club_spending = df.groupby('Team')['Fee (M€)'].sum().sort_values(ascending=False)
club_spending = club_spending[club_spending > 0]  # Exclude teams with no spending
bars = ax1.bar(club_spending.index, club_spending.values, 
               color=[club_colors.get(t, '#666666') for t in club_spending.index])

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height, 
             f'€{height:.1f}M', ha='center', va='bottom', fontsize=10)

ax1.set_title('Total Transfer Expenditure by Club', fontsize=14)
ax1.set_ylabel('Million Euros', fontsize=10)
ax1.tick_params(axis='x', rotation=45)

# Performance
club_performance = df.groupby('Team')['Contribution'].sum().sort_values(ascending=False)
bars = ax2.bar(club_performance.index, club_performance.values, 
               color=[club_colors.get(t, '#666666') for t in club_performance.index])

for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, height, 
             f'{height}', ha='center', va='bottom', fontsize=10)

ax2.set_title('Total Goal Contributions by Club', fontsize=14)
ax2.set_ylabel('Goals + Assists', fontsize=10)
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
save_and_show('1_club_performance')

# 2. Top 10 Players by Contribution
plt.figure(figsize=(12, 7))
top_players = df.sort_values('Contribution', ascending=False).head(10)

colors = []
for team in top_players['Team']:
    colors.append(club_colors.get(team, '#666666'))

bars = plt.barh(top_players['Player'], top_players['Contribution'], color=colors)

for i, bar in enumerate(bars):
    width = bar.get_width()
    player = top_players.iloc[i]
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
             f'{player["Goals"]}G, {player["Assists"]}A | Rating: {player["Rating"]:.1f}', 
             ha='left', va='center', fontsize=10)

plt.title('Top 10 Players by Goal Contributions', fontsize=16)
plt.xlabel('Goals + Assists', fontsize=12)
plt.grid(axis='x', alpha=0.2)
plt.tight_layout()
save_and_show('2_top_players')

# 3. Transfer Fee vs Performance (with all player names)
plt.figure(figsize=(14, 10))

# Create scatter plot with team colors
scatter = plt.scatter(
    x=df['Fee (M€)'], 
    y=df['Rating'], 
    s=df['Contribution']*15, 
    c=[club_colors.get(t, '#666666') for t in df['Team']],
    alpha=0.85,
    edgecolors='w',
    linewidth=0.5
)

# Add all player names with optimized positioning
for i, row in enumerate(df.itertuples()):
    # Calculate offset to prevent overlapping
    x_offset = 0.3
    y_offset = 0.01 * (i % 3)  # Alternate vertical position
    
    # Special adjustments for crowded areas
    if row.Player in ['Mauro Icardi', 'Nicolò Zaniolo', 'Michy Batshuayi']:
        y_offset = -0.05
    elif row.Player in ['Dries Mertens', 'Vincent Aboubakar']:
        y_offset = 0.05
    elif row.Player in ['Cenk Tosun', 'Gedson Fernandes']:
        y_offset = -0.03
    
    plt.annotate(row.Player, 
                (row[4] + x_offset, row.Rating + y_offset), 
                fontsize=8, 
                alpha=0.9)

plt.title('Transfer Fee vs Player Performance', fontsize=16)
plt.xlabel('Transfer Fee (Million €)', fontsize=12)
plt.ylabel('Performance Rating', fontsize=12)
plt.grid(True, alpha=0.2)
plt.xlim(-1, 20)
plt.ylim(6.0, 8.0)

# Custom legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#e82229', markersize=10, label='Galatasaray'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#0a5494', markersize=10, label='Fenerbahçe'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#000000', markersize=10, label='Beşiktaş'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#666666', markersize=10, label='Other Clubs')
]
plt.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
save_and_show('3_fee_performance')

# 4. Best Value Transfers
plt.figure(figsize=(12, 8))
value_transfers = df[df['Fee (M€)'] > 0].sort_values('Value', ascending=False).head(10)

# Create value for money score
value_transfers['Value Score'] = np.log(value_transfers['Value'] + 1) * 10

plt.scatter(
    x=value_transfers['Fee (M€)'], 
    y=value_transfers['Contribution'], 
    s=value_transfers['Value Score']*20, 
    c=[club_colors.get(t, '#666666') for t in value_transfers['Team']],
    alpha=0.85,
    edgecolors='w',
    linewidth=0.5
)

# Add labels
for i, row in value_transfers.iterrows():
    plt.annotate(f'{row["Player"]}\n€{row["Fee (M€)"]:.1f}M → {row["Contribution"]}',
                (row['Fee (M€)'] + 0.1, row['Contribution'] + 0.2), 
                fontsize=9)

plt.title('Best Value Transfers: Contribution vs Fee', fontsize=16)
plt.xlabel('Transfer Fee (Million €)', fontsize=12)
plt.ylabel('Goals + Assists', fontsize=12)
plt.grid(True, alpha=0.2)

# Add value lines
plt.axline((0, 0), slope=5, color='gray', linestyle='--', alpha=0.3)
plt.axline((0, 0), slope=10, color='gray', linestyle='--', alpha=0.3)
plt.axline((0, 0), slope=20, color='gray', linestyle='--', alpha=0.3)

plt.text(15, 10, "€1M = 5 Contributions", fontsize=9, rotation=35, alpha=0.7)
plt.text(15, 18, "€1M = 10 Contributions", fontsize=9, rotation=35, alpha=0.7)
plt.text(15, 35, "€1M = 20 Contributions", fontsize=9, rotation=35, alpha=0.7)

plt.xlim(0, 18)
plt.ylim(0, 40)

plt.tight_layout()
save_and_show('4_value_transfers')

# 5. Position Analysis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
position_performance = df.groupby('Position').agg(
    Avg_Rating=('Rating', 'mean'),
    Avg_Contribution=('Contribution', 'mean'),
).reset_index()

# Position ratings
sns.barplot(data=position_performance, x='Position', y='Avg_Rating', 
            palette=['#e66100', '#1a5fb4', '#26a269'], ax=ax1)
ax1.set_title('Average Rating by Position', fontsize=14)
ax1.set_ylabel('Rating', fontsize=12)
ax1.set_ylim(6.5, 7.5)

# Add value labels
for p in ax1.patches:
    ax1.annotate(f'{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points')

# Position contributions
sns.barplot(data=position_performance, x='Position', y='Avg_Contribution', 
            palette=['#e66100', '#1a5fb4', '#26a269'], ax=ax2)
ax2.set_title('Average Contribution by Position', fontsize=14)
ax2.set_ylabel('Goals + Assists', fontsize=12)

# Add value labels
for p in ax2.patches:
    ax2.annotate(f'{p.get_height():.1f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points')

plt.tight_layout()
save_and_show('5_position_performance')

print("Analysis complete! All assets saved to: " + ASSETS_DIR)