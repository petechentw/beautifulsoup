from bs4 import SoupStrainer
from bs4 import BeautifulSoup
import sys
import time
import os

only_tag = SoupStrainer(True)

filename = sys.argv[1]
ext = os.path.splitext(filename)[1].lower() 
if ext == ".html":
    parser = "html.parser"
else:
    parser = "lxml"

soup = BeautifulSoup(open(filename),parser,parse_only=only_tag)





for tag in soup.find_all(True):
    print(tag.name)
