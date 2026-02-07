import pytest
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

def test_bToblockquote():
    """ <b> -> <blockquote>"""
    html = "<html><body><b>bold text</b></body></html>"
    replacer = SoupReplacer("b", "b")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

  
    assert soup.find("b") is None
    tag = soup.find("blockquote")
    assert tag is not None
    assert tag.text == "bold text"


def test_manytags():
    
    html = """
    <div>
        <b>Outer bold</b>
        <p><b>Inner bold</b></p>
        <p><i>Keep italics</i></p>
    </div>
    """
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    b_tags = soup.find_all("b")
    assert len(b_tags) == 0
    blockquotes = soup.find_all("blockquote")
    assert len(blockquotes) == 2




