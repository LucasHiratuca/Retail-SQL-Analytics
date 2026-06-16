import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean2.db')

query = """
        SELECT
            Product_Category,
            COUNT(CASE WHEN Gender = 'Male' THEN 1 END) AS num_male,
            COUNT(CASE WHEN Gender = 'Female' THEN 1 END) AS num_fem,
            ROUND((COUNT(CASE WHEN Gender = 'Male' THEN 1 END) * 100.0) / COUNT(Gender), 2) AS porc_male,
            ROUND((COUNT(CASE WHEN Gender = 'Female' THEN 1 END) * 100.0) / COUNT(Gender), 2) AS porc_fem
        FROM vendas2
        GROUP BY Product_Category;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()