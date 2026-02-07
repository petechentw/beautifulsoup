from bs4 import SoupStrainer
from bs4 import BeautifulSoup
import sys
import time
import os

start_time = time.time()




filename = sys.argv[1]
ext = os.path.splitext(filename)[1].lower() 
only_a_tags = SoupStrainer("b") #only pare the tag i need.
# therefore, it does not have to build the whole tree. 

if ext == ".html":
    parser = "html.parser"
else:
    parser = "lxml"

soup = BeautifulSoup(open(filename),parser,parse_only=only_a_tags)
print(filename + "--- %s seconds ---" % (time.time() - start_time))
print(soup.prettify)