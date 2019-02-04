import codeacademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())

df['Total Goals'] = df['Home Team Gaols'] + df['Away Team Goals']

print(df.head())

sns.set_style('whitegrid')
sns.set_context('poster', font_size=10)
f, ax = plt.subplots(figsize=(10,25))
ax=sns.barplot(data=df, x=df['year'], y=df['total goals'])
ax.set_title('Year vs. Av Goals')


df_goals = pd.read_csv('goals.csv')
#print(df_goals.head())
f, ax2 = sns.subplots(figsize=(12,7))
ax2 = sns.set_context('notebook', font_scale=1.25)
ax2 = sns.boxplot(data=d_goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Boxplot')

plt.show()

