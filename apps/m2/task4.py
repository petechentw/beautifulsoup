from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import sys
import time
import os
start_time = time.time()

filename = sys.argv[1]
ext = os.path.splitext(filename)[1].lower()
only_id_tag = SoupStrainer(id = True)

if ext == ".html":
    parser = "html.parser"
else:
    parser = "lxml"



soup = BeautifulSoup(open(filename),parser,parse_only=only_id_tag)



print(soup.prettify)

