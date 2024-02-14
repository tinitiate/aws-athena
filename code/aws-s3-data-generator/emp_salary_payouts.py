import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random
import io

# Initialize Faker for generating fake data
fake = Faker()

# Generate fake employee data
employee_data = []
for employee_id in range(1, 10001):
    first_name = fake.first_name()
    last_name = fake.last_name()
    department = fake.word()
    email = fake.email()
    hire_date = fake.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2022, 2, 13))
    start_date = fake.date_between_dates(date_start=hire_date, date_end=datetime(2022, 2, 13))
    end_date = fake.date_between_dates(date_start=start_date, date_end=datetime(2022, 2, 13))
    
    employee_data.append({
        'EmployeeID': employee_id,
        'FirstName': first_name,
        'LastName': last_name,
        'departname': department,
        'Email': email,
        'HireDate': hire_date,
        'StartDate': start_date,
        'EndDate': end_date
    })

# Create DataFrame from employee data
employee_df = pd.DataFrame(employee_data)

# Generate random salaries for the last 20 years
salaries_data = []
current_date = datetime.now()

for _, employee_row in employee_df.iterrows():
    employee_id = employee_row['EmployeeID']
    start_date = employee_row['StartDate']
    end_date = employee_row['EndDate'] if not pd.isnull(employee_row['EndDate']) else current_date

    for year in range(start_date.year, min(current_date.year, end_date.year) + 1):
        for month in range(1, 13):
            salary_month = f"{year}-{month:02d}"
            salary_year = str(year)
            salary_amount = round(random.uniform(30000, 120000), 2)  # Random salary amount between 30000 and 120000
            month_year = datetime(year, month, 1).date()

            salaries_data.append({
                'EmployeeID': employee_id,
                'SalaryAmount': salary_amount,
                'salary_month': salary_month,
                'salary_year': salary_year,
                'MonthYear': month_year
            })

# Create DataFrame from salary data
salaries_df = pd.DataFrame(salaries_data)

# Merge employee and salary DataFrames
result_df = pd.merge(employee_df, salaries_df, on='EmployeeID', how='inner')

# Display the result
print(result_df.head())

# Output to Bytes (CSV)
csv_bytes = result_df.to_csv(index=False).encode('utf-8')

# Output to Bytes (JSON)
json_bytes = result_df.to_json(orient='records', lines=True).encode('utf-8')

# Output to Bytes (Parquet)
parquet_buffer = io.BytesIO()
result_df.to_parquet(parquet_buffer, index=False)
parquet_bytes = parquet_buffer.getvalue()

# Example usage of the bytes (you can use these bytes as needed)
print(f"CSV Bytes Size: {len(csv_bytes)}")
print(f"JSON Bytes Size: {len(json_bytes)}")
print(f"Parquet Bytes Size: {len(parquet_bytes)}")
