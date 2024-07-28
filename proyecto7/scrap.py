import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')


table =  soup.find_all("table", attrs={"id": "weather_records"})
#Encabezados:
heading_table = [] 
for row in table[0].find_all('th'):
    #Al revisar table, note que es una lista de un elemento, no entiendo por que tiene esta estructura. en todo caso para trabajar con dicho elemento se usa: "table[0]"
    heading_table.append(row.text)  
#print(heading_table)

#Valores td:
content = [] 
for row in table[0].find_all('tr'):
    if not row.find_all('th'):
        content.append([element.text for element in row.find_all('td')])
#print(content)

weather_records=pd.DataFrame(content, columns=heading_table)
print(weather_records)
weather_records.to_csv('datos.csv')
