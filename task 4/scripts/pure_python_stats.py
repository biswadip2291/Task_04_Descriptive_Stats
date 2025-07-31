import csv
from collections import defaultdict, Counter
from math import sqrt

# === CONFIGURATION ===
file_path = "2024_fb_ads_president_scored_anon.csv"  # Change path as needed
numeric_columns = ["estimated_audience_size", "estimated_impressions", "estimated_spend"]
non_numeric_columns = ["page_id", "ad_id", "currency", "bylines", "publisher_platforms"]

# === DATA LOADING ===
data = defaultdict(list)

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for col in numeric_columns:
            try:
                val = float(row[col])
                data[col].append(val)
            except:
                continue
        for col in non_numeric_columns:
            data[col].append(row[col])

# === STATS FUNCTIONS ===
def compute_basic_stats(values):
    count = len(values)
    if count == 0:
        return count, None, None, None, None
    mean = sum(values) / count
    std_dev = sqrt(sum((x - mean) ** 2 for x in values) / count)
    return count, mean, min(values), max(values), std_dev

def compute_non_numeric_stats(values):
    count = len(values)
    unique = len(set(values))
    most_common = Counter(values).most_common(1)[0]
    return count, unique, most_common

# === SUMMARY RESULTS ===
print("\n==== NUMERIC STATS ====\n")
for col in numeric_columns:
    count, mean, min_val, max_val, std_dev = compute_basic_stats(data[col])
    print(f"{col}:")
    print(f"  Count: {count}")
    print(f"  Mean: {mean:.2f}")
    print(f"  Min: {min_val}")
    print(f"  Max: {max_val}")
    print(f"  Std Dev: {std_dev:.2f}")
    print()

print("\n==== NON-NUMERIC STATS ====\n")
for col in non_numeric_columns:
    count, unique, most_common = compute_non_numeric_stats(data[col])
    print(f"{col}:")
    print(f"  Count: {count}")
    print(f"  Unique Values: {unique}")
    print(f"  Most Common: {most_common}")
    print()



# === GROUPED STATS (Single and Double Key) ===

from collections import defaultdict

# Reload rows
data_rows = []
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data_rows.append(row)

# --- Grouped by page_id ---
group1 = defaultdict(list)
for row in data_rows:
    key = row.get("page_id", "").strip()
    if key == "":
        continue
    try:
        val = float(row.get("estimated_spend", ""))
        group1[key].append(val)
    except ValueError:
        pass

print(f"\n==== GROUPED BY page_id ====\n")
for k in sorted(group1):
    vals = group1[k]
    if not vals:
        continue
    mean = sum(vals) / len(vals)
    minimum = min(vals)
    maximum = max(vals)
    stddev = sqrt(sum((x - mean) ** 2 for x in vals) / len(vals))
    print(f"{k} - Count: {len(vals)}, Mean: {mean:.2f}, Min: {minimum}, Max: {maximum}, StdDev: {stddev:.2f}")

# --- Grouped by page_id + ad_id ---
group2 = defaultdict(list)
for row in data_rows:
    k1 = row.get("page_id", "").strip()
    k2 = row.get("ad_id", "").strip()
    if not k1 or not k2:
        continue
    try:
        val = float(row.get("estimated_spend", ""))
        group2[(k1, k2)].append(val)
    except ValueError:
        pass

print(f"\n==== GROUPED BY page_id AND ad_id ====\n")
for k in sorted(group2):
    vals = group2[k]
    if not vals:
        continue
    mean = sum(vals) / len(vals)
    minimum = min(vals)
    maximum = max(vals)
    stddev = sqrt(sum((x - mean) ** 2 for x in vals) / len(vals))
    print(f"{k} - Count: {len(vals)}, Mean: {mean:.2f}, Min: {minimum}, Max: {maximum}, StdDev: {stddev:.2f}")

