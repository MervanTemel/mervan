# E-Commerce Pricing Strategies and Their Impact on Sales

**Student:** Mustafa Mervan Temel  
**University:** Sabancı University  
**Course:** DSA210, Spring 2025  

---

## Motivation  
Pricing is a critical lever in e-commerce success. As the owner of **Popizone** on Trendyol, I observed that small price adjustments and promotional campaigns had a significant impact on daily sales. This project applies data science techniques to systematically uncover how pricing and promotions drive customer behavior, enabling data-driven decisions to optimize revenue and competitiveness.

---

## Project Goal  
Identify the optimal pricing range and promotional tactics that maximize sales volume and conversion rates for my **Popizone** store on Trendyol.  
Store link: [Popizone Store on Trendyol](https://www.trendyol.com/magaza/popizone-m-994801?sst=0)

---

## Data Sources and Preprocessing  
- **Popizone Store Data:**  
  - Daily Price (TL)  
  - Sales Volume (units/day)  
  - Visitor Traffic (views/day)  
  - Promotion Status (Yes/No)  

- **Competitor Pricing:**  
  - Daily competitor prices manually collected from Etsy, Amazon, and similar platforms.

**Preprocessing Steps:**  
1. Converted `Date` to datetime.  
2. Filled missing numeric values with column mean.  
3. Standardized `Promotion Status` to Yes/No.  
4. Rounded competitor prices to integers.

---

## Data Analysis Plan  
1. **Correlation Analysis** to quantify relationships.  
2. **Time Series Trends** for price and sales.  
3. **Scatter Plots** to explore pairwise effects.  
4. **Competitor Comparison** for benchmarking.  
5. **Hypothesis Testing** on pricing effects.

---

## Findings & Visual Analysis

### 1. Correlation Matrix  
![Correlation Matrix](./Correlation%20Matrix-1.png)

- **Null Hypothesis (H₀):** No correlation between pricing, visitor traffic, and sales volume.  
- **Alternative Hypothesis (H₁):** Significant correlation exists.

**Results:**  
- **Daily Price vs Sales Volume:** r = –0.51  
- **Visitor Traffic vs Sales Volume:** r = +0.98  
- **Competitor Price vs Sales Volume:** r ≈ 0

**Conclusion:**  
Moderate negative correlation between price and sales, strong positive correlation between traffic and sales. Competitor pricing had negligible impact.

---

### 2. Price Change Over Time  
![Price Change Over Time](./Price%20Change%20Over%20Time-1.png)

- **Null Hypothesis (H₀):** Price changes do not affect sales trends.  
- **Alternative Hypothesis (H₁):** Price fluctuations impact sales.

**Results:**  
- Prices ranged between **TL 315** and **TL 350**.  
- Lowest prices corresponded with high sales.

**Conclusion:**  
Strategic price drops to TL 315 boosted sales significantly.

---

### 3. Sales Change Over Time  
![Sales Change Over Time](./Sales%20Change%20Over%20Time-1.png)

- **Null Hypothesis (H₀):** Sales remain constant over time.  
- **Alternative Hypothesis (H₁):** Sales vary with time due to pricing/promotions.

**Results:**  
- Daily sales ranged from **3** to **10 units**.  
- Sales peaked after price drops and during promotions.

**Conclusion:**  
Sales trends are directly tied to pricing and promotional events.

---

### 4. Price vs Sales Volume  
![Price vs Sales Volume](./Price%20vs%20Sales%20Volume.png)

- **Null Hypothesis (H₀):** Price has no effect on sales volume.  
- **Alternative Hypothesis (H₁):** Lower prices lead to higher sales.

**Results:**  
- **TL ≤ 330:** **8–10 units/day** sold.  
- **TL ≥ 350:** **3–5 units/day** sold.

**Conclusion:**  
There is an inverse relationship; lower prices result in significantly higher sales volumes.

---

### 5. Visitor Traffic vs Sales Volume  
![Visitor Traffic vs Sales Volume](./Visitor%20Traffic%20vs%20Sales%20Volume.png)

- **Null Hypothesis (H₀):** Visitor traffic has no impact on sales.  
- **Alternative Hypothesis (H₁):** Higher traffic leads to more sales.

**Results:**  
- r = 0.98  
- Every **10 additional visitors** resulted in **~1 extra sale**.

**Conclusion:**  
Traffic volume is the strongest predictor of sales.

---

### 6. Competitor Price vs Sales Volume  
![Competitor Price vs Sales Volume](./Competitor%20Price%20vs%20Sales%20Volume.png)

- **Null Hypothesis (H₀):** Competitor prices influence sales.  
- **Alternative Hypothesis (H₁):** No significant influence.

**Results:**  
- No observable pattern.  
- Sales unaffected by external pricing.

**Conclusion:**  
Short-term sales are independent of competitor pricing.

---

## Hypothesis Testing

### Hypothesis 1:  
**Null Hypothesis (H₀):** Price changes do not significantly affect sales.  
**Alternative Hypothesis (H₁):** Lower prices significantly increase sales.

- **T-Statistic:** –2.84  
- **P-Value:** 0.01  
- **Conclusion:** Reject H₀. Price reductions have a significant effect on sales growth.

---

## Machine Learning (Optional Exploration)  
Using **Linear Regression**, sales were predicted based on price and traffic.

- **R² Score:** 0.88  
- **Key Insight:** Traffic explains the majority of variance in sales, with price having a secondary effect.

---

## Limitations & Future Work

**Limitations:**  
- Small sample size (30 days).  
- Competitor data was manually collected.  
- Visitor traffic sources not differentiated.

**Future Work:**  
- Expand dataset over 3-6 months.  
- Automate competitor price tracking.  
- Analyze multi-product pricing strategies.

---

## Conclusion

- **Optimal Price Range:** TL 315–330 for highest sales.  
- **Discount Effects:** Promotions lead to immediate sales boosts but require careful profit analysis.  
- **Traffic Sensitivity:** Increasing visitors directly increases sales; focus on marketing.  
- **Competitor Prices:** Minimal short-term impact; focus on internal optimizations.

---

This project provided valuable insights into how dynamic pricing and marketing strategies directly affect e-commerce performance for my **Popizone** store.
