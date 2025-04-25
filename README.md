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
**Store link:** [https://www.trendyol.com/magaza/popizone-m-994801?sst=0](https://www.trendyol.com/magaza/popizone-m-994801?sst=0)

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

## Data Analysis  
1. **Correlation Analysis** to quantify relationships.  
2. **Time Series Trends** for price and sales.  
3. **Scatter Plots** to explore pairwise effects.  
4. **Competitor Comparison** for benchmarking.

---

## Findings  

### 1. Correlation Matrix  
This heatmap shows correlations between key variables.  
![Correlation Matrix](./Correlation%20Matrix-1.png)  
- **Daily Price vs Sales Volume (r = –0.51):** Moderate negative correlation—higher prices generally reduce sales.  
- **Visitor Traffic vs Sales Volume (r = +0.98):** Very strong positive correlation—more visitors almost always mean more sales.  
- **Competitor Price has minimal correlation** to my store’s daily sales.

---

### 2. Price Change Over Time  
Tracks daily price fluctuations over the 30-day period.  
![Price Change Over Time](./Price%20Change%20Over%20Time-1.png)  
- Prices oscillated between **TL 250** and **TL 450**.  
- A notable price drop to **TL 250** corresponded with one of the highest sales days.

---

### 3. Sales Change Over Time  
Visualizes daily sales volume over the same period.  
![Sales Change Over Time](./Sales%20Change%20Over%20Time-1.png)  
- Sales ranged from **3** to **10** units per day.  
- Peaks often followed price reductions or promotion days.

---

### 4. Price vs Sales Volume  
A scatter plot illustrating the inverse relationship between price and sales.  
![Price vs Sales Volume](./Price%20vs%20Sales%20Volume.png)  
- **Low prices (≤ TL 330)** yield **8–10** units sold.  
- **High prices (≥ TL 350)** result in **3–5** units sold.

---

### 5. Visitor Traffic vs Sales Volume  
Shows the direct impact of traffic on sales.  
![Visitor Traffic vs Sales Volume](./Visitor%20Traffic%20vs%20Sales%20Volume.png)  
- Nearly linear trend: every **10 extra visitors** leads to roughly **1 additional sale**.

---

### 6. Competitor Price vs Sales Volume  
Examines whether competitor pricing affects my sales.  
![Competitor Price vs Sales Volume](./Competitor%20Price%20vs%20Sales%20Volume.png)  
- No clear pattern: competitor prices have **minimal short-term influence** on my store’s sales.

---
