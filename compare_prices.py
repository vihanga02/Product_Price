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
    glomark_response = requests.get(product_glomark, headers=user_agent)

    
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    laugh = BeautifulSoup(laughs_response.text,'html.parser')

    product_name_laughs = laugh.find('div' , class_ = 'product-name').text
    price_laughs = laugh.find('span', class_  = 'price').text

    price_laughs_float = float(price_laughs.replace('Rs.',''))

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs_float)
    # print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    # if(price_laughs>price_glomark):
    #     print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    # elif(price_laughs<price_glomark):
    #     print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    # else:
    #     print('Price is the same')