from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
	"""
	this will attempt to get content from the url by making a HTM get request
	content response is HTML or XML content returned
	otherwise return None
	"""
	try:
		with closing(get(url, stream=True))as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None
	except RequestException as e:
		log_error('Error during requests to {0}:{1}'.format(url, str(e)))
		return None
		
def is_good_response(resp):
	"""
	Returns True if response is HTML else false otherwise
	"""
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200 and content_type is not None and content_type.find('html')>-1)

def log_error(e):
	"""
	prints out the error messages
	"""
	print(e)
	
