# ==========================================================
# Employment Services Client Outcomes FY 2022-23 Analysis
# Author: Aude Ines
# Description:
#   This analysis explores employment outcomes for clients of
#   Employment Services (ES) across 258 Service Delivery Sites (SDS)
#   in Ontario during fiscal year 2022–2023.
#
#   The notebook covers:
#     - Data loading and inspection
#     - Cleaning and transformation
#     - Descriptive statistics (univariate)
#     - Bivariate relationships
#     - Multivariate relationships
#     - Logistic regression modeling
#
#   Tools: Python, pandas, seaborn, matplotlib, scikit-learn
# ==========================================================


# === 1. Import Required Libraries ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import statsmodels.api as sm

# Configure plotting aesthetics
sns.set(style="whitegrid", palette="muted", font_scale=1.1)


# === 2. Load Dataset ===
# The dataset contains outcome and client count data for Employment Services (ES)
# Each row represents one Service Delivery Site (SDS)
# Columns include employment outcomes, training participation, and unknown statuses at exit and 3 months
df = pd.read_csv('../data/ES_Client_Outcomes_2022_23.csv')

print("=== Dataset Loaded ===")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
print(df.head(3))  # preview first 3 rows


# === 3. Data Inspection ===
# Check for missing values, datatypes, and suppressed codes
print("\n=== Data Information ===")
print(df.info())
print("\nMissing values per column:")
print(df.isna().sum())

# Look at column names to understand structure
print("\nColumn names:")
print(df.columns.tolist())


# === 4. Data Cleaning ===
# The dataset uses suppression codes (x, SP, p, r, .)
# These represent suppressed or missing values for privacy or data quality reasons.
# We replace them with NaN (Python’s representation for missing data).

df.replace(['x', 'SP', 'p', 'r', '.'], np.nan, inplace=True)

# Some numeric columns are stored as strings with commas ("1,200")
# Remove commas to safely convert them to numeric
df.replace(',', '', regex=True, inplace=True)

# Convert all numeric-like columns to numeric data types
df = df.apply(pd.to_numeric, errors='ignore')

print("\nData cleaning complete — suppression codes replaced, columns converted.")


# === 5. Derived Indicators ===
# To fairly compare sites of different sizes (some have 20 clients, others >1,500),
# we create percentage-based performance indicators.
df['pct_emp_exit'] = df['out_exit_sum_emp'] / df['num_assist']
df['pct_emp_3m'] = df['out_3_sum_emp'] / df['num_assist']

print("\nDerived indicators created:")
print(df[['pct_emp_exit', 'pct_emp_3m']].head(3))


# === 6. Summary Statistics ===
# Before analyzing outcomes, understand how large the sites are.
# The number of clients assisted (num_assist) varies dramatically.

summary = df['num_assist'].describe()
print("\n=== Summary Statistics: Assisted Clients ===")
print(summary)

# Visualize the distribution of assisted clients per site
plt.figure(figsize=(8, 5))
sns.histplot
