import numpy
import pandas
from bs4 import BeautifulSoup
import requests
import lxml


import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'https://www.mlb.com/stats/home-runs'

# Fetch the web page
response = requests.get(url)
html_content = response.text

# Parse HTML content
soup = BeautifulSoup(html_content, 'lxml')

# Find the table (make sure this correctly identifies the table you need)
table = soup.find('table')

# Check if the table was found
if table:
    # Find all rows in the table
    rows = table.find_all('tr')
    
    # List to hold combined lines
    combined_lines = []

    # Iterate through rows
    for row in rows:
        # Find all <span> elements with the specific class inside the row
        spans = row.find_all('span', class_='full-G_bAyq40')
        names = ' '.join(span.text.strip() for span in spans)

        # Find all <a> elements with the specific class inside the row
        links = row.find_all('a', class_='bui-link')
        
        player_ids = []
        for link in links:
            # Extract the href attribute
            href = link.get('href', '')

            # Check if the href contains '/player/'
            if '/player/' in href:
                # Extract player ID by splitting the href
                player_id = href.split('/player/')[1].split('/')[0]
                player_ids.append(player_id)
        for player_id in player_ids:
             x = f"{names.lower()} {player_id}"
             print(x.split(' '))
        

    

else:
    print("No table found on the page.")



