import requests
from bs4 import BeautifulSoup


BASE_URL = "http://localhost:8000/sales_"

def fetch_sales(month_url:str) -> list[dict]:
  response = requests.get(BASE_URL + month_url +'.html')

  print(BASE_URL + month_url +'.html')
  soup = BeautifulSoup(response.text, 'html.parser')
  table = soup.find('table')

  if table is None:
    print("No table found on the page.")
    return []

  headers = [th.get_text(strip=True) for th in table.find_all('th')]

  rows = []

  for tr in table.find_all('tr')[1:]:  # Ignorer l'en-tête
    cells = [td.get_text(strip=True) for td in tr.find_all('td')]
    if len(cells) == len(headers):  # Ignore les lignes incomplètes
        rows.append(dict(zip(headers, cells)))

  print('Extracting data from table is done for', month_url, len(rows), 'rows')
  return rows

# print(fetch_sales('january'))
fetch_sales('january')
fetch_sales('february')
fetch_sales('march')