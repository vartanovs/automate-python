# Module that hits Amazon and scrapes a price

from bs4 import BeautifulSoup
import requests

def get_Amazon_Price(productURL):
  # Request Amazon webpage, save into response object
  res = requests.get(productURL)
  # Confirm successful request
  res.raise_for_status()
  # Create a BS object
  soup = BeautifulSoup(res.text, 'html.parser')
  # Extract and return price
  elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
  price = elems[0].text.strip()
  return price

automate_python_url = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994'
automate_python_price = get_Amazon_Price(automate_python_url)

print(f'The current price of "Automate the Boring Stuff" is: {automate_python_price}')
