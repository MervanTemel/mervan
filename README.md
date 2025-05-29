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
- Determine the impact of pricing and promotions on sales  
- Benchmark against competitors  
- Develop predictive models for sales volume  

---

## Data Sources & Preprocessing

- **Daily Price (TL)**  
- **Sales Volume (units/day)**  
- **Visitor Traffic (views/day)**  
- **Promotion Status (Yes/No)**  
- **Competitor Price (TL)**

### Preprocessing Steps:
1. Converted `Date` to datetime  
2. Filled missing values with column means  
3. Encoded `Promotion Status` (Yes → 1, No → 0)  
4. Rounded competitor prices to integers  

---

## Exploratory Analysis & Findings

### 1. Correlation Matrix  
![Correlation Matrix](Correlation%20Matrix-1.png)  
**Visitor traffic** has a very strong positive correlation with sales (r = 0.98), while price has a moderate negative impact (r = -0.51).  
Competitor price appears uncorrelated with sales in this short-term dataset.

---

### 2. Price Change Over Time  
![Price Change Over Time](Price%20Change%20Over%20Time-1.png)  
As price dropped around day 15, a surge in sales occurred. This confirms customer **price sensitivity**, particularly near TL 315–320.

---

### 3. Sales Change Over Time  
![Sales Change Over Time](Sales%20Change%20Over%20Time-1.png)  
Promotional periods and lower price ranges correlate with spikes in sales volume. Sales were highest when discounts were active.

---

### 4. Price vs Sales Volume  
![Price vs Sales Volume](Price%20vs%20Sales%20Volume.png)  
Sales volume decreases as prices rise. Highest volumes (8–10 units/day) were seen at TL ≤ 330.

---

### 5. Visitor Traffic vs Sales Volume  
![Visitor Traffic vs Sales Volume](Visitor%20Traffic%20vs%20Sales%20Volume.png)  
This plot confirms the **direct and strong linear relationship** between store visits and sales.  

> Every 10 additional visitors yield approximately 1 extra sale.

---

### 6. Competitor Price vs Sales Volume  
![Competitor Price vs Sales Volume](Competitor%20Price%20vs%20Sales%20Volume.png)  
Competitor pricing appears to have **no short-term impact** on daily sales. Customer decisions were likely more influenced by internal store factors.

---

## Hypothesis Testing

**Null Hypothesis (H₀):** Price changes have no effect on sales volume  
**Alternative Hypothesis (H₁):** Lower prices lead to higher sales

- **T-statistic:** –2.84  
- **P-value:** 0.01  

✅ **Result:** Reject H₀ → Lower prices **significantly** increase sales

---

## Machine Learning Models

### 🔹 Model 1: Linear Regression (Daily Price → Sales Volume)  
![Model 1](Model%201%20-%20ML.png)  
- **R² Score:** 0.35  
- **MAE:** ~1.9  

📌 **Interpretation:** Price alone is a weak predictor. The model captures the general trend but has high residual error, suggesting that **price should not be modeled in isolation**.

---

### 🔹 Model 2: Linear Regression (Visitor Traffic → Sales Volume)  
![Model 2](Model%202%20-%20ML.png)  
- **R² Score:** 0.87  
- **MAE:** ~1.2  

📌 **Interpretation:** This model demonstrates that **traffic volume is a reliable and strong predictor** of sales. High R² indicates that most variance in sales can be explained by traffic.

---

### 🔹 Model 3: Decision Tree (Price + Traffic → Sales Volume)  
![Model 3](Model%203%20-%20ML.png)  
- **R² Score:** 0.91  
- **MAE:** ~0.8  

📌 **Interpretation:** A decision tree using both price and traffic captures **nonlinear interactions** better than linear models. This model performs well and reduces error significantly.

---

### 🔹 Model 4: Decision Tree (All Features)  
![Model 4](Model%204%20-%20ML.png)  
- **R² Score:** 0.92  
- **MAE:** ~0.7  

📌 **Interpretation:** Incorporating all features—including promotion and competitor prices—slightly improves accuracy. However, **competitor pricing has minimal importance**.

---

## Feature Importance – Decision Tree Model  
![Decision Tree](Decision%20Tree.png)

### Ranked Importance:
1. **Visitor Traffic** – Most critical variable  
2. **Daily Price** – High impact  
3. **Promotion Status** – Moderate effect  
4. **Competitor Price** – Negligible contribution  

🧠 **Conclusion:** Internal store factors (traffic, pricing) drive performance more than external competitor behavior.

---

## Limitations & Future Work

### Limitations:
- Only 30 days of data  
- Manual competitor price tracking  
- No distinction between ad and organic traffic  
- Limited generalization power of short-term models

### Future Enhancements:
- Extend dataset over multiple months for seasonality analysis  
- Use advanced models like Random Forest or XGBoost  
- Automate data extraction and tracking tools  
- Integrate conversion rate and advertising spend metrics

---

## Final Conclusion

- 📉 **Lower Prices → Higher Sales**  
- 📈 **Traffic = Strongest Predictor**  
- 🛍️ **Promotions Help, But Need Margin Control**  
- 🤖 **Decision Tree Model (Model 4) performs best (R² = 0.92)**  
- ❌ **Competitor Prices = Little Immediate Impact**

This study enabled me to transform personal business intuition into measurable, actionable insight. With statistical tools and machine learning, I developed a scalable approach to pricing optimization for **Popizone**.

---

## Appendix: Use of AI Assistance

This project was completed independently by myself. However, OpenAI’s ChatGPT (GPT-4) was used in the following areas to support the process:

- ChatGPT assisted in improving the grammar, sentence structure, and clarity of the README file. All written content ideas and interpretations were originally created by me and verified with AI assistance.

- Since I didn't know how to use GitHub at first, guidance was received on:
  - How to upload files  
  - Embed images into the README  
  - Structure the repository content clearly

- During the preparation of the Jupyter Notebook, ChatGPT also helped with:
  - Data visualization  
  - Interpreting regression and decision tree outputs  
  - Summarizing findings into coherent explanations

All AI-generated suggestions were critically reviewed, revised, and finalized to ensure originality and academic integrity.

---
