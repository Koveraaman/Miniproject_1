import streamlit as st
import pg8000
import pandas as pd
import plotly.express as px 

# ... (Your existing code for database connection and execute_query) ...
def connect_to_db():
    return pg8000.connect(
        host="raamdb.c9qmcwaue6li.ap-south-1.rds.amazonaws.com",
        port="5432",
        database="postgres",
        user="postgres",
        password="#Raam123456789"
    )

# Function to execute a query and return a DataFrame
def execute_query(query):
    conn = connect_to_db()
    try:
        df = pd.read_sql_query(query, conn)
        return df
    finally:
        conn.close()


# Define your queries (queries and my_queries remain the same)
queries = {
    "Top 10 Revenue Generating Products": """
        SELECT p.sub_category, s.product_id, s.sales_price AS total_revenue
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.sub_category, s.product_id, s.sales_price 
        ORDER BY total_revenue DESC 
        LIMIT 10;""",

    "Top 5 Cities with Highest Profit Margins": """
        SELECT p.city, SUM(s.profit) AS total_profit
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.city 
        ORDER BY total_profit DESC 
        LIMIT 5;""",
    
    "Average Sale Price per Product Category": """
        SELECT p.category, CAST(AVG(s.sales_price) AS int) AS average_sales
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.category 
        ORDER BY average_sales DESC;""",
    
    "Region with Highest Average Sale Price": """
        SELECT p.region, CAST(AVG(s.sales_price) AS int) AS highest_avg_sales
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.region 
        ORDER BY highest_avg_sales DESC 
        LIMIT 1;""",

    "Calculate the total discount given for each category": """
        select p.category, sum(s.discount) as total_discount
        from sales as s join product_details as p on p.order_id = s.order_id
        group by p.category order by total_discount;""",
    
    "Find the total profit per category": """
        select p.category, sum(s.profit) as total_profit
        from sales as s join product_details as p on p.order_id = s.order_id
        group by p.category;""",

    "Identify the top 3 segments with the highest quantity of orders": """
        select p.segment, s.quantity as highest_quant
        from sales as s join product_details as p on p.order_id = s.order_id
        group by p.segment, s.quantity order by highest_quant desc limit 3;""",
    
    "Determine the average discount percentage given per region": """
        select p.region, cast(avg(s.discount_percent)as real) as avg_disc_per_region
        from sales as s join product_details as p on p.order_id = s.order_id
        group by p.region;""",

    "Find the product category with the highest total profit": """
        select p.category, sum(s.profit) as highest_total_profit
        from sales as s join product_details as p on p.order_id = s.order_id
        group by p.category order by highest_total_profit desc limit 1;""",
    
    "Calculate the total revenue generated per year": """
        select p.year, cast(sum(s.sales_price) as real) as tot_rev_generated
        from sales as s join product_details as p on p.order_id = s.order_id
        group by p.year;"""
 
}


