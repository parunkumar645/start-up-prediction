"""
Generate sample startup data for testing the ML pipeline
"""
import pandas as pd
import numpy as np
import os
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create data directories
project_root = Path(__file__).parent
data_dir = project_root / "data"
raw_dir = data_dir / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

print("Generating sample startup data...")

# Generate sample data with similar structure to Crunchbase
n_samples = 5000  # Generate 5000 sample records

# Define features matching the model expectations
data = {
    'name': [f'Startup_{i}' for i in range(n_samples)],
    'founded_at': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], n_samples),
    'founded_month': np.random.randint(1, 13, n_samples),
    'founded_year': np.random.choice(range(1995, 2015), n_samples),
    'founded_quarter': np.random.randint(1, 5, n_samples),
    'status': np.random.choice(['acquired', 'operating', 'closed'], n_samples, p=[0.08, 0.78, 0.14]),
    'country_code': np.random.choice(['USA', 'GBR', 'CAN', 'IND', 'DEU', 'FRA', 'CHN', 'JPN', 'AUS', 'NLD'], n_samples, p=[0.75, 0.05, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.04]),
    'state_code': np.random.choice(['CA', 'NY', 'MA', 'TX', 'WA', 'IL', 'PA', 'NC', 'GA', 'CO', 'Other'], n_samples),
    'city': np.random.choice(['San Francisco', 'New York', 'Boston', 'Austin', 'Seattle', 'Chicago', 'Los Angeles', 'Denver', 'Atlanta', 'Other'], n_samples),
    'region': np.random.choice(['Northern America', 'Western Europe', 'Eastern Asia', 'Southern Asia', 'Other'], n_samples),
    'category_code': np.random.choice(['software', 'web', 'mobile', 'enterprise', 'analytics', 'photo_video', 'search', 'medical', 'finance', 'clean_tech', 'hospitality', 'hardware', 'advertising', 'network_hosting', 'public_relations', 'games_video', 'news', 'nanotech', 'ecommerce', 'manufacturing', 'education', 'semiconductor', 'biotech', 'consulting', 'fashion'], n_samples),
    'funding_total_usd': np.random.lognormal(mean=3.5, sigma=2.5, size=n_samples).astype(int),
    'funding_rounds': np.random.choice(range(0, 8), n_samples),
    'founded_days': np.random.randint(0, 365, n_samples),
    'age_first_milestone_year': np.random.randint(0, 20, n_samples),
    'age_last_milestone_year': np.random.randint(0, 20, n_samples),
    'age_first_funding_year': np.random.randint(0, 20, n_samples),
}

# Create DataFrame
df = pd.DataFrame(data)

# Ensure status distribution is realistic
acquired_mask = (df['founded_year'] < 2010) & (np.random.random(n_samples) < 0.15)
df.loc[acquired_mask, 'status'] = 'acquired'
df.loc[~acquired_mask & (np.random.random(n_samples) < 0.3), 'status'] = 'closed'
df.loc[~acquired_mask & (df['status'] != 'closed'), 'status'] = 'operating'

# Add some missing values to be more realistic
missing_rate = 0.05
for col in ['state_code', 'city', 'age_first_funding_year']:
    missing_indices = np.random.choice(n_samples, size=int(n_samples * missing_rate), replace=False)
    df.loc[missing_indices, col] = np.nan

print(f"Generated {n_samples} sample records")
print(f"Status distribution:\n{df['status'].value_counts()}")
print(f"Sample data shape: {df.shape}")

# Save the raw data
output_path = raw_dir / "startups_data.csv"
df.to_csv(output_path, index=False, encoding='latin-1')
print(f"\nSaved sample data to: {output_path}")

# Also create sample unique cities and regions for the dropdown
unique_regions = df['region'].unique()
unique_cities = df[df['city'].notna()]['city'].unique()

processed_dir = data_dir / "processed"
processed_dir.mkdir(parents=True, exist_ok=True)

regions_df = pd.DataFrame({'region': sorted(unique_regions)})
cities_df = pd.DataFrame({'city': sorted(unique_cities)})

regions_df.to_csv(processed_dir / "unique_regions.csv", index=False)
cities_df.to_csv(processed_dir / "unique_cities.csv", index=False)

print(f"Saved {len(regions_df)} regions to {processed_dir / 'unique_regions.csv'}")
print(f"Saved {len(cities_df)} cities to {processed_dir / 'unique_cities.csv'}")

print("\n✓ Sample data generation complete!")
print("You can now run the notebooks to train the models.")
