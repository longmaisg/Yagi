import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for scraping with page number variable
base_url = "https://unghodongbao.vietnampedia.com/ung-ho-dong-bao?page={}&sort=-time"

# Number of pages to process before saving to a new CSV file
pages_per_file = 50

# List to hold the scraped data
data = []

# Set initial page number
page = 0

# Loop through pages until there's no more data
while True:
    # Print the current page number
    print(f"Processing page {page}")

    # Generate the URL for the current page
    url = base_url.format(page)
    response = requests.get(url)
    
    # If the response is not OK, stop scraping
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
        break

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all relevant rows (adjust the selector as necessary)
    rows = soup.find_all('tr', {'data-key': True})

    # If no more rows, stop scraping
    if not rows:
        print(f"No more data found on page {page}. Ending scraping.")
        break

    # Process each row
    for row in rows:
        # Extract each column data
        cols = row.find_all('td')
        if len(cols) >= 4:
            time = cols[0].text.strip()
            amount = cols[1].text.strip()
            ck_tm = cols[2].text.strip()
            message = cols[3].text.strip()

            # Append the row data to the list
            data.append([time, amount, ck_tm, message])

    # Save the data every `pages_per_file` pages to a separate CSV file
    if (page + 1) % pages_per_file == 0:
        file_number = (page // pages_per_file) + 1
        df = pd.DataFrame(data, columns=["Thời gian", "Số tiền (VNĐ)", "CK / TM", "Nội dung chuyển khoản"])
        df.to_csv(f'yagi/yagi{file_number}.csv', index=False, encoding='utf-8-sig')

        # Clear the data list to free memory
        data = []

    # Increment the page number
    page += 1

# Save any remaining data after scraping ends
if data:
    file_number = (page // pages_per_file) + 1
    df = pd.DataFrame(data, columns=["Thời gian", "Số tiền (VNĐ)", "CK / TM", "Nội dung chuyển khoản"])
    df.to_csv(f'yagi/yagi{file_number}.csv', index=False, encoding='utf-8-sig')

print(f"Scraping completed! Data saved into yagi/yagi{file_number}.csv")
