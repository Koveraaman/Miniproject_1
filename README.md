**Streamlit PostgreSQL Sales Dashboard**

**Overview**

This project is a Streamlit web application that connects to an AWS-hosted PostgreSQL database to analyze and visualize sales data. The dashboard includes multiple tabs that allow users to run predefined SQL queries and visualize the results using Plotly charts.

**Features**

Connects to an AWS PostgreSQL database using the pg8000 driver.

Supports various SQL queries to analyze sales data, including revenue, profit margins, product performance, and regional sales.

Interactive visualizations using Plotly.

Three main sections:

Queries: Predefined analytical queries.

My Queries: Custom queries focusing on specific insights.

Business Insights: Key takeaways for business decision-making.

**Prerequisites**

Ensure you have the following installed:

Python 3.x

PostgreSQL database (AWS RDS instance)

Required Python packages (see below for installation)

**Installation**

Clone the repository:

git clone https://github.com/yourusername/streamlit-sales-dashboard.git
cd streamlit-sales-dashboard

Install dependencies:

pip install streamlit pg8000 pandas plotly

Configure database connection in the connect_to_db() function:

def connect_to_db():
    return pg8000.connect(
        host="your-db-host",
        port="5432",
        database="your-db-name",
        user="your-db-user",
        password="your-db-password"
    )

Run the Streamlit application:

streamlit run app.py

**Project Structure**

|-- app.py                 # Main Streamlit application file
|-- README.txt             # Project documentation
|-- requirements.txt       # Python dependencies
|-- queries.py             # SQL queries dictionary

Usage

Open the Streamlit web app in your browser.

Navigate through the available tabs:

Queries: Select predefined queries to explore insights such as top-selling products, highest profit margins, and revenue analysis.

My Queries: Custom queries to analyze sales trends, order counts, and profit margins.

Business Insights: Summary reports on product performance, discount analysis, and regional sales trends.

Visualize the query results with interactive charts.

Example Queries

Some example queries available in the dashboard:

Top 10 Revenue Generating Products

Average Sale Price per Product Category

Region with Highest Average Sale Price

Total Revenue Generated per Year

**Troubleshooting**

If you encounter a database connection issue:

Ensure the AWS RDS instance is accessible and the security group allows inbound traffic.

Verify database credentials.

Check network connectivity.

**Contribution**

Feel free to contribute by opening pull requests or raising issues.

**Author**

Developed by Kove Raaman.