my_queries= {
    "Count the number of orders in each year": """
        SELECT pd.year, COUNT(s.order_id) AS total_orders
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.year
        ORDER BY pd.year DESC;""",

    "Determine the most popular category by total sales quantity.": """
        SELECT pd.category, SUM(s.quantity) AS total_sales_quantity
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.category
        ORDER BY total_sales_quantity DESC
        LIMIT 1;""",

    "Identify states with profit greater than $10,000.": """
        SELECT pd.state, SUM(s.profit) AS total_profit
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.state
        HAVING SUM(s.profit) > 10000
        ORDER BY total_profit DESC;""",

    "Compute the average list price for each sub-category.": """
        SELECT pd.sub_category, AVG(s.list_price) AS avg_list_price
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.sub_category
        ORDER BY avg_list_price DESC;""",

    "List the total sales by ship mode.": """
        SELECT pd.ship_mode, SUM(s.sales_price) AS total_sales
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.ship_mode
        ORDER BY total_sales DESC;""",

    "List 5 cities with the lowest average profit.": """
        SELECT pd.city, AVG(s.profit) AS avg_profit
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.city
        ORDER BY avg_profit ASC
        LIMIT 5;""",

    "Find the year with the highest total discount given.": """
        SELECT pd.year, SUM(s.discount) AS total_discount
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.year
        ORDER BY total_discount DESC
        LIMIT 1;""",

    "Determine which state had the highest sales price in 2023.": """
        SELECT pd.state, SUM(s.sales_price) AS total_sales
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        WHERE pd.year = 2023
        GROUP BY pd.state
        ORDER BY total_sales DESC
        LIMIT 1;""",

    "Compute the average profit for each ship mode.": """
        SELECT pd.ship_mode, AVG(s.profit) AS avg_profit
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.ship_mode
        ORDER BY avg_profit DESC;""",

    "List the least 3 products by profit in each sub-category.": """
        SELECT pd.sub_category, s.product_id, SUM(s.profit) AS total_profit
        FROM sales s
        JOIN product_details pd ON s.order_id = pd.order_id
        GROUP BY pd.sub_category, s.product_id
        ORDER BY total_profit ASC
        LIMIT 3;"""
}
business_insights={
    "TOP SELLING PRODUCTS": """
        SELECT p.sub_category, s.product_id, s.sales_price AS total_revenue
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.sub_category, s.product_id, s.sales_price 
        ORDER BY total_revenue DESC 
        LIMIT 10;""",
    
    "MONTHY SALES ANALYSIS": """
        SELECT p.month, p.year, SUM(s.sales_price) AS total_sales
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.month, p.year
        ORDER BY p.year, p.month;""",
    "PRODUCT PERFORMANCE ANALYSIS": """
        WITH ProductRevenue AS (SELECT product_id,CAST(SUM(sales_price) as real) AS total_revenue,
        AVG(profit) AS profit_margin
        FROM sales GROUP BY product_id)
        SELECT 
            product_id,
            total_revenue,
            profit_margin,
            ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS revenue_rank
        FROM 
            ProductRevenue
        ORDER BY 
            revenue_rank;
;""",
    "REGIONAL SALES ANALYSIS": """
        SELECT p.region, CAST(AVG(s.sales_price) AS int) AS highest_avg_sales
        FROM sales AS s 
        JOIN product_details AS p ON p.order_id = s.order_id
        GROUP BY p.region 
        ORDER BY highest_avg_sales DESC 
        LIMIT 1;""",
    
    "DISCOUNT ANALYSIS": """
        SELECT product_id, SUM(sales_price) AS total_revenue,
        SUM(discount) AS total_discount_impact
        FROM sales
        WHERE (discount_percent * quantity) > 20
        GROUP BY product_id ORDER BY total_discount_impact DESC;"""
}


tab1, tab2, tab3 = st.tabs(["Queries", "My Queries", "Business Insights"])

with tab1:
    st.header("Queries")
    query_name_tab1 = st.selectbox("Select a Query", list(queries.keys()))
    query = queries.get(query_name_tab1)
    if query:
        data = execute_query(query)

        if not data.empty:
            st.write("Query Results:")
            st.dataframe(data)

    if query_name_tab1 == "Top 10 Revenue Generating Products":
        fig = px.bar(data, x="product_id", y="total_revenue", color="sub_category", 
                     title="Top 10 Revenue Generating Products")
        st.plotly_chart(fig)

    elif query_name_tab1 == "Top 5 Cities with Highest Profit Margins":
        fig = px.bar(data, x="city", y="total_profit", color="city", 
                     title="Top 5 Cities with Highest Profit Margins")
        st.plotly_chart(fig)

    elif query_name_tab1 == "Average Sale Price per Product Category":
        fig = px.bar(data, x="category", y="average_sales", color="category", 
                     title="Average Sale Price per Product Category")
        st.plotly_chart(fig)

    elif query_name_tab1 == "Identify the top 3 segments with the highest quantity of orders":
        fig = px.pie(data, names="segment", values="highest_quant", 
                     title="Top 3 Segments with Highest Quantity of Orders")
        st.plotly_chart(fig)

    elif query_name_tab1 == "Determine the average discount percentage given per region":
        fig = px.bar(data, x="region", y="avg_disc_per_region", color="region", 
                     title="Average Discount Percentage per Region")
        st.plotly_chart(fig)

    elif query_name_tab1 == "Calculate the total revenue generated per year":
        fig = px.bar(data, x="year", y="tot_rev_generated", color="year", 
                     title="Total Revenue Generated per Year")
        st.plotly_chart(fig)

