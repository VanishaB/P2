import requests 
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"  #+ str(i)

#pages = []

#for i in range(10):



response = requests.get(url)
print(response)
if response.ok:
	soup = BeautifulSoup(response.text, "html.parser")

#while len(pages) > 0:
	article = soup.findAll("article")
	#print(article)
	print("fdcf")
	for a in article:
		href = a.findAll("a")
		link = a.findAll("h3")
		print(link)