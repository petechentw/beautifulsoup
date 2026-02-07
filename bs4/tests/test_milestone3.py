import pytest
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer



# Simple tag replacement

def test_simple_tag_replacement():
    html = "<b>Hello</b>"
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("strong") is not None
    assert str(soup) == "<strong>Hello</strong>"



# name_xformer

def test_name_xformer():
    html = "<b>Hello</b>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None
    assert str(soup) == "<blockquote>Hello</blockquote>"



# attrs_xformer

def test_attrs_xformer():
    html = "<p>Hi</p>"
    replacer = SoupReplacer(
        attrs_xformer=lambda tag: {"class": ["demo"]} if tag.name == "p" else tag.attrs
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("p")
    assert tag is not None
    assert tag["class"] == ["demo"]



# xformer 

def test_xformer():
    def add_id(tag):
        if tag.name == "p":
            tag.attrs["id"] = "newid"

    html = "<p>Hi</p>"
    replacer = SoupReplacer(xformer=add_id)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("p")
    assert tag is not None
    assert tag["id"] == "newid"



#  No transformers

def test_no_transformers():
    html = "<p>unchanged</p>"
    replacer = SoupReplacer()
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("p").text.strip() == "unchanged"
    assert str(soup) == "<p>unchanged</p>"



# Combined name_xformer + attrs_xformer

def test_combined_name_and_attrs():
    html = "<b>Mix</b>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "strong" if tag.name == "b" else "",
        attrs_xformer=lambda tag: {"style": "color:red;"} 
        if tag.name in ["b", "strong"] else tag.attrs,
    )
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("strong")
    assert tag is not None
    assert "style" in tag.attrs
    assert "color:red" in tag["style"]
    assert str(soup) == '<strong style="color:red;">Mix</strong>'

