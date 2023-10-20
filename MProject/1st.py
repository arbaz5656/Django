'''
import requests
from bs4 import BeautifulSoup
w_url="https://www.aajtak.in/"

v=requests.get(w_url)
v1=v.content
'''
# print(v1)
# Store the text response
# print(v.text)
# Store the status code
# print(v.status_code)

# v2=BeautifulSoup(v1,'html.parser')
# print(v2.prettify())

# v3=v2.title.text
# print(v3)

# v3=v2.title
# print(type(v3.string))

# print(v2.find('p').get_text())
# print(v2.get_text())
# v4=v2.find('p')
# print(v4)
# print(v2.find_all('h1'))
# print(v2.find_all('h2'))
# print(v2.find_all('h3'))
# print(v2.find_all('h4'))
# print(v2.find_all('h5'))
# print(v2.find_all('h6'))

# ************ #
'''
import requests
from bs4 import BeautifulSoup
w_url="https://www.aajtak.in/"

v=requests.get(w_url)
v1=v.content
v2=BeautifulSoup(v1,'html.parser')
v3=v2.find_all('p')
print(v3)
print(v2.find_all('h1'))
print(v2.find_all('h2'))
print(v2.find_all('h3'))
print(v2.find_all('h4'))
'''
'''

import requests
from bs4 import BeautifulSoup

url_link="https://zeenews.india.com/"
v1=requests.get(url_link)
v2=v1.content
v3=BeautifulSoup(v2,'html.parser')
# v4=v3.title
# print(v4.text)
v4=v3.find_all('p')
print(v4)
'''
'''
import requests
from bs4 import BeautifulSoup
url_link = "https://timesofindia.indiatimes.com/"
v1 = requests.get(url_link)
v2 = v1.content
v3 = BeautifulSoup(v2,'html.parser')
# vb= v3.find('p')

v4 = v3.find_all('p')
v5 = v3.find_all('h1')
v6 = v3.find_all('h2')
v7 = v3.find_all('h3')
v8 = v3.find_all('h4')
v9 = v3.find_all('h5')
v10 = v3.find_all('h6')
import pymysql
c = pymysql.connect(host="localhost", user="root", password="", database="test")
c1 = c.cursor()
c1.execute("INSERT INTO hard(DATA) VALUES ('%s')" % (v8))
print("data enter")
c.commit()
c.close()

'''

import requests
from bs4 import BeautifulSoup
url_link = "https://zeenews.india.com/"
v1 = requests.get(url_link)
v2 = v1.content
v3 = BeautifulSoup(v2,'html.parser')
import pymysql
c = pymysql.connect(host="localhost", user="root", password="", database="test")
c1 = c.cursor()
d1="INSERT INTO hard(DATA) VALUES (%s)"
v4 = v3.find_all('p')
v5 = v3.find_all('h1')
v6 = v3.find_all('h2')
v7 = v3.find_all('h3')
v8 = v3.find_all('h4')
v9 = v3.find_all('h5')
v10 = v3.find_all('h6')
d2 = str([(v4),(v5),(v6),(v7),(v8),(v9),(v10)])
c1.execute(d1,d2)
print(c1.rowcount, "data enter")
c.commit()
c.close()


