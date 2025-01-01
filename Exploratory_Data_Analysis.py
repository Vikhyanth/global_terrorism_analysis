import pandas as pd


df = pd.read_csv('data/cleaned_global_terrorism.csv', encoding='latin1')  # Adjust file path and encoding as needed

print(df.info())
print(df.head())
# Perform some operations on df (e.g., checking for missing values)
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv('data/cleaned_global_terrorism.csv')

# Define output directory and ensure it exists
output_dir = 'visualizations'
if os.path.isfile(output_dir):  # Remove conflicting file if it exists
    os.remove(output_dir)
if not os.path.exists(output_dir):  # Create directory if it doesn't exist
    os.makedirs(output_dir)
#1 Visualize Terrorist attack by region--
# Count incidents by region
region_counts = df['region_txt'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
region_counts.plot(kind='bar', color='skyblue')
plt.title('Terrorist Incidents by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()

# Save plot as JPG in 'visualizations/' folder
output_path = os.path.join(output_dir, 'incidents_by_region.jpg')
plt.savefig(output_path, format='jpg', dpi=300)
plt.close()  # Close plot to free memory

print(f"Plot saved successfully at {output_path}")

#2 Analyse Attack Types--
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data/cleaned_global_terrorism.csv')

# Count the occurrences of each attack type
attack_counts = df['attacktype1_txt'].value_counts()

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
attack_counts.plot(kind='barh', color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Frequency of Attack Types', fontsize=16)
plt.xlabel('Number of Incidents', fontsize=12)
plt.ylabel('Attack Type', fontsize=12)
plt.tight_layout()

# Save the plot as a JPG file
plt.savefig('visualizations/attack_types_bar_chart.jpg', format='jpg', dpi=300)

# Show the plot
plt.show()

#3 Geographical Mapping of Incidents
# Create scatter plot for geographical mapping
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/cleaned_global_terrorism.csv')

# Aggregate data by region to count the number of incidents
region_data = df.groupby('region_txt').size().reset_index(name='incident_count')

# Map regions to ISO country codes or region names recognized by Plotly
# (Plotly does not directly support "regions" like Western Europe, so we use countries as proxies)
region_country_map = {
    'North America': 'USA',
    'Central America & Caribbean': 'MEX',
    'South America': 'BRA',
    'Western Europe': 'FRA',
    'Eastern Europe': 'RUS',
    'Middle East & North Africa': 'EGY',
    'Sub-Saharan Africa': 'ZAF',
    'South Asia': 'IND',
    'Southeast Asia': 'IDN',
    'East Asia': 'CHN',
    'Australasia & Oceania': 'AUS'
}

# Add a column for country codes based on the region
region_data['country_code'] = region_data['region_txt'].map(region_country_map)

# Create the choropleth map
fig = px.choropleth(
    region_data,
    locations='country_code',  # Use country codes for mapping
    locationmode='ISO-3',      # Specify ISO-3 country code format
    color='incident_count',    # Data to visualize (number of incidents)
    hover_name='region_txt',   # Display region name on hover
    color_continuous_scale='RdYlGn_r',  # Green (low) to Red (high)
    title='Global Terrorism Heatmap by Region'
)

# Customize layout for better visualization
fig.update_geos(
    projection_type="natural earth",  # Use natural earth projection
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="LightGray",
    showocean=True,
    oceancolor="LightBlue"
)

fig.update_layout(
    coloraxis_colorbar=dict(
        title="Incident Count",
        ticks="outside"
    ),
    margin={"r":0,"t":30,"l":0,"b":0}
)

# Save the map as an image file
fig.write_image('visualizations/global_terrorism_heatmap.jpg', format='jpg', scale=2)

# Display the map in an interactive window
fig.show()

#4 Analyse success rates of attack
# Count success rates
success_counts = df['success'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))
success_counts.plot(kind='bar', color=['green', 'red'])
plt.title('Success Rate of Terrorist Attacks', fontsize=16)
plt.xlabel('Success (1 = Yes, 0 = No)', fontsize=12)
plt.ylabel('Number of Attacks', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot as a JPG file
plt.savefig('visualizations/success_rate.jpg', format='jpg', dpi=300)
plt.close()
