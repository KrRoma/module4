import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'http://www.cbr.ru/scripts/xml_daily.asp?'
today=datetime.today()
today=today.surftime('%d/%n/%Y')

date={'date_req': today}
responce = requests.get(url+date)
xml = BeautifulSoup(responce.content, 'html.parser')

def getCourse(id):
    course = xml.find("valute", {'id': id}).value.text
    return course
print(getCourse('R01280'), 'рублей за 10000 индонезийских рупий')


