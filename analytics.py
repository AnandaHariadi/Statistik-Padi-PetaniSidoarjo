import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import os

# Set style for matplotlib
plt.style.use('seaborn-v0_8')
sns.set_palette('husl')

# Create graphs directory
if not os.path.exists('graphs'):
    os.makedirs('graphs')

# Function to display and save plots
def display_and_save_plot(fig, filename, plotly=False, show=True):
    if plotly:
        if show:
            fig.show()
        fig.write_image(f'graphs/{filename}.png')
    else:
        if show:
            plt.show()
        fig.savefig(f'graphs/{filename}.png', dpi=300, bbox_inches='tight')
        plt.close('all')

# Simulate data
np.random.seed(42)
districts = ['Balongbendo', 'Buduran', 'Candi', 'Gedangan', 'Jabon', 'Krembung', 'Porong', 'Prambon', 'Sedati', 'Sukodono', 'Tanggulangin', 'Taman', 'Tarik', 'Tulangan', 'Waru', 'Wonoayu']
years = list(range(2010, 2024))
n_rows = len(districts) * len(years)

# Nama-nama warga Sidoarjo sebagai petani
farmer_names = [
    'Ahmad Sidoarjo', 'Siti Nurhaliza Sidoarjo', 'Budi Santoso Sidoarjo', 'Dewi Kartika Sidoarjo', 'Joko Widodo Sidoarjo',
    'Sri Wahyuni Sidoarjo', 'Agus Setiawan Sidoarjo', 'Rina Puspita Sidoarjo', 'Hadi Susanto Sidoarjo', 'Maya Sari Sidoarjo',
    'Dwi Cahyono Sidoarjo', 'Lestari Indah Sidoarjo', 'Eko Prasetyo Sidoarjo', 'Wulan Dari Sidoarjo', 'Slamet Riyadi Sidoarjo',
    'Ani Lestari Sidoarjo', 'Bambang Sidoarjo', 'Sari Dewi Sidoarjo', 'Tono Sidoarjo', 'Rita Anggraini Sidoarjo',
    'Yudi Sidoarjo', 'Nurul Hidayah Sidoarjo', 'Surya Lesmana Sidoarjo', 'Indah Permata Sidoarjo', 'Dian Fitriani Sidoarjo',
    'Ari Wibowo Sidoarjo', 'Santi Lestari Sidoarjo', 'Rudi Hartono Sidoarjo', 'Mega Puspitasari Sidoarjo', 'Adi Nugroho Sidoarjo',
    'Lina Marlina Sidoarjo', 'Supriyadi Sidoarjo', 'Fitria Wulandari Sidoarjo', 'Gunawan Sidoarjo', 'Sri Rejeki Sidoarjo',
    'Bayu Aji Sidoarjo', 'Yeni Melati Sidoarjo', 'Dodi Setiawan Sidoarjo', 'Rina Amelia Sidoarjo', 'Hendra Kusuma Sidoarjo',
    'Putri Lestari Sidoarjo', 'Arif Rahman Sidoarjo', 'Siska Amelia Sidoarjo', 'Wawan Setiawan Sidoarjo', 'Dewi Sartika Sidoarjo',
    'Iwan Kurniawan Sidoarjo', 'Ratih Purwanti Sidoarjo', 'Fajar Siddiq Sidoarjo', 'Maya Indriani Sidoarjo', 'Denny Sidoarjo'
]

data = {
    'Year': np.repeat(years, len(districts)),
    'District': districts * len(years),
    'Farmer_Name': np.random.choice(farmer_names, n_rows),
    'Area_Harvested': np.random.uniform(500, 2000, n_rows),
    'Production': np.random.uniform(1000, 5000, n_rows),
    'Yield': np.random.uniform(2, 6, n_rows),
    'Rainfall': np.random.uniform(1500, 3000, n_rows),
    'Temperature': np.random.uniform(25, 35, n_rows),
    'Fertilizer_Use': np.random.uniform(100, 500, n_rows),
    'Pesticide_Use': np.random.uniform(50, 200, n_rows),
    'Labor_Cost': np.random.uniform(50000, 200000, n_rows),
    'Farmer_Count': np.random.randint(50, 200, n_rows)
}

