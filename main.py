import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as mtick
import os

# Create a directory for saving visualizations
os.makedirs('visualizations', exist_ok=True)

# Use a simpler font configuration that should work on any system
plt.rcParams['font.family'] = 'DejaVu Sans'
# If you still get font errors, try uncommenting this line:
# plt.rcParams.update({'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif']})

# Set other plot parameters
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16

# Custom color palette
beer_colors = ['#ffc107', '#ff9800', '#ff5722', '#8d6e63', '#5d4037', '#3e2723', '#212121']
pale_color = '#FFC107'
ipa_color = '#FF5722'
stout_color = '#3E2723'
wild_color = '#8D6E63'

# ===== Manually create DataFrames from the exploration data =====

# Top-Rated Beer Styles
top_styles_data = {
    'beer_style': ['American Wild Ale', 'Gueuze', 'Quadrupel (Quad)', 'Lambic - Unblended', 'American Double / Imperial Stout', 
                 'Russian Imperial Stout', 'Weizenbock', 'American Double / Imperial IPA', 'Flanders Red Ale', 'Eisbock', 
                 'Keller Bier / Zwickel Bier', 'Rye Beer', 'American IPA', 'Belgian IPA', 'Saison / Farmhouse Ale'],
    'review_count': [17794, 6009, 18086, 1114, 50705, 54129, 9412, 85977, 6664, 2663, 2591, 10130, 117586, 12471, 31480],
    'avg_overall': [4.09, 4.09, 4.07, 4.05, 4.03, 4.02, 4.01, 4.00, 3.99, 3.98, 3.98, 3.98, 3.97, 3.96, 3.96],
    'avg_taste': [4.15, 4.13, 4.21, 4.12, 4.19, 4.15, 4.08, 4.09, 4.09, 4.21, 3.84, 4.00, 3.92, 4.01, 3.93],
    'avg_abv': [7.3, 5.5, 10.4, 4.9, 10.5, 9.9, 8.0, 9.3, 6.0, 11.3, 4.9, 6.4, 6.4, 8.2, 6.8]
}
top_styles_df = pd.DataFrame(top_styles_data)

# Beer Ratings by ABV
abv_ratings_data = {
    'abv_category': ['Under 5%', '5-7%', '7-9%', '9-12%', 'Over 12%'],
    'review_count': [204076, 706899, 334359, 243692, 29803],
    'overall_rating': [3.55, 3.81, 3.93, 3.95, 3.87],
    'taste': [3.37, 3.73, 3.99, 4.09, 4.14],
    'aroma': [3.28, 3.66, 3.94, 4.06, 4.13],
    'appearance': [3.49, 3.80, 4.00, 4.07, 4.04],
    'palate': [3.36, 3.69, 3.92, 4.03, 4.06]
}
abv_ratings_df = pd.DataFrame(abv_ratings_data)

# Top Rated Breweries
top_breweries_data = {
    'brewery_name': ['The Alchemist', 'Brouwerij Westvleteren', 'Russian River Brewing Company', 'Live Oak Brewing Company', 
                    'Hill Farmstead Brewery', 'Bayerische Staatsbrauerei Weihenstephan', 'Kern River Brewing Company', 
                    'Brouwerij Drie Fonteinen', 'Brasserie de Rochefort', 'Surly Brewing Company', 'Klosterbrauerei Andechs', 
                    'COAST Brewing Company', 'Minneapolis Town Hall Brewery', 'Selin\'s Grove Brewing Company', 'Maine Beer Company'],
    'review_count': [527, 2378, 11311, 584, 1531, 6269, 929, 1668, 4494, 6271, 557, 980, 2914, 728, 818],
    'unique_beers': [3, 5, 65, 11, 53, 15, 21, 29, 3, 42, 11, 38, 312, 62, 5],
    'avg_rating': [4.58, 4.54, 4.37, 4.31, 4.30, 4.29, 4.29, 4.29, 4.27, 4.26, 4.25, 4.24, 4.24, 4.23, 4.22],
    'avg_abv': [8.3, 8.8, 7.6, 5.6, 7.4, 5.9, 7.2, 6.1, 9.9, 6.7, 6.3, 7.8, 5.8, 5.8, 6.5]
}
top_breweries_df = pd.DataFrame(top_breweries_data)

