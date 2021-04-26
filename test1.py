import requests 
from bs4 import BeautifulSoup

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
	tds = soup.findAll("tr")
	for td in tds:
		info = td.find("th")
		info_rep = td.find("td")
		print(info.text)
		print(info_rep.text)
		
	

	if info.text == "UPC":
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
	



	













