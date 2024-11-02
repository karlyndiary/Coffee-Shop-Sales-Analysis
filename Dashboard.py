import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

st.set_page_config(
    page_title="Coffee Shop Sales Dashboard",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Streamlit application
st.title('☕ Coffee Shop Sales Dashboard')

df = pd.read_csv('cleaned_coffee_sales_dataset.csv')

# Display each KPI in a separate column for better layout
col1, col2, col3, col4 = st.columns(4)

# Total Sales Revenue
total_revenue = df['sales'].sum()
col1.metric("Total Sales Revenue", f"${total_revenue:,.2f}")

# Total Orders
total_orders = df['id'].nunique()
col2.metric("Total Orders", f"{total_orders:,}")

# Average Order Value (AOV)
aov = total_revenue/total_orders
col3.metric("Average Order Value (AOV)", f"${aov:.2f}")

# Peak Sales Location
peak_sales_location = df.groupby('location')['sales'].sum().idxmax()
peak_sales_location_revenue = df.groupby('location')['sales'].sum().max()
col4.metric("Peak Sales Location", f"{peak_sales_location}", f"${peak_sales_location_revenue:,.2f}")

# Sales by Month
# Sum of sales for each month
revenue = df.groupby('month')['sales'].sum().reset_index()

# Specify the order of months
month_order = ['January', 'February', 'March', 'April', 'May', 'June']

# Convert the month column to a categorical type with the specified order
revenue['month'] = pd.Categorical(revenue['month'], categories=month_order, ordered=True)

# Sort by month to ensure it appears in the correct order
revenue = revenue.sort_values('month')

fig1 = px.bar(
    revenue,
    x='month',
    y='sales',
    title='Sales by Month',
    labels={'sales': 'Sales', 'month': 'Month'},
    color='month',
)

# Remove the legend
fig1.update_layout(showlegend=False)

# Sum of sales for each location
location_revenue = df.groupby('location')['sales'].sum().reset_index()

# Sales by Location
fig2 = px.pie(
    location_revenue,
    names='location',
    values='sales',
    title='Sales by Location',
    labels={'sales': 'Sales', 'location': 'Location'},
    color='location',
)

# Modify the pie chart to make it a donut chart
fig2.update_traces(hole=0.4)

# Sort the DataFrame by sales in descending order and select the top 10 products
product_revenue = df.groupby('product')['sales'].sum().reset_index()
top_10_products = product_revenue.sort_values('sales', ascending = False)[0:10]

# Top 10 Products by Revenue
fig3 = px.bar(
    top_10_products,
    x='sales',
    y='product',
    title='Top 10 Products by Revenue',
    labels={'product': 'Product', 'sales': 'Sales'},
    color='product',
)
# Remove the legend
fig3.update_layout(showlegend=False)

category_aov = df.groupby('category')['sales'].mean().reset_index()
category_aov = category_aov.sort_values(by='sales', ascending=False)

# Average Order Value by Category
fig4 = px.bar(
    category_aov,
    x='sales',
    y='category',
    title='Average Order Value by Category',
    labels={'sales': 'Sales', 'category': 'Category'},
    color='category',
)

# Remove the legend
fig4.update_layout(showlegend=False)

category_count = df['category'].value_counts().reset_index()

# Popular Category
fig5 = px.bar(
    category_count,
    x='count',
    y='category',
    title='Popular Category',
    labels={'count': 'Count', 'category': 'Category'},
    color='category',
)

# Remove the legend
fig5.update_layout(showlegend=False)

order_per_hour = df.groupby('hour')['id'].count().reset_index()

# rename columns
order_per_hour.rename(columns = {'id':'count_of_orders'}, inplace = True)

# Peak Hour
fig6 = px.line(
    order_per_hour,
    x='hour',
    y='count_of_orders',
    title='Peak Hour',
    labels={'hour': 'Hour', 'count_of_orders': 'Count of Orders'},
    markers=True,
)

# Remove the legend
fig6.update_layout(showlegend=False)

weekdays_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Group by weekday and count the number of orders
weekday_order_counts = df['weekday'].value_counts().reindex(weekdays_order).reset_index()
weekday_order_counts.columns = ['weekday', 'count_of_orders']

# Peak Day
fig7 = px.bar(
    weekday_order_counts,
    x='weekday',
    y='count_of_orders',
    title='Peak Day',
    labels={'weekday': 'Weekday', 'count_of_orders': 'Count of Orders'},
    color='weekday',
)

# Remove the legend
fig7.update_layout(showlegend=False)

coffee_type = df[df['category'] == 'Coffee'][['product']]
coffee_type_count = coffee_type['product'].value_counts().reset_index()

# Order Distribution by Coffee Type
fig8 = px.pie(
    coffee_type_count,
    names='product',
    values='count',
    title='Order Distribution by Coffee Type',
    labels={'sales': 'Sales', 'location': 'Location'},
    color='product',
)

# Modify the pie chart to make it a donut chart
fig8.update_traces(hole=0.4)

# Create columns for displaying the charts
col1, col2 = st.columns([3, 3])

with col1:
    st.plotly_chart(fig1)

with col2:
    st.plotly_chart(fig2)

# Create columns for displaying the charts
col3, col4 = st.columns([3, 3])

with col3:
    st.plotly_chart(fig3)

with col4:
    st.plotly_chart(fig4)

# Create columns for displaying the charts
col5, col6 = st.columns([3, 3])

with col5:
    st.plotly_chart(fig5)

with col6:
    st.plotly_chart(fig6)

# Create columns for displaying the charts
col7, col8 = st.columns([3, 3])

with col7:
    st.plotly_chart(fig7)

with col8:
    st.plotly_chart(fig8)