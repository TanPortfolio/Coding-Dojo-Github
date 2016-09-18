# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module (make sure bs4 is pip installed)
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# Construct a PrettyPrinter instance
pp = pprint.PrettyPrinter()
# choose the url to crawl
url = 'http://www.codingdojo.com'
def print_links(url):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links = soup.findAll('a', href=True)
    list_of_links = []
    for link in links:
        if link not in list_of_links:
            list_of_links.append(str(link['href']))
    pp.pprint(list_of_links)
print_links(url)
def print_all_links(url):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links = soup.findAll('a', href=True)
    dict_of_links = {}
    for link in links:
        if str(link['href']) in dict_of_links:
            dict_of_links[str(link['href'])] +=1
        else:
            dict_of_links[str(link['href'])] = 1
    pp.pprint(dict_of_links)
print_all_links(url)