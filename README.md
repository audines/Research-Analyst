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


##  Dataset Description & Dictionary

The dataset contains **program performance data** for Ontario’s *Employment Services (ES)* network for the **2022–2023 fiscal year**.  
Each row represents one **Service Delivery Site (SDS)** — a location that delivers Employment Ontario programs.

The dataset reports **client outcomes** at two key points:
- **At Exit** — when the client leaves the program.
- **At 3-Month Follow-Up** — to measure sustained employment.

---

## 🧾 Overview

| Category | Description |
|-----------|--------------|
| **Name** | Employment Services Client Outcomes – FY 2022–23 |
| **Source** | Ontario Ministry of Labour, Immigration, Training and Skills Development |
| **Observation Level** | Service Delivery Site (SDS) |
| **Records** | 258 sites across Ontario |
| **Timeframe** | April 2022 – March 2023 |
| **Purpose** | Evaluate how Employment Services help clients gain and sustain employment |
| **Format** | CSV |
| **Author (Analysis)** | *Aude Ines* |
| **Main Indicators** | % Employed at Exit, % Employed at 3-Months |

---

## 🗂️ 1. Data Structure

| Column | Meaning | Notes / Examples |
|---------|----------|------------------|
| **est_region** | Economic region of Ontario | e.g., Durham, Halton, London, Northeast |
| **fiscal_year** | Fiscal year of reporting | 2022–2023 |
| **eo_program** | Employment Ontario program type | "ES" (Employment Service) |
| **sds_id** | Service Delivery Site unique ID | 1273 |
| **sds_name** | Name of the delivery site | "Durham College Employment Centre" |
| **sds_sec** | Secondary sector or service type | Funding or service classification |
| **num_assist** | Number of clients assisted | Clients served during the year |

---

## 🧮 2. Exit Outcomes (Immediate Program Results)

These fields record **client outcomes at the moment of program exit**.

| Column | Description | Interpretation |
|---------|--------------|----------------|
| `out_exit_sum_emp` | Clients employed at exit | Immediate job success |
| `out_exit_sum_te` | Clients in training or education | Continued education or upskilling |
| `out_exit_unemp` | Clients unemployed | Left without a job or training |
| `out_exit_sum_oth` | Other outcomes | Withdrew, relocated, etc. |
| `out_exit_unkn` | Unknown outcomes | Information not collected |
| `out_exit_null` | Null/missing outcomes | Suppressed or unavailable |

## 🧾 

| File | Description |
|------|--------------|
| **`Dataset_ES_Client_Outcomes_2223_Table_1.csv`** | Raw dataset |
| **`Technical_Dictionary_ES_Client_Outcomes_2223.csv`** | Variable definitions |
| **`Contextual Documentation - ES Client Outcomes (22-23).docx`** | Official methodology context |


## 1. Data Loading & Inspection
| Aspect            | Details                            |
| ----------------- | ---------------------------------- |
| Total Sites       | 258                                |
| Columns           | 19                                 |
| Suppression Codes | `x` (357), `SP` (158)              |
| Duplicates        | None                               |
| Small Sites       | Some with only a few dozen clients |




## 2. Data Cleaning & Transformation

- Replaced suppression codes (x, SP, p, r, .) with NaN.

- Converted outcome columns to numeric values.

- Created derived indicators:

pct_emp_exit = out_exit_sum_emp / num_assist
pct_emp_3m = out_3_sum_emp / num_assist

(to allow fair comparison across sites of different sizes)

## 3. Descriptive Statistics

---

### 🔹 Data Distribution — Assisted Clients per Site
Shows the variation in client volume across 258 service delivery sites (SDSs).

![Assisted Clients Summary](https://raw.githubusercontent.com/audines/Research-Analyst/main/assisted_clients_hist_with_stats.png)

*Figure 1 : Résumé numérique des clients assistés (exercice 2022–23).*



- Most sites serve fewer than 500 clients; a few exceed 1,000,  creating strong data skew.  
> → **Conclusion:** Use normalized rates (percentages) instead of raw counts.




### 🔹  Exit Outcomes (Univariate Analysis)
Immediate program effectiveness — what happened when clients exited the program.

> **Employment dominates**, followed by **Training/Education**.  
> About **10% of cases are “Unknown”**, flagging a data quality concern.

![Exit Outcomes](https://raw.githubusercontent.com/audines/Research-Analyst/main/exit_outcomes_with_numbers.png)

-  dominates exit outcomes (~55,000 clients), followed by training (~13,000).

- Unknown outcomes (~10%) highlight data quality issues.

- 
### 🔹  3-Month Outcomes (Univariate Analysis)
Short-term sustainability — are clients still employed 3 months after exit?

> Employment decreases slightly, but the main issue is **missing data**:  
> over **35,000 Null** and **16,000 Unknown** outcomes.  
> → Follow-up data quality must improve for reliable evaluation.


![3-Month Outcomes](https://raw.githubusercontent.com/audines/Research-Analyst/main/threemonths_outcomes_with_numbers.png)

### Regional Representation — Count of Records by Region
Shows how many service sites are in each Ontario region.

> **Toronto = ~25% of all SDSs**, heavily influencing provincial averages.  
> → Normalization and regional disaggregation are required for fairness.

[![Regional Counts](https://raw.githubusercontent.com/audines/Research-Analyst/main/categorical_summary_visual.png)
  

##  4. Multivariate & Regression Analysis



### 🔹Bivariate Relationship — Exit vs 3-Month Employment
Scatterplot + density plot of employment rates.

> Positive correlation **(r ≈ 0.40)**:  
> Sites with strong exit outcomes tend to maintain good 3-month performance,  
> but other contextual factors also influence sustainability.

![Exit vs 3 Month Employment](https://raw.githubusercontent.com/audines/Research-Analyst/main/mul.png)

---

###  Multivariate Analysis — Scatter Matrix
Examines interactions among multiple indicators: site size, exit employment, 3-month employment, and unemployment.

> Confirms moderate positive relationships but no clear link between **site size** and success.  
> → **Conclusion:** Quality and context matter more than scale.

![Scatter Matrix](https://raw.githubusercontent.com/audines/Research-Analyst/main/corr.png)




### 🔹  Predictive Modeling — Logistic Regression
Tests whether exit outcomes predict follow-up employment.

> **Coefficients:**  
> + Employed at Exit → +0.0124 (positive effect)  
> + Unemployed at Exit → –0.0148 (negative effect)  
>  
> **Accuracy:** ~97%, but inflated by class imbalance (most sites had employment at follow-up).  
>  
> → Exit success predicts sustainability, but additional factors should be modeled.

![Logistic Regression Results](https://raw.githubusercontent.com/audines/Research-Analyst/main/logistic_results_side_by_side_with_legend.png)

- Moderate correlation between employment at exit and at 3 months (r ≈ 0.40).

-  sites are not always more effective — quality and context matter.

- Logistic regression confirms that:

-  employed clients at exit → higher odds of sustained employment.

- More unemployed at exit → lower odds of sustained employment.

## 🧠 | Theme | Key Finding | Policy/Program Implication |

| Predictive Power | Exit employment moderately predicts 3-month employment ($r ≈ 0.40$) | Programs with strong exit results tend to sustain success |
| Regional Balance | Toronto dominates dataset (~25%) | Use normalized rates and regional analysis for fairness |
| Data Quality | Many Null/Unknown follow-ups | Improve tracking systems |
| Site Size | Scale doesn’t guarantee better outcomes | Focus on service quality and client context |
| Sustainability | Employment declines modestly after 3 months | Extend analysis to 6- and 12-month periods |

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




