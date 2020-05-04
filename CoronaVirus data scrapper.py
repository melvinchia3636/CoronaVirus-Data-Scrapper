#modules import
import requests
from bs4 import BeautifulSoup

#create list needed
data=[]
country = []
infected = []
infectedtoday = []
deaths = []
deathtoday = []
recovered = []
recoveredtoday = []
active = []
critical = []
main_data=[]

#request the webpage
URL = 'https://corona.help/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#get the data we want
table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

#sort out the data into different list
[country.append(data[i][0]) for i in range(len(data))]
[infected.append(data[i][1]) for i in range(len(data))]
[infectedtoday.append(data[i][2]) for i in range(len(data))]
[deaths.append(data[i][3]) for i in range(len(data))]
[deathtoday.append(data[i][4]) for i in range(len(data))]
[recovered.append(data[i][5]) for i in range(len(data))]
[recoveredtoday.append(data[i][6]) for i in range(len(data))]
[active.append(data[i][7]) for i in range(len(data))]
[critical.append(data[i][8]) for i in range(len(data))]

#centralize the data into one big database
for i in range(len(country)):
    main_data.append({
        'country':country[i],
        'infected':infected[i],
        'infected today':infectedtoday[i],
        'deaths':deaths[i],
        'deaths today':deathtoday[i],
        'recovered':recovered[i],
        'recovered today':recoveredtoday[i],
        'active cases':active[i],
        'critical cases':critical[i]
        })

#unlock this part if you want the data to print in the console
'''
for keys in list(main_data.keys()):
    print('\u2500'*50)
    print(keys,'\n')
    for key, value in main_data[keys].items():
        print(key, ' : ', value)
'''


#unlock this part of you want to get the csv file
'''
import csv

csv_columns = [ 'country','infected','infected today','deaths','deaths today','recovered','recovered today','active cases','critical cases']

with open('corona.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for data in main_data:
        writer.writerow(data) 
'''
