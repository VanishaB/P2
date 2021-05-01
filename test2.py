import requests 
from bs4 import BeautifulSoup


url0 = "http://books.toscrape.com/catalogue/category/books/fantasy_19/"
index = "index.html"  
pages = []
lien = True
count = 1



	

while lien == True:
	page = "page-"+str(count)+str(".html")
	if count == 1:
		url = ""
		url = str(url0) + str(index)
		print(url)
		count += 1
	elif count != 1:
		url = ""
		url = str(url0) + str(page)
		response = requests.get(url)
		if response.status_code == 200:
			soup = BeautifulSoup("response.text", "html.parser")
			print(url)
			count += 1
		else:
			lien = False

	

"""
	response = requests.get(url)

	if response.ok:
		soup = BeautifulSoup(response.text, "html.parser")
		
	else:
		lien == False


		article = soup.findAll("article")
		print("fdcf")
		for a in article:
		href = a.findAll("a")
		link = a.findAll("h3")
		print(link)
"""