# Most Reviewed Beers
most_reviewed_data = {
    'beer_name': ['90 Minute IPA', 'Old Rasputin Russian Imperial Stout', 'Sierra Nevada Celebration Ale', 'Two Hearted Ale', 
                 'Arrogant Bastard Ale', 'Stone Ruination IPA', 'Sierra Nevada Pale Ale', 'Stone IPA', 'Pliny The Elder', 
                 'Founders Breakfast Stout', 'Sierra Nevada Bigfoot Barleywine', 'La Fin Du Monde', '60 Minute IPA', 
                 'Storm King Stout', 'Duvel'],
    'brewery': ['Dogfish Head Brewery', 'North Coast Brewing Co.', 'Sierra Nevada Brewing Co.', 'Bell\'s Brewery, Inc.', 
               'Stone Brewing Co.', 'Stone Brewing Co.', 'Sierra Nevada Brewing Co.', 'Stone Brewing Co.', 
               'Russian River Brewing Company', 'Founders Brewing Company', 'Sierra Nevada Brewing Co.', 'Unibroue', 
               'Dogfish Head Brewery', 'Victory Brewing Company', 'Brouwerij Duvel Moortgat NV'],
    'style': ['American Double/Imperial IPA', 'Russian Imperial Stout', 'American IPA', 'American IPA', 'American Strong Ale', 
             'American Double/Imperial IPA', 'American Pale Ale (APA)', 'American IPA', 'American Double/Imperial IPA', 
             'American Double/Imperial Stout', 'American Barleywine', 'Tripel', 'American IPA', 'Russian Imperial Stout', 
             'Belgian Strong Pale Ale'],
    'abv': [9.0, 9.0, 6.8, 7.0, 7.2, 7.7, 5.6, 6.9, 8.0, 8.3, 9.6, 9.0, 6.0, 9.1, 8.5],
    'review_count': [3290, 3111, 3000, 2728, 2704, 2704, 2587, 2575, 2527, 2502, 2492, 2483, 2475, 2452, 2450],
    'avg_rating': [4.15, 4.17, 4.17, 4.33, 4.08, 4.16, 4.25, 4.26, 4.59, 4.35, 3.97, 4.30, 4.17, 4.09, 4.34]
}
most_reviewed_df = pd.DataFrame(most_reviewed_data)

# Beer Style Rating Components
style_components_data = {
    'beer_style': ['Gueuze', 'American Wild Ale', 'Quadrupel (Quad)', 'Lambic - Unblended', 'American Double/Imperial Stout', 
                  'Russian Imperial Stout', 'Weizenbock', 'American Double/Imperial IPA', 'Flanders Red Ale', 'Keller Bier/Zwickel Bier', 
                  'Rye Beer', 'Eisbock', 'American IPA', 'Baltic Porter', 'Saison/Farmhouse Ale'],
    'reviews': [6009, 17794, 18086, 1114, 50705, 54129, 9412, 85977, 6664, 2591, 10130, 2663, 117586, 11572, 31480],
    'overall': [4.09, 4.09, 4.07, 4.05, 4.03, 4.02, 4.01, 4.00, 3.99, 3.98, 3.98, 3.98, 3.97, 3.96, 3.96],
    'taste': [4.13, 4.15, 4.21, 4.12, 4.19, 4.15, 4.08, 4.09, 4.09, 3.84, 4.00, 4.21, 3.92, 4.03, 3.93],
    'aroma': [4.12, 4.13, 4.13, 4.12, 4.16, 4.08, 4.04, 4.10, 4.04, 3.68, 3.89, 4.16, 3.89, 3.95, 3.93],
    'appearance': [4.03, 4.01, 4.12, 3.91, 4.16, 4.21, 4.01, 4.08, 4.00, 3.84, 4.00, 3.96, 3.97, 4.04, 4.00],
    'palate': [4.05, 4.04, 4.12, 3.96, 4.10, 4.09, 3.99, 4.02, 3.97, 3.81, 3.92, 4.11, 3.87, 3.94, 3.90]
}
style_components_df = pd.DataFrame(style_components_data)

