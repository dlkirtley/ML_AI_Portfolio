import numpy
import pandas as pd
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

else:
    print("No table found on the page.")
    raise ValueError(f"No Table Found")

#Lists to store player names and id numbers
names = []
player_ids = []

# Iterate through rows
for row in rows:
    # Find all <span> elements with the specific class inside the row
    spans = row.find_all('span', class_='full-G_bAyq40')
    name = ' '.join(span.text.strip() for span in spans)
    if name != '':
        names.append(name.lower())
    # Find all <a> elements with the specific class inside the row
    links = row.find_all('a', class_='bui-link')
    
    
    for link in links:
        # Extract the href attribute
        href = link.get('href', '')

        # Check if the href contains '/player/'
        if '/player/' in href:
            # Extract player ID by splitting the href
            player_id = href.split('/player/')[1].split('/')[0]
            if player_id != '':
                player_ids.append(player_id)

#Check that lengths of names list and player_id list are the same
if len(names)!=len(player_ids):
        raise ValueError(f"Lists are not of the same length: Names({len(names)}) != Player IDs({len(player_ids)})")
else:
    print('success')


df = pd.DataFrame({
    'Name': names,
    'ID': player_ids})[0:4]



for i in range(1):
    fname = str(df.iloc[i,0]).split()[0]
    lname = str(df.iloc[i,0]).split()[1]
    id = str(df.iloc[i,1])
    url = f"https://www.mlb.com/player/{fname}-{lname}-{id}?stats=gamelogs-r-hitting-mlb&year=2024"
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

    for row in rows: 
        spans = row.find_all('span')

    print(spans)

    


    
    









