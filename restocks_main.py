import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def restocks_url(SKU):
  base_url = 'https://restocks.net/de/shop/search?q='
  request_url = base_url + SKU + '&page=1&filters[0][range][price][gte]=1'

  r = requests.get(request_url)

  json_restocks = json.loads(r.text)
  product_url = json_restocks["data"][0]['slug']
  print('Scraped Restocks URL: ' + product_url)
  return product_url

def format_list(price_list):
    result = ""
    for i in range(len(price_list)):
        if i % 2 == 0:
            result += price_list[i] + ": "
        else:
            result += price_list[i]
            if i < len(price_list) - 1 and price_list[i+1] != "":
                result += "\n"
    return result

def restocks_stock(SKU):
  base_url = 'https://restocks.net/de/shop/search?q='
  request_url = base_url + SKU + '&page=1&filters[0][range][price][gte]=1'

  r = requests.get(request_url)

  json_restocks = json.loads(r.text)
  product_url = json_restocks["data"][0]['slug']
  print('Scraped Restocks URL: ' + product_url)

  options = Options()
  options.headless = True
  driver = webdriver.Chrome(options=options)
  driver.get(product_url)

  cookies = driver.find_element(by=By.ID, value='save__first__localization__button')
  cookies.click()
  time.sleep(2)

  driver.execute_script("window.scrollBy(0,500)", "")

  size_list = driver.find_element(by=By.CLASS_NAME, value='select__label')
  size_list.click()
  time.sleep(2)

  prices = driver.find_element(by=By.CLASS_NAME, value='select__size__list').text
  prices_replace = prices.replace(" ½", "½")
  prices_replace2 = prices_replace.replace("Notify me", "OOS!")
  prices_replace3 = prices_replace2.replace(" €", "€")
  price_list = prices_replace3.split("\n")


  price_list = [item for item in price_list if item != 'Noch 1 auf Lager' and item != 'Noch 2 auf Lager']

  formatted_list = format_list(price_list)

  driver.quit
  return formatted_list

def restocks_product_img(SKU,restocks_url):
  product_url = restocks_url(SKU)
  r = requests.get(product_url)
  soup = BeautifulSoup(r.content, 'html.parser')
  picture = soup.find("div", class_ = "swiper-wrapper")
  image = picture.find_all('img')[0].get('src')
  print('Scraped Product picture!')
  return image

def product_title(SKU):
  product_url = restocks_url(SKU)
  r = requests.get(product_url)
  soup = BeautifulSoup(r.content, 'html.parser')
  title = soup.find("div", class_ = "product__title")
  title2 = title.text
  product_title_formated = title2.replace("\n", "")
  print('Scraped Title!')
  return product_title_formated

def stockx_url(SKU):
  url = "https://stockx.com/api/browse?_search=" + SKU

  headers = {
          'accept': 'application/json',
          'accept-encoding': 'utf-8',
          'accept-language': 'en-DE',
          'app-platform': 'Iron',
          'referer': 'https://stockx.com/en-DE',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'
      }

  request1 = requests.get(url=url, headers=headers)

  product_id = json.loads(request1.text)
  product_id_final = product_id['Products'][0]['id']


  ID = product_id_final
  url_stockX = "https://stockx.com/" + ID
  print("Scraped StockX URL: " + url_stockX)
  return url_stockX

def hypeboost_product_url(SKU):
    url = "https://hypeboost.com/en/search/shop?keyword=" + SKU
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    for a in soup.find_all('a', href=True):
      print("Scraped Hypeboost URL:", a['href'])

    url2 = a['href']
    #print("Scraped Hypeboost URL:", url2)
    return url2