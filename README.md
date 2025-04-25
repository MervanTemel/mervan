E-Commerce Pricing Strategies and Their Impact on Sales
Student: Mustafa Mervan Temel
University: Sabancı University
Course: DSA210, Spring 2025

Hypotheses
Hypothesis 1: Lower prices and promotional discounts significantly increase the daily sales volume compared to regular pricing periods.

Hypothesis 2: Visitor traffic has a stronger and more consistent impact on sales volume than pricing or promotions.

Contents
Motivation

Project Goal

Data Sources and Preprocessing

Data Analysis

Findings

Hypothesis Testing

Machine Learning Techniques

Limitations and Future Work

Motivation
In a highly competitive e-commerce landscape, especially on platforms like Trendyol, success is closely tied to dynamic and responsive pricing strategies. As the founder of the Popizone store, I observed fluctuations in daily sales patterns that seemed correlated to price changes, discount events, and traffic volume. However, without a data-driven approach, it was difficult to confirm the magnitude or nature of these relationships. This project seeks to uncover actionable insights that could guide future pricing decisions, ensuring not only higher revenue but also better customer retention and strategic market positioning. By applying concepts learned in DSA210, I aim to transition from intuitive pricing tactics to scientifically-backed strategies that scale.

Project Goal
The main objective of this project is to rigorously analyze the relationship between pricing strategies and sales performance for products sold via my Trendyol store Popizone. Through detailed examination of price elasticity, promotional effectiveness, and traffic analysis, I intend to discover patterns that can be exploited to maximize revenue. Additionally, the project benchmarks internal pricing decisions against external competitor trends on platforms such as Etsy and Amazon, providing a holistic view of the competitive environment.

Store Link: Popizone on Trendyol

Data Sources and Preprocessing
Data Sources
Internal Popizone Store Data (Trendyol):

Daily Price (TL)

Daily Sales Volume (units sold)

Visitor Traffic (unique views per day)

Discount % (if applicable)

Promotion Status (Yes/No)

Competitor Pricing Data:

Collected manually from Etsy and Amazon over a 30-day period.

Focused on similar product categories for direct comparison.

Preprocessing
Date Formatting: Standardized all dates using pd.to_datetime.

Missing Values: Handled missing entries in traffic and competitor data by filling with column mean values.

Categorical Encoding: Promotion status encoded as binary for analysis (Yes=1, No=0).

Outlier Detection: Used IQR to detect and exclude anomalous traffic spikes likely due to Trendyol promotions not controlled by Popizone.

Normalization: Competitor prices rounded and normalized for clearer correlation analysis.

Data Analysis Overview
Descriptive Statistics: Evaluated mean, median, and standard deviation of price, traffic, and sales.

Correlation Matrix: Identified pairwise relationships between key variables.

Time Series Analysis: Visualized how price and sales evolved over the month.

Scatter Plots: Explored non-linear interactions between price, traffic, and sales.

Elasticity Measurement: Calculated price elasticity of demand to assess customer sensitivity.

Findings
1. Correlation Matrix

Daily Price vs Sales Volume (r = –0.51): Indicates a moderate negative correlation. Higher prices lead to reduced sales, confirming that Popizone’s market operates in a price-sensitive segment.

Visitor Traffic vs Sales Volume (r = +0.98): A very strong positive correlation, emphasizing that marketing efforts that drive traffic are highly effective in boosting sales.

Competitor Price vs Sales Volume (r ≈ 0.02): Shows negligible correlation, implying that short-term competitor pricing doesn’t significantly influence Popizone’s daily sales.

2. Price Change Over Time

Prices varied between TL 315 and TL 350 over the 30-day period.

Notable drops in price aligned with increased sales activity, particularly during a TL 315 promotional period.

Price remained stable for multiple days at TL 340, resulting in consistent but lower sales.

3. Sales Change Over Time

Sales peaked at 10 units/day during promotional pricing days.

Non-promotional days saw a steady average of 4–5 units/day.

The sharpest increase in sales followed a sudden price drop and coincided with increased traffic.

4. Price vs Sales Volume

Low Prices (≤ TL 330): Corresponded to 8–10 units/day.

Higher Prices (> TL 340): Limited sales to 3–5 units/day, reinforcing the idea of elastic demand in this market.

Clustered data points indicate that the optimal price range for maximum sales is around TL 315–330.

5. Visitor Traffic vs Sales Volume

Clear linear relationship: every 10 additional visitors yielded approximately 1 extra sale.

Outliers were identified where traffic increased but sales remained flat, likely due to higher prices during that period.

6. Competitor Price vs Sales Volume

No discernible pattern. Even when competitor prices dropped, Popizone sales remained unaffected.

Suggests that Popizone’s customers are more influenced by internal factors (pricing, promotions, traffic) than by external competitor actions.

Hypothesis Testing
Hypothesis 1: Price Reductions and Promotions Increase Sales
T-Test Results:

T-Statistic: 2.45

P-Value: 0.024

Conclusion: Reject the null hypothesis. Promotional pricing has a statistically significant impact on increasing daily sales.

Hypothesis 2: Visitor Traffic is the Strongest Predictor of Sales
Pearson Correlation:

r = 0.98, p < 0.001

Conclusion: Traffic volume is an extremely strong predictor of sales. Prioritizing traffic-driving strategies such as social media marketing and Trendyol ads would yield better returns.

Machine Learning Techniques
Multiple Linear Regression:

Dependent Variable: Sales Volume

Independent Variables: Daily Price, Visitor Traffic, Competitor Price, Promotion Status

R² Score: 0.91

Model Insight: Traffic had the highest coefficient, followed by price. Competitor price was not a significant variable.

Price Elasticity of Demand:

Elasticity = –1.2

Interpretation: Demand is elastic; small changes in price cause larger percentage changes in quantity sold.

Limitations and Future Work
Limitations
Data was collected over a 30-day period, limiting seasonal insights.

Competitor price tracking was manual, introducing possible inconsistencies.

The analysis excludes factors like customer reviews, product ratings, and platform-driven promotions.

Future Work
Extend data collection to 3–6 months for more robust trend analysis.

Automate competitor price tracking using web scraping tools like BeautifulSoup or Selenium.

Incorporate sentiment analysis from customer feedback.

Conduct A/B testing with different pricing models and monitor live results.
