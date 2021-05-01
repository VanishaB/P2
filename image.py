import requests
from bs4 import BeautifulSoup
import os
url = "http://books.toscrape.com/"

def imagedown(url,folder):
	try:
		os.mkdir(os.path.join(o.getcwd(), folder)) #cree dossier
	except:
		pass
	os.chdir(os.mkdir(os.path.join(o.getcwd(), folder)))

response = requests.get(url)

soup=BeautifulSoup(response.text, "html.parser")

images = soup.findAll('img')

for image in images:
	name = image['alt']
	link = image['src']
	print(name,link)
	

	with open(name + '.jpg') as f:
		im = requests.get(link)
		f.write(im.content)
		print('Writing: ', name)
		
imagedown('http://books.toscrape.com/', 'imgg')		



