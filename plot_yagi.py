import pandas as pd
import os
import re

# Directory containing the CSV files
csv_dir = 'yagi'

# Initialize an empty DataFrame to hold all the data
all_data = pd.DataFrame()

# Loop through all CSV files in the directory
for file in os.listdir(csv_dir):
    if file.endswith(".csv"):
        file_path = os.path.join(csv_dir, file)
        df = pd.read_csv(file_path, dtype=str)  # Read as string to handle specific formatting
        
        # Clean and convert 'Số tiền (VNĐ)' to numeric
        df['Số tiền (VNĐ)'] = df['Số tiền (VNĐ)'].str.replace('.', '', regex=False)  # Remove dots
        df['Số tiền (VNĐ)'] = pd.to_numeric(df['Số tiền (VNĐ)'], errors='coerce')  # Convert to numeric
        
        all_data = pd.concat([all_data, df], ignore_index=True)

# Strip any leading or trailing spaces from column names
all_data.columns = all_data.columns.str.strip()

# Convert 'Thời gian' to datetime
all_data['Thời gian'] = pd.to_datetime(all_data['Thời gian'], format='%Y-%m-%d %H:%M:%S')

# Prepare the data for embedding in HTML
columns_to_use = ['Thời gian', 'Số tiền (VNĐ)', 'Nội dung chuyển khoản']
data_list = all_data[columns_to_use].to_dict(orient='records')

# Convert each record to the required format
formatted_data = []
for item in data_list:
    item['Số tiền (VNĐ)'] = float(item['Số tiền (VNĐ)'])  # Ensure amount is a float
    item['Thời gian'] = item['Thời gian'].strftime('%Y-%m-%d %H:%M:%S')
    item['Nội dung chuyển khoản'] = item['Nội dung chuyển khoản'].replace('\n', ' ').replace('\r', ' ')  # Remove new lines from messages
    
    formatted_entry = '{{ time: "{0}", amount: {1}, type: "Chuyển khoản", message: "{2}" }}'.format(
        item['Thời gian'].replace('"', '\\"'),
        item['Số tiền (VNĐ)'],  # No quotes around the number
        item['Nội dung chuyển khoản'].replace('"', '\\"')
    )
    
    formatted_data.append(formatted_entry)

# Join the formatted data into a multi-line JSON array
data_json = '[\n    ' + ',\n    '.join(formatted_data) + '\n]'

# Read the existing HTML file
with open('plot_yagi.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Regular expression to find and replace the const data array
pattern = r'const data = \[.*?\];'
replacement = f'const data = {data_json};'
updated_html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# Write the updated HTML content back to the file
with open('plot_yagi.html', 'w', encoding='utf-8') as file:
    file.write(updated_html_content)
