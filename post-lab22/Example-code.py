import pandas as pd

# Load data from CSV
csv_file_path = 'sample_data.csv'
df_csv = pd.read_csv(csv_file_path)

# Display the DataFrame
print("CSV Data:")
print(df_csv)

# Basic data manipulation: Filter by age
filtered_data = df_csv[df_csv['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)

json_file_path = 'sample_data.json'
df_json = pd.read_json(json_file_path)

# Display the DataFrame
print("\nJSON Data:")
print(df_json)

# Basic data manipulation: Find the average age
average_age = df_json['Age'].mean()
print("\nAverage Age:", average_age)

excel_file_path = 'sample_data.xlsx'
df_excel = pd.read_excel(excel_file_path)

# Display the DataFrame
print("\nExcel Data:")
print(df_excel)

# Basic data manipulation: Count the number of entries
entry_count = df_excel.shape[0]
print("\nNumber of entries in Excel file:", entry_count)

# Save filtered CSV data to a new file
filtered_data.to_csv('filtered_data.csv', index=False)
print("\nFiltered data saved to 'filtered_data.csv'.")

# Save DataFrame to a new JSON file
df_json.to_json('new_data.json', orient='records', lines=True)
print("JSON data saved to 'new_data.json'.")

# Save DataFrame to a new Excel file
df_excel.to_excel('new_data.xlsx', index=False)
print("Excel data saved to 'new_data.xlsx'.")
