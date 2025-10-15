# ==========================================================
# Employment Services Client Outcomes FY 2022-23 Analysis
# Author: Aude Ines
# ==========================================================

# === Import Libraries ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import statsmodels.api as sm

# === Load Data ===
df = pd.read_csv('../data/ES_Client_Outcomes_2022_23.csv')

# === Inspect Data ===
print(df.shape)
print(df.head())
print(df.info())

# === Cleaning ===
df.replace(['x', 'SP', 'p', 'r', '.'], np.nan, inplace=True)
df.replace(',', '', regex=True, inplace=True)
df = df.apply(pd.to_numeric, errors='ignore')

# === Derived Variables ===
df['pct_emp_exit'] = df['out_exit_sum_emp'] / df['num_assist']
df['pct_emp_3m'] = df['out_3_sum_emp'] / df['num_assist']

# === Summary Statistics ===
summary = df['num_assist'].describe()
print(summary)

plt.figure(figsize=(8, 5))
sns.histplot(df['num_assist'], bins=30, kde=True, color='steelblue')
plt.title('Distribution of Assisted Clients per Site')
plt.xlabel('Number of Clients Assisted')
plt.ylabel('Frequency')
plt.savefig('../figures/numeric_summary_visual.png')
plt.show()

# === Univariate Analysis: Exit Outcomes ===
exit_cols = ['out_exit_sum_emp', 'out_exit_sum_te', 'out_exit_unemp', 'out_exit_oth', 'out_exit_unkn']
exit_totals = df[exit_cols].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=exit_totals.values, y=exit_totals.index, palette='viridis')
plt.title('Exit Outcomes Across All Sites')
plt.xlabel('Number of Clients')
plt.ylabel('Outcome Type')
for i, val in enumerate(exit_totals.values):
    plt.text(val + 500, i, f"{val:,}", va='center')
plt.savefig('../figures/exit_outcomes_with_numbers.png')
plt.show()

# === Univariate: 3-Month Outcomes ===
three_cols = ['out_3_sum_emp', 'out_3_sum_te', 'out_3_unemp', 'out_3_oth', 'out_3_unkn', 'out_3_null']
three_totals = df[three_cols].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=three_totals.values, y=three_totals.index, palette='magma')
plt.title('3-Month Outcomes Across All Sites')
plt.xlabel('Number of Clients')
plt.ylabel('Outcome Type')
for i, val in enumerate(three_totals.values):
    plt.text(val + 500, i, f"{val:,}", va='center')
plt.savefig('../figures/threemonths_outcomes_with_numbers.png')
plt.show()

# === Bivariate: Employment at Exit vs 3 Months ===
plt.figure(figsize=(7, 5))
sns.regplot(x='pct_emp_exit', y='pct_emp_3m', data=df, color='teal')
plt.title('Employment Rate: Exit vs 3 Months')
plt.xlabel('Employment Rate at Exit')
plt.ylabel('Employment Rate at 3 Months')
plt.savefig('../figures/mul.png')
plt.show()

corr = df[['pct_emp_exit', 'pct_emp_3m']].corr().iloc[0, 1]
print(f"Correlation between Exit and 3-Month Employment: {corr:.2f}")

# === Multivariate: Scatter Matrix ===
vars_for_matrix = ['num_assist', 'pct_emp_exit', 'pct_emp_3m', 'out_exit_unemp']
sm_df = df[vars_for_matrix].dropna()
plt.figure(figsize=(10, 10))
scatter_matrix(sm_df, alpha=0.7, diagonal='kde')
plt.suptitle("Multivariate Scatter Matrix", y=0.92)
plt.savefig('../figures/corr.png')
plt.show()

# === Logistic Regression ===
X = df[['out_exit_sum_emp', 'out_exit_unemp']].fillna(0)
y = (df['out_3_sum_emp'] > 0).astype(int)
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

y_pred = model.predict(X)
acc = accuracy_score(y, y_pred)
cm = confusion_matrix(y, y_pred)

print("Coefficients:", model.coef_)
print("Accuracy:", acc)
print("Confusion Matrix:\n", cm)

# Plot coefficients
coef_df = pd.DataFrame({
    'Variable': ['Employed at Exit', 'Unemployed at Exit'],
    'Coefficient': model.coef_[0]
})

plt.figure(figsize=(6, 4))
sns.barplot(data=coef_df, x='Variable', y='Coefficient', palette='coolwarm')
plt.title('Logistic Regression Coefficients')
plt.savefig('../figures/log.png')
plt.show()
