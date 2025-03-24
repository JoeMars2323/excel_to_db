CREATE TABLE banking_marketing (
    id SERIAL PRIMARY KEY,
    age TEXT,
    job TEXT,
    marital TEXT,
    education TEXT,
    default_value TEXT,
    housing TEXT,
    loan TEXT,
    contact TEXT,
    month TEXT,
    day_of_week TEXT,
    duration TEXT,
    campaign TEXT,
    pdays TEXT,
    previous TEXT,
    poutcome TEXT,
    emp_var_rate TEXT,
    cons_price_idx TEXT,
    cons_conf_idx TEXT,
    euribor3m TEXT,
    nr_employed TEXT,
    y TEXT
);



COPY banking_marketing(age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, y)
FROM '/path/to/your/file.csv'
DELIMITER ','
CSV HEADER;