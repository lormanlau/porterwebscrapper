from bs4 import BeautifulSoup
import csv

html = open("data.htm", "r")

soup  = BeautifulSoup(html.read(), 'html.parser')

datatemp = []
data = []

count = 1

for people in soup.find_all("div", class_="friends__overview"):
	name = people.find("div", class_="friends__name")
	timestamp = people.find("div", class_="friends__registration")
	datatemp.append([name.string, timestamp.string])

for i in range(len(datatemp) - 1, -1, -1):
	data.append([count] + datatemp[i])
	count += 1

with open('registered.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data)

# print(soup.prettify())
