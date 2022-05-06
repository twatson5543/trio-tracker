# /////////////////////////////// Main Imports ///////////////////////////////
# Libraries
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen as uReq
# Py-Files
import cfg


# ///////////////////////////////// Functions /////////////////////////////////

# Turns URL into HTML
def website_pull(url):
    link = uReq(url)
    html = BeautifulSoup(link, 'html.parser')
    return html


def parser_ptext_byclass(html, clsname):
    pt_raw = html.find_all('p')
    #print(pt_raw)
    for printLoop in pt_raw:
        print(printLoop)
    return pt_raw


def parser_ptext_byclass_list(html, clsname):
    pt_raw = [i.find_all(attrs={'class': [clsname]}) for i in html]
    #print(pt_raw)
    for printLoop in pt_raw:
        print(printLoop)
    return pt_raw


def parser_ptext(html, atr):
    pt_raw = [i.find(atr) for i in html]
    #print(pt_raw)
    #for printLoop in pt_raw:
    #    print(printLoop)


# ======================== Sequences ========================
# Main Sequence1
def Sequence1():
    html_raw = website_pull(cfg.url_01)
    text_list = parser_ptext_byclass(html_raw, 'product-collection__content')
    print("")
    print("")
    #text_list2 = parser_ptext_byclass_list(
    #    text_list, "category-saber-slider.position-relative.initialized")
    print("")
    print("")
    parser_ptext(text_list, 'h2')


# ///////////////////////////////// Sequence /////////////////////////////////

# Run Main Sequence
Sequence1()
