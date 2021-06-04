import requests 
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
response = requests.get(url)


allinfos = {
			"UPC" : "universal_ product_code",
			"Prix (taxe excl.)" : "price_excluding_tax",
			"Prix (taxe incl.)" : "price_including_tax",
			"disponibilité" : "number_available",
			"Nombre d’avis" : "review_rating",
			}


if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	title = soup.find('title')
	print(title.text)
	tds = soup.findAll("tr")
	for td in tds:
		info = td.find("th")
		info_rep = td.find("td")
		print(info.text)
		print(info_rep.text)
		
	

	if allinfos == "UPC":
		allinfos["universal_ product_code"] = info_rep.text
		print(allinfos["universal_ product_code"])
	if info.text == "Prix (taxe excl.)":
		allinfos["price_excluding_tax"] = info_rep.text
		print(allinfos["price_excluding_tax"])
	if info.text == "Prix (taxe incl.)":
		allinfos["price_including_tax"] = info_rep.text
		print(allinfos["price_including_tax"])
	if info.text == "disponibilité":
		allinfos["number_available"] = info_rep.text
		print(allinfos["number_available"])
	if info.text == "Nombre d'avis":
		allinfos["review_rating"] = info_rep.text
		print(allinfos["review_rating"])


description = soup.find("meta", {"name":"description"})
print(description)

image_url = soup.find("img")
print(image_url)

category=soup.findAll("a")[3]
print(category.text)



prod_url = soup.select("h3")
for link in prod_url:
    print(link.a["href"])

"""

"""


import csv
with open('files.csv','w',newline='') as fichiercsv:
	writer=csv.writer(fichiercsv)
	writer.writerow(['UPC', 'Price (excl. tax)','Product Type','Price (incl. tax)','tax' ,'Availability','Number of reviews',])
	writer.writerow(['90fa61229261140a', 'Â£53.74', 'Books', 'Â£53.74', 'Â£0.00', 'In stock (20 available)','0'])
	writer.writerow(['URL'])


with open('files.csv', newline='') as csvfile:
	reader= csv.DictReader(csvfile)
	for row in reader:
		print(row)










