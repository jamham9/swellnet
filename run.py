import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


page = requests.get('https://www.swellnet.com/reports/australia/new-south-wales/eastern-beaches')

soup = BeautifulSoup(page.content,'html.parser')

spans = soup.find_all('div', {'class' : 'view-display-id-latest_report'})

for content in spans:
    results = content.find_all(class_='field-content')

updated = results[0].text
d = datetime.strptime(updated, '%Y-%m-%d %H:%M:%S')
updated = d.strftime('%A %d at %-I:%M%p')
surf = results[1].text
surf = surf.strip()
surf_direction = surf.rsplit(' ', 1)[1]
surf_size = surf.rsplit(' ', 1)[0].split()
surf_size = surf_size[-1]
winds = results[2].text
wind_direction = re.findall(r'\s[A-Z]{1,3}', winds)[0].strip()
wind_speed = winds.rsplit(' ', 1)[0]
weather = results[3].text
rating = results[4].text
rating_number = rating.strip("/")[0]


print("Updated Time: {}".format(updated))
print("Surf Direction: {}".format(surf_direction))
print("Surf Size: {}".format(surf_size))
print("Wind Speed: {}".format(wind_speed))
print("Wind Direction: {}".format(wind_direction))
print("Weather: {}".format(weather))
print("Rating: {}".format(rating_number))
