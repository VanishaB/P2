import requests 
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
response = requests.get(url)
#print(response)
if response.ok:
	soup=BeautifulSoup(response.text,"html.parser")

	bloc_cat=soup.findAll("ul")
	#print(bloc_cat)
	allcat=soup.find(class_="side_categories")
	print(allcat.text)


	
	ol=soup.findAll("ol")
	for li in ol:
		prod=li.findAll("article")
		f_prod=li.findAll("div")
	print(prod)
	print(f_prod)




