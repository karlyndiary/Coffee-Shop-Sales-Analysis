# Coffee Shop Sales Analysis

![Coffee Sales Dashboard](https://github.com/user-attachments/assets/c9189338-17b1-46e2-9b2b-e27389545ab5)

# Table of Contents
* [Project Background](#project-background)
* [Data Structure](#data-structure)
* [Executive Summary](#executive-summary)
* [Recommendations](#recommendations)

# Project Background 
Maven Roasters is a fictitious coffee shop operating across three locations in New York City. The dataset includes transaction records, timestamps, location details, and product-level information. This project aims to analyze sales performance and customer behavior by examining key metrics such as transaction trends, product performance, and customer order patterns. Through the development of interactive dashboards, the project will provide valuable insights to optimize sales strategies, improve operational efficiency, and enhance customer satisfaction across Maven Roasters' locations.

Insights and recommendations are provided on the following key areas : 

- **Total Revenue, Orders, AOV, Peak Location**: A comprehensive evaluation of historical sales data, focusing on key metrics such as Total Revenue, Order Volume, Average Order Value (AOV), and the identification of peak sales locations.

- **Sales by Month and Location**: A thorough analysis of sales performance across various months and locations, identifying trends and variations.

- **Popular Products by Revenue**: A detailed analysis of products, assessing their contribution to overall revenue and identifying the top-performing products.

- **Popular Category and AOV by Category**: An evaluation of the most popular product categories based on order count, alongside an analysis of Average Order Value (AOV) for each category.

- **Peak Hour and Day**: An analysis to identify the hours and days with the highest revenue, providing insights for optimizing operations during peak business periods.

- **Order Distribution by Coffee Type**: An analysis of the distribution of orders across different coffee types, ranking them based on sales count to highlight customer preferences.

Detailed Resources: 

- The Pre-Processing process utilized can be found [here](https://github.com/karlyndiary/Coffee-Shop-Sales-Analysis/blob/main/EDA.ipynb). 
- An interactive Streamlit dashboard can be viewed [here](https://coffee-shop-sales-analysis.streamlit.app/).

# Data Structure

Coffee shop's database structure as seen below consists of one table: sales with 149,115 records.

# Executive Summary 

### Overview of Findings 

Total revenue of $698K was generated from 149K orders, with June being the peak month at $166K. Hell's Kitchen led all locations with $236K in revenue, while Barista Espresso topped the product list with $91K in sales. Coffee Beans showed the highest AOV at $22, and Coffee emerged as the most popular category. Sales peak at 10 AM, with steady performance across all weekdays and Gourmet Brewed Coffee leading in popularity.

Below is the overview page from the Streamlit dashboard and more examples are included throughout the report. The interactive dashboard can be viewed [here](https://coffee-shop-sales-analysis.streamlit.app/).

### Sales Dashboard
- **Total Revenue:** The total revenue is $698K, generated from 149K orders, with an Average Order Value (AOV) of $4.69.

- **Revenue by Month and Location:** June recorded the highest monthly revenue at $166K, likely driven by seasonal preferences, as the summer months typically see increased foot traffic. In contrast, January, being colder, had lower revenue. February generated $76K in revenue. Performance across all three locations has been consistent, with Hell's Kitchen leading as the top-performing location, generating a total of $236K in revenue.

- **Top Products by Revenue:** Barista Espresso is the top-performing product, contributing $91K, followed by Brewed Chai Tea at $77K and Hot Chocolate at $72K. The lowest-performing product in the top 10 is Drip Coffee, generating $31K.

- **Average Order Value by Product:** Coffee Beans lead with the highest AOV at $22, followed by Coffee at $4, Packaged and Drinking Chocolate at $9 and $6 respectively, and Bakery items at $3.

- **Popular Product Categories:** Coffee is the most popular category, with $58K in sales, followed by Tea at $45K and Bakery at $22K. The lowest-performing categories include Coffee Beans, Loose Tea, Branded Chocolate, and Packaged Chocolate, with sales ranging from $1,753 to $487.

- **Peak Hour and Day:** The peak hour for sales is 10 AM, with 18K orders, while the lowest hour is 8 PM, with only 603 orders. There is no clear peak day, as sales are consistent across all days of the week, with each day averaging 21K orders.

- **Coffee Type Performance:** Gourmet Brewed Coffee is the most popular coffee type, with 16K orders (29%), while Premium Brewed Coffee is the least popular, with 8K orders (14%).

# Recommendations

Based on the uncovered insights, the following recommendations have been provided : 

- **Target High-Value Products:** Coffee Beans, being the top-performing product, can benefit from a seasonal "Buy One Get One Free" offer. This would encourage bulk purchases, especially during colder months when customers are more likely to brew coffee at home. Introducing this deal a month in advance would help maximize sales.

- **Boost Sales During Slow Months:** January and February are typically lower-earning months. To counter this, implement seasonal offers such as reward cards or a complimentary drink of choice on customers' birthdays. This strategy can help increase customer engagement, boost sign-ups, and drive revenue during the quieter winter period.

- **Optimize Operating Hours and Product Categories:** Since 8PM is the lowest-performing hour, introducing end-of-day deals with attractive discounts can help drive sales and engage customers. Additionally, consider rotating product categories or swapping underperforming ones with new offerings to generate fresh interest and appeal.

- **Customer Feedback for Continuous Improvement:** At the end of each season, send out surveys to gather customer feedback on service quality, product satisfaction, and overall experience. This valuable insight can help fine-tune offerings and improve the overall business performance.
