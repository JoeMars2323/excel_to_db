import pandas as pd
import psycopg2

df = pd.read_excel('banking_marketing.xlsx')
print(df)

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "123"
)
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO banking_marketing (age, job, marital, education, default_value, housing, loan, contact, "
        "month, day_of_week, duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, "
        "euribor3m, nr_employed, y) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (row['age'], row['job'], row['marital'], row['education'], row['default'], row['housing'], row['loan'],
         row['contact'], row['month'], row['day_of_week'], row['duration'], row['campaign'], row['pdays'], row['previous'],
         row['poutcome'], row['emp_var_rate'], row['cons_price_idx'], row['cons_conf_idx'], row['euribor3m'],
         row['nr_employed'], row['y'])
    )

conn.commit()
cursor.close()
conn.close()



