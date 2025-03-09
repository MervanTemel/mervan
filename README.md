# E-Commerce Pricing Strategies and Their Impact on Sales  

## **Project Overview**  

Over the next three months, I will analyze how different pricing strategies impact the sales performance of my e-commerce products. By tracking factors like daily product prices, discounts, promotions, visitor traffic, and sales volume, I aim to uncover the optimal pricing strategies that drive the highest revenue and conversion rates.  

Using data visualization and statistical tools, I will explore trends, correlations, and the effects of price fluctuations on customer purchasing behavior. Additionally, I will gather pricing data from e-commerce platforms like **Etsy, Amazon, and other competitor marketplaces** to benchmark my pricing strategies against industry trends.  

Ultimately, this project aims to provide **data-driven insights to optimize pricing strategies and maximize profitability**.  

---

## **Objectives**  

1. **Understand Pricing Effects**  
   - Analyze the relationship between price changes, discounts, and e-commerce sales.  

2. **Identify Key Pricing Strategies**  
   - Determine which pricing models drive the most sales and optimize revenue.  

3. **Benchmark Against Competitors**  
   - Compare my pricing with similar products on **Etsy, Amazon, and other platforms** to identify trends and competitive advantages.  

4. **Data-Driven Decision Making**  
   - Use insights from data analysis to refine pricing strategies for long-term growth.  

5. **Apply Data Science Skills**  
   - Implement statistical and visualization techniques learned in my **DSA 210** course in a real-world business context.  

---

## **Motivation**  

This project brings together two of my interests: **e-commerce and data science**. Here’s why it matters:  

- **Business Optimization**: Understanding how pricing affects sales will help me make more strategic decisions in my e-commerce business.  
- **Scientific Approach**: Rather than guessing the best prices, I want to rely on data and analytics to drive pricing strategies.  
- **Competitive Analysis**: By benchmarking my prices against those on **Etsy, Amazon, and similar platforms**, I can understand market trends and set the best price points.  
- **Long-Term Impact**: The findings will not only optimize my pricing strategies now but will also help in future product launches and e-commerce growth.  

---

## **Dataset & Data Sources**  

The dataset for this project consists of **daily records** over three months. I will track the following variables:  

- **Date**: The specific day of the record  
- **Product Name**: The item being tracked  
- **Daily Price**: The listed product price (in local currency)  
- **Sales Volume**: The number of units sold per day  
- **Discount Percentage**: Any applied discount percentage (%)  
- **Visitor Traffic**: The number of visitors viewing the product page  
- **Promotion Status**: Whether the product was part of a campaign (Yes/No)  
- **Competitor Pricing**: Daily prices of similar products on **Etsy, Amazon, and competitor websites**  

### **Data Sources**  

- **Etsy & Amazon Product Listings**: Pricing trends for similar products.  
- **Google Shopping & Price Comparison Tools**: Analysis of price fluctuations.  
- **Google Trends & Marketplace Insights**: Identifying seasonal trends.  
- **Own Store Data (Etsy, Trendyol, Shopify, etc.)**: Daily sales and visitor data.  
- **Web Scraping (BeautifulSoup / Selenium)**: To extract competitor pricing data when needed.  

---

## **Tools and Technologies**  

- **Python**: For data cleaning, processing, and analysis  
- **Pandas**: To manipulate and preprocess data  
- **Matplotlib & Seaborn**: For visualizing trends, correlations, and pricing effects  
- **SciPy & Statsmodels**: For hypothesis testing and regression analysis  
- **Excel / Google Sheets**: For initial data collection and tracking  
- **Web Scraping Tools (BeautifulSoup / Selenium)**: Extract competitor pricing data  
- **Google Trends API**: Analyze market demand and seasonal pricing trends  

---

## **Analysis Plan**  

### **1. Data Collection & Preprocessing**  
- Import daily sales and pricing data into a Pandas DataFrame.  
- Gather competitor pricing data from **Etsy, Amazon, and price tracking tools**.  
- Handle missing values, outliers, and ensure data consistency.  

### **2. Visualization & Initial Insights**  
- **Time Series Analysis**: Analyze sales trends over time.  
- **Scatter Plots**: Explore relationships between price and sales volume.  
- **Heatmaps**: Identify correlations between discounts, promotions, and visitor traffic.  
- **Competitor Price Comparison**: Compare my product prices with similar listings on **Etsy & Amazon**.  

### **3. Hypothesis Testing**  
- **H₀ (Null Hypothesis):** Price changes have no significant effect on sales volume.  
- **Hₐ (Alternative Hypothesis):** Price changes significantly impact sales performance.  
- Conduct **t-tests** or **ANOVA** to compare sales performance under different pricing conditions.  

### **4. Regression & Price Elasticity Analysis**  
- Use regression models to predict how price fluctuations affect sales.  
- Calculate **price elasticity of demand (PED)** to measure how sensitive customers are to price changes:  

  \[
  \text{Price Elasticity} = \frac{\%\text{ Change in Sales}}{\%\text{ Change in Price}}
  \]  

  - If **PED > 1**, demand is elastic (price-sensitive).  
  - If **PED < 1**, demand is inelastic (price changes have little effect).  

### **5. Trend & Campaign Analysis**  
- Compare sales patterns before, during, and after discount campaigns.  
- Investigate whether discounts attract more visitors but reduce overall profitability.  
- Examine the impact of **seasonal trends from Google Trends & competitor promotions on pricing strategies**.  

---

## **Example Analysis**  

1. **Scatter Plot Analysis**  
   - Relationship between price and sales volume.  
   - If a downward trend is observed, it may indicate a strong negative correlation between price increases and demand.  

2. **Competitor Pricing Comparison**  
   - I will compare my pricing with competitor products on **Etsy & Amazon** to determine whether I am **overpriced, underpriced, or competitive**.  

3. **Discount vs. Non-Discount Sales Performance**  
   - I will analyze whether discounted products drive higher total revenue or just short-term sales spikes.  

---

## **Conclusion**  

By the end of this project, I aim to answer the following questions:  

1. What is the **optimal price range** for maximizing sales and revenue?  
2. Do **discounts always lead to higher profits**, or do they just attract short-term sales spikes?  
3. How **sensitive are customers to price changes** (elastic vs. inelastic demand)?  
4. How does my **pricing compare to competitors on Etsy & Amazon**?  
5. What are the **best pricing strategies for different types of products**?  

This project will provide **actionable pricing insights**, leveraging **data from my own store, Etsy, Amazon, and market trends** to improve profitability and optimize pricing strategies.  



