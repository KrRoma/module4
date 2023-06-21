import requests
import random
from bs4 import BeautifulSoup
response=requests.get(input('Введите сайт'))
response=response.content
html=BeautifulSoup(response,'lxml')
header=html.find(r'>.+</h3>', response)
print(header.text)