with tab2:
    st.header("My Queries")
    query_name_tab2 = st.selectbox("Select a Query", list(my_queries.keys()))
    query = my_queries.get(query_name_tab2)
    if query:
        data = execute_query(query)

        if not data.empty:
            st.write("Query Results:")
            st.dataframe(data)

    if query_name_tab2 == "Count the number of orders in each year":
        fig = px.bar(data, x="year", y="total_orders", color="year", 
                     title="Number of Orders per Year")
        st.plotly_chart(fig)

    elif query_name_tab2 == "Determine the most popular category by total sales quantity.":
        fig = px.bar(data, x="category", y="total_sales_quantity", color="category", 
                     title="Most Popular Category by Total Sales Quantity")
        st.plotly_chart(fig)

    elif query_name_tab2 == "Identify states with profit greater than $10,000.":
        fig = px.bar(data, x="state", y="total_profit", color="state", 
                     title="States with Profit Greater than $10,000")
        st.plotly_chart(fig)

    elif query_name_tab2 == "Compute the average list price for each sub-category.":
        fig = px.bar(data, x="sub_category", y="avg_list_price", color="sub_category", 
                     title="Average List Price per Sub-Category")
        st.plotly_chart(fig)

    elif query_name_tab2 == "List the total sales by ship mode.":
        fig = px.bar(data, x="ship_mode", y="total_sales", color="ship_mode", 
                     title="Total Sales by Ship Mode")
        st.plotly_chart(fig)

    elif query_name_tab2 == "List 5 cities with the lowest average profit.":
        fig = px.bar(data, x="city", y="avg_profit", color="city", 
                     title="5 Cities with the Lowest Average Profit")
        st.plotly_chart(fig)

    elif query_name_tab2 == "Find the year with the highest total discount given.":
        fig = px.bar(data, x="year", y="total_discount", color="year", 
                     title="Year with the Highest Total Discount")
        st.plotly_chart(fig)

    elif query_name_tab2 == "Determine which state had the highest sales price in 2023.":
        fig = px.bar(data, x="state", y="total_sales", color="state", 
                     title="State with the Highest Sales Price in 2023")
        st.plotly_chart(fig)

    elif query_name_tab2 == "Compute the average profit for each ship mode.":
        fig = px.bar(data, x="ship_mode", y="avg_profit", color="ship_mode", 
                     title="Average Profit for Each Ship Mode")
        st.plotly_chart(fig)

    elif query_name_tab2 == "List the least 3 products by profit in each sub-category.":
        fig = px.pie(data, names="product_id", values="total_profit", 
                     title="Least 3 Products by Profit in Each Sub-Category")
        st.plotly_chart(fig)

with tab3:
    st.header("Business Insights")

    st.write("""
        We have identified top-performing products, analyzed regional seasonal sales trends, 
        evaluated the impact of discounts on revenue, and assessed the profitability across categories. 
        This comprehensive analysis enables data-driven decisions to optimize inventory, 
        marketing, and pricing strategies for better profitability and growth.
    """)
    
    query_name_tab3 = st.selectbox("Select a Query", list(business_insights.keys()))
    query = business_insights.get(query_name_tab3)
    if query:
        data = execute_query(query)

        if not data.empty:
            st.write("Query Results:")
            st.dataframe(data)

    if query_name_tab3 == "TOP SELLING PRODUCTS":
        st.write("""
            Identified the products generating the highest revenue. 
            This helps focus on popular items and optimize inventory management.
        """)
      
    elif query_name_tab3 == "PRODUCT PERFORMANCE ANALYSIS":
        st.write("""
            Analyzed monthly sales trends year-over-year to detect growth or 
            decline during specific months. It aids in understanding seasonality or 
            market shifts.
        """)

    elif query_name_tab3 == "REGIONAL SALES ANALYSIS":
        st.write("""
            Identified regions contributing the most to revenue. This helps to tailor marketing strategies 
            and allocate resources effectively.
        """)

    elif query_name_tab3 == "DISCOUNT ANALYSIS":
        st.write("""
            Examined products with discounts exceeding 20% and their impact on revenue. 
            Understanding if discounts drive sales significantly or result in a loss.
        """)


    
