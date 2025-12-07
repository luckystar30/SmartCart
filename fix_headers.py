import pandas as pd

path = r"C:\Users\sdtho\OneDrive\Desktop\myproject\data\final_recommendations_with_promos.csv"

# Read the file
df = pd.read_csv(path)

# Clean column names — remove quotes and whitespace
df.columns = [col.strip().replace("'", "").replace('"', '') for col in df.columns]

# Save cleaned file
df.to_csv(path, index=False)

print("✅ Cleaned headers:", df.columns.tolist())