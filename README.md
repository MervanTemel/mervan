# E-Commerce Pricing Strategies and Their Impact on Sales  

**Student:** Mustafa Mervan Temel  
**University:** Sabancı University  
**Course:** DSA210, Spring 2025  

---

## Hypotheses  

1. **Hypothesis 1:** Lower prices and promotional discounts significantly increase daily sales volume compared to regular pricing periods.  
2. **Hypothesis 2:** Visitor traffic has a stronger and more consistent impact on sales volume than pricing or promotions.  

---

## Contents  
- Motivation  
- Project Goal  
- Data Sources and Preprocessing  
- Data Analysis  
- Findings  
- Hypothesis Testing  
- Machine Learning Techniques  
- Limitations and Future Work  

---

## Motivation  

Pricing in e-commerce is one of the most crucial tools that directly influence customer purchasing decisions. Running my store **Popizone** on **Trendyol**, I noticed that even small price adjustments or promotional events could lead to significant differences in daily sales. However, to truly understand which strategies work best, a systematic, data-driven approach is essential. This project applies data science principles to analyze how pricing, promotions, and visitor traffic affect sales outcomes, enabling me to make informed decisions to optimize revenue and customer engagement.

---

## Project Goal  

To identify the most effective pricing strategies and understand how promotions and traffic volume impact sales in my Trendyol store **Popizone**. The goal is to find actionable insights that will guide future pricing, improve conversion rates, and enhance overall store performance.  

**Store Link:** [Popizone on Trendyol](https://www.trendyol.com/magaza/popizone-m-994801?sst=0)

---

## Data Sources and Preprocessing  

### Data Sources  
- **Popizone Store Data:**  
  - Daily Price (TL)  
  - Sales Volume (units/day)  
  - Visitor Traffic (views/day)  
  - Promotion Status (Yes/No)  

- **Competitor Pricing Data:**  
  - Collected manually from Etsy and Amazon for similar products.

### Preprocessing Steps  
1. Converted `Date` column to datetime format.  
2. Filled missing values in numeric columns with column means.  
3. Encoded `Promotion Status` as binary values (Yes = 1, No = 0).  
4. Rounded competitor prices for consistency in analysis.  

---

## Data Analysis Overview  

1. **Descriptive Statistics** for understanding the basic distribution of data.  
2. **Correlation Matrix** to explore relationships between key variables.  
3. **Time Series Trends** to visualize changes in price and sales over time.  
4. **Scatter Plots** to investigate direct effects between variables.  
5. **Elasticity Calculation** to measure price sensitivity.

---

## Findings  

### 1. Correlation Matrix  
This heatmap reveals the strength of relationships between key variables.  

![Correlation Matrix](./Correlation%20Matrix-1.png)  

- **Daily Price vs Sales Volume (r = –0.51):** Higher prices are moderately correlated with lower sales.  
- **Visitor Traffic vs Sales Volume (r = +0.98):** More visitors lead directly to more sales.  
- **Competitor Price vs Sales Volume (r ≈ 0):** Competitor prices have little effect.

---

### 2. Price Change Over Time  
This graph tracks the fluctuations in daily pricing.  

![Price Change Over Time](./Price%20Change%20Over%20Time-1.png)  

- Price ranged between **TL 315** and **TL 350**.  
- Lower prices aligned with higher sales peaks, especially around **TL 315**.

---

### 3. Sales Change Over Time  
Daily sales volume visualized over the same period.  

![Sales Change Over Time](./Sales%20Change%20Over%20Time-1.png)  

- Sales varied from **3** to **10 units/day**.  
- Higher sales days often coincided with promotional periods or price reductions.

---

### 4. Price vs Sales Volume  
A scatter plot showing the inverse relationship between price and sales.  

![Price vs Sales Volume](./Price%20vs%20Sales%20Volume.png)  

- Sales volume is highest when prices are **TL 315–330**.  
- As price exceeds **TL 340**, sales drop to **3–5 units/day**.

---

### 5. Visitor Traffic vs Sales Volume  
Illustrates the strong impact of visitor traffic.  

![Visitor Traffic vs Sales Volume](./Visitor%20Traffic%20vs%20Sales%20Volume.png)  

- Almost a perfect linear relationship: **+10 visitors ≈ +1 sale**.  
- Indicates that driving traffic is as important as pricing.

---

### 6. Competitor Price vs Sales Volume  
Explores whether competitor pricing influences sales.  

![Competitor Price vs Sales Volume](./Competitor%20Price%20vs%20Sales%20Volume.png)  

- No clear correlation found.  
- Suggests that internal pricing decisions matter more than external competitor actions.

---

## Hypothesis Testing  

### Hypothesis 1: Promotional Pricing Increases Sales  

- **T-Test:**  
  - **T-Statistic:** 2.45  
  - **P-Value:** 0.024  

**Conclusion:**  
Promotional pricing significantly boosts sales. The null hypothesis is rejected.

---

### Hypothesis 2: Traffic as a Strong Predictor  

- **Correlation:**  
  - **r = 0.98**, **p < 0.001**  

**Conclusion:**  
Visitor traffic is the strongest predictor of sales performance. More targeted advertising could yield high returns.

---

## Machine Learning Techniques  

### Multiple Linear Regression  

- **Dependent Variable:** Sales Volume  
- **Independent Variables:** Daily Price, Visitor Traffic, Promotion Status, Competitor Price  
- **R² Score:** 0.91  

**Insights:**  
- Visitor traffic has the highest influence, followed by price.  
- Promotions have a positive but lesser effect.  
- Competitor pricing is not significant.

---

### Price Elasticity of Demand  

- **Elasticity = –1.2**  
- **Interpretation:** Demand is elastic. Small price changes result in large variations in quantity sold.

---

## Limitations and Future Work  

### Limitations  
- **Short Data Period:** 30 days limits seasonal trend analysis.  
- **Manual Competitor Data:** Prone to human error.  
- **External Influences:** Not all sales factors (e.g., reviews, platform promotions) are included.

### Future Work  
- Extend data collection for a **longer duration**.  
- Use **web scraping** for more accurate competitor monitoring.  
- Incorporate **sentiment analysis** on customer feedback.  
- Implement **real-time A/B testing** for dynamic pricing.

---
