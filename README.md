# E-Commerce Pricing Strategies and Their Impact on Sales

**Student:** Mustafa Mervan Temel, 32539  
**University:** Sabancı University  
**Course:** DSA210, Spring 2025  

---

## Project Overview

This project explores how pricing, visitor traffic, and promotional strategies affect sales volume in an e-commerce setting. The data was collected from my own online store, **Popizone**, operating on Trendyol. By combining domain experience and data science techniques, the goal is to evaluate the impact of various business decisions and develop predictive models to support future pricing strategies.

---

## Motivation

### Business Growth

- In e-commerce, small changes in pricing or promotion can lead to major shifts in sales.
- I wanted to quantify these effects using real business data from Popizone.

### Academic Development

- The project allowed me to apply core concepts from **DSA210**, such as correlation analysis, hypothesis testing, and machine learning.
- It served as a hands-on bridge between theoretical knowledge and real-life business optimization.

---

## Objectives

- Determine the correlation between pricing and sales performance.
- Evaluate the effect of visitor traffic and promotional activity.
- Identify key predictors of daily sales volume.
- Use regression and tree-based models to forecast sales.
- Compare results across different modeling techniques.

---

## Data Sources

- **Daily Price (TL):** Price of the product on a given day.
- **Sales Volume:** Number of units sold.
- **Visitor Traffic:** Number of visitors to the product page.
- **Promotion Status:** Whether the product was in a promotion (Yes/No).
- **Competitor Price:** Manually tracked competitor pricing.

---

## Analysis Plan

- Correlation analysis and statistical testing.
- Time-series visualization of prices and sales.
- Evaluation of promotional effects.
- Regression modeling (linear and tree-based).
- Feature importance analysis.

---

## Expected Outcomes

- Understand how different pricing strategies affect sales.
- Discover patterns between traffic and conversion.
- Determine the effectiveness of promotional events.
- Build models to support pricing decisions based on real data.

---

## Findings

### 1. Correlation Matrix  
![Correlation Matrix](Correlation%20Matrix-1.png)

- **Visitor Traffic** has a very strong positive correlation with sales volume (**r = 0.98**).
- **Daily Price** is moderately negatively correlated (**r = -0.51**).
- **Competitor Price** showed no meaningful correlation.

**Insight:** Visitor traffic is the most significant driver of sales. Lower prices are associated with higher sales.

---

### 2. Price Change Over Time  
![Price Change Over Time](Price%20Change%20Over%20Time-1.png)

**Insight:** Strategic discounts (e.g., dropping from TL 350 to TL 315) directly corresponded with an increase in units sold.

---

### 3. Sales Change Over Time  
![Sales Change Over Time](Sales%20Change%20Over%20Time-1.png)

**Insight:** Peaks in sales align with promotional days and lower price points.

---

### 4. Price vs Sales Volume  
![Price vs Sales Volume](Price%20vs%20Sales%20Volume.png)

**Insight:** There is a clear inverse relationship—sales decline as price increases.

---

### 5. Visitor Traffic vs Sales Volume  
![Visitor Traffic vs Sales Volume](Visitor%20Traffic%20vs%20Sales%20Volume.png)

**Insight:** This is a nearly linear relationship. For every 10 additional visitors, sales increased by roughly 1 unit.

---

### 6. Competitor Price vs Sales Volume  
![Competitor Price vs Sales Volume](Competitor%20Price%20vs%20Sales%20Volume.png)

**Insight:** Competitor price does not appear to impact Popizone’s short-term sales.

---

## Hypothesis Testing

### Hypothesis: Lower product prices increase sales volume.

- **Null Hypothesis (H₀):** Price changes have no effect on sales.
- **Alternative Hypothesis (H₁):** Lower prices lead to higher sales.

**T-Statistic:** –2.84  
**P-Value:** 0.01 ✅  
**Conclusion:** Reject H₀ → Lower prices significantly increase sales volume.

---

## Machine Learning Models

### Model 1: Linear Regression (Price → Sales Volume)  
![Model 1](Model%201%20-%20ML.png)

- **R²:** 0.35  
- **MAE:** 1.9  

**Interpretation:** Price has a moderate inverse relationship with sales, but other variables are needed for stronger predictions.

---

### Model 2: Linear Regression (Traffic → Sales Volume)  
![Model 2](Model%202%20-%20ML.png)

- **R²:** 0.87  
- **MAE:** 1.2  

**Interpretation:** Visitor traffic is a powerful standalone predictor of sales. The model captures 87% of variance.

---

### Model 3: Decision Tree (Price + Traffic → Sales Volume)  
![Model 3](Model%203%20-%20ML.png)

- **R²:** 0.91  
- **MAE:** 0.8  

**Interpretation:** Combining price and traffic improves performance. The tree model handles interactions between features better.

---

### Model 4: Decision Tree (All Features → Sales Volume)  
![Model 4](Model%204%20-%20ML.png)

- **R²:** 0.92  
- **MAE:** 0.7  

**Interpretation:** Adding promotion and competitor prices gives minimal gain. Most of the performance still comes from internal metrics.

---

## Feature Importance: Decision Tree  
![Decision Tree](Decision%20Tree.png)

**Top Predictors:**

1. **Visitor Traffic** — strongest driver of sales  
2. **Daily Price** — secondary impact  
3. **Promotion Status** — mild contribution  
4. **Competitor Price** — negligible impact

**Conclusion:** Internal store decisions outweigh external pricing competition in the short term.

---

## Comparison Table

| Model                      | R²    | MAE  |
|---------------------------|-------|------|
| Price Only (Linear)       | 0.35  | 1.9  |
| Traffic Only (Linear)     | 0.87  | 1.2  |
| Decision Tree (2 vars)    | 0.91  | 0.8  |
| Decision Tree (All vars)  | 0.92  | 0.7  |

---

## Limitations & Future Work

### Limitations:
- Only 30 days of data  
- Competitor price was manually collected  
- No data on advertising or conversion rates  
- Traffic sources (organic vs. ad) not differentiated

### Future Plans:
- Automate competitor price collection  
- Track ad spend and conversion metrics  
- Build ensemble models with longer-term data  
- Apply time-series forecasting techniques (e.g., ARIMA)

---

## Conclusion

- 📊 **Visitor traffic is the strongest sales driver**  
- 📉 **Lower prices result in significantly higher sales**  
- 🛍️ **Promotions help—but depend on timing and pricing**  
- ❌ **Competitor prices had no immediate effect**  
- 🧠 **Model 4 (Decision Tree - All Features) performed best (R² = 0.92)**

This project helped me combine real-world business data with academic tools from DSA210. I now have a data-backed approach to pricing and marketing in e-commerce.

---

## Appendix: Use of AI Assistance

This project was completed independently by myself. However, OpenAI’s ChatGPT (GPT-4) was used in the following areas to support the process:

- Assisted in improving grammar, sentence structure, and clarity of the README file.
- Provided guidance on GitHub usage, such as uploading files and embedding images.
- Supported interpretation of regression outputs and plotting in the Jupyter Notebook.

All content was reviewed and finalized by me to ensure originality and accuracy.

---
