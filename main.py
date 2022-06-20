# Objective: This program is to scrape MingPao news articles whose titles contain specific keywords based on beautifulsoup and regular expressions
# Note: This version can be extended

from bs4 import BeautifulSoup as bs
import requests
import re

# make get request to the link
result = requests.get("https://www.mingpao.com")

# create a Beautiful Soup object that takes .content
# to avoid problems with character encoding
# The.content attribute holds raw bytes, which can be decoded better than the text representation you printed earlier using the.text attribute.
soup = bs(result.content, "html.parser")


# lis of path
list_path = []

# return list of paths containing text "government" in
list_of_path = soup.find_all("a",string=re.compile("政府"))

# print out links
for i in range(len(list_of_path)):
    print(list_of_path[i]['href'])


