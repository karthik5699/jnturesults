import urllib
import requests
import bs4


jntu_url = 'http://jntuhceh.ac.in/'

def get_results(url):
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	results_div = soup.find(id='Results').find_all('a')

	results_list = []

	for link in results_div:
		results_list.append(link.get('href'))

	print(results_list)


get_results(jntu_url)