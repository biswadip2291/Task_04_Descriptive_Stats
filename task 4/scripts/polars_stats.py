import polars as pl

# === CONFIGURATION ===
file_path = "2024_fb_ads_president_scored_anon.csv"  # Change path if needed
numeric_columns = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
non_numeric_columns = ["page_id", "ad_id", "currency", "bylines", "publisher_platforms"]

# === LOAD DATA ===
df = pl.read_csv(file_path)

# === NUMERIC SUMMARY ===
print("\n==== NUMERIC STATS ====\n")
print(df.select([
    pl.col(col).mean().alias(f"{col}_mean") for col in numeric_columns
] + [
    pl.col(col).min().alias(f"{col}_min") for col in numeric_columns
] + [
    pl.col(col).max().alias(f"{col}_max") for col in numeric_columns
] + [
    pl.col(col).std().alias(f"{col}_std") for col in numeric_columns
] + [
    pl.col(col).count().alias(f"{col}_count") for col in numeric_columns
]))

# === NON-NUMERIC SUMMARY ===
print("\n==== NON-NUMERIC STATS ====\n")
for col in non_numeric_columns:
    count = df[col].len()
    unique = df[col].n_unique()
    top = df[col].mode()[0] if len(df[col].mode()) > 0 else None
    print(f"{col}:")
    print(f"  Count: {count}")
    print(f"  Unique Values: {unique}")
    print(f"  Most Common: {top}")
    print()

# === GROUP BY page_id ===
print("\n==== GROUPED BY page_id ====\n")
grouped_page = df.group_by("page_id").agg([
    pl.col(col).mean().alias(f"{col}_mean") for col in numeric_columns
] + [
    pl.col(col).min().alias(f"{col}_min") for col in numeric_columns
] + [
    pl.col(col).max().alias(f"{col}_max") for col in numeric_columns
] + [
    pl.col(col).std().alias(f"{col}_std") for col in numeric_columns
] + [
    pl.col(col).count().alias(f"{col}_count") for col in numeric_columns
])
print(grouped_page.head())

# === GROUP BY page_id AND ad_id ===
print("\n==== GROUPED BY page_id AND ad_id ====\n")
grouped_page_ad = df.group_by(["page_id", "ad_id"]).agg([
    pl.col(col).mean().alias(f"{col}_mean") for col in numeric_columns
] + [
    pl.col(col).min().alias(f"{col}_min") for col in numeric_columns
] + [
    pl.col(col).max().alias(f"{col}_max") for col in numeric_columns
] + [
    pl.col(col).std().alias(f"{col}_std") for col in numeric_columns
] + [
    pl.col(col).count().alias(f"{col}_count") for col in numeric_columns
])
print(grouped_page_ad.head())