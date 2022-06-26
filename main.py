# Objective: This program is to scrape MingPao news articles whose titles contain specific keywords based on beautifulsoup and regular expressions
# Note: This version can be extended

from bs4 import BeautifulSoup as bs
import requests
import re

# make get request to the link
result = requests.get("https://news.mingpao.com/ins/即時新聞/main")

# create a Beautiful Soup object that takes .content
# to avoid problems with character encoding
# The.content attribute holds raw bytes, which can be decoded better than the text representation you printed earlier using the.text attribute.
soup = bs(result.content, "html.parser")



# lis of path
list_path = []

# return list of paths containing text "government" in
list_of_tag_title = soup.find_all("a",attrs={"title" : re.compile("政府")})
list_of_tag = soup.find_all("a",string=re.compile("政府"))

# process special url ../ins/%e6%b8%af%e8%81%9e/a...
# to start with https://news.mingpao.com/ins/.....
for i in range(len(list_of_tag_title)):
    if list_of_tag_title[i]['href'].startswith("../"):
        list_of_tag_title[i]['href'] = "https://news.mingpao.com/" + list_of_tag_title[i]['href'][3:]


# print out links
for i in range(len(list_of_tag_title)):
    print(list_of_tag_title[i]['href'])

for i in range(len(list_of_tag)):
    print(list_of_tag[i]['href'])


