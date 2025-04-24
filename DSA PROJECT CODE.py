import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind
import statsmodels.api as sm

# 1. Load Data
file_path = "ecommerce_30day_data.xlsx" 
df = pd.read_excel(file_path)

# 2. Data Cleaning
# Convert date format
df['Date'] = pd.to_datetime(df['Date'])

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# (If any missing values, fill with mean - none expected in this case)
# df.fillna(df.mean(), inplace=True)

# 3. Correlation Analysis
correlation_matrix = df[['Daily Price', 'Sales Volume', 'Visitor Traffic', 'Competitor Price']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# 4. Visualizations

# Daily Price vs Sales Volume Scatter
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Daily Price', y='Sales Volume', data=df)
plt.title('Price vs Sales Volume')
plt.xlabel('Daily Price (TL)')
plt.ylabel('Sales Volume')
plt.show()

# Visitor Traffic vs Sales Volume Scatter
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Visitor Traffic', y='Sales Volume', data=df)
plt.title('Visitor Traffic vs Sales Volume')
plt.xlabel('Visitor Traffic')
plt.ylabel('Sales Volume')
plt.show()

# Price Over Time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Daily Price'], marker='o', label='Price (TL)')
plt.title('Price Change Over Time')
plt.xlabel('Date')
plt.ylabel('Price (TL)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales Over Time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales Volume'], marker='s', label='Sales Volume', color='orange')
plt.title('Sales Change Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Regression Analysis
X = df['Daily Price']
y = df['Sales Volume']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# 6. Hypothesis Testing - Promotion Effect
promo_sales = df[df['Promotion Status'] == 'Yes']['Sales Volume']
no_promo_sales = df[df['Promotion Status'] == 'No']['Sales Volume']
t_stat, p_val = ttest_ind(promo_sales, no_promo_sales)
print("T-Statistic:", t_stat)
print("P-Value:", p_val)
if p_val < 0.05:
    print("Significant difference in sales due to promotion.")
else:
    print("No significant difference in sales due to promotion.")

# 7. Additional Visualization: Competitor Price vs Sales Volume
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Competitor Price', y='Sales Volume', data=df)
plt.title('Competitor Price vs Sales Volume')
plt.xlabel('Competitor Price (TL)')
plt.ylabel('Sales Volume')
plt.show()

import os
print("Current Working Directory:", os.getcwd())
