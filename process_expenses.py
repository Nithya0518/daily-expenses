import pandas as pd

def extract(file_path):
    data = pd.read_csv(file_path)
    print(f"Successfully read file: {file_path}")
    return data

def transform(data):
  
    data['expense_date'] = pd.to_datetime(data['expense_date'], format='%d-%m-%Y')
    category_summary = data.groupby('category')['amount'].sum().reset_index()
    category_summary.columns = ['category', 'total_expense']
    print("Total Expenses by Category:")
    print(category_summary.to_string(index=False))

  
    data['week_start'] = data['expense_date'] - pd.to_timedelta(data['expense_date'].dt.weekday, unit='d')
    weekly_summary = data.groupby('week_start')['amount'].sum().reset_index()
    weekly_summary.columns = ['week_start_date', 'total_expense']
    print("Weekly Expense Summary:")
    print(weekly_summary.to_string(index=False))

    print("Transformation successful")
    return {'category_summary': category_summary, 'weekly_summary': weekly_summary}

def load(category_df, weekly_df, file_name):
    print("Saving output files")
    category_file = f"{file_name}_category.csv"
    weekly_file = f"{file_name}_weekly.csv"

    category_df.to_csv(category_file, index=False)
    weekly_df.to_csv(weekly_file, index=False)

    print(f"Files saved successfully: {category_file}- {weekly_file}")


def main(file_path, file_name):
    expenses = extract(file_path)
    transformed_data = transform(expenses)
    load(transformed_data['category_summary'], transformed_data['weekly_summary'], file_name)


main(file_path=r'C:\DA Project\TASKS\daily_expenses.csv', file_name='Expenses_summary')
