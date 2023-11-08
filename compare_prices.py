import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    laughs_response = requests.get(product_laughs)
    glomark_response = requests.get(product_glomark)

     
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    laugh = BeautifulSoup(laughs_response.text,'html.parser')

    product_name_laughs = laugh.find('div' , class_ = 'product-name').text
    price_laughs = laugh.find('span', class_  = 'regular-price').text
    price_laughs_float = float(price_laughs.replace('Rs.',''))

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    glomark = BeautifulSoup(glomark_response.text , 'html.parser')

    glomark_script = glomark.find('script', {'type': 'application/ld+json'})
    json_load = json.loads(glomark_script.text)

    price_glomark = round(float(json_load['offers'][0]['price']),2)
    product_name_glomark = json_load['name']
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs_float)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs_float>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs_float - price_glomark)
    elif(price_laughs_float<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs_float)    
    else:
        print('Price is the same')