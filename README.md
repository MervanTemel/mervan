# E-Commerce Pricing Strategies and Their Impact on Sales

**Student:** Mustafa Mervan Temel, 32539  
**University:** Sabancı University  
**Course:** DSA210, Spring 2025  

---

## Motivation  

In the highly competitive environment of e-commerce, pricing is not just a number—it is a strategic tool that directly influences customer behavior, sales volume, and ultimately, business profitability. Having managed my own online store, **Popizone**, on Trendyol, I have noticed significant fluctuations in daily sales corresponding to even slight adjustments in product prices and promotional campaigns. However, these observations were anecdotal, lacking a systematic, data-driven understanding of the dynamics at play.

This project is driven by my desire to move beyond intuition and leverage data science techniques to scientifically explore the relationship between pricing and sales performance. My aim is to uncover actionable insights that can enhance my decision-making process when setting prices, launching promotions, and responding to competitor strategies.

By collecting and analyzing data from my store’s daily operations—spanning prices, sales volumes, visitor traffic, and competitor prices—I aim to identify patterns and correlations that are not immediately obvious. Furthermore, I want to benchmark my pricing strategies against major competitors on platform like **Trendyol**, understanding how external market trends might influence my performance.

This project aligns with both my business goals and academic interests. It provides an opportunity to apply data analysis, statistical testing, and machine learning methods learned in **DSA210**, not only to deepen my technical skills but also to create tangible value for my store. In the long term, this study will serve as a foundation for more advanced pricing models and will support more efficient inventory management and promotional planning.

---

## Project Goal  

The primary objective of this project is to develop a comprehensive understanding of how pricing strategies affect customer purchasing behavior and overall sales performance in the context of my **Popizone** store on Trendyol.

### Specific Goals:

1. **Quantify the Impact of Pricing:**  
   - Analyze how changes in daily prices correlate with variations in sales volume.
   - Identify the price points that maximize conversion rates and profitability.

2. **Evaluate Promotional Effectiveness:**  
   - Assess whether promotional periods (discounts, campaigns) significantly boost sales.
   - Determine the balance between increased sales volume and potential loss in profit margins due to discounts.

3. **Understand Traffic Dynamics:**  
   - Investigate how visitor traffic interacts with pricing to influence sales.
   - Analyze whether high traffic periods correlate with high conversion rates or if pricing adjustments are necessary to capitalize on traffic.

4. **Benchmark Against Competitors:**  
   - Compare my pricing data with that of competitors on **Etsy** and **Amazon**.
   - Evaluate whether being competitively priced influences my own sales.

5. **Develop Predictive Insights:**  
   - Use statistical models to predict sales volume based on price, traffic, and promotions.
   - Explore the concept of **price elasticity** to understand customer sensitivity to price changes.

By achieving these goals, I aim to formulate an optimized pricing strategy that balances competitiveness, profitability, and customer acquisition, ultimately driving sustainable growth for **Popizone**.

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

### Hypothesis: Price reductions significantly increase sales.

- **Null Hypothesis (H₀):** Price changes have no effect on sales volume.  
- **Alternative Hypothesis (H₁):** Lower prices lead to significantly higher sales volume.

- **T-Statistic:** –2.84  
- **P-Value:** 0.01  
- **Conclusion:** Reject H₀. Sales volumes are significantly higher when prices are reduced, confirming a price-sensitive customer base.

---

## Machine Learning (Optional Exploration)  
A simple **Linear Regression Model** was used to predict sales based on price and visitor traffic.

- **R² Score:** 0.88  
- **Key Insight:** Visitor traffic explains most of the variance in sales, with price being a critical but secondary variable.

---

## Limitations & Future Work

**Limitations:**  
- Small dataset limited to 30 days.  
- Competitor pricing manually tracked and limited in scope.  
- Traffic sources (organic vs. ads) not differentiated.

**Future Work:**  
- Extend data collection to 3-6 months for seasonal analysis.  
- Automate competitor tracking using web scraping tools.  
- Incorporate advertising spend and conversion rates for more holistic insights.

---

## Conclusion

- **Optimal Price Range:** TL 315–330 achieves highest daily sales.  
- **Promotional Strategies:** Discounts and campaigns significantly boost sales, but must be evaluated for profit margins.  
- **Traffic Dependency:** Sales are highly dependent on visitor traffic; marketing efforts must align with pricing strategies.  
- **Competitor Influence:** Minimal in the short term; internal optimizations are more impactful.

This project has provided me with actionable insights into how pricing directly influences customer behavior, sales, and revenue in an e-commerce setting. Leveraging data-driven strategies, I can now refine my pricing models to maximize the success of **Popizone**.
