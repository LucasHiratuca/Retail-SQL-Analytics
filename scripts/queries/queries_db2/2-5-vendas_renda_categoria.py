import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean2.db')

query = """
    SELECT
        Product_Category,
        SUM(Total_Amount) AS receita,
        COUNT(*) AS qnt_vendas,
        DENSE_RANK() OVER (ORDER BY SUM(Total_Amount) DESC) AS rank_sum,
        DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_quant
    FROM vendas2
    GROUP BY Product_Category;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()