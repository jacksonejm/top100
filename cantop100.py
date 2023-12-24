import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage
url = 'https://www.canadastop100.com/national/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the container with the company list
company_list_container = soup.find(id='winners')
if not company_list_container:
    raise Exception("Could not find the company list container on the webpage.")

# Regular expression to identify unwanted items (years, categories)
unwanted_pattern = re.compile(r'^\d{4}$|^[A-Z]-[A-Z]$|Previous winners:')

# Extract company names
companies = []
for li in company_list_container.find_all('li'):
    # Get all text, strip leading/trailing whitespace, and replace newlines and excess spaces
    text = ' '.join(li.get_text(strip=True).split())
    if text and not unwanted_pattern.match(text):
        companies.append(text)

# Optionally, sort the companies alphabetically
companies.sort()

# Write to file
with open('company_names.txt', 'w') as f:
    for company in companies:
        f.write(company + '\n')

print("Filtered company names have been successfully written to 'company_names.txt'")