# Top 15 Highest-Rated Beers
top_beers_data = {
    'beer_name': ['Citra DIPA', 'Heady Topper', 'Cantillon Blåbær Lambik', 'Deviation - Bottleworks 9th Anniversary', 
                 'Trappist Westvleteren 12', 'Pliny The Younger', 'Founders CBS Imperial Stout', 'Pliny The Elder', 
                 'Live Oak HefeWeizen', 'Portsmouth Kate The Great', 'Rare Bourbon County Stout', 'Duck Duck Gooze', 
                 'Reality Czeck', 'Weihenstephaner Hefeweissbier', 'Zombie Dust'],
    'brewery': ['Kern River Brewing Company', 'The Alchemist', 'Brasserie Cantillon', 'Russian River Brewing Company', 
               'Brouwerij Westvleteren', 'Russian River Brewing Company', 'Founders Brewing Company', 
               'Russian River Brewing Company', 'Live Oak Brewing Company', 'Portsmouth Brewery', 'Goose Island Beer Co.', 
               'The Lost Abbey', 'Moonlight Brewing Company', 'Bayerische Staatsbrauerei Weihenstephan', 'Three Floyds Brewing Co.'],
    'style': ['American Double/Imperial IPA', 'American Double/Imperial IPA', 'Lambic - Fruit', 'American Wild Ale', 
             'Quadrupel (Quad)', 'American Double/Imperial IPA', 'American Double/Imperial Stout', 'American Double/Imperial IPA', 
             'Hefeweizen', 'Russian Imperial Stout', 'American Double/Imperial Stout', 'American Wild Ale', 'Czech Pilsener', 
             'Hefeweizen', 'American Pale Ale (APA)'],
    'abv': [8.0, 8.0, 5.0, 6.8, 10.2, 11.0, 10.6, 8.0, 5.2, 12.0, 13.0, 7.0, 4.8, 5.4, 6.2],
    'reviews': [252, 469, 156, 112, 1272, 610, 637, 2527, 322, 428, 249, 182, 131, 1981, 393],
    'overall': [4.63, 4.63, 4.63, 4.62, 4.62, 4.60, 4.59, 4.59, 4.56, 4.55, 4.54, 4.54, 4.53, 4.52, 4.51],
    'taste': [4.57, 4.61, 4.63, 4.69, 4.72, 4.72, 4.70, 4.63, 4.39, 4.62, 4.77, 4.58, 4.41, 4.43, 4.49]
}
top_beers_df = pd.DataFrame(top_beers_data)

# Top Beer By Style
top_by_style_data = {
    'beer_style': ['American Double/Imperial IPA', 'American Double/Imperial Stout', 'Belgian Strong Pale Ale', 
                  'Quadrupel (Quad)', 'American IPA', 'Tripel', 'Doppelbock', 'American Pale Ale (APA)', 
                  'Belgian Strong Dark Ale', 'Russian Imperial Stout', 'Oatmeal Stout', 'American Strong Ale', 
                  'Milk/Sweet Stout', 'Vienna Lager', 'Maibock/Helles Bock', 'American Barleywine', 'Irish Dry Stout'],
    'beer_name': ['Pliny The Elder', 'Founders Breakfast Stout', 'Duvel', 'Trappistes Rochefort 10', 'Two Hearted Ale', 
                 'La Fin Du Monde', 'Ayinger Celebrator Doppelbock', 'Sierra Nevada Pale Ale', 'Chimay Grande Réserve (Blue)', 
                 'Stone Imperial Russian Stout', 'Samuel Smith\'s Oatmeal Stout', 'Arrogant Bastard Ale', 
                 'Young\'s Double Chocolate Stout', 'Samuel Adams Boston Lager', 'Dead Guy Ale', 'Sierra Nevada Bigfoot Barleywine', 
                 'Guinness Draught'],
    'brewery': ['Russian River Brewing Company', 'Founders Brewing Company', 'Brouwerij Duvel Moortgat NV', 
               'Brasserie de Rochefort', 'Bell\'s Brewery, Inc.', 'Unibroue', 'Privatbrauerei Franz Inselkammer', 
               'Sierra Nevada Brewing Co.', 'Bières de Chimay S.A.', 'Stone Brewing Co.', 'Samuel Smith Old Brewery', 
               'Stone Brewing Co.', 'Wells & Young\'s Ltd', 'Boston Beer Company', 'Rogue Ales', 'Sierra Nevada Brewing Co.', 
               'Guinness Ltd.'],
    'abv': [8.0, 8.3, 8.5, 11.3, 7.0, 9.0, 6.7, 5.6, 9.0, 10.5, 5.0, 7.2, 5.2, 4.9, 6.5, 9.6, 4.2],
    'reviews': [2527, 2502, 2450, 2170, 2728, 2483, 2070, 2587, 2009, 2329, 2025, 2704, 2257, 2418, 2234, 2492, 2210],
    'overall': [4.59, 4.35, 4.34, 4.34, 4.33, 4.30, 4.30, 4.25, 4.25, 4.24, 4.24, 4.08, 4.07, 4.04, 4.04, 3.97, 3.69],
    'taste': [4.63, 4.50, 4.33, 4.54, 4.32, 4.40, 4.43, 4.12, 4.37, 4.45, 4.27, 4.28, 4.09, 3.87, 4.02, 4.19, 3.35]
}
top_by_style_df = pd.DataFrame(top_by_style_data)

