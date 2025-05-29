# E-Commerce Pricing Strategies and Their Impact on Sales

**Student:** Mustafa Mervan Temel, 32539  
**University:** Sabancı University  
**Course:** DSA210, Spring 2025  

---

## Motivation

In the highly competitive environment of e-commerce, pricing is not just a number—it is a strategic tool that directly influences customer behavior, sales volume, and ultimately, business profitability.

Having managed my own online store, **Popizone**, on Trendyol, I noticed fluctuations in daily sales due to even small pricing or promotional changes. This project aims to move beyond anecdotal evidence and provide a **data-driven analysis** of sales behavior influenced by pricing, promotions, and traffic.

---

## Project Goal

To quantify and analyze how changes in price, promotions, and visitor traffic influence the sales performance of the **Popizone** online store.

### Key Objectives:
- Determine the impact of pricing and promotions on sales.  
- Benchmark against competitors.  
- Develop predictive models for sales volume.

---

## Data Sources & Preprocessing

**Store data includes:**
- Daily Price (TL)  
- Sales Volume (units/day)  
- Visitor Traffic (views/day)  
- Promotion Status (Yes/No)  
- Competitor Price (TL)

**Preprocessing steps:**
1. Converted `Date` to datetime  
2. Filled missing values with column means  
3. Encoded `Promotion Status` (Yes → 1, No → 0)  
4. Rounded competitor prices to integers

---

## Exploratory Analysis & Visual Findings

### 1. Correlation Matrix  
![Correlation Matrix](Correlation%20Matrix-1.png)  
📌 **Visitor Traffic** and **Sales Volume** show strong correlation (r = 0.98).  
**Daily Price** has a moderate negative impact.

---

### 2. Price Change Over Time  
![Price Change Over Time](Price%20Change%20Over%20Time-1.png)  
📉 Price drops to TL 315–320 correlate with spikes in sales.

---

### 3. Sales Change Over Time  
![Sales Change Over Time](Sales%20Change%20Over%20Time-1.png)  
🟠 Sales increased following promotional periods or price drops.

---

### 4. Price vs Sales Volume  
![Price vs Sales Volume](Price%20vs%20Sales%20Volume.png)  
💡 Lower prices (≤ TL 330) result in higher sales (8–10 units/day).

---

### 5. Visitor Traffic vs Sales Volume  
![Visitor Traffic vs Sales Volume](Visitor%20Traffic%20vs%20Sales%20Volume.png)  
🚀 Sales strongly tied to traffic: every 10 new visitors ≈ 1 more sale.

---

### 6. Competitor Price vs Sales Volume  
![Competitor Price vs Sales Volume](Competitor%20Price%20vs%20Sales%20Volume.png)  
🔍 Competitor prices had minimal short-term impact on Popizone’s sales.

---

## Hypothesis Testing

**T-Test:**  
- H₀: Price changes do not affect sales  
- H₁: Lower prices increase sales  
- **T-statistic:** -2.84  
- **P-value:** 0.01 → ✅ **Reject H₀**

➡️ **Conclusion:** Lower prices **significantly** boost sales.

---

## Machine Learning Models

### 🔹 Model 1: Linear Regression – *Daily Price → Sales Volume*  
![Model 1](Model%201%20-%20ML.png)  
- **R² Score:** 0.35  
- **MAE:** ~1.9  
- Insight: Price alone only partially explains sales variation.

---

### 🔹 Model 2: Linear Regression – *Visitor Traffic → Sales Volume*  
![Model 2](Model%202%20-%20ML.png)  
- **R² Score:** 0.87  
- **MAE:** ~1.2  
- Insight: Visitor traffic is the **strongest single predictor**.

---

### 🔹 Model 3: Decision Tree – *Price + Traffic → Sales Volume*  
![Model 3](Model%203%20-%20ML.png)  
- **R² Score:** 0.91  
- **MAE:** ~0.8  
- Insight: Combined effects model improves predictive power.

---

### 🔹 Model 4: Decision Tree – *All Features (Price, Traffic, Promotion, Competitor Price)*  
![Model 4](Model%204%20-%20ML.png)  
- **R² Score:** 0.92  
- **MAE:** ~0.7  
- Insight: Promotional status improves accuracy, competitor pricing contributes minimally.

---

## Feature Importance – Decision Tree Model  
![Decision Tree](Decision%20Tree.png)  
**Top Influencers:**  
- 🥇 Visitor Traffic  
- 🥈 Daily Price  
- 🥉 Promotion Status  
- ❌ Competitor Price (negligible effect)

---

## Limitations & Future Work

### Limitations:
- Only 30 days of data  
- Manual tracking of competitor prices  
- No differentiation of ad vs organic traffic

### Future Enhancements:
- Collect data over several months  
- Add conversion rates & ad metrics  
- Use advanced models (Random Forest, XGBoost)  
- Automate data collection with scraping scripts

---

## Final Conclusion

- 📉 **Lower Prices → Higher Sales**  
- 📈 **Traffic = Strongest Driver**  
- 🛍️ **Promotions Help, But Impact Margins**  
- 📊 **Competitor Pricing: Low Short-Term Impact**  
- 🤖 **ML Models Reveal Actionable Sales Predictors**

This study empowered me to turn my business intuition into measurable insight. The combination of hands-on data analysis and machine learning has equipped me to make better pricing, promotion, and growth decisions for **Popizone**.

---
