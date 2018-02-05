import urllib
import requests
import bs4
import smtplib
import base64



jntu_url = 'http://jntuhceh.ac.in/'

def get_results(url):
	"""
	To get results from the jntuurl and return a list of a tags which are 
	present in the #results fragment of the page
	"""
	response = requests.get(url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	#get results with id of Results and of type a tags
	results_div = soup.find(id='Results').find_all('a')

	results_list = []

	for link in results_div:
		results_list.append(link)


	return results_list


def connectToUrl():
	"""
	a function to help connect to the url and a controller for the get_results and the print function
	like a controller
	"""
	response_received_list = get_results(jntu_url)
	
	if response_received_list!=None:
		print_results(response_received_list)

	else:
		print('Something went wrong')


def print_results(news):
	"""
		To print the results and call the waytomail function when a condition is satisfied
	"""

	
	for i in range(len(news)):
		print(news[i].text)
		print('------------------------')

		if 'B.Tech II' in news[i].text:
			try:
				wayToMail()
				break
			except smtplib.SMTPAuthenticationError:
				print("Error in authenticating your account. Email or password is incorrect")


def wayToMail():
	"""
		To send a email to the user itself 
	"""
	fromaddr = input("Your Email address\t")
	password = input("Your password\t")
	toaddr = fromaddr
	message = "New result added to the results list"
	server = smtplib.SMTP(host='smtp.gmail.com',port=587)
	server.starttls()
	server.login(fromaddr,password)
	
	server.sendmail(fromaddr,toaddr,message)
	server.quit()


	

try:	
	connectToUrl()


 	
except IOError:
 	print("No internet access")


	