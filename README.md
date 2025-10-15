## Employment Services Client Outcomes – FY 2022–23 Analysis in Python 

## 📊 Overview
This project analyzes the **Employment Services (ES) Client Outcomes** dataset for the **2022–23 fiscal year**, covering 258 service delivery sites (SDS) across Ontario.  
The goal is to evaluate program effectiveness through **descriptive and inferential statistics**, focusing on employment at program exit and follow-up outcomes at 3 months.

The analysis is conducted in **Python (Jupyter Notebook)** using `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`.

---

## 🧩 Objectives
- Explore and describe the dataset using appropriate descriptive statistics.
- Perform univariate, bivariate, and multivariate analyses.
- Identify key patterns and potential data quality issues.
- Test whether **employment at exit** predicts **employment at 3 months**.
- Generate actionable insights for program evaluation and policy decisions.

---
## 🔍 Key Steps in the Analysis
The project follows a structured pipeline:

## 1. Data Loading & Inspection
| Aspect            | Details                            |
| ----------------- | ---------------------------------- |
| Total Sites       | 258                                |
| Columns           | 19                                 |
| Suppression Codes | `x` (357), `SP` (158)              |
| Duplicates        | None                               |
| Small Sites       | Some with only a few dozen clients |




## 2. Data Cleaning & Transformation

Replaced suppression codes (x, SP, p, r, .) with NaN.

Converted outcome columns to numeric values.

Created derived indicators:

pct_emp_exit = out_exit_sum_emp / num_assist
pct_emp_3m = out_3_sum_emp / num_assist

(to allow fair comparison across sites of different sizes)

## 3. Descriptive Statistics

Most sites serve fewer than 500 clients; a few exceed 1,000.

Employment dominates exit outcomes (~55,000 clients), followed by training (~13,000).

Unknown outcomes (~10%) highlight data quality issues.

At 3 months, employment declines, with 35,000 “Null” and 16,000 “Unknown” follow-ups.

##  4. Multivariate & Regression Analysis

Moderate correlation between employment at exit and at 3 months (r ≈ 0.40).

Larger sites are not always more effective — quality and context matter.

Logistic regression confirms that:

More employed clients at exit → higher odds of sustained employment.

More unemployed at exit → lower odds of sustained employment.

## 🧠 Key Findings

Exit outcomes moderately predict short-term follow-up.

Employment and training are the two dominant exit pathways.

Toronto accounts for ~25% of all sites, shaping provincial averages.

“Unknown” and “Null” outcomes reduce data reliability.

Site size is not a strong predictor of success.

## 🚧 Data Quality Challenges


| Issue               | Description                        | Impact                  |
| ------------------- | ---------------------------------- | ----------------------- |
| Suppressed Values   | `x`, `SP` codes used for privacy   | Bias in small sites     |
| Missing Follow-Ups  | Many NaNs at 3, 6, 12 months       | Reduced sample size     |
| Inconsistent Scales | Site sizes from 15 to 1500 clients | Skews provincial totals |
| Aggregation         | 25 raw categories → 5 grouped      | Limits detail           |
| Class Imbalance     | Most sites show employment         | Inflates model accuracy |


##  💡 Recommendations

-  Use percentages instead of raw counts for site comparisons.

-  Conduct regional comparisons to balance Toronto’s influence.

-  Analyze training-to-employment pathways for long-term effects.

-  Extend evaluation to 6- and 12-month outcomes.

-  Improve follow-up reporting to reduce “Unknown” and “Null” outcomes.

-  Include equity analyses (age, gender, region) if data available.


