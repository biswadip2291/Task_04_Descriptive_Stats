
# 📊 Task_04_Descriptive_Stats

This repository contains scripts to generate descriptive statistics for the **2024 Facebook Ads Presidential Dataset** using three different approaches: pure Python (no external libraries), Pandas, and Polars.

---

## 📁 Files Included

| Filename              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `pure_python_stats.py`| Descriptive statistics using only Python standard libraries                 |
| `pandas_stats.py`     | Analysis using the Pandas library                                           |
| `polars_stats.py`     | Fast and memory-efficient analysis using Polars                             |
| `visualizations.py`   | (Optional) Visualizations using Matplotlib and Seaborn *(if applicable)*    |

---

## 📌 Dataset

**Name:** 2024 Facebook Ads Presidential Dataset  
**Source:** [Download from Google Drive](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view)  

---

## 🧪 How to Run

1. **Install dependencies** (for Pandas/Polars visualizations):
   ```bash
   pip install pandas polars matplotlib seaborn
   ```

2. **Run each script individually**:
   ```bash
   python pure_python_stats.py
   python pandas_stats.py
   python polars_stats.py
   ```

3. **For visualizations** *(optional)*:
   ```bash
   python visualizations.py
   ```

---

## 📈 What the Scripts Do

Each script:
- Loads the dataset
- Computes count, mean, min, max, and standard deviation for numeric columns
- Identifies unique and most frequent values for categorical fields
- Performs grouped analysis by `page_id` and `page_id + ad_id`

---

## 💡 Summary of Insights

- Most ads targeted a small number of states and demographic groups.
- `estimated_spend` and `estimated_impressions` showed wide variation across `page_id`.
- Grouped statistics revealed recurring ad patterns by organization.

---

## 📚 Skills Practiced

- Python scripting and data parsing
- Descriptive statistical computation
- Grouped aggregation techniques
- Working with multiple data libraries (Pandas, Polars)
- Performance and usability comparison of tools


## 🔍 Reflection

Working on this task deepened my understanding of descriptive statistics and the trade-offs between different data processing tools. Implementing the same analysis pipeline using pure Python, Pandas, and Polars helped me appreciate how library design affects readability, speed, and usability.

Pure Python offered full control but required more verbose logic, especially for grouped aggregations and type handling. Pandas stood out for its clear syntax and extensive documentation, making it a natural choice for most analysis tasks. Polars, on the other hand, impressed me with its speed and modern features — especially its lazy evaluation and strict type system, which made operations both fast and predictable.

One of the main challenges was ensuring consistency in results across all three approaches, particularly when handling missing values and different numeric representations. This reinforced the importance of rigorous data cleaning and validation before analysis.

Additionally, this task allowed me to practice organizing reusable, modular code and develop strategies for adapting the analysis to new datasets. Overall, the experience strengthened both my technical and analytical thinking, and gave me a better framework for choosing tools based on project goals and dataset size.