df = pd.DataFrame(data)
df['Yield'] = df['Production'] / df['Area_Harvested']  # Ensure yield is calculated properly

# Function to save plots
def save_plot(fig, filename, plotly=False):
    if plotly:
        fig.write_image(f'graphs/{filename}.png')
    else:
        fig.savefig(f'graphs/{filename}.png', dpi=300, bbox_inches='tight')
    plt.close('all') if not plotly else None

print("=== ANALISIS PRODUKTIVITAS PADI SIDOARJO ===")
print("📊 KELOMPOK ANALISIS:")
print("1️⃣  GRAFIK 1-10: ANALISIS PRODUKTIVITAS DAN TREN PRODUKSI")
print("2️⃣  GRAFIK 11-20: ANALISIS EKONOMI DAN BIAYA PRODUKSI")
print("3️⃣  GRAFIK 21-30: ANALISIS LINGKUNGAN DAN CUACA")
print("4️⃣  GRAFIK 31-36: ANALISIS LANJUTAN DAN PREDIKSI")
print("=" * 80)

# 1. Line plot: Average yield over years
avg_yield = df.groupby('Year')['Yield'].mean()
plt.figure(figsize=(10, 6))
plt.plot(avg_yield.index, avg_yield.values, marker='o', linewidth=2, color='darkgreen')
plt.title('Tren Produktivitas Padi Rata-rata per Tahun di Sidoarjo', fontsize=14, fontweight='bold')
plt.xlabel('Tahun', fontsize=12)
plt.ylabel('Produktivitas (ton/ha)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=avg_yield.mean(), color='red', linestyle='--', alpha=0.7, label=f'Rata-rata: {avg_yield.mean():.2f}')
plt.legend()
display_and_save_plot(plt, '01_avg_yield_line')

# 2. Bar chart: Total production by district (2023)
prod_2023 = df[df['Year'] == 2023].groupby('District')['Production'].sum()
plt.figure(figsize=(12, 6))
prod_2023.plot(kind='bar', color='skyblue', edgecolor='black', alpha=0.8)
plt.title('Total Produksi Padi per Kecamatan (2023)', fontsize=14, fontweight='bold')
plt.xlabel('Kecamatan', fontsize=12)
plt.ylabel('Produksi (ton)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(prod_2023.values):
    plt.text(i, v + max(prod_2023.values)*0.01, f'{v:.0f}', ha='center', va='bottom', fontweight='bold')
display_and_save_plot(plt, '02_prod_bar_2023')

# 3. Scatter plot: Yield vs Rainfall
plt.figure(figsize=(10, 6))
plt.scatter(df['Rainfall'], df['Yield'], alpha=0.6, c=df['Year'], cmap='viridis')
plt.colorbar(label='Year')
plt.title('Rice Yield vs Rainfall')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Yield (tons/ha)')
save_plot(plt, '03_yield_rainfall_scatter')

# 4. Histogram: Distribution of Area Harvested
plt.figure(figsize=(10, 6))
plt.hist(df['Area_Harvested'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of Harvested Area')
plt.xlabel('Area Harvested (ha)')
plt.ylabel('Frequency')
save_plot(plt, '04_area_hist')

# 5. Box plot: Yield by District
plt.figure(figsize=(12, 6))
df.boxplot(column='Yield', by='District', figsize=(12, 6))
plt.title('Rice Yield Distribution by District')
plt.suptitle('')
plt.xticks(rotation=45)
save_plot(plt, '05_yield_box_district')

# 6. Pie chart: Production share by district (2023)
prod_2023 = df[df['Year'] == 2023].groupby('District')['Production'].sum()
plt.figure(figsize=(10, 10))
prod_2023.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Production Share by District (2023)')
plt.ylabel('')
save_plot(plt, '06_prod_pie_2023')

# 7. Line plot: Temperature trend
avg_temp = df.groupby('Year')['Temperature'].mean()
plt.figure(figsize=(10, 6))
plt.plot(avg_temp.index, avg_temp.values, marker='s', color='red', linewidth=2)
plt.title('Average Temperature Over Years')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.grid(True)
save_plot(plt, '07_temp_line')

# 8. Bar chart: Fertilizer use by year
fert_year = df.groupby('Year')['Fertilizer_Use'].mean()
plt.figure(figsize=(10, 6))
fert_year.plot(kind='bar', color='green')
plt.title('Average Fertilizer Use Over Years')
plt.xlabel('Year')
plt.ylabel('Fertilizer Use (kg/ha)')
save_plot(plt, '08_fert_bar')

# 9. Scatter plot: Production vs Labor Cost
plt.figure(figsize=(10, 6))
plt.scatter(df['Labor_Cost'], df['Production'], alpha=0.6, c=df['Area_Harvested'], cmap='plasma')
plt.colorbar(label='Area Harvested (ha)')
plt.title('Production vs Labor Cost')
plt.xlabel('Labor Cost (IDR)')
plt.ylabel('Production (tons)')
save_plot(plt, '09_prod_labor_scatter')

# 10. Histogram: Pesticide use distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Pesticide_Use'], bins=25, edgecolor='black', alpha=0.7, color='orange')
plt.title('Distribution of Pesticide Use')
plt.xlabel('Pesticide Use (liters/ha)')
plt.ylabel('Frequency')
save_plot(plt, '10_pest_hist')

# 11-20: Seaborn plots
# 11. Line plot with confidence interval
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Yield', errorbar=('ci', 95))
plt.title('Rice Yield Trend with Confidence Interval')
save_plot(plt, '11_yield_line_ci')

# 12. Bar plot: Production by district and year (subset)
subset = df[df['Year'].isin([2020, 2021, 2022])]
plt.figure(figsize=(12, 6))
sns.barplot(data=subset, x='District', y='Production', hue='Year')
plt.title('Production by District (2020-2022)')
plt.xticks(rotation=45)
save_plot(plt, '12_prod_bar_hue')

# 13. Scatter plot with regression
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Rainfall', y='Yield', scatter_kws={'alpha':0.6})
plt.title('Yield vs Rainfall with Regression Line')
save_plot(plt, '13_yield_rain_reg')

# 14. Histogram with KDE
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Area_Harvested', kde=True, bins=30)
plt.title('Harvested Area Distribution with KDE')
save_plot(plt, '14_area_hist_kde')

# 15. Box plot: Yield by year
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Year', y='Yield')
plt.title('Yield Distribution by Year')
plt.xticks(rotation=45)
save_plot(plt, '15_yield_box_year')

# 16. Violin plot: Temperature by district
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='District', y='Temperature')
plt.title('Temperature Distribution by District')
plt.xticks(rotation=45)
save_plot(plt, '16_temp_violin')

# 17. Heatmap: Correlation matrix
corr = df[['Area_Harvested', 'Production', 'Yield', 'Rainfall', 'Temperature', 'Fertilizer_Use', 'Pesticide_Use', 'Labor_Cost']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Farming Variables')
save_plot(plt, '17_corr_heatmap')

# 18. Pair plot: Key variables
pair_vars = ['Yield', 'Rainfall', 'Temperature', 'Fertilizer_Use']
sns.pairplot(df[pair_vars], diag_kind='kde')
plt.suptitle('Pair Plot of Key Variables', y=1.02)
save_plot(plt, '18_pair_plot')

# 19. Count plot: Farmer count by district (simulated as bar since count)
plt.figure(figsize=(12, 6))
sns.barplot(data=df.groupby('District')['Farmer_Count'].mean().reset_index(), x='District', y='Farmer_Count')
plt.title('Average Farmer Count by District')
plt.xticks(rotation=45)
save_plot(plt, '19_farmer_bar')

# 20. Swarm plot: Yield by district
plt.figure(figsize=(12, 6))
sns.swarmplot(data=df, x='District', y='Yield', size=3)
plt.title('Yield Swarm Plot by District')
plt.xticks(rotation=45)
save_plot(plt, '20_yield_swarm')

# 21-30: Plotly plots
# 21. Line plot: Yield over time
fig = px.line(df.groupby('Year')['Yield'].mean().reset_index(), x='Year', y='Yield', title='Average Yield Over Years')
save_plot(fig, '21_yield_line_plotly', plotly=True)

# 22. Bar chart: Production by district
prod_district = df.groupby('District')['Production'].sum().reset_index()
fig = px.bar(prod_district, x='District', y='Production', title='Total Production by District')
save_plot(fig, '22_prod_bar_plotly', plotly=True)

# 23. Scatter plot: Yield vs Rainfall
fig = px.scatter(df, x='Rainfall', y='Yield', color='Year', title='Yield vs Rainfall')
save_plot(fig, '23_yield_rain_scatter_plotly', plotly=True)

# 24. Histogram: Area harvested
fig = px.histogram(df, x='Area_Harvested', title='Harvested Area Distribution')
save_plot(fig, '24_area_hist_plotly', plotly=True)

# 25. Box plot: Yield by district
fig = px.box(df, x='District', y='Yield', title='Yield by District')
save_plot(fig, '25_yield_box_plotly', plotly=True)

# 26. Pie chart: Production share
fig = px.pie(prod_district, names='District', values='Production', title='Production Share by District')
save_plot(fig, '26_prod_pie_plotly', plotly=True)

# 27. Heatmap: Correlation
fig = px.imshow(corr, title='Correlation Heatmap')
save_plot(fig, '27_corr_heatmap_plotly', plotly=True)

# 28. Scatter matrix
fig = px.scatter_matrix(df[pair_vars], title='Scatter Matrix')
save_plot(fig, '28_scatter_matrix_plotly', plotly=True)

# 29. Area chart: Production over years
prod_year = df.groupby('Year')['Production'].sum().reset_index()
fig = px.area(prod_year, x='Year', y='Production', title='Total Production Over Years')
save_plot(fig, '29_prod_area_plotly', plotly=True)

# 30. Violin plot: Temperature by district
fig = px.violin(df, x='District', y='Temperature', title='Temperature by District')
save_plot(fig, '30_temp_violin_plotly', plotly=True)

# 31-36: More varied plots
# 31. Matplotlib: Stacked bar for inputs
inputs = df.groupby('Year')[['Fertilizer_Use', 'Pesticide_Use']].mean()
plt.figure(figsize=(10, 6))
inputs.plot(kind='bar', stacked=True)
plt.title('Fertilizer and Pesticide Use Over Years')
plt.xlabel('Year')
plt.ylabel('Use (kg/liters per ha)')
save_plot(plt, '31_inputs_stacked_bar')

# 32. Seaborn: Facet grid for yield by district and year
g = sns.FacetGrid(df, col='District', col_wrap=4, height=3)
g.map(sns.lineplot, 'Year', 'Yield')
g.set_titles('{col_name}')
g.set_axis_labels('Year', 'Yield')
plt.suptitle('Yield Trends by District', y=1.02)
save_plot(plt, '32_yield_facet')

# 33. Plotly: 3D scatter
fig = px.scatter_3d(df, x='Rainfall', y='Temperature', z='Yield', color='Year', title='3D Scatter: Yield vs Rainfall and Temperature')
save_plot(fig, '33_3d_scatter_plotly', plotly=True)

# 34. Matplotlib: Error bar plot
yield_stats = df.groupby('Year')['Yield'].agg(['mean', 'std']).reset_index()
plt.figure(figsize=(10, 6))
plt.errorbar(yield_stats['Year'], yield_stats['mean'], yerr=yield_stats['std'], fmt='o-', capsize=5)
plt.title('Yield with Error Bars')
plt.xlabel('Year')
plt.ylabel('Yield (tons/ha)')
save_plot(plt, '34_yield_error_bar')

# 35. Seaborn: Joint plot
plt.figure(figsize=(10, 8))
sns.jointplot(data=df, x='Rainfall', y='Yield', kind='reg')
plt.suptitle('Joint Plot: Yield vs Rainfall', y=1.02)
save_plot(plt, '35_yield_rain_joint')

# 36. Plotly: Sunburst chart (simulated hierarchy)
df['Region'] = np.random.choice(['North', 'South', 'East', 'West'], n_rows)
sunburst_data = df.groupby(['Region', 'District'])['Production'].sum().reset_index()
fig = px.sunburst(sunburst_data, path=['Region', 'District'], values='Production', title='Production Sunburst')
save_plot(fig, '36_prod_sunburst_plotly', plotly=True)

print("All 36 graphs generated and saved in 'graphs' folder.")
