import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean2.db')

query = """
    SELECT 
        Customer_ID,
        strftime('%Y', Date) AS ano,
        strftime('%m', Date) AS mes,
        SUM(Total_Amount) AS valor_total_user,
        SUM(Total_Amount) OVER (PARTITION BY strftime('%Y', Date), strftime('%m', Date)) AS valor_total_mes,
        ROUND((CAST(SUM(Total_Amount) AS FLOAT) * 100 / SUM(Total_Amount) OVER (PARTITION BY strftime('%Y', Date), strftime('%m', Date))), 2) AS percentual_contribuicao
    FROM vendas2
    GROUP BY Customer_ID, ano, mes
    ORDER BY ano ASC, mes ASC;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()