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
		results_list.append(link)

	return results_list


def connectToUrl():
	response_received_list = get_results(jntu_url)
	if response_received_list!=None:
		print_results(response_received_list)

	else:
		print('Something went wrong')


def print_results(news):
	
	for i in range(len(news)):
		print(news[i].text)
		


connectToUrl()

	