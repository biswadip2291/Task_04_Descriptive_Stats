import pandas as pd

# === CONFIGURATION ===
file_path = "2024_fb_ads_president_scored_anon.csv"  # Change path if needed
numeric_columns = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
non_numeric_columns = ["page_id", "ad_id", "currency", "bylines", "publisher_platforms"]

# === LOAD DATA ===
df = pd.read_csv(file_path)

# === NUMERIC STATS ===
print("\n==== NUMERIC STATS ====\n")
numeric_summary = df[numeric_columns].describe().T
print(numeric_summary)

# === NON-NUMERIC STATS ===
print("\n==== NON-NUMERIC STATS ====\n")
for col in non_numeric_columns:
    count = df[col].count()
    unique = df[col].nunique()
    top = df[col].value_counts().idxmax()
    top_count = df[col].value_counts().max()
    
    print(f"{col}:")
    print(f"  Count: {count}")
    print(f"  Unique Values: {unique}")
    print(f"  Most Common: {top} (appears {top_count} times)")
    print()

# === GROUPED STATS (Optional) ===
print("\n==== GROUPED BY `page_id` ====\n")
grouped_page = df.groupby("page_id")[numeric_columns].describe()
print(grouped_page.head())

print("\n==== GROUPED BY `page_id` and `ad_id` ====\n")
grouped_page_ad = df.groupby(["page_id", "ad_id"])[numeric_columns].describe()
print(grouped_page_ad.head())
