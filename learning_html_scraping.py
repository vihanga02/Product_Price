#importing libraries
from bs4 import BeautifulSoup
import requests

#initiating the websit's url
websit = "https://subslikescript.com/movie/Titanic-120338"

#geting contents from the website
result = requests.get(websit)
content = result.text

#geting htm contents of the website
soup = BeautifulSoup(content, 'lxml')

#get the contents of the article on the webpage
box = soup.find('article' , class_ = 'main-article')

#get the heading of the article
head = soup.find('h1').get_text()

#get the transcropt as a text
htranscript= soup.find('div',class_='full-script').get_text(strip = True, separator=' ')

print(head)