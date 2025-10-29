import pytest
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

def test_single_tag_replacement():
    """測試 <b> 是否在解析時被替換成 <blockquote>"""
    html = "<html><body><b>bold text</b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # 原始 <b> 標籤不應存在
    assert soup.find("b") is None
    # 新標籤 <blockquote> 應存在
    tag = soup.find("blockquote")
    assert tag is not None
    assert tag.text == "bold text"


def test_multiple_and_nested_tags():
    """測試多個與巢狀標籤替換"""
    html = """
    <div>
        <b>Outer bold</b>
        <p><b>Inner bold</b></p>
        <p><i>Keep italics</i></p>
    </div>
    """
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # 所有 <b> 應該都被替換成 <blockquote>
    b_tags = soup.find_all("b")
    assert len(b_tags) == 0

    # 至少有兩個 blockquote
    blockquotes = soup.find_all("blockquote")
    assert len(blockquotes) >= 2

    # 驗證文字內容是否包含替換過的字樣
    all_text = " ".join(bq.get_text(strip=True) for bq in blockquotes)
    assert "Outer bold" in all_text
    assert "Inner bold" in all_text

    # 其他標籤保持不變
    italics = soup.find("i")
    assert italics.text.strip() == "Keep italics"