# ===== Create Visualizations =====

# Visualization 1: Top Beer Styles by Average Rating
plt.figure(figsize=(12, 8))
bars = sns.barplot(x='avg_overall', y='beer_style', data=top_styles_df.sort_values('avg_overall', ascending=False), 
                  palette=sns.color_palette("YlOrBr", n_colors=len(top_styles_df)))

# Add review count information as text
for i, row in enumerate(top_styles_df.sort_values('avg_overall', ascending=False).itertuples()):
    plt.text(row.avg_overall + 0.01, i, f"{row.review_count:,} reviews", va='center', fontsize=9)

plt.title('Top-Rated Beer Styles (minimum 1,000 reviews)', fontsize=16, pad=20)
plt.xlabel('Average Rating (out of 5)', fontsize=12)
plt.ylabel('Beer Style', fontsize=12)
plt.xlim(3.9, 4.2)
plt.tight_layout()
plt.savefig('visualizations/top_beer_styles.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 2: ABV vs. Ratings Relationship
plt.figure(figsize=(12, 8))
barWidth = 0.15
r1 = np.arange(len(abv_ratings_df))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

plt.bar(r1, abv_ratings_df['overall_rating'], width=barWidth, label='Overall', color='#FF9800')
plt.bar(r2, abv_ratings_df['taste'], width=barWidth, label='Taste', color='#F44336')
plt.bar(r3, abv_ratings_df['aroma'], width=barWidth, label='Aroma', color='#9C27B0')
plt.bar(r4, abv_ratings_df['appearance'], width=barWidth, label='Appearance', color='#2196F3')
plt.bar(r5, abv_ratings_df['palate'], width=barWidth, label='Palate', color='#4CAF50')

plt.xlabel('Alcohol Content (ABV)', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.title('How Alcohol Content Affects Beer Ratings', fontsize=16, pad=20)
plt.xticks([r + barWidth*2 for r in range(len(abv_ratings_df))], abv_ratings_df['abv_category'])
plt.ylim(3.0, 4.3)

# Add review count as text above each group
for i, row in enumerate(abv_ratings_df.itertuples()):
    plt.text(i + barWidth*2, 3.1, f"{row.review_count:,}\nreviews", ha='center', va='bottom', fontsize=9, 
             bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.2'))

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
plt.tight_layout()
plt.savefig('visualizations/abv_vs_ratings.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 3: Top Breweries Analysis
plt.figure(figsize=(12, 10))
brewery_plot = sns.barplot(x='avg_rating', y='brewery_name', 
                           data=top_breweries_df.sort_values('avg_rating', ascending=False),
                           palette=sns.color_palette("YlOrBr_r", len(top_breweries_df)))

# Add custom labels for each brewery
for i, row in enumerate(top_breweries_df.sort_values('avg_rating', ascending=False).itertuples()):
    plt.text(row.avg_rating + 0.01, i, f"{row.review_count:,} reviews, {row.unique_beers} beers, {row.avg_abv}% ABV", 
             va='center', fontsize=9)

plt.title('Top-Rated Breweries (with 500+ reviews)', fontsize=16, pad=20)
plt.xlabel('Average Rating (out of 5)', fontsize=12)
plt.ylabel('Brewery', fontsize=12)
plt.xlim(4.15, 4.65)
plt.tight_layout()
plt.savefig('visualizations/top_breweries.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 4: Most Reviewed Beers - Scatter Plot of Rating vs Reviews
plt.figure(figsize=(14, 10))

# Convert lists to arrays to ensure proper sizes for scatter plot
x_vals = most_reviewed_df['review_count'].values
y_vals = most_reviewed_df['avg_rating'].values
sizes = most_reviewed_df['abv'].values * 50  # Size proportional to ABV
colors = most_reviewed_df['abv'].values  # Color by ABV

scatter = plt.scatter(x_vals, y_vals, s=sizes, c=colors, cmap='YlOrBr', alpha=0.8)

# Add labels for each beer
for i, row in enumerate(most_reviewed_df.itertuples()):
    plt.annotate(row.beer_name, 
                xy=(row.review_count, row.avg_rating),
                xytext=(5, 0), 
                textcoords='offset points',
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

plt.colorbar(scatter, label='ABV %')
plt.title('Most Reviewed Beers: Popularity vs. Rating', fontsize=16, pad=20)
plt.xlabel('Number of Reviews', fontsize=12)
plt.ylabel('Average Rating (out of 5)', fontsize=12)
plt.tight_layout()
plt.savefig('visualizations/most_reviewed_beers.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 5: Rating Components Heatmap
# Create a pivot table for the heatmap
components_pivot = style_components_df.set_index('beer_style')
components_pivot = components_pivot[['taste', 'aroma', 'appearance', 'palate']]
components_pivot = components_pivot.sort_values('taste', ascending=False)

plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(components_pivot, annot=True, cmap='YlOrBr', fmt=".2f", linewidths=.5, 
                     cbar_kws={'label': 'Rating (out of 5)'})

plt.title('Beer Style Rating Components', fontsize=16, pad=20)
plt.ylabel('Beer Style', fontsize=12)
plt.tight_layout()
plt.savefig('visualizations/rating_components_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 6: Top 15 Beers - Polar Chart
# Prepare data for polar chart
fig = plt.figure(figsize=(14, 10))

# Create categories
categories = ['Overall', 'Taste', 'ABV Score']

# Map ABV to a score out of 5 (highest ABV gets 5, lowest gets 1)
abv_min = top_beers_df['abv'].min()
abv_max = top_beers_df['abv'].max()
top_beers_df['abv_score'] = 1 + 4 * (top_beers_df['abv'] - abv_min) / (abv_max - abv_min)

# Number of beers to show
N = 10  # Limiting to top 10 for clarity
top_n_beers = top_beers_df.head(N)

# Number of categories
num_cats = len(categories)

# Plot 
ax = plt.subplot(111, polar=True)

# Set category labels
angles = [n / float(num_cats) * 2 * np.pi for n in range(num_cats)]
angles += angles[:1]  # Close the loop

# Draw the axes
plt.xticks(angles[:-1], categories)

# Draw the values
for i, beer in enumerate(top_n_beers.itertuples()):
    values = [beer.overall, beer.taste, beer.abv_score]
    values += values[:1]
    ax.plot(angles, values, linewidth=2, label=beer.beer_name)
    ax.fill(angles, values, alpha=0.1)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title('Top 10 Highest-Rated Beers: Rating Components', fontsize=16, pad=20)
plt.tight_layout()
plt.savefig('visualizations/top_beers_polar.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 7: Style vs ABV Bubble Chart
plt.figure(figsize=(14, 10))

# Fix for scatter plot - create proper numpy arrays
x_vals = top_styles_df['avg_abv'].values
y_vals = top_styles_df['avg_overall'].values
sizes = top_styles_df['review_count'].values / 100
colors = top_styles_df['avg_taste'].values

# Create bubble chart - size represents number of reviews
scatter = plt.scatter(x_vals, y_vals, s=sizes, alpha=0.7, c=colors, cmap='YlOrBr')

# Add labels for each style
for i, row in enumerate(top_styles_df.itertuples()):
    plt.annotate(row.beer_style, 
                xy=(row.avg_abv, row.avg_overall),
                xytext=(5, 0), 
                textcoords='offset points',
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7))

plt.colorbar(scatter, label='Average Taste Rating')
plt.title('Beer Styles: ABV vs. Overall Rating', fontsize=16, pad=20)
plt.xlabel('Average ABV %', fontsize=12)
plt.ylabel('Average Overall Rating', fontsize=12)
plt.xlim(4, 12)
plt.ylim(3.9, 4.15)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('visualizations/style_abv_bubble.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualization 8: Top Beer by Style - Horizontal Bar Chart
plt.figure(figsize=(14, 18))

# Sort by overall rating
sorted_df = top_by_style_df.sort_values('overall', ascending=True)

# Create horizontal bars
bars = plt.barh(sorted_df['beer_style'], sorted_df['overall'], color='#FF9800')

# Add beer names as labels
for i, (_, row) in enumerate(sorted_df.iterrows()):
    plt.text(4.0, i, f"{row['beer_name']} ({row['brewery'].split(' ')[0]})", 
             ha='left', va='center', fontsize=9, color='black',
             bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.2'))

plt.xlabel('Average Rating (out of 5)', fontsize=12)
plt.ylabel('Beer Style', fontsize=12)
plt.title('Top Beer by Style (Most Popular Only)', fontsize=16, pad=20)
plt.xlim(3.6, 4.8)
plt.tight_layout()
plt.savefig('visualizations/top_beer_by_style.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations have been created and saved to the 'visualizations' directory.")