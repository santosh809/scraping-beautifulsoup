from bs4 import BeautifulSoup
import requests
import csv

url = requests.get("https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=popular")
soup = BeautifulSoup(url.text, "html.parser")
table = soup.table
tag = table.find_all('tr')
data = []
for tags in tag:
    x = tags.text
    data.append(x)
    print(data)

datas=[]
for i in data:
    datas.append(i.split('\n')[1:-1])
    print(datas)

file = open('anme_data.csv',"w")
x = csv.writer(file)
for i in datas:
    x.writerow(i)

file.close